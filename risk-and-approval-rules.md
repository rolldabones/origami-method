# Risk and approval rules

**Part of Origami Method · last changed in v1.2.0 · 17 September 2026 · License: [CC BY-NC-SA 4.0](LICENSE)**

The deployed instructions classify risk as Impact × Likelihood, each Low, Med or High, and require approvals at Stage 3, Stage 3.5, Stage 7.5 and, from this version of the method, at release. They do not say how the two ratings combine, which unknowns hold a gate, what an approval consists of or what undoes one. This file says so. It is method reference; the compact form of the same rules is proposed for the instructions themselves in [candidate-instructions.md](candidate-instructions.md), folds 6 and 8, and is not deployed.

Thresholds and floors below are the author's judgment. They are stated so they can be disagreed with, not derived from any standard.

## 1. Risk matrix

### 1.1 Rating Impact

| Rating | Meaning |
|---|---|
| High | A wrong or leaked output could harm a person, create legal or regulatory exposure, cause financial loss the decision owner would need to report upward or cannot be reversed once acted on |
| Med | A wrong output would be caught downstream at real cost: rework, a delayed decision, an embarrassing correction, a loss the decision owner can absorb without reporting |
| Low | A wrong output is cosmetic, or is corrected in the normal course of review before anyone acts on it |

### 1.2 Rating Likelihood

| Rating | Meaning |
|---|---|
| High | The failure is expected in ordinary use: inputs vary, the task needs judgment, the model has been seen to get it wrong |
| Med | The failure is plausible under foreseeable conditions: an unusual input, a busy reviewer, a source in a new format |
| Low | The failure needs conditions that do not arise in the workflow as designed |

Rate Likelihood for the workflow **without** the mitigations you are about to design. Mitigations are recorded at Stage 3 and tested at Stage 8; rating them into the Likelihood before they exist is how a High workflow reaches Stage 7.5 rated Low.

### 1.3 The matrix

| Impact \ Likelihood | Low | Med | High |
|---|---|---|---|
| **Low** | Low | Low | Med |
| **Med** | Low | Med | High |
| **High** | Med | High | High |

Read across from Impact, down from Likelihood. The Overall rating is the cell.

Two floors apply after the cell is read:

- A workflow whose Stage 3.5 sensitivity class is Confidential or Restricted rates no lower than **Med** overall.
- A workflow whose output is acted on without a Human reading it first rates no lower than **High** overall. The method assumes a Human reads; a design that removes the reader is a High design whatever the cell says.

### 1.4 What the Overall rating requires

| Overall | Minimum controls the design must carry |
|---|---|
| Low | Self-check step (Stage 5 step 3) against creases and gates; one human review before finalize |
| Med | Everything in Low; at least one automated gate at intake; human review by someone other than the person who requested the output; Release Approval by the Accountable party in the RACI |
| High | Everything in Med; a Red-Team role in the Base A review step; human gate before any handoff between roles; no autonomous handoff; escalation trigger tied to every High-impact failure mode; re-test of the full Stage 8A table after any fold, not only the impacted cases |

A design that cannot carry the controls its rating requires does not proceed. It either changes scope to lower the rating, which reopens Stage 1, or it stops.

## 2. Unknowns: blocking and carried

The method's rule is that a missing item is written as "Unknown / Insufficient data" and requested. Not every unknown holds the gate. The table names the ones that do.

| Stage | Blocking unknowns (the stage cannot be confirmed) | Carried unknowns (recorded with an owner and a due stage, then confirmed past) |
|---|---|---|
| 1 Target | Deliverable; decision owner; the decision | Boundaries not yet named |
| 2 Context Packet | Decision owner; definition of done; the privacy and jurisdiction boundaries | Background detail; a listed input not yet in hand |
| 3 Risk and RACI | Impact; Likelihood; the Accountable party | Consulted and Informed parties; mitigations still being drafted |
| 3.5 Data Handling | Sensitivity class; whether PII, PHI or financial data is present; approval owner | Retention period; the list of third-party processors, provided none is known to touch Restricted data |
| 4 Creases | Acceptance criteria for the output | Optional sections of the skeleton |
| 5 Base A | Which step carries the human review | Naming of the role at each step |
| 6 Gates | Fail routing for any gate | Automation of a gate that a Human can run by hand in the meantime |
| 7 Roles | Permissions and forbidden tools for any role | Escalation contact's deputy |
| 7.5 Export Readiness (design approval) | Any checklist item | None; the checklist is the gate |
| 8 Testing | Expected value for any test case; the result of any test case | Notes |
| Release Approval | Any open blocking unknown from any stage; any test case at F without a passed re-test | None |

A carried unknown is written into the Workflow Record with three things: what is unknown, who owns finding out and the stage by which it must be resolved. Every carried unknown is either resolved or explicitly accepted by the decision owner, with the reason, before Release Approval. An accepted unknown is a recorded decision, not a gap.

## 3. Approvals of record

An approval is recorded, not implied. A confirmation in the session ("continue", "looks right", "next stage") advances the stage and is not an approval of record. The method has four approvals of record.

| Approval | Stage | Who | What is approved |
|---|---|---|---|
| Risk and RACI | 3 | The Accountable party named in the RACI | The Impact, Likelihood and Overall ratings; the RACI; the mitigations; the escalation triggers |
| Data Handling | 3.5 | The approval owner named in the Data Handling Review | The sensitivity class; the redaction and minimization plan; the processors; the locality and retention rules |
| Design | 7.5 | The decision owner | The whole design as it stands: the versions of every artifact from Stage 1 to Stage 7, the Stage 8A test table with expected values filled and actual values empty |
| Release | after 8 | The decision owner, or the Accountable party where the Overall rating is Med or High | The Stage 8A table with every case at P, the Stage 8B validation log, the fold log and the Builder Packets at the versions being released |

Each approval of record consists of five things, written into the Workflow Record: the approver's name and role; the artifact and version approved; the date; the word "approved", or "approved with conditions" followed by the conditions; and, for Release Approval, the packet versions. An approval missing any of the five is not an approval.

**Design Approval is what makes a workflow ready to export.** Builder Packets may be generated once it is recorded, at status Draft. **Release Approval is what makes a workflow ready to use.** Packets are re-issued at status Released once it is recorded, and not before. A Draft packet built into a GPT is a test configuration, not a working one, and the packet says so on its face.

## 4. Invalidation: what reopens what

Any change to an approved artifact invalidates the approval of the stage that produced it and every approval of record downstream of that stage. Re-approval follows re-test. The table names the common cases so that nobody has to reason it out under pressure.

| Change | Stages reopened | Approvals invalidated |
|---|---|---|
| Deliverable, decision owner or the decision changes | 1 and everything after it | All four |
| A new input source, file type or data class is introduced, including confidential or restricted data reaching a workflow designed for public or internal data | 3.5, 4, 6, 7, 8 | Data Handling, Design, Release |
| A boundary changes (privacy, jurisdiction, time, tone) | 2, 3, 3.5, 8 | Risk and RACI, Data Handling, Design, Release |
| Impact or Likelihood is re-rated | 3, 6, 8 | Risk and RACI, Design, Release |
| The output skeleton or its acceptance criteria change | 4, 6, 8 | Design, Release |
| A gate's pass criteria or fail routing change | 6, 8 | Design, Release |
| A tool, capability, permission or third-party processor is added | 3.5, 7, 6, 8 | Data Handling, Design, Release |
| A role is added or removed, or an escalation rule changes | 7, 6, 8 | Design, Release |
| A fold of type Compress, Refactor or Invert is applied | The stages the fold log names, then 8 | Release, until the re-test passes and Release Approval is recorded again |
| A fold of type Expose, Lock or Audit is applied | 8 | Release, re-confirmed by the decision owner on the re-test result |
| The underlying model or platform changes version | 8 | Release |
| The Accountable party or decision owner is replaced | 3 | Risk and RACI; Design and Release stand only if the new party re-confirms them by name |

Two consequences the table implies and this paragraph states outright. First, a fold never moves a workflow from Released to Released; it moves it to Draft and the re-test moves it back. Second, "we only added one field" is a change to the output skeleton and is in the table. The size of a change is not what decides whether an approval survives it.

## 5. Workflow Record

One record per workflow, kept by the decision owner or the person they name, updated at every stage confirmation and every approval. It is the compact record the export packets cite as their provenance. Copy the block and fill it in.

```
WORKFLOW RECORD

Workflow name: …
Record version: …            Date of this version: …
Current stage: …             Mode: standard / expert
Decision owner: …            Accountable party (RACI): …
Approval owner (data): …

ARTIFACT VERSIONS
Target Statement v…      Context Packet v…      Risk and RACI v…
Data Handling Review v…  Creases v…             Base A v…
Gates v…                 Roles v…               Builder Packets v… (status: Draft / Released)
Testing Table 8A v…      Validation Log 8B v…   Fold Log v…

APPROVALS OF RECORD (name and role | artifact and version | date | approved / approved with conditions)
Risk and RACI: …
Data Handling: …
Design: …
Release: …

OPEN UNKNOWNS (what | owner | blocking? | due stage | resolved or accepted, with reason)
…

FOLDS APPLIED (see Fold Log): …
LAST RE-TEST: date … | result … | cases re-run …
```

A Workflow Record whose Release Approval line is empty describes a workflow that is not in use. If it is in use anyway, that is the first finding.

---

Final Liability rests with the Human.
