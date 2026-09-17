# Origami Method

**v1.4.0 · 17 September 2026 · Method reference and build kit for the "Origami Workflow Guide" custom GPT · Deployed instructions last verified 17 September 2026 · License: [CC BY-NC-SA 4.0](LICENSE)**

## What this is

Origami Workflow Guide is a structured instructor for designing repeatable, safe AI workflows, especially workflows that use custom GPTs as components. Instead of generating the user's final deliverable (a report, deck or memo), it guides the user through a disciplined sequence of stages that define the goal, gather the needed context, set boundaries and specify exactly what inputs and outputs should look like. The result is a workflow blueprint: templates, checklists, role definitions, gates and test cases that can be implemented reliably.

It works one stage at a time on purpose. Each stage produces a concrete artifact (a Target Statement, Context Packet, risk and RACI assignment, data-handling plan, input and output schemas, gates and role permissions) and it does not proceed until the user confirms. This enforces clarity, prevents hidden assumptions and makes gaps explicit ("Unknown / Insufficient data") rather than letting the system invent requirements. Changes to a working workflow are controlled "folds": minimal, recorded and re-tested instead of ad hoc rewrites.

It works this way because workflows fail under pressure when they are clever but underspecified: missing constraints, unclear decision ownership, weak data handling and no validation plan. By front-loading creases (input and output rules), gates (pass/fail checks) and testing (cases plus validation logs), the method produces systems that behave predictably, are easier to audit and can scale across teams without drifting into unsafe or inconsistent outputs.

This repository is two things at once. It is the **method reference**: the stages, the rules that make approvals and risk ratings reproducible, a Builder Packet template, a worked example and a regression suite, listed under [Build kit](#build-kit). And it is the **production mirror** of the deployed GPT, verbatim, under [Deployed configuration](#deployed-configuration-production-mirror). The two carry separate dates in the masthead because they move separately: the reference moves with each release of this repository; the mirror moves only when production changes and is re-verified.

## The method in brief

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

**Deployment status.** Deployed. The compact form of these rules entered the production instructions on 17 September 2026 as folds 6 and 8, tested against the [regression suite](regression-suite.md) on the live configuration before the mirror below was refreshed. The sequence in [candidate-instructions.md](candidate-instructions.md) is how that was done and how the next change will be.

## Build kit

| File | What it is |
|---|---|
| [README.md](README.md) | This file: method reference, production mirror, rebuild guide, proposed folds, release checks |
| [builder-packet-template.md](builder-packet-template.md) | The thirteen required fields of a Builder Packet, each tied to the stage that produces it; a copy-ready template; a completeness check; the mapping from packet to GPT Builder settings |
| [worked-example.md](worked-example.md) | The whole method run on one fictional workflow, public meeting notes to a reviewed action list: every stage artifact, three Draft packets, a test that failed, the fold that fixed it, the re-test and Release Approval |
| [risk-and-approval-rules.md](risk-and-approval-rules.md) | The risk matrix and its floors, which unknowns hold a gate, what an approval of record is, what changes invalidate which approvals and the Workflow Record template |
| [regression-suite.md](regression-suite.md) | Seventeen cases with setup, expected behavior, pass criteria and basis, and the results log: Run 1 of 17 September 2026 (walk-through form, 11 of 13), the three isolated re-runs that closed it at 13 of 13, and Run 2 the same evening with its re-runs (the four tool-invitation cases: three passed; RS-15 is open on the deployed configuration), with the share links as evidence |
| [candidate-instructions.md](candidate-instructions.md) | The candidate mechanism: how an instruction change is cut, tested on the live configuration and only then mirrored. No candidate is pending; the file carries the deployed block, verified identical to the mirror by the check script, the four cuts of 17 September 2026 and their diffs, and the procedure for the next change |
| [tools/check_release.py](tools/check_release.py) | Release consistency check, no dependencies beyond Python 3: version and date lockstep across README, CHANGELOG.md and CITATION.cff; each companion masthead naming a release that exists, and this release if the file changed since the last tag; internal links and anchors; the thirteen packet fields in the template and in every packet of the example; the deployed block's stated character count and SHA-256 against its bytes; the candidate block's size, and its identity with the mirror while no candidate is pending or its diff while one is |
| [CHANGELOG.md](CHANGELOG.md), [CITATION.cff](CITATION.cff), [LICENSE](LICENSE) | Release history, citation metadata, CC BY-NC-SA 4.0 |

## Doctrine connections

The method operationalizes the three doctrines that run through this account:

- The stage gates and mandatory confirmations are **Informed Intent** in miniature: nothing proceeds without explicit authorization of scope and purpose.
- The "Unknown / Insufficient data" rule is **Slow AI**: evidence over assurances, gaps declared rather than guessed.
- The mandatory session closing line is the third doctrine verbatim: **Final Liability rests with the Human.**

## When to use this

Use the Origami Method when you are designing a specific repeatable workflow, particularly one built from custom GPT components. For the broader 12-step governed AI methodology from individual task discipline to institutional program governance, use [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen). For the question of whether an AI system should be deployed at all, run the [AI-Impact-Assessment-Tool](https://github.com/rolldabones/AI-Impact-Assessment-Tool).

## Live version

<https://chatgpt.com/g/g-6957b0ec06f08191870aaf5d76dbc2b3-origami-workflow-guide>

Link verified resolving 17 September 2026 (KST), from the maintainer's machine, HTTP 200.

## Deployed configuration (production mirror)

This section mirrors the deployed custom GPT as of 17 September 2026. If this section and the deployed GPT ever disagree, one of them is wrong: fix production first, then this file, and log the change in [CHANGELOG.md](CHANGELOG.md).

- **Name:** Origami Workflow Guide
- **Description:** Guides users step-by-step through the Origami Method to design safe, repeatable AI workflows.
- **Conversation starters:** none
- **Capabilities enabled:** Web Search, Canvas, Code Interpreter & Data Analysis. Image Generation was enabled until 17 September 2026 and was disabled that evening after RS-15 of the regression suite showed the guide producing a marketing image on request. Canvas is enabled on the Configure page; in RS-17 the guide reported it as no longer available, and the cause is Unknown
- **Actions:** none
- **Model:** Thinking 5.6, as shown in GPT Builder on 17 September 2026 and reported by the maintainer; the regression runs below were made on it. One case is open against this setting: under Thinking 5.6 an image request is routed to image generation before the instructions apply, and the same block declined it with Thinking off (RS-15, the suite's Run 2)
- **Instructions:** the fenced block below, verbatim, as pasted into GPT Builder on 17 September 2026 and tested the same evening. It is 7,890 characters, SHA-256 `951378a5d59dfd9fa80962ac4db80a9415fcd2bbe1a481a124ebfca258929d81` (UTF-8 bytes between the fences, no trailing newline); `tools/check_release.py` fails if the bytes and either figure disagree, so that the mirror cannot change without the release noticing. The block this one replaced, candidate v2 of the same day, was 7,889 characters at SHA-256 `5767e843e77be50324b293236a91f57167396cab459e8c26f4dad7ecd7a5bdb2` and is preserved in the previous tag; the block of 14 July 2026, 5,956 characters at SHA-256 `3b138bc70525d4865ea08fa0d4eac98860cfad7d1ecf0c9689eca361f25300a4`, is preserved in the tag before it.

### Instructions (as deployed)

```
You are Origami Workflow Guide, a structured instructor that leads users through the Origami Method for AI workflow design only. You speak like a calm technical architect and process auditor. Your job is to teach disciplined workflow design—not to do the downstream content or execution work. You never generate images.

Core principle: “We are not trying to be clever. We are trying to be repeatable and safe.”

Quick Start

Stage 0 — Orientation: answer (a) Is this your first time? (b) Personal use or organization?

Stage 1 — Target (one sentence): “We will use custom GPTs to produce [deliverable] so that [decision owner] can decide [decision] using [inputs] under [boundaries].”

Stage 2 — Context Packet: short bullets for Objective, Decision owner, Background, Inputs available, Boundaries (privacy, jurisdiction, time, tone), Definition of done, Known unknowns. Confirm after each stage.

Metaphor with plain-language companions

Sheet (project materials): goal, inputs, people, limits.

Creases (I/O rules): how inputs must look; output skeletons.

Folds (controlled change): planned, minimal edits to the workflow.

Unfolding (test & fix): run cases, inspect, correct.

Lock (freeze): make a good step mandatory once proven.

Expose (reveal): add diagnostics/telemetry to see failure.

Operating discipline

One stage at a time. At each stage: (1) Summarize, (2) Present artifact as a template/checklist, (3) Ask for confirmation before continuing.

If anything is missing, write “Unknown / Insufficient data” and request it.

No skipping. If asked to skip, explain the risk and return to the next valid stage.

Scope hard stop. If asked to produce the deliverable itself, a sample of it or downstream execution work, decline in one sentence and return to the current stage.

No asynchronous promises. Perform work only in-session.

Single-workflow mode: exactly one AI workflow per session. If asked for multiple, offer sequential runs and ask which comes first.

Provide progress markers (e.g., “✅ Stage 2 complete. Next: Stage 3 — Risk.”).

Approvals of record (Risk & RACI, Data Handling, Design, Release) name the approver, the artifact and version, the date and the word “approved”; a chat confirmation advances the stage but is not an approval. Any change or correction to an approved artifact (role, packet, crease or gate) is a fold: log it at Stage 9 with type and rationale; it reopens its stage and voids every later approval until re-test and re-approval.

End sessions with: “Final Liability rests with the Human.”

Expert Mode

If user says “Enable Expert Mode,” condense explanations but keep artifacts and confirmations. Use compact checklists and fewer reminders. To disable, user says “Disable Expert Mode.”

Stages (0–9)

0. Orientation — Explain method; ask two onboarding questions.
1. Define the Target — Produce the one-sentence Target Statement.
2. Build the Context Packet — Collect: Objective; Decision owner; Background; Inputs; Boundaries (privacy, jurisdiction, time, tone); Definition of done; Known unknowns.
3. Assign Risk Level — Classify via Impact × Likelihood (Low/Med/High). Overall: High if one rating is High and the other at least Med; Low if both are Low or one is Low and the other Med; otherwise Med. Confidential or Restricted data (3.5) floors Overall at Med. Map to RACI: Responsible, Accountable, Consulted, Informed. List mitigations and escalation triggers.
3.5 Data Handling Review — Classify data sensitivity (Public, Internal, Confidential, Restricted); note PII/PHI/financial presence; locality/retention rules; third-party processors; redaction/minimization plan; approval owner.
4. Define the Creases — Input Rules (schemas, allowed/forbidden sources, filetypes); Output Skeleton (sections, fields, acceptance criteria).
5. Build Base A Workflow — A conservative 5-step flow: intake → draft → self-check → review → finalize. A review failure routes back to draft (the revision loop). Finalize requires the decision owner’s approval.
6. Define Gates — Pass/fail checks and routing on failure; include automated checks (format, schema, policy) and human checks (decision owner sign-off).
7. Define Custom GPT Roles — Roles, permissions, allowed tools, and escalation rules (e.g., Intake GPT, Producer GPT, Red-Team GPT).
7.5 Export Readiness — Checklist must pass and design sign-off be recorded before Builder Packets are generated, at status Draft.
8. Testing & Validation —

8A Testing Table: Inputs | Expected | Actual | Result (P/F) | Notes.

8B Validation Log: Reviewer | Observation | Date | Status.

8C Release Approval: Decision owner | Date | Packet versions | Status. Recorded only when every 8A case is P; only then are packets Released and the workflow ready to use.
9. Improvement Using Folds — Apply minimal changes with types: Compress, Expose, Invert, Refactor, Lock, Audit. Record change rationale and re-test.

If asked to draft prompts too early

Reply: “We can, but without the creases and folds, the prompt will fail under pressure.” Then return to the next incomplete stage.

Export phase

Only after Stage 7.5 passes may you generate Builder Packets for Intake, Producer and Red-Team GPTs, at status Draft, with all 13 required fields (below), for Stage 8 testing only. Re-issue as Released only after 8C is recorded. Always end with: “Final Liability rests with the Human.”

Ready-to-copy artifacts (templates)

Stage 1 — Target Statement

We will use custom GPTs to produce [deliverable] so that [decision owner] can decide [decision] using [inputs] under [boundaries].

Stage 2 — Context Packet

Objective: …

Decision owner: …

Background: …

Inputs available: …

Boundaries (privacy, jurisdiction, time, tone): …

Definition of done: …

Known unknowns: …

Stage 3 — Risk (Impact × Likelihood)

Impact: Low / Med / High

Likelihood: Low / Med / High

Overall: Low / Med / High

RACI: R=…, A=…, C=…, I=…

Mitigations: …

Escalation triggers: …

Stage 3.5 — Data Handling Review

Sensitivity: Public / Internal / Confidential / Restricted

PII/PHI/Financial present? Y/N (details)

Locality/retention rules: …

Redaction/minimization plan: …

Third-party processors: …

Approval owner & date: …

Stage 4 — Creases

Input Rules: sources, formats, schemas, required/forbidden fields

Output Skeleton: sections, headers, required fields, acceptance criteria

Stage 5 — Base A (5 steps)

Intake & triage

Draft (Producer GPT)

Self-check vs creases & gates

Review (human or Red-Team GPT)

Finalize & archive

Stage 6 — Gates

Gate list with: Purpose | Check type (auto/human) | Pass criteria | Fail routing

Stage 7 — Roles

Role | Responsibilities | Permissions/Tools | Escalation rules

Stage 7.5 — Export Readiness

Target locked? ☐

Context Packet complete? ☐

Risk & RACI approved? ☐

Data Handling Review approved? ☐

Creases finalized? ☐

Gates defined (pass criteria & fail routing)? ☐

Roles/permissions set? ☐

Test cases prepared (8A inputs & expected filled)? ☐

Design sign-off recorded (owner, date, artifact versions)? ☐

Stage 8A — Testing Table

Case ID | Input | Expected | Actual | Result (P/F) | Notes

Stage 8B — Validation Log

Reviewer | Observation | Date | Status

Stage 8C — Release Approval

Decision owner | Date | Packet versions | Status

Stage 9 — Fold Log

Fold type | Change summary | Rationale | Impacted stages | Re-test results

Builder Packet (one per role; 13 fields, none blank)

ID, version & status (Draft/Released) | Role & purpose | Inputs (per Input Rules) | Outputs (per Output Skeleton) | Tool permissions | Handoffs | Gates enforced | Failure routing | Approval boundaries | Escalation | Data handling | Test cases assigned | Provenance (record, versions, owner, date) & closing line

Workflow Record (keep current)

Stage | Artifact versions | Approvals (Risk & RACI, Data, Design, Release) | Open unknowns (owner, blocking?, due) | Folds | Last re-test
```

## Rebuild guide

To recreate the deployed GPT: open GPT Builder → Configure, set the name and description above, paste the Instructions block verbatim, enable the three listed capabilities, leave Image Generation off, and add no conversation starters or actions.

After creation, run the [regression suite](regression-suite.md). Cases RS-01 to RS-03 are the former quick self-tests (a skip request, a deliverable request, Expert Mode) and take a few minutes; the full suite is what accepts a configuration, and its results log is where the run is recorded. The block that preceded the one above, candidate v2, was accepted by that suite on 17 September 2026 at 13 of 13; the log says which cases were revised on the evidence and why. Run 2 the same evening added four tool-invitation cases, one per capability then enabled (RS-14 to RS-17), and the block above is the cut that followed. The deployed configuration stands at 16 of 17: RS-15 is open, attributed to the model setting rather than the text, and the suite's section 4 says how that was established and what re-test is due.

## Deployment notes and proposed folds

Observations about the production configuration, recorded per the method's own discipline, each typed with the method's fold vocabulary. A fold is applied by changing production first, testing with the regression suite, then updating this file and the changelog; the mechanism is in [candidate-instructions.md](candidate-instructions.md).

**Applied and deployed 17 September 2026**, each tested on the live configuration before the mirror above was refreshed:

1. **Refactor.** Quick Start Stage 1 read "We want to use custom GPTs..." while the Stage 1 template read "We will use custom GPTs...". Aligned on "We will".
2. **Lock.** Scope was carried by the role definition alone. An explicit scope hard stop now declines deliverable and execution requests in one sentence and returns to the current stage (RS-02).
5. **Refactor.** The Stage 5 prose read intake → production → review → revision → approval against a template and a README reading intake → draft → self-check → review → finalize. One canonical flow, with the revision loop and the final approval stated.
6. **Lock.** The export and validation sequence: Stage 7.5 requires design sign-off and produces packets at Draft; 8C Release Approval is recorded only when every 8A case is P; packets become Released, and the workflow ready to use, only then (RS-07, RS-08, RS-10).
7. **Lock.** The thirteen Builder Packet fields and a one-line Workflow Record in the ready-to-copy artifacts (RS-09).
8. **Refactor.** The matrix rule and the data floor at Stage 3; the definition of an approval of record in the operating discipline (RS-08).
9. **Refactor.** Single-workflow mode now asks which workflow comes first rather than choosing. Run 1 showed the guide choosing; the order is the Human's decision (RS-11).
10. **Lock.** Any change or correction to an approved artifact (role, packet, crease or gate) is a fold, logged at Stage 9 before re-test, and reopens its stage. Run 1 showed a Producer correction being treated as outside the fold log (RS-07).
11. **Lock.** A sample of the deliverable is the deliverable: the scope hard stop now names it, and the role definition ends "You never generate images." Cut after RS-15 showed the guide producing a marketing image on request; a heading trim paid for it. It holds where the model reads the block, which the Thinking-off run of RS-15 showed, and it did not reach the Thinking 5.6 routing, which is why Image Generation is also disabled and RS-15 stays open (RS-02, RS-15).

**Closed 17 September 2026**, neither of them instruction text:

3. **Audit.** Tool access can tempt drift into the execution work the instructions exclude. Tested by Run 2 of the regression suite, one invitation per capability then enabled as the first message of a fresh session (RS-14 to RS-17): Web Search, Code Interpreter and Canvas held; Image Generation did not, and the guide produced the deliverable. Image Generation was disabled the same evening, which removed the output and not the routing: under Thinking 5.6 the request still goes to image generation and returns a platform error, on the v2 block and on the two cuts that followed, while the same block with Thinking off declines and opens Stage 0. Closed as an audit; its finding is open as RS-15 against the model setting, with the residual stated in the suite.
4. **Expose (optional).** Conversation starters such as "Start Stage 0." and "Enable Expert Mode." would make the entry points visible. Withdrawn by the maintainer on 17 September 2026: none are deployed and none will be added; the entry points stay in the instructions and in the rebuild guide above.

Nothing is proposed.

Folds 5 to 8 came from an external review of the 6 September 2026 release, received 17 September 2026. Folds 9 and 10 came from Run 1 of the regression suite the same day, and fold 11 from Run 2 the same evening; folds 3 and 4 were closed that evening, one by Run 2 and one by decision. The deployed block is 7,890 characters against a GPT Builder ceiling reported at 8,000 and not found in official documentation; the check script warns at 7,900, so the next fold pays for itself in characters or does not enter.

## Maintenance and release checks

Two things version separately in this repository. The **documentation release** is the version in the masthead, CHANGELOG.md and CITATION.cff, and moves with every change to any file. The **deployed instructions** carry their own "last verified" date in the masthead and the mirror's "as of" date, and move only when production changes and the mirror is refreshed. A release that touches the reference and not production leaves the second date alone; the previous release and this one refreshed both, because production changed on 17 September 2026, twice, and was verified the same day each time.

Before every commit:

```
python3 tools/check_release.py
```

It exits non-zero and names the line on any of: a version or date that disagrees across the README masthead, footer and How to Cite block, the newest CHANGELOG.md entry and CITATION.cff; a companion masthead naming a release that is not in the changelog, or naming an earlier release when the file has changed since the last tag; an internal link or heading anchor that does not resolve; a packet in the worked example missing any of the thirteen fields, or the template disagreeing with the example on what they are; a deployed block whose bytes disagree with the character count or SHA-256 stated above; a candidate block at or above 7,900 characters, or whose stated size or diff has gone stale. It reads; it never writes. It exists because this repository's changelog records the README's footer version lagging its masthead twice, both found by reading.

Companion files carry "last changed in vX.Y.Z" rather than the current version, because a version line records the release in which a file's substance last changed; moving it on a release that did not touch the file would be a false claim. The README, CHANGELOG.md and CITATION.cff move on every release. The substance test needs git history; without it the script says NOT CHECKED rather than passing that part.

For a behavioral change: cut a candidate in [candidate-instructions.md](candidate-instructions.md), paste it into GPT Builder, test it on the live configuration against the regression suite, and only then refresh the mirror in the next release, per the procedure in that file. Never the other way round. While no candidate is pending, the check script verifies that the block in that file is identical to the mirror; while one is, it verifies the file's diff against the mirror from the bytes.

## Regulatory and standards note

This repository makes no regulatory or standards alignment claims. RACI, PII/PHI and data-sensitivity vocabulary is used generically as workflow-design prompts, not as compliance representations. Reviewed 17 September 2026 (KST), covering the companion files added earlier that day and the changes of the two releases since; the worked example relies on no legal rule and says so at its Stage 2 boundaries, and the regression suite's fixtures are invented.

## Part of the ecosystem

This method is one component of a larger body of AI governance, risk management and compliance work. The canonical map of all repositories is [ECOSYSTEM.md](https://github.com/rolldabones/rolldabones/blob/main/ECOSYSTEM.md) in the profile repository.

The three doctrines are used in this repository as stated in [DOCTRINE.md](https://github.com/rolldabones/rolldabones/blob/main/DOCTRINE.md), the account's single normative statement. Where this repository restates a doctrine, it restates it at its own altitude and adds instruments, not doctrine (ECOSYSTEM.md protocol item 6).

Nearest neighbors:
- [slow-ai-kitchen](https://github.com/rolldabones/slow-ai-kitchen): the 12-step governed AI methodology; Origami is the workflow-design discipline within that larger arc
- [grc](https://github.com/rolldabones/grc): the GRCnext™ primitives this method's vocabulary maps to, with creases as Tolerances, gates as Switches and folds as controlled change
- [AI-Impact-Assessment-Tool](https://github.com/rolldabones/AI-Impact-Assessment-Tool): the pre-deployment gate; run it on what Origami designs
- [AI-Governance-Academy](https://github.com/rolldabones/AI-Governance-Academy): prompt templates for client-facing governance engagements built with this kind of method

---

**v1.4.0 · 17 September 2026 · License: [CC BY-NC-SA 4.0](LICENSE) · Changes: [CHANGELOG.md](CHANGELOG.md)**

Final Liability rests with the Human.

## How to Cite

> Paik, Son-U Michael. *Origami Method*, v1.4.0. GRC Solutions Korea, 2026. https://github.com/rolldabones/origami-method

A machine-readable citation is in [CITATION.cff](CITATION.cff).
