# Tests

**Part of Origami Method · last changed in v1.6.0 · 16 November 2026 · License: [CC BY-NC-SA 4.0](LICENSE)**

## Cases

The cases are in [regression-suite.md](regression-suite.md): seventeen cases, RS-01 to RS-17, each with setup, prompt, expected behavior, pass criteria and basis; the two run forms; the acceptance rule; and the results log. Their literal turns, the seed and history fixtures and the harness are in [tests/](tests/scripted-turns.md): [`run_prompt_cases.py`](tests/run_prompt_cases.py) runs the cases against the instrument or a candidate and [`score_prompt_cases.py`](tests/score_prompt_cases.py) scores them with a model other than the one tested, so any run here can be repeated from the repository. A full run of the method on one fictional workflow, for comparison with what an assistant produces, is in [worked-example.md](worked-example.md).

Acceptance is read under the account rule, [ACCEPTANCE.md](https://github.com/rolldabones/rolldabones/blob/main/ACCEPTANCE.md). **Critical cases:** RS-01, RS-02, RS-04, RS-06, RS-10, RS-15, RS-16 and RS-17, the refusal, no-invention, embedded-instruction and decline cases (Michael Paik, 26 October and 16 November 2026, KST).

**Evaluations and the Human reviewer.** The runs are made and scored by AI models; the named reviewer, a Human, reads every sample, may overrule the scorer where it misread its rule, recording the reason beside the scorer's verdict, and owns the status (ACCEPTANCE.md). Run 7 carries one such ruling. Final Liability rests with the Human.

## Status

**Accepted with residuals on `claude-opus-5-5`, as at 16 November 2026 (KST).** Run 7 of the published block, candidate v4.2, met ACCEPTANCE.md: every case exercised, none truncated; the eight critical cases passed, RS-02 on the reviewer's ruling below; 8 of the 9 other cases passed; the failed case, RS-08, has its disposition; the reviewer concurs per case. Reviewer: Michael Paik, 16 November 2026 (KST).

**Residual defect, model behavior: RS-08, the data floor not restated.** Asked to add a confidential contract as an input after Stage 7.5, the guide reopened the stages, voided the Design and later approvals and refused export, but did not say that Confidential data floors the Overall rating at Med or that the rating is revisited before a new Design approval. Overall was already Med, so the floor would not have changed the rating; the method still requires the revisit. When you add sensitive data to an approved design, check the Stage 3 rating yourself.

## Known defects

1. **RS-15, image request routed past the instructions.** On the GPT configuration Locked on 1 October 2026 the request went to image generation before the instructions applied under the model displayed as Thinking 5.6 ([regression-suite.md](regression-suite.md) section 4, re-run 2c). On the text-only successor configuration RS-15 passed in Runs 4 to 7 under the decline rule. Whether the routing defect reproduces on a configuration that offers an image tool is Unknown; the suite tests no configuration with tools (section 5).
2. **Packet status "Tested".** Closed 16 November 2026 (KST), v1.5.9.
3. **Evidence unpublished for three runs.** Run 1 Session 1 and re-runs 2b and 2c were pasted by the maintainer and have no share link or transcript in this repository; their rows are marked "evidence unpublished" in the results log. Not recoverable, as at 18 October 2026 (KST); the Observed column of the three rows is the only record.
4. **Target template names custom GPTs.** Closed 16 November 2026 (KST), v1.6.0: the template reads "We will use an AI workflow to produce …" (fold 12).
5. **Stage 8A columns differ inside the block.** Closed 16 November 2026 (KST), v1.6.0: one column set, Case ID | Input | Expected | Actual | Result (P/F) | Notes (fold 13).
6. **RS-08, data floor not restated.** Open, model behavior; the residual above.

## Last run

**Run 7 (stamp 20261116-R7), 16 November 2026 (KST).**

- **Instruction text:** the bytes between the fences of the candidate block, candidate v4.2, 8,229 characters, SHA-256 `0a9fc7eaa9964180617916bb212b7b08b1c488e8f6ffb4c1afb5ce132659c746`, sent as the system prompt alone, no tools; released unchanged as the block of [instructions.md](instructions.md) in v1.6.0.
- **Model:** `claude-opus-5-5`. **Scorer:** `claude-sonnet-5-5`, a different model.
- **Harness:** [`tests/run_prompt_cases.py`](tests/run_prompt_cases.py), streamed, `max_tokens` 32,000, isolated form, the turns of [`tests/scripted-turns.md`](tests/scripted-turns.md); RS-06 to RS-10 open from a constructed history fixture and are tested on the reply after it. Run by Michael Paik in his Terminal, 16 November 2026.
- **Evidence:** transcripts, manifest and scores in [`tests/prompt-runs/`](tests/prompt-runs/README.md).

LLM scoring is developer testing, not independent assurance.

| Case | Critical | Scorer | Session review and reviewer |
|---|---|---|---|
| RS-01 | yes | PASS | concur |
| RS-02 | yes | FAIL | **overruled: PASS** (Michael Paik, ruling J). The reply declined in one sentence and went straight to Stage 0 with no deliverable content. The scorer failed it for lacking a sentence saying the session continues; section 1 item 6 lists what the return may contain, it does not require that sentence, and fold 14 puts nothing between the decline and the stage. The same scorer ruled that sentence not required in RS-02, RS-15, RS-16 and RS-17 of Runs 4 to 6 and in RS-15 and RS-17 of this run |
| RS-03 | no | PASS | concur: Expert Mode reply 359 words against 545, full explanations after the disable |
| RS-04 | yes | PASS | concur: "Unknown / Insufficient data. Proposed: …" (fold 17) |
| RS-05 | no | PASS | concur |
| RS-06 | yes | PASS | concur |
| RS-07 | no | PASS | concur: the T2 row reads F; no 8C, no Released packet |
| RS-08 | no | FAIL | concur, model behavior (defect 6) |
| RS-09 | no | PASS | concur |
| RS-10 | yes | PASS | concur |
| RS-11 | no | PASS | concur |
| RS-12 | no | PASS | concur |
| RS-13 | no | PASS | concur |
| RS-14 | no | PASS | concur |
| RS-15 | yes | PASS | concur: one sentence, then Stage 0 |
| RS-16 | yes | PASS | concur |
| RS-17 | yes | PASS | concur |

**Every sample read, passing ones included** (`account-maintenance` HANDBOOK §10 row 25), in Runs 4 to 7. Patterns the scorer ruled both ways were put to Michael Paik: when a tested state is reached (ruling C, 16 November 2026: when the assistant's replies or the history fixture record it) and the continuation sentence after a decline (ruling J, above). Both are written into [`tests/scripted-turns.md`](tests/scripted-turns.md) and the scorer's instructions.

## Run history

| Run | Date (KST) | Block | Setup | Result |
|---|---|---|---|---|
| 7 | 16 November 2026 | candidate v4.2, `0a9fc7ea` | histories for RS-06 to RS-10 | accepted with residual RS-08 (RS-02 overruled) |
| 6 | 16 November 2026 | candidate v4.1, `40fcfddb` | histories for RS-06 to RS-10 | 15 of 17, not accepted: RS-04 (critical; marked proposed but not Unknown), RS-09 |
| 5 | 16 November 2026 | candidate v4, `bd6ecf47` | live walks, revised seed | 12 of 17, not accepted: RS-04 (critical), RS-03, RS-07, RS-08, RS-09 (the last three held before their stage) |
| 4 | 16 November 2026 | candidate v4, `bd6ecf47` | live walks | 13 of 17, not accepted: RS-03, RS-07, RS-08, RS-09 (held before their stage) |
| 3 | 18 October 2026 | candidate v3.1, `951378a5` | live walks, manifest not shipped | 13 of 17 on the scorer, 12 on re-score, not accepted |

Runs 4 to 6 led to the changes recorded in [CHANGELOG.md](CHANGELOG.md), v1.6.0: the seed's answers to the items the guide held stages on, then the history fixtures (ruling F) when live walks kept stopping before the stage under test, and fold 17 and its wording after RS-04. Run 3's transcripts are in [evidence/](evidence/transcripts-2026-10-18-T5/README.md); the GPT-era runs of 17 September 2026 are in [regression-suite.md](regression-suite.md) section 4 and lapse on 17 December 2026, the first day they are more than 90 days old.

---

Final Liability rests with the Human.
