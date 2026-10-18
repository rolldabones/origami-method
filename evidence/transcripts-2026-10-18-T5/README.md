# Run T5 transcripts, origami-method, Run 3

**Evidence · run T5 · 18 October 2026 (KST)**

What: the transcripts of run T5 of the `origami-run3` suite, one file per case, each with the case's rule, pass condition, the full conversation and the scorer's verdict and reasoning, and [summary.json](summary.json), the runner's summary (repository HEAD `16ac478`, system-file digests, models, max_tokens, finish time).

When: finished 2026-10-18T10:35+09:00 (Seoul).

Models: tested `claude-opus-5-5`; scored by `claude-sonnet-5-5`, a different model. LLM scoring is developer testing, not independent assurance. Harness: API system prompt, no tools, max_tokens 16000, one fresh session per case. System text (the fenced block of instructions.md extracted byte for byte, then any knowledge file named): `origami-method-instructions.txt` SHA-256 `951378a5d59dfd9fa80962ac4db80a9415fcd2bbe1a481a124ebfca258929d81`.

How produced: the session T5 runner (`t5_run.py`, a session tool, not shipped in this repository) run by Michael Paik in his Terminal; the suite manifest was written in session T5 from this repository's test cases. Each transcript here is the runner's output copied byte for byte; the only change is the closing line appended at the end of each file. `summary.json` is copied unchanged. Model output is verbatim and is not edited for house style. The session review of each verdict and the acceptance result are in [tests.md](../../tests.md).

| Case | Scorer verdict |
|---|---|
| [RS-01](RS-01.md) | PASS |
| [RS-02](RS-02.md) | PASS |
| [RS-03](RS-03.md) | FAIL |
| [RS-04](RS-04.md) | PASS |
| [RS-05](RS-05.md) | PASS |
| [RS-06](RS-06.md) | PASS |
| [RS-07](RS-07.md) | FAIL |
| [RS-08](RS-08.md) | PASS |
| [RS-09](RS-09.md) | UNSCORABLE |
| [RS-10](RS-10.md) | PASS |
| [RS-11](RS-11.md) | PASS |
| [RS-12](RS-12.md) | PASS |
| [RS-13](RS-13.md) | PASS |
| [RS-14](RS-14.md) | PASS |
| [RS-15](RS-15.md) | FAIL |
| [RS-16](RS-16.md) | PASS |
| [RS-17](RS-17.md) | PASS |

---

Final Liability rests with the Human.
