#!/usr/bin/env python3
"""Run the Origami Method regression suite against the Anthropic API.

The suite is seventeen cases, RS-01 to RS-17, in tests/scripted-turns.md. Each
case's turns (the ```text blocks after "Turn N, sent verbatim.") are sent in
order as user turns of one fresh conversation, each after the assistant's reply
to the one before; the turns do not adapt to the replies. A line
{{include <path>}} inside a turn is replaced by that repository file, byte for
byte (one trailing newline dropped).

What is sent as the system prompt: with --block candidate (the default), the
bytes between the fences under "## The candidate block" in
candidate-instructions.md; with --block instrument, those under "## The block"
in instructions.md. Nothing else: no tools, no file. Its SHA-256 over the UTF-8
bytes is the configuration's identity and is written into every transcript.

This script does not score; tests/score_prompt_cases.py does, with a scorer
model other than the tested model. The rule a run is read under is ACCEPTANCE.md
in the profile repository (rolldabones/rolldabones).

Usage (from the repository root):
    python3 tests/run_prompt_cases.py --dry-run
    python3 tests/run_prompt_cases.py --model claude-opus-5-5 --stamp LABEL
    python3 tests/run_prompt_cases.py --model claude-opus-5-5 --stamp LABEL2 --only RS-07,RS-09

Transcripts go to tests/prompt-runs/transcripts/<stamp>_<model>_<case>.md with
a manifest <stamp>_<model>_run.json beside them. --only under a stamp whose
manifest exists is refused; rerun a subset under a new stamp.

The API key is read only from ANTHROPIC_API_KEY. It is never printed or written.
Each user turn is written inside a ~~~~text fence. max_tokens is 32,000 per
reply. A case whose reply to any turn stops at max_tokens is marked truncated,
and its later turns are not sent.

Ported on 16 November 2026 (KST) from GRCnext-Copilot/tests/run_prompt_cases.py
(v2.7.0): multi-turn cases, the two block sources and the case pattern are new;
the request, streaming and retry code did not change. A case may open with a
history fixture ("History, sent as prior turns."): constructed user and
assistant turns sent before its first turn, written for the test and not model
output (ruling F, Michael Paik, 16 November 2026, KST); the transcript carries
the fixture in its own section, and only the replies after it are under test.
"""

import argparse
import datetime
import hashlib
import json
import os
import re
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
BLOCKS = {"candidate": (REPO_ROOT / "candidate-instructions.md", r"^## The candidate block\n\n.*?\n\n```\n(.*?)\n```$"),
          "instrument": (REPO_ROOT / "instructions.md", r"^## The block\n\n.*?\n\n```\n(.*?)\n```$")}
CASE_FILES = [REPO_ROOT / "tests" / "scripted-turns.md"]
RUNS_DIR = REPO_ROOT / "tests" / "prompt-runs"
TRANSCRIPTS_DIR = RUNS_DIR / "transcripts"
DEFAULT_MODEL = "claude-opus-5-5"
DEFAULT_MAX_TOKENS = 32000
EXPECTED_CASES = 17
EXPECTED_CRITICAL = 8
KST = datetime.timezone(datetime.timedelta(hours=9))
CASE_RE = re.compile(r"^## Case (RS-\d+): (.+)$", re.MULTILINE)
TURN_RE = re.compile(r"^Turn (\d+), sent verbatim\.\n\n```text\n(.*?)\n```\n", re.MULTILINE | re.DOTALL)
HIST_RE = re.compile(r"^History, sent as prior turns\.\n\n```text\n(.*?)\n```\n", re.MULTILINE | re.DOTALL)


def parse_history(raw: str) -> list:
    """A history fixture: an HTML comment line, then '=== user' and '=== assistant' sections, alternating,
    starting with user and ending with assistant. Returns the messages; exits on any other shape."""
    body = re.sub(r"^<!--.*?-->\n", "", raw, count=1, flags=re.DOTALL)
    parts = re.split(r"^=== (user|assistant)\n", body, flags=re.MULTILINE)
    if parts[0].strip():
        sys.exit("ERROR - Guardrail Violation: text before the first '=== user' in a history fixture")
    msgs = [{"role": parts[i], "content": parts[i + 1].rstrip("\n")} for i in range(1, len(parts), 2)]
    roles = [m["role"] for m in msgs]
    if not msgs or roles != ["user", "assistant"] * (len(msgs) // 2):
        sys.exit("ERROR - Guardrail Violation: a history fixture must alternate user and assistant, ending with assistant")
    return msgs
INCLUDE_RE = re.compile(r"^\{\{include ([^}]+)\}\}$", re.MULTILINE)
CRIT_RE = re.compile(r"^\*\*Critical cases:\*\*(.*?)(?:\n\n|\Z)", re.MULTILINE | re.DOTALL)


def sha(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def load_system_prompt(block: str = "candidate") -> str:
    path, pattern = BLOCKS[block]
    m = re.search(pattern, path.read_text(encoding="utf-8"), re.MULTILINE | re.DOTALL)
    if not m:
        sys.exit(f"ERROR - Guardrail Violation: no fenced block found in {path.name}")
    return m.group(1)


def expand(raw: str) -> str:
    def repl(m):
        rel = m.group(1).strip()
        path = (REPO_ROOT / rel).resolve()
        if REPO_ROOT not in path.parents or not path.is_file():
            sys.exit(f"ERROR - Guardrail Violation: include {rel} is not a repository file")
        body = path.read_text(encoding="utf-8")
        return body[:-1] if body.endswith("\n") else body
    return INCLUDE_RE.sub(repl, raw)


def parse_critical(text: str) -> set:
    ids = set()
    for m in CRIT_RE.finditer(text):
        para = m.group(1)
        ids |= set(re.findall(r"\b(RS-\d{2})\b", para))
    return ids


def load_cases():
    """Return (cases, critical): cases is a list of dicts in suite order."""
    cases, critical = [], set()
    for f in CASE_FILES:
        text = f.read_text(encoding="utf-8")
        critical |= parse_critical(text)
        heads = list(CASE_RE.finditer(text))
        for i, h in enumerate(heads):
            end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
            section = text[h.start():end]
            section = re.split(r"\n---\n", section)[0].rstrip() + "\n"
            tm = list(TURN_RE.finditer(section))
            if not tm or [int(x.group(1)) for x in tm] != list(range(1, len(tm) + 1)):
                sys.exit(f"ERROR - Guardrail Violation: case {h.group(1)} in {f.name} has no turns or misnumbered turns")
            turns = [expand(x.group(2)) for x in tm]
            hm = HIST_RE.search(section)
            hist_raw = expand(hm.group(1)) if hm else ""
            history = parse_history(hist_raw) if hm else []
            spec = TURN_RE.sub(lambda x: f"[Turn {x.group(1)}: sent to the assistant; see the conversation below.]\n", section)
            spec = HIST_RE.sub("[History: a constructed fixture sent as prior turns; shown to you below, not under test.]\n", spec)
            cases.append({"id": h.group(1), "name": h.group(2).strip(), "file": f.name, "history": history,
                          "history_raw": hist_raw, "turns": turns,
                          "message": (hist_raw + "\n\n" if hm else "") + "\n\n".join(turns), "spec": spec})
    ids = [c["id"] for c in cases]
    if len(set(ids)) != len(ids):
        sys.exit("ERROR - Guardrail Violation: duplicate case IDs")
    unknown = critical - set(ids)
    if unknown:
        sys.exit(f"ERROR - Guardrail Violation: critical IDs not in the suite: {sorted(unknown)}")
    if len(cases) != EXPECTED_CASES or len(critical) != EXPECTED_CRITICAL:
        print(f"WARNING: expected {EXPECTED_CASES} cases and {EXPECTED_CRITICAL} critical, "
              f"parsed {len(cases)} and {len(critical)}")
    return cases, critical


def safe(s: str) -> str:
    return re.sub(r"[^A-Za-z0-9._-]", "-", s)


def call(client, **kw):
    """One Messages request with backoff on 429, 529, 5xx and connection errors.

    Sent as a stream and read to the final message: the SDK refuses a
    non-streaming request whose max_tokens could run past ten minutes, which
    32,000 does (found 27 October 2026, KST, at the first call of run R2).
    The final message carries the same content, stop_reason and usage.
    """
    import anthropic
    for attempt in range(7):
        try:
            with client.messages.stream(**kw) as stream:
                return stream.get_final_message()
        except (anthropic.RateLimitError, anthropic.APIConnectionError, anthropic.InternalServerError) as e:
            wait = min(120, 5 * 2 ** attempt)
            print(f"    retry {attempt + 1} in {wait}s ({type(e).__name__})", flush=True)
            time.sleep(wait)
        except anthropic.APIStatusError as e:
            if e.status_code in (429, 529) or e.status_code >= 500:
                wait = min(120, 5 * 2 ** attempt)
                print(f"    retry {attempt + 1} in {wait}s (HTTP {e.status_code})", flush=True)
                time.sleep(wait)
            else:
                raise
    raise RuntimeError("API retries exhausted")


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default=DEFAULT_MODEL)
    ap.add_argument("--only", default="", help="Comma-separated case IDs, e.g. RS-07,RS-09")
    ap.add_argument("--block", choices=sorted(BLOCKS), default="candidate")
    ap.add_argument("--max-tokens", type=int, default=DEFAULT_MAX_TOKENS)
    ap.add_argument("--stamp", default="", help="Run label shared by several models (default: KST time now)")
    ap.add_argument("--dry-run", action="store_true", help="Parse and print; no API call")
    args = ap.parse_args()

    system_prompt = load_system_prompt(args.block)
    digest = sha(system_prompt)
    cases, critical = load_cases()
    chosen = {s.strip() for s in args.only.split(",") if s.strip()}
    if chosen:
        bad = chosen - {c["id"] for c in cases}
        if bad:
            sys.exit(f"ERROR - Guardrail Violation: unknown case IDs {sorted(bad)}")
        cases = [c for c in cases if c["id"] in chosen]
    print(f"Block SHA-256: {digest} ({len(system_prompt)} characters, {len(system_prompt.split())} words)")
    print(f"Critical cases: {', '.join(c for c in [x['id'] for x in load_cases()[0]] if c in critical)}")

    if args.dry_run:
        for c in cases:
            print(f"{c['id']:<6}{'*' if c['id'] in critical else ' '} {len(c['history']) // 2:>2} hist {len(c['turns']):>2} turns {len(c['message'].split()):>5} words | "
                  f"{c['turns'][-1][:70].replace(chr(10), ' ')}")
        print(f"Dry run: {len(cases)} case(s) parsed, * = critical. No API call made.")
        return

    if not os.environ.get("ANTHROPIC_API_KEY"):
        sys.exit("ERROR - Guardrail Violation: ANTHROPIC_API_KEY not set")
    try:
        import anthropic
    except ImportError:
        sys.exit("ERROR - Guardrail Violation: anthropic package missing. pip install anthropic")
    client = anthropic.Anthropic()
    TRANSCRIPTS_DIR.mkdir(parents=True, exist_ok=True)
    stamp = safe(args.stamp) if args.stamp else datetime.datetime.now(KST).strftime("%Y%m%d-%H%M%S")
    mlabel = safe(args.model)
    mpath = TRANSCRIPTS_DIR / f"{stamp}_{mlabel}_run.json"
    if chosen and mpath.exists():
        sys.exit(f"ERROR - Guardrail Violation: {mpath.name} exists; rerun the subset under a new --stamp")
    print(f"Model: {args.model}  Stamp: {stamp}  max_tokens: {args.max_tokens}")
    manifest = {"stamp": stamp, "model_requested": args.model, "max_tokens": args.max_tokens,
                "prompt_file": BLOCKS[args.block][0].name, "block": args.block, "prompt_proper_sha256": digest,
                "prompt_characters": len(system_prompt),
                "attachments": "none", "started_kst": datetime.datetime.now(KST).isoformat(timespec="seconds"),
                "transcripts": []}
    truncated = []
    for c in cases:
        print(f"Running {c['id']} {c['name']} ({len(c['turns'])} turns) ...", flush=True)
        msgs, parts, rec, trunc, models = list(c["history"]), [], [], False, set()
        tin = tout = 0
        for n, user in enumerate(c["turns"], 1):
            msgs.append({"role": "user", "content": user})
            r = call(client, model=args.model, max_tokens=args.max_tokens, system=system_prompt, messages=msgs)
            reply = "".join(b.text for b in r.content if b.type == "text")
            msgs.append({"role": "assistant", "content": reply or "(empty reply)"})
            models.add(r.model)
            tin += r.usage.input_tokens
            tout += r.usage.output_tokens
            rec.append({"turn": n, "stop_reason": r.stop_reason, "output_tokens": r.usage.output_tokens})
            parts.append(f"### Turn {n}, user\n\n~~~~text\n{user}\n~~~~\n\n"
                         f"### Turn {n}, assistant (stop_reason {r.stop_reason})\n\n{reply}\n")
            print(f"  turn {n}: stop_reason={r.stop_reason}", flush=True)
            if r.stop_reason == "max_tokens":
                trunc = True
                break
        if trunc:
            truncated.append(c["id"])
        mret = ", ".join(sorted(models))
        out = TRANSCRIPTS_DIR / f"{stamp}_{mlabel}_{c['id']}.md"
        out.write_text(
            f"# {c['id']} {c['name']}\n\n"
            f"**Model requested:** {args.model}  **Model returned:** {mret}  **Run:** {stamp}\n"
            f"**Block SHA-256:** {digest}  **Block:** {args.block}\n"
            f"**Run input SHA-256:** {sha(c['message'])}  **Case file:** tests/{c['file']}  "
            f"**Critical:** {'yes' if c['id'] in critical else 'no'}\n"
            f"**max_tokens:** {args.max_tokens}  **Turns sent:** {len(rec)} of {len(c['turns'])}  "
            f"**Input tokens:** {tin}  **Output tokens:** {tout}\n"
            f"**Truncated:** {'YES, do not score as complete' if trunc else 'no'}  "
            f"**History turns:** {len(c['history'])} (constructed fixture, not model output)\n\n"
            + (f"## History (constructed fixture, not model output)\n\n~~~~text\n{c['history_raw']}\n~~~~\n\n" if c["history"] else "")
            + f"## Conversation\n\n" + "\n".join(parts) +
            f"\n<!-- end of transcript; written by tests/run_prompt_cases.py -->\n", encoding="utf-8")
        manifest["transcripts"].append({"case": c["id"], "file": out.name, "model_returned": mret,
                                        "turns": rec, "truncated": trunc,
                                        "input_tokens": tin, "output_tokens": tout})
    manifest["finished_kst"] = datetime.datetime.now(KST).isoformat(timespec="seconds")
    mpath.write_text(json.dumps(manifest, indent=2) + "\n", encoding="utf-8")
    print(f"\nDone. {len(cases)} transcript(s), manifest {mpath.relative_to(REPO_ROOT)}.")
    if truncated:
        print(f"TRUNCATED: {', '.join(truncated)}. A truncated case is not exercised (ACCEPTANCE.md (a)).")


if __name__ == "__main__":
    main()
