# Origami Method

**Version 1.5.0 · 18 October 2026 · Instrument, formerly the Origami Workflow Guide custom GPT (retired 1 October 2026) · Instructions last verified against the GPT on 17 September 2026, before the conversion · License: [CC BY-NC-SA 4.0](LICENSE)**

> **Retired 1 October 2026 (KST).** The Origami Workflow Guide custom GPT was retired on 1 October 2026 and converted to a private plug-in on the OpenAI platform. The instructions published in this repository are the text of record and suffice for anyone who wants to build their own. History and sources: [RETIREMENT.md](https://github.com/rolldabones/rolldabones/blob/main/RETIREMENT.md).

## What it does

The instructions in [instructions.md](instructions.md) make any current assistant a structured instructor for designing repeatable, safe AI workflows, especially workflows that use custom GPTs as components. Instead of generating the user's final deliverable (a report, deck or memo), it guides the user through a disciplined sequence of stages that define the goal, gather the needed context, set boundaries and specify exactly what inputs and outputs should look like. The result is a workflow blueprint: templates, checklists, role definitions, gates and test cases that can be implemented reliably.

This repository is the method reference (the stages, the rules that make approvals and risk ratings reproducible, a Builder Packet template, a worked example and a regression suite, listed under [Build kit](#build-kit)) and the text of record of the instructions.

## Run it in three steps

1. Paste the fenced block in [instructions.md](instructions.md) into the system prompt, custom instructions or project instructions of any current assistant. There is no reference file.
2. Give it the inputs it asks for: it opens at Stage 0 with two questions. To see the whole method on one workflow first, start from the seed in [worked-example.md](worked-example.md).
3. Review the output yourself and check the assistant's behavior against the cases in [tests.md](tests.md). You own sign-off.

## The method in brief

The assistant works one stage at a time on purpose. Each stage produces a concrete artifact (a Target Statement, Context Packet, risk and RACI assignment, data-handling plan, input and output schemas, gates and role permissions) and it does not proceed until the user confirms. This enforces clarity, prevents hidden assumptions and makes gaps explicit ("Unknown / Insufficient data") rather than letting the system invent requirements. Changes to a working workflow are controlled "folds": minimal, recorded and re-tested instead of ad hoc rewrites.

It works this way because workflows fail under pressure when they are clever but underspecified: missing constraints, unclear decision ownership, weak data handling and no validation plan. By front-loading creases (input and output rules), gates (pass/fail checks) and testing (cases plus validation logs), the method produces systems that behave predictably, are easier to audit and can scale across teams without drifting into unsafe or inconsistent outputs.

Twelve gated steps, run strictly in order, one confirmed artifact per step: ten numbered stages (0 to 9) and two checkpoints (3.5 and 7.5).

- **0. Orientation**: first-time and personal-vs-organization onboarding
- **1. Target Statement**: the whole workflow in one sentence
- **2. Context Packet**: objective, decision owner, background, inputs, boundaries, definition of done, known unknowns
- **3. Risk level and RACI**: Impact × Likelihood classification read from the [risk matrix](risk-and-approval-rules.md#1-risk-matrix), mitigations, escalation triggers
- **3.5 Data Handling Review**: sensitivity class, PII/PHI/financial presence, locality and retention, processors, redaction plan, approval owner
- **4. Creases**: input rules and output skeleton
- **5. Base A workflow**: the conservative five-step baseline, intake → draft → self-check → review → finalize; a review failure routes back to draft, and finalize requires the decision owner's approval
- **6. Gates**: pass/fail checks with fail routing, automated and human
- **7. Custom GPT roles**: roles, permissions, allowed tools, escalation rules
- **7.5 Export Readiness**: the checklist and the design sign-off that must pass before Builder Packets are generated, at status Draft
- **8. Testing and validation**: testing table (8A), validation log (8B) and release approval (8C), after which packets are Released and the workflow is ready to use
- **9. Improvement using folds**: Compress, Expose, Invert, Refactor, Lock, Audit; every change recorded, re-tested and re-approved

"Base A" names the conservative baseline workflow every design starts from. Variants are folds away from Base A, never fresh improvisations.

Core vocabulary: **Sheet** (project materials), **Creases** (input and output rules), **Folds** (controlled change), **Unfolding** (test and fix), **Lock** (freeze a proven step), **Expose** (add diagnostics to see failure).

## Approvals and the export sequence

Two states that earlier versions of this method left to inference are now named.

**Ready to export** means Design Approval has been recorded at Stage 7.5: every artifact from Stage 1 to Stage 7 is at a confirmed version, the Stage 8A test table has its inputs and expected values filled and the decision owner has signed the design off by name and date. Builder Packets may then be generated, one per role, at status **Draft**. A Draft packet built into a GPT is a test configuration.

**Ready to use** means Release Approval (8C) has been recorded: every 8A case is at P on the same built configuration in the same run, the 8B validation log is written, every carried unknown is resolved or accepted with a reason and the decision owner (the Accountable party where the Overall rating is Med or High) has approved the packet versions by name and date. Packets are re-issued at status **Released** only then.

So the sequence is: approve the design → export Draft packets → run the tests → approve the release. The earlier wording, which asked at Stage 7.5 for gates "tested" and a "sign-off captured" before any test had run, was circular, and it is one of the items an external review of the 6 September 2026 release identified.

Approvals are recorded, not implied. There are four approvals of record (Risk and RACI, Data Handling, Design, Release), each consisting of approver, artifact and version, date and the word "approved". A change to an approved artifact reopens its stage and invalidates every later approval until re-test and re-approval; the [invalidation table](risk-and-approval-rules.md#4-invalidation-what-reopens-what) says which change reopens what. The rules in full, including the risk matrix, the blocking unknowns and a Workflow Record template, are in [risk-and-approval-rules.md](risk-and-approval-rules.md).

**Instruction status.** The compact form of these rules entered the instructions on 17 September 2026 as folds 6 and 8, tested against the [regression suite](regression-suite.md) on the GPT configuration of that date. They are in [instructions.md](instructions.md); how the next change is made is under [Change control](#change-control).

## Build kit

| File | What it is |
|---|---|
| [README.md](README.md) | This file: method reference, how to run it, fold history, change control, release checks |
| [instructions.md](instructions.md) | The instructions, text of record: candidate v3.1 as last verified against the GPT on 17 September 2026, with its character count and SHA-256 |
| [builder-packet-template.md](builder-packet-template.md) | The thirteen required fields of a Builder Packet, each tied to the stage that produces it; a copy-ready template; a completeness check; the mapping from packet to the settings of an assistant, with GPT Builder kept as a historical example |
| [worked-example.md](worked-example.md) | The whole method run on one fictional workflow, public meeting notes to a reviewed action list: every stage artifact, three Draft packets, a test that failed, the fold that fixed it, the re-test and Release Approval |
| [risk-and-approval-rules.md](risk-and-approval-rules.md) | The risk matrix and its floors, which unknowns hold a gate, what an approval of record is, what changes invalidate which approvals and the Workflow Record template |
| [regression-suite.md](regression-suite.md) | Seventeen cases with setup, expected behavior, pass criteria and basis, and the results log: Run 1 of 17 September 2026 (walk-through form, 11 of 13), the three isolated re-runs that closed it at 13 of 13, and Run 2 the same evening with its re-runs (the four tool-invitation cases: three passed; RS-15 was open on the GPT configuration when it was Locked), with the share links as evidence where published |
| [tests.md](tests.md) | Pointer to the regression suite, the known defects and the Last run record for the successor configuration |
| [candidate-instructions.md](candidate-instructions.md) | The candidate mechanism: how an instruction change is cut, run as a system prompt on a current frontier model against the regression suite with one logged run, and only then copied into instructions.md. No candidate is pending; the file carries the instrument block, verified identical to instructions.md by the check script, the four cuts of 17 September 2026 and their diffs, and the procedure for the next change |
| [tools/check_release.py](tools/check_release.py) | Release consistency check, no dependencies beyond Python 3: version and date lockstep across README, CHANGELOG.md and CITATION.cff; each companion masthead naming a release that exists, and this release if the file changed since the last tag; internal links and anchors; the thirteen packet fields in the template and in every packet of the example; the instrument block's stated character count and SHA-256 in instructions.md against its bytes; the candidate block's size, and its identity with instructions.md while no candidate is pending or its diff while one is; the closing line as the last line of every markdown file |
| [CHANGELOG.md](CHANGELOG.md), [CITATION.cff](CITATION.cff), [LICENSE](LICENSE) | Release history, citation metadata, CC BY-NC-SA 4.0 |

## Doctrine connections

The method operationalizes the three doctrines that run through this account:

- The stage gates and mandatory confirmations are **Informed Intent** in miniature: nothing proceeds without prior authorization carrying the elements and conditions stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md#8-short-forms).
- The "Unknown / Insufficient data" rule is **Slow AI**: evidence over assurances, gaps declared rather than guessed.
- The mandatory session closing line is the third doctrine verbatim: **Final Liability rests with the Human.**

## When to use this

Use the Origami Method when you are designing a specific repeatable workflow, particularly one built from custom GPT components. For the broader 12-step governed AI methodology from individual task discipline to institutional program governance, use [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen). For the question of whether an AI system should be deployed at all, run the [AI-Impact-Assessment-Tool](https://github.com/rolldabones/AI-Impact-Assessment-Tool).

## Fold history and proposed folds

Observations about the GPT configuration up to its conversion, recorded per the method's own discipline, each typed with the method's fold vocabulary. Until 1 October 2026 a fold was applied by changing production first, testing with the regression suite, then updating this file and the changelog. From this release a fold is applied as under [Change control](#change-control); the mechanism is in [candidate-instructions.md](candidate-instructions.md).

**Applied 17 September 2026**, each tested on the GPT configuration of that date before the mirror was refreshed:

1. **Refactor.** Quick Start Stage 1 read "We want to use custom GPTs..." while the Stage 1 template read "We will use custom GPTs...". Aligned on "We will".
2. **Lock.** Scope was carried by the role definition alone. An explicit scope hard stop now declines deliverable and execution requests in one sentence and returns to the current stage (RS-02).
5. **Refactor.** The Stage 5 prose read intake → production → review → revision → approval against a template and a README reading intake → draft → self-check → review → finalize. One canonical flow, with the revision loop and the final approval stated.
6. **Lock.** The export and validation sequence: Stage 7.5 requires design sign-off and produces packets at Draft; 8C Release Approval is recorded only when every 8A case is P; packets become Released, and the workflow ready to use, only then (RS-07, RS-08, RS-10).
7. **Lock.** The thirteen Builder Packet fields and a one-line Workflow Record in the ready-to-copy artifacts (RS-09).
8. **Refactor.** The matrix rule and the data floor at Stage 3; the definition of an approval of record in the operating discipline (RS-08).
9. **Refactor.** Single-workflow mode now asks which workflow comes first rather than choosing. Run 1 showed the guide choosing; the order is the human's decision (RS-11).
10. **Lock.** Any change or correction to an approved artifact (role, packet, crease or gate) is a fold, logged at Stage 9 before re-test, and reopens its stage. Run 1 showed a Producer correction being treated as outside the fold log (RS-07).
11. **Lock.** A sample of the deliverable is the deliverable: the scope hard stop now names it, and the role definition ends "You never generate images." Cut after RS-15 showed the guide producing a marketing image on request; a heading trim paid for it. It holds where the model reads the block, which the Thinking-off run of RS-15 showed, and it did not reach the Thinking 5.6 routing, which is why Image Generation was also disabled and RS-15 stayed open (RS-02, RS-15).

**Closed 17 September 2026**, neither of them instruction text:

3. **Audit.** Tool access can tempt drift into the execution work the instructions exclude. Tested by Run 2 of the regression suite, one invitation per capability then enabled as the first message of a fresh session (RS-14 to RS-17): Web Search, Code Interpreter and Canvas held; Image Generation did not, and the guide produced the deliverable. Image Generation was disabled the same evening, which removed the output and not the routing: under Thinking 5.6 the request still goes to image generation and returns a platform error, on the v2 block and on the two cuts that followed, while the same block with Thinking off declines and opens Stage 0. Closed as an audit; its finding is open as RS-15 against the model setting, with the residual stated in the suite.
4. **Expose (optional).** Conversation starters such as "Start Stage 0." and "Enable Expert Mode." would make the entry points visible. Withdrawn by the maintainer on 17 September 2026: none were configured and none will be added; the entry points stay in the instructions.

Nothing is proposed.

Folds 5 to 8 came from an external review of the 6 September 2026 release, received 17 September 2026. Folds 9 and 10 came from Run 1 of the regression suite the same day, and fold 11 from Run 2 the same evening; folds 3 and 4 were closed that evening, one by Run 2 and one by decision. The block is 7,890 characters. The GPT Builder ceiling, reported at 8,000 and not found in official documentation, no longer binds; the check script keeps its warning line at 7,900 as this repository's size discipline, so the next fold still pays for itself in characters or does not enter.

## Maintenance and release checks

Two things version separately in this repository. The **documentation release** is the version in the masthead, CHANGELOG.md and CITATION.cff, and moves with every change to any file. The **instruction block** in [instructions.md](instructions.md) moves only when a candidate is accepted under [Change control](#change-control). Its last verification against the GPT, 17 September 2026, is a historical date and no longer moves: the GPT configuration has been Locked since 1 October 2026.

Before every commit:

```
python3 tools/check_release.py
```

It exits non-zero and names the line on any of: a version or date that disagrees across the README masthead, footer and How to Cite block, the newest CHANGELOG.md entry and CITATION.cff; a companion masthead naming a release that is not in the changelog, or naming an earlier release when the file has changed since the last tag; an internal link or heading anchor that does not resolve; a packet in the worked example missing any of the thirteen fields, or the template disagreeing with the example on what they are; an instruction block in instructions.md whose bytes disagree with the character count or SHA-256 stated there; a candidate block at or above 7,900 characters, or whose stated size or diff has gone stale; a markdown file whose last line is not the closing line. It reads; it never writes. It exists because this repository's changelog records the README's footer version lagging its masthead twice, both found by reading.

Companion files carry "last changed in vX.Y.Z" rather than the current version, because a version line records the release in which a file's substance last changed; moving it on a release that did not touch the file would be a false claim. The README, CHANGELOG.md and CITATION.cff move on every release. The substance test needs git history; without it the script says NOT CHECKED rather than passing that part.

## Regulatory and standards note

This repository makes no regulatory or standards alignment claims. RACI, PII/PHI and data-sensitivity vocabulary is used generically as workflow-design prompts, not as compliance representations. Reviewed 17 September 2026 (KST), covering the companion files added earlier that day and the changes of the two releases since; the worked example relies on no legal rule and says so at its Stage 2 boundaries, and the regression suite's fixtures are invented.

## Change control

The GPT configuration is Locked as of 1 October 2026, Lock being the method's own fold type: it is archived in [CHANGELOG.md](CHANGELOG.md) under v1.5.0 and no longer changes. Changes are made in [instructions.md](instructions.md) under this repository's version rule: a change to the block is a minor release, as when production changed on 17 September 2026 (v1.4.0). A changed block is accepted only after one logged run of the published instructions as a system prompt on a current frontier model, recorded in [tests.md](tests.md) with the model string and date. The procedure is in [candidate-instructions.md](candidate-instructions.md): cut a candidate there, run it against the [regression suite](regression-suite.md), log the run and only then copy it into instructions.md in the next release. Never the other way round. While no candidate is pending, the check script verifies that the block in that file is identical to instructions.md; while one is, it verifies the file's diff against instructions.md from the bytes.

## Part of the ecosystem

This method is one component of a larger body of AI governance, risk management and compliance work. The canonical map of all repositories is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository.

The three doctrines are used in this repository as stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement. Where this repository restates a doctrine, it restates it at its own altitude and adds instruments, not doctrine (ECOSYSTEM.md protocol item 6).

Nearest neighbors:
- [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen): the 12-step governed AI methodology; Origami is the workflow-design discipline within that larger arc
- [grc](https://github.com/rolldabones/grc): the GRCnext™ primitives this method's vocabulary maps to, with creases as Tolerances, gates as Switches and folds as controlled change
- [AI-Impact-Assessment-Tool](https://github.com/rolldabones/AI-Impact-Assessment-Tool): the pre-deployment gate; run it on what Origami designs
- [AI-Governance-Academy](https://github.com/rolldabones/AI-Governance-Academy): prompt templates for client-facing governance engagements built with this kind of method
- [computational-drafting](https://github.com/rolldabones/computational-drafting): the specification layer whose eight-element artifact the Context Packet and folds carry into a workflow

## How to Cite

> Paik, Son-U Michael. *Origami Method*, v1.5.0. GRC Solutions Korea, 2026. https://github.com/rolldabones/origami-method

A machine-readable citation is in [CITATION.cff](CITATION.cff).

## License

Creative Commons Attribution-NonCommercial-ShareAlike 4.0 International ([CC BY-NC-SA 4.0](LICENSE)).

---

**v1.5.0 · 18 October 2026 · License: [CC BY-NC-SA 4.0](LICENSE) · Changes: [CHANGELOG.md](CHANGELOG.md)**

Final Liability rests with the Human.
