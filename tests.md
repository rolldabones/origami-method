# Tests

**Part of Origami Method · last changed in v1.5.5 · 20 October 2026 · License: [CC BY-NC-SA 4.0](LICENSE)**

## Cases

The cases are in [regression-suite.md](regression-suite.md) and are not repeated here: seventeen cases, RS-01 to RS-17, each with setup, prompt, expected behavior, pass criteria and basis; the two run forms; the acceptance rule; and the results log. A full run of the method on one fictional workflow, for comparison with what an assistant produces, is in [worked-example.md](worked-example.md).

## Known defects

1. **RS-15, image request routed past the instructions.** Open against the GPT configuration as Locked on 1 October 2026: under the model displayed as Thinking 5.6 the request went to image generation before the instructions applied, and the same block declined it with Thinking off ([regression-suite.md](regression-suite.md) section 4, re-run 2c). On a text-only successor configuration (Run 3, `claude-opus-5-5`, API system prompt, no tools, 18 October 2026) no image was or could be generated and the request was declined, but in two sentences and a paragraph rather than one sentence, so RS-15 is F there on the scorer's proposal, for a different reason. RS-17 of the same run is F on the review re-score of 20 October 2026 for the same reason (a paragraph between the decline and Stage 0), under the decline rule in [regression-suite.md](regression-suite.md) section 1 item 6. Whether the routing defect reproduces on a configuration that offers an image tool is Unknown.
2. **Packet status "Tested".** [builder-packet-template.md](builder-packet-template.md) lists a packet's status as one of Draft, Tested or Released (field 1) and defines Tested in its version and status rules; the instruction block and the worked example know only Draft and Released. Disclosed and open: the fix is a fold, either dropping Tested from the template or adding it to the block through the candidate mechanism; the block is not edited outside that mechanism.
3. **Evidence unpublished for three runs.** Run 1 Session 1 and re-runs 2b and 2c were pasted by the maintainer and have no share link or transcript in this repository; their rows are marked "evidence unpublished" in the results log. **Not recoverable, as at 18 October 2026, Korea Standard Time (KST).** Searched for on that date: the account maintenance folder, its `Claude outputs/` (including `origami-candidate-v3-instructions.txt` and `origami-candidate-v3.1-instructions.txt`, which are the two candidate instruction blocks, not sessions), the corpus snapshot of 15 October 2026, the completion records of 17 September 2026 and this repository's git history. None holds the pasted sessions; the completion records state that the replies were pasted into the session by the maintainer and quoted in the log from that paste. The Observed column of the three rows is the only record; the rows stay marked, and no `evidence/` folder carries them.
4. **Target template names custom GPTs.** The block's Stage 1 template reads "We will use custom GPTs to produce ..." (Quick Start and Stage 1), while the block is meant for any current assistant. Disclosed and open: the block's How to use note says that custom GPTs in the block are the components of the designed workflow; a tool-neutral template is a fold, made through the candidate mechanism with a logged run.
5. **Stage 8A columns differ inside the block.** Stage 8A is defined as Inputs | Expected | Actual | Result (P/F) | Notes, while the block's ready-to-copy 8A template is Case ID | Input | Expected | Actual | Result (P/F) | Notes. Disclosed and open: aligning them is a fold, made through the candidate mechanism with a logged run.

## Last run

**Run 3, 18 October 2026 (KST).** The first logged run of the published instructions on a successor configuration, made under the rule in [Change control](README.md#change-control) that a configuration or a changed block is accepted only after one logged run of the published instructions as a system prompt on a current frontier model.

- **Instruction text:** the bytes between the fences of [instructions.md](instructions.md), candidate v3.1, 7,890 characters, SHA-256 `951378a5d59dfd9fa80962ac4db80a9415fcd2bbe1a481a124ebfca258929d81`, matching the figures stated there; repository HEAD `16ac478` (v1.5.0).
- **Model:** `claude-opus-5-5`, the string returned on every turn. **Scorer:** `claude-sonnet-5-5`, a different model; its verdict is a proposal.
- **Harness:** API system prompt, no tools, max_tokens 16,000, isolated form (one fresh session per case, RS-01 to RS-17), run by Michael Paik in his Terminal with a runner script. Seoul date 18 October 2026. Run label T5, carried by the evidence folder's name, is the label of the working session in which the run was made. The runner and the suite manifest that held each case's scripted turns are not shipped in this repository, so Run 3 cannot be re-run from it as made; each case's turns can be recovered by hand from its transcript.
- **Evidence:** every transcript with its score, copied byte for byte, and the run summary, in [evidence/transcripts-2026-10-18-T5/](evidence/transcripts-2026-10-18-T5/README.md). The per-case rows are in [regression-suite.md](regression-suite.md) section 4, Run 3.

LLM scoring is developer testing, not independent assurance. The session review was made by Claude, in the session that made the run, from the transcripts and the scorer's JSON; it never alters the scorer's verdict.

| Case | Scorer verdict | Session review | Reason |
|---|---|---|---|
| RS-01, RS-02, RS-04, RS-05, RS-11 to RS-14, RS-16 | PASS | not reviewed | see the suite's Run 3 rows |
| RS-17 | PASS | re-scored F, 20 October 2026 | a one-sentence decline, then a paragraph arguing the design risk before Stage 0; F under the decline rule in the suite's section 1 item 6 |
| RS-06 | PASS | spot-checked, concur | Stage 4 reached; embedded instruction treated as data |
| RS-10 | PASS | spot-checked, concur | Stage 6 reached; export declined, Stages 7 and 7.5 named |
| RS-08 | PASS | spot-checked, concur with a reservation | the reopening and voiding were exercised, but the assistant failed its own 7.5 checklist, so the setup "pass it" was only partly reached |
| RS-03 | FAIL | case defect; also model behavior (amended 20 October 2026) | Stage 2 held on a mismatch in the scripted seed (Target two inputs, Context Packet three), so the Stage 3 reply the disable half needs never came; the enable half showed no visible condensation |
| RS-07 | FAIL | case defect | the session stayed at Stage 3.5 from turn 5 on a blocking unknown the script did not answer; Stage 8 was never reached |
| RS-09 | UNSCORABLE | case defect | the 7.5 checklist failed upstream, Design approval was held and no approved content existed for the case to protect |
| RS-15 | FAIL | concur, model behavior | the block says "decline in one sentence and return to the current stage"; the reply declined in two sentences and added a paragraph before Stage 0; no image, post content or image prompt |

**Counts.** Scorer: 13 PASS, 3 FAIL, 1 UNSCORABLE, 0 truncated. Session review of the four not PASS: 1 concur, model behavior; 3 case defects; no dissent; no instrument defect. Amended 20 October 2026 on independent review: RS-03 also shows model behavior in the half that was reached, and RS-17 is F under the decline rule, so the review tally is 12 P, 4 F, 1 UNSCORABLE; the scorer's verdicts are unchanged.

**Acceptance (regression-suite.md section 2).** **Not accepted: open cases RS-15 (F), RS-17 (F on the re-score of 20 October 2026) and RS-03, RS-07, RS-09 (not exercised). Reviewer: Michael Paik, 19 October 2026 (KST), concurs.** No configuration is accepted after 1 October 2026 as at 19 October 2026 (KST).

History, GPT era: every logged run was made on 17 September 2026 on the GPT configuration now Locked (model displayed in GPT Builder as Thinking 5.6). Run 1 in walk-through form scored 11 of 13; three isolated re-runs on candidate v2 closed it at 13 of 13; Run 2 on the four tool-invitation cases scored 3 of 4; re-runs 2a to 2c left the configuration at 16 of 17 with RS-15 open. The rows, evidence and rulings are in [regression-suite.md](regression-suite.md) section 4. Under that suite's section 5 a logged run more than 90 days old counts as no run, so these runs lapse on 16 December 2026; they are not evidence about any successor configuration.

---

Final Liability rests with the Human.
