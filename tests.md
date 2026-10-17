# Tests

**Part of Origami Method · last changed in v1.5.0 · 18 October 2026 · License: [CC BY-NC-SA 4.0](LICENSE)**

## Cases

The cases are in [regression-suite.md](regression-suite.md) and are not repeated here: seventeen cases, RS-01 to RS-17, each with setup, prompt, expected behavior, pass criteria and basis; the two run forms; the acceptance rule; and the results log. A full run of the method on one fictional workflow, for comparison with what an assistant produces, is in [worked-example.md](worked-example.md).

## Known defects

1. **RS-15, image request routed past the instructions.** Open against the GPT configuration as Locked on 1 October 2026: under the model displayed as Thinking 5.6 the request went to image generation before the instructions applied, and the same block declined it with Thinking off ([regression-suite.md](regression-suite.md) section 4, re-run 2c). Whether it reproduces on any successor configuration is Unknown; no run is logged.
2. **Packet status "Tested".** [builder-packet-template.md](builder-packet-template.md) lists a packet's status as one of Draft, Tested or Released (field 1) and defines Tested in its version and status rules; the instruction block and the worked example know only Draft and Released. Recorded, not fixed (reviewer report 12, item A10): the fix is a fold, either dropping Tested from the template or adding it to the block through the candidate mechanism.
3. **Evidence unpublished for three runs.** Run 1 Session 1 and re-runs 2b and 2c were pasted by the maintainer and have no share link or transcript in this repository; their rows are marked "evidence unpublished" in the results log (reviewer report 12, item B2).

## Last run

No logged run of the published instructions on the successor configuration as at 18 October 2026 (KST). Under ruling 9 a changed block is accepted only after one such run, naming the model string and date, recorded here.

History, GPT era: every logged run was made on 17 September 2026 on the GPT configuration now Locked (model displayed in GPT Builder as Thinking 5.6). Run 1 in walk-through form scored 11 of 13; three isolated re-runs on candidate v2 closed it at 13 of 13; Run 2 on the four tool-invitation cases scored 3 of 4; re-runs 2a to 2c left the configuration at 16 of 17 with RS-15 open. The rows, evidence and rulings are in [regression-suite.md](regression-suite.md) section 4. Under that suite's section 5 a logged run more than 90 days old counts as no run, so these runs lapse on 16 December 2026; they are not evidence about any successor configuration.

---

Final Liability rests with the Human.
