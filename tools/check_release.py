#!/usr/bin/env python3
"""
check_release.py: release consistency check for the origami-method repository.

Run from anywhere:  python3 tools/check_release.py [repo-root]
Exit 0 when every check passes, 1 when any fails, 2 when a check could not run.
It reads. It never writes.

What it checks, and why each check exists:

  1. Version and date lockstep. The README masthead is the reference. The README footer,
     the README How to Cite block, the newest CHANGELOG.md entry and CITATION.cff must carry
     the same version, and the dates must agree. CHANGELOG.md records the footer lagging the
     masthead twice (v1.1.2, v1.1.3), both found by reading and neither by a guard.
     Companion files are different: their masthead names the release in which the file's
     substance last changed, so the check is that the named release exists in CHANGELOG.md
     with the same date, does not exceed the README version, and equals the README version
     when the file has changed since the last tag or in the working tree. That last part
     needs git and is reported NOT CHECKED without it.
  2. Internal links and heading anchors, outside fenced code blocks, in every markdown file.
     A link to a file that is not there, or to a heading that is not there, is a defect.
  3. Builder Packet fields. builder-packet-template.md defines the required fields in its
     numbered table. Every packet in worked-example.md must carry every one of them, by the
     same name, in the same order. The candidate instruction block's compact packet line must
     list the same number of fields.
  4. Mirror integrity. The README states the character count and the SHA-256 of the deployed
     instruction block. Both are recomputed from the bytes between the fences (UTF-8, no
     trailing newline). A mirror that changes without the stated figures changing fails.
  5. Candidate size. The candidate block in candidate-instructions.md must be under the
     warning ceiling of 7,900 characters, and the count the file states must equal the bytes.
     The file's diff block must equal a freshly computed unified diff of deployed against
     candidate, so the diff cannot go stale.
  6. Closing line. Every markdown file except LICENSE carries the closing line.

A check that cannot find its input reports a failure, never a pass (a guard that cannot run
must not report safety).
"""
import difflib
import hashlib
import os
import re
import sys

CANDIDATE_CEILING = 7900
MONTHS = {m: i for i, m in enumerate(
    ["January", "February", "March", "April", "May", "June", "July", "August",
     "September", "October", "November", "December"], 1)}
CLOSING = "Final Liability rests with the Human."
MD_LINK = re.compile(r"(?<!!)\[[^\]]*\]\(([^)\s]+)\)")
FENCE = re.compile(r"^\s*(```|~~~)")

failures = []
notes = []


def fail(msg):
    failures.append(msg)


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def fenced_lines(lines):
    """Return the set of 1-based line numbers inside fenced code blocks (fence lines included)."""
    inside = set()
    open_fence = None
    for i, line in enumerate(lines, 1):
        m = FENCE.match(line)
        if m:
            if open_fence is None:
                open_fence = m.group(1)
                inside.add(i)
                continue
            if m.group(1) == open_fence:
                inside.add(i)
                open_fence = None
                continue
        if open_fence is not None:
            inside.add(i)
    return inside


def slug(heading):
    """GitHub-style anchor: lowercase, drop everything but letters, digits, spaces, hyphens,
    then spaces to hyphens. Markdown emphasis markers are stripped first."""
    h = re.sub(r"[*_`]", "", heading).strip()
    h = h.lower()
    h = re.sub(r"[^\w\- ]", "", h)
    return h.replace(" ", "-")


def headings(text):
    out = []
    lines = text.splitlines()
    inside = fenced_lines(lines)
    for i, line in enumerate(lines, 1):
        if i in inside:
            continue
        m = re.match(r"^#{1,6}\s+(.*?)\s*#*\s*$", line)
        if m:
            out.append(slug(m.group(1)))
    return out


def date_iso(day, month_name, year):
    return f"{int(year):04d}-{MONTHS[month_name]:02d}-{int(day):02d}"


def vtuple(v):
    return tuple(int(x) for x in v.split("."))


def changed_since_release(root):
    """Names of files at the repository root changed since the latest tag or in the working
    tree. None when git is unavailable or the root is not a git work tree; the caller reports
    NOT CHECKED rather than passing."""
    import subprocess
    def git(*args):
        r = subprocess.run(["git", "-C", root] + list(args), capture_output=True, text=True)
        if r.returncode != 0:
            raise RuntimeError(r.stderr.strip())
        return r.stdout
    try:
        git("rev-parse", "--is-inside-work-tree")
        names = set()
        for line in git("status", "--porcelain").splitlines():
            if len(line) > 3:
                names.add(os.path.basename(line[3:].strip().strip('"')))
        tags = [t for t in git("tag", "--list").split() if re.fullmatch(r"v\d+\.\d+\.\d+", t)]
        if tags:
            latest = max(tags, key=lambda t: vtuple(t[1:]))
            for line in git("diff", "--name-only", latest, "HEAD").splitlines():
                names.add(os.path.basename(line.strip()))
        return names
    except (RuntimeError, FileNotFoundError, OSError):
        return None


def main(root):
    readme_p = os.path.join(root, "README.md")
    if not os.path.exists(readme_p):
        print(f"FAIL: {readme_p} not found; nothing checked")
        return 2
    readme = read(readme_p)
    rlines = readme.splitlines()

    # ---- 1. version and date lockstep ---------------------------------------------------
    m = re.search(r"^\*\*v(\d+\.\d+\.\d+) · (\d{1,2}) (\w+) (\d{4}) · ", readme, re.M)
    if not m:
        fail("README.md: masthead not found in the form **vX.Y.Z · D Month YYYY · ...**")
        ver, iso = None, None
    else:
        ver = m.group(1)
        if m.group(3) not in MONTHS:
            fail(f"README.md: masthead month {m.group(3)!r} is not a month name")
            iso = None
        else:
            iso = date_iso(m.group(2), m.group(3), m.group(4))
            notes.append(f"masthead v{ver} · {iso}")

    if ver:
        footers = [i for i, l in enumerate(rlines, 1)
                   if l.startswith("**v") and "Changes:" in l]
        if len(footers) != 1:
            fail(f"README.md: expected exactly one footer line carrying 'Changes:', found {len(footers)}")
        else:
            fl = rlines[footers[0] - 1]
            fm = re.match(r"^\*\*v(\d+\.\d+\.\d+) · (\d{1,2}) (\w+) (\d{4}) · ", fl)
            if not fm:
                fail(f"README.md:{footers[0]}: footer not in masthead form")
            else:
                if fm.group(1) != ver:
                    fail(f"README.md:{footers[0]}: footer version v{fm.group(1)} differs from masthead v{ver}")
                fiso = date_iso(fm.group(2), fm.group(3), fm.group(4)) if fm.group(3) in MONTHS else None
                if fiso != iso:
                    fail(f"README.md:{footers[0]}: footer date {fiso} differs from masthead date {iso}")

        cm = re.search(r"^#{2,4}\s*How to cite\s*\n(.*?)(?=^#{2,4}\s|\Z)", readme, re.M | re.S | re.I)
        if not cm:
            fail("README.md: How to Cite section not found")
        else:
            cited = set(re.findall(r"\bv(\d+\.\d+\.\d+)\b", cm.group(1)))
            if cited != {ver}:
                fail(f"README.md: How to Cite carries {sorted(cited) or 'no version'}, masthead is v{ver}")

        cff_p = os.path.join(root, "CITATION.cff")
        if not os.path.exists(cff_p):
            fail("CITATION.cff: missing")
        else:
            cff = read(cff_p)
            vm = re.search(r"^version:\s*[\"']?v?([0-9][^\s\"']*)", cff, re.M)
            dm = re.search(r"^date-released:\s*[\"']?(\d{4}-\d{2}-\d{2})", cff, re.M)
            if not vm:
                fail("CITATION.cff: no version line")
            elif vm.group(1) != ver:
                fail(f"CITATION.cff: version {vm.group(1)} differs from README masthead v{ver}")
            if not dm:
                fail("CITATION.cff: no date-released line")
            elif dm.group(1) != iso:
                fail(f"CITATION.cff: date-released {dm.group(1)} differs from README masthead date {iso}")

        cl_p = os.path.join(root, "CHANGELOG.md")
        if not os.path.exists(cl_p):
            fail("CHANGELOG.md: missing")
        else:
            hm = re.search(r"^## v(\d+\.\d+\.\d+) \((\d{4}-\d{2}-\d{2})\)", read(cl_p), re.M)
            if not hm:
                fail("CHANGELOG.md: no entry heading in the form '## vX.Y.Z (YYYY-MM-DD)'")
            else:
                if hm.group(1) != ver:
                    fail(f"CHANGELOG.md: newest entry v{hm.group(1)} differs from README masthead v{ver}")
                if hm.group(2) != iso:
                    fail(f"CHANGELOG.md: newest entry date {hm.group(2)} differs from README masthead date {iso}")

        # Companion mastheads name the release in which the file's substance last changed, not
        # the current release. That is the account's practice (a version line that moves on a
        # metadata release manufactures a false claim). So the test is in two parts: the named
        # release must exist in CHANGELOG.md with the same date and must not exceed the README's
        # version; and a companion changed since the last tag, or changed in the working tree,
        # must name this release. The second part needs git and reports NOT CHECKED without it.
        entries = {}
        if os.path.exists(cl_p):
            for em in re.finditer(r"^## v(\d+\.\d+\.\d+) \((\d{4}-\d{2}-\d{2})\)", read(cl_p), re.M):
                entries[em.group(1)] = em.group(2)
        companions = sorted(f for f in os.listdir(root)
                            if f.endswith(".md") and f not in ("README.md", "CHANGELOG.md"))
        if not companions:
            fail("no companion .md files found; the build kit is missing")
        changed = changed_since_release(root)
        for c in companions:
            text = read(os.path.join(root, c))
            pm = re.search(r"^\*\*Part of Origami Method · last changed in v(\d+\.\d+\.\d+) · (\d{1,2}) (\w+) (\d{4}) · ", text, re.M)
            if not pm:
                fail(f"{c}: no companion masthead '**Part of Origami Method · last changed in vX.Y.Z · D Month YYYY · ...**'")
                continue
            cver = pm.group(1)
            ciso = date_iso(pm.group(2), pm.group(3), pm.group(4)) if pm.group(3) in MONTHS else None
            if cver not in entries:
                fail(f"{c}: masthead names v{cver}, which has no CHANGELOG.md entry")
            elif entries[cver] != ciso:
                fail(f"{c}: masthead date {ciso} differs from the CHANGELOG.md date for v{cver} ({entries[cver]})")
            if vtuple(cver) > vtuple(ver):
                fail(f"{c}: masthead names v{cver}, later than the README masthead v{ver}")
            if changed is not None and c in changed and cver != ver:
                fail(f"{c}: changed since the last release but its masthead names v{cver}, not v{ver}")
        if changed is None:
            notes.append(f"companions checked: {len(companions)}; substance test NOT CHECKED (no git history available)")
        else:
            hit = sorted(c for c in companions if c in changed)
            if hit:
                notes.append(f"companions checked: {len(companions)}; changed since the last release: {len(hit)} "
                             f"({', '.join(hit)}), each naming v{ver}")
            else:
                notes.append(f"companions checked: {len(companions)}; none changed since the last release")

    # ---- 2. internal links and anchors ---------------------------------------------------
    md_files = []
    for dirpath, dirnames, filenames in os.walk(root):
        dirnames[:] = [d for d in dirnames if d not in (".git",)]
        for fn in filenames:
            if fn.endswith(".md"):
                md_files.append(os.path.join(dirpath, fn))
    md_files.sort()
    if not md_files:
        fail("no markdown files found under the repository root")
    heading_cache = {}
    link_count = 0
    for p in md_files:
        text = read(p)
        lines = text.splitlines()
        inside = fenced_lines(lines)
        for i, line in enumerate(lines, 1):
            if i in inside:
                continue
            for target in MD_LINK.findall(line):
                if target.startswith(("http://", "https://", "mailto:")):
                    continue
                link_count += 1
                file_part, _, anchor = target.partition("#")
                if file_part:
                    tp = os.path.normpath(os.path.join(os.path.dirname(p), file_part))
                    if not os.path.exists(tp):
                        fail(f"{os.path.relpath(p, root)}:{i}: link target not found: {file_part}")
                        continue
                else:
                    tp = p
                if anchor:
                    if not tp.endswith(".md"):
                        fail(f"{os.path.relpath(p, root)}:{i}: anchor on a non-markdown target: {target}")
                        continue
                    if tp not in heading_cache:
                        heading_cache[tp] = headings(read(tp))
                    if anchor not in heading_cache[tp]:
                        fail(f"{os.path.relpath(p, root)}:{i}: anchor #{anchor} not found in {os.path.relpath(tp, root)}")
    notes.append(f"internal links checked: {link_count} across {len(md_files)} markdown files")

    # ---- 3. Builder Packet fields ---------------------------------------------------------
    tpl_p = os.path.join(root, "builder-packet-template.md")
    ex_p = os.path.join(root, "worked-example.md")
    fields = []
    if not os.path.exists(tpl_p):
        fail("builder-packet-template.md: missing")
    else:
        for row in re.findall(r"^\|\s*(\d{1,2})\s*\|\s*([^|]+?)\s*\|", read(tpl_p), re.M):
            fields.append((int(row[0]), row[1]))
        nums = [n for n, _ in fields]
        if nums != list(range(1, len(nums) + 1)) or not nums:
            fail(f"builder-packet-template.md: field table rows are not numbered 1..N: {nums}")
        else:
            notes.append(f"required packet fields: {len(fields)}")
    if fields and not os.path.exists(ex_p):
        fail("worked-example.md: missing")
    elif fields:
        ex = read(ex_p)
        packets = re.split(r"^### Builder Packet: ", ex, flags=re.M)[1:]
        if not packets:
            fail("worked-example.md: no '### Builder Packet:' sections found")
        for pk in packets:
            pname = pk.splitlines()[0].strip()
            body = pk.split("\n### ", 1)[0].split("\n## ", 1)[0]
            found = re.findall(r"^(\d{1,2})\. \*\*([^*]+?):\*\*", body, re.M)
            expected = [(n, name) for n, name in fields]
            got = [(int(n), name) for n, name in found]
            if got != expected:
                missing = [f"{n}. {name}" for n, name in expected if (n, name) not in got]
                extra = [f"{n}. {name}" for n, name in got if (n, name) not in expected]
                fail(f"worked-example.md: packet {pname} fields differ from the template. "
                     f"missing: {missing or 'none'}; unexpected: {extra or 'none'}")
        notes.append(f"packets checked in worked-example.md: {len(packets)}")

    # ---- 4. mirror integrity ----------------------------------------------------------------
    bm = re.search(r"### Instructions \(as deployed\)\n\n```\n(.*?)\n```", readme, re.S)
    deployed = None
    if not bm:
        fail("README.md: deployed instruction block not found under '### Instructions (as deployed)'")
    else:
        deployed = bm.group(1)
        n = len(deployed)
        sha = hashlib.sha256(deployed.encode("utf-8")).hexdigest()
        sm = re.search(r"It is ([\d,]+) characters, SHA-256 `([0-9a-f]{64})`", readme)
        if not sm:
            fail("README.md: stated character count and SHA-256 of the deployed block not found "
                 "in the form 'It is N characters, SHA-256 `hex`'")
        else:
            stated_n = int(sm.group(1).replace(",", ""))
            if stated_n != n:
                fail(f"README.md: deployed block is {n} characters, README states {stated_n}")
            if sm.group(2) != sha:
                fail(f"README.md: deployed block SHA-256 is {sha[:12]}..., README states {sm.group(2)[:12]}...")
        notes.append(f"deployed block: {n} characters, sha256 {sha[:12]}...")

    # ---- 5. candidate size and diff -------------------------------------------------------
    cand_p = os.path.join(root, "candidate-instructions.md")
    if not os.path.exists(cand_p):
        fail("candidate-instructions.md: missing")
    else:
        ct = read(cand_p)
        cm = re.search(r"## The candidate block\n\n.*?\n\n```\n(.*?)\n```", ct, re.S)
        if not cm:
            fail("candidate-instructions.md: candidate block not found under '## The candidate block'")
        else:
            cand = cm.group(1)
            cn = len(cand)
            cu = len(cand.encode("utf-16-le")) // 2
            if cn >= CANDIDATE_CEILING:
                fail(f"candidate-instructions.md: candidate block is {cn} characters, at or above the "
                     f"{CANDIDATE_CEILING} warning ceiling")
            stm = re.search(r"The candidate block is \*\*([\d,]+) characters\*\* \(([\d,]+) UTF-16 code units", ct)
            if not stm:
                fail("candidate-instructions.md: stated size sentence not found")
            else:
                if int(stm.group(1).replace(",", "")) != cn:
                    fail(f"candidate-instructions.md: block is {cn} characters, file states {stm.group(1)}")
                if int(stm.group(2).replace(",", "")) != cu:
                    fail(f"candidate-instructions.md: block is {cu} UTF-16 units, file states {stm.group(2)}")
            if deployed is not None:
                dm = re.search(r"```diff\n(.*?)```", ct, re.S)
                if not dm:
                    fail("candidate-instructions.md: diff block not found")
                else:
                    fresh = "".join(difflib.unified_diff(
                        deployed.splitlines(True), cand.splitlines(True),
                        fromfile="deployed (README mirror, 14 July 2026)",
                        tofile="candidate (17 September 2026, not deployed)", n=1))
                    if dm.group(1) != fresh:
                        fail("candidate-instructions.md: the diff block does not match a fresh diff of the "
                             "deployed block against the candidate block; regenerate it")
            pl = re.search(r"^Builder Packet \(one per role; (\d+) fields, none blank\)\n\n(.+)$", cand, re.M)
            if not pl:
                fail("candidate-instructions.md: compact Builder Packet line not found in the candidate block")
            elif fields:
                stated = int(pl.group(1))
                listed = len(pl.group(2).split(" | "))
                if stated != len(fields) or listed != len(fields):
                    fail(f"candidate-instructions.md: packet line states {stated} fields and lists {listed}; "
                         f"template defines {len(fields)}")
            notes.append(f"candidate block: {cn} characters ({CANDIDATE_CEILING - cn} below the warning ceiling)")

    # ---- 6. closing line --------------------------------------------------------------------
    for p in md_files:
        text = read(p)
        if CLOSING not in text:
            fail(f"{os.path.relpath(p, root)}: closing line absent")

    # ---- report ---------------------------------------------------------------------------
    for n in notes:
        print(f"  {n}")
    if failures:
        print(f"FAIL: {len(failures)} check(s) failed")
        for f in failures:
            print(f"  - {f}")
        return 1
    print("OK: all checks passed")
    return 0


if __name__ == "__main__":
    here = os.path.dirname(os.path.abspath(__file__))
    default_root = os.path.normpath(os.path.join(here, ".."))
    root = sys.argv[1] if len(sys.argv) > 1 else default_root
    sys.exit(main(root))
