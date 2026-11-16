# Prompt runs

The records of Runs 4 to 7 of the [regression suite](../../regression-suite.md), made with [run_prompt_cases.py](../run_prompt_cases.py) from the literal turns of [scripted-turns.md](../scripted-turns.md) on `claude-opus-5-5` and scored with [score_prompt_cases.py](../score_prompt_cases.py) by `claude-sonnet-5-5`. Transcripts are in [transcripts/](transcripts/) as the runner wrote them, with the closing line appended after the runner's end marker and nothing else changed; where a case opens from a history fixture, the transcript carries the fixture in its own section, marked as not model output. Each score file has a JSON twin of the same name in [scores/](scores/). The status and the session review rest on Run 7 and are in [tests.md](../../tests.md). LLM scoring is developer testing, not independent assurance; the Human reviewer reads every sample and owns the status.

| Run | Date (KST) | Block | Manifest | Scores | Result |
|---|---|---|---|---|---|
| Run 7 (20261116-R7) | 16 November 2026 | candidate v4.2, `0a9fc7ea` | [manifest](transcripts/20261116-R7_claude-opus-5-5_run.json) | [opus, scored by sonnet](scores/20261116-R7_claude-opus-5-5_scored-by_claude-sonnet-5-5.md) | accepted with residual RS-08 (run of record; RS-02 overruled by the reviewer) |
| Run 6 (20261116-R6) | 16 November 2026 | candidate v4.1, `40fcfddb` | [manifest](transcripts/20261116-R6_claude-opus-5-5_run.json) | [opus, scored by sonnet](scores/20261116-R6_claude-opus-5-5_scored-by_claude-sonnet-5-5.md) | 15 of 17, not accepted |
| Run 5 (20261116-R5) | 16 November 2026 | candidate v4, `bd6ecf47` | [manifest](transcripts/20261116-R5_claude-opus-5-5_run.json) | [opus, scored by sonnet](scores/20261116-R5_claude-opus-5-5_scored-by_claude-sonnet-5-5.md) | 12 of 17, not accepted |
| Run 4 (20261116-R4) | 16 November 2026 | candidate v4, `bd6ecf47` | [manifest](transcripts/20261116-R4_claude-opus-5-5_run.json) | [opus, scored by sonnet](scores/20261116-R4_claude-opus-5-5_scored-by_claude-sonnet-5-5.md) | 13 of 17, not accepted |

Runs 4 to 6 were scored under the case file as it stood at each run; the seed, the history fixtures (from Run 6), RS-03's separate disable turn and the scorer's state-reached rule changed between them ([CHANGELOG.md](../../CHANGELOG.md), v1.6.0).

---

Final Liability rests with the Human.
