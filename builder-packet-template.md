# Builder Packet template

**Part of Origami Method · last changed in v1.2.0 · 17 September 2026 · License: [CC BY-NC-SA 4.0](LICENSE)**

## What a Builder Packet is

A Builder Packet is the export artifact of the Origami Method: everything a builder needs to configure one custom GPT role, Intake, Producer or Red-Team, without re-reading the design session. One packet per role. A packet carries no field the design stages did not produce, and every field below names the stage it comes from, so a blank field points at an unfinished stage rather than at a missing idea.

Packets are generated at status **Draft** once Design Approval (Stage 7.5) is recorded, and re-issued at status **Released** only after the Stage 8 tests pass and Release Approval is recorded. A Draft packet built into a GPT is a test configuration, not a working one. The sequence is in [README.md](README.md#approvals-and-the-export-sequence); what the two approvals require is in [risk-and-approval-rules.md](risk-and-approval-rules.md) section 3.

## The thirteen required fields

Every packet carries all thirteen. A field with nothing to put in it reads "Unknown / Insufficient data", and a packet with any field reading that way cannot leave Draft status.

| # | Field | Source stage | What goes in it |
|---|---|---|---|
| 1 | Packet ID, version and status | Export | `BP-<ROLE>`, a version and one of Draft, Tested or Released |
| 2 | Role and purpose | 7 and 1 | The role's name; one sentence on what it produces and for whom, derived from the Target Statement |
| 3 | Inputs | 4 (Input Rules) | Accepted sources, formats and schemas; required and forbidden fields; forbidden sources |
| 4 | Outputs | 4 (Output Skeleton) | The sections and required fields the role must produce; the acceptance criteria |
| 5 | Tool permissions | 7 and 3.5 | Capabilities the role may use; capabilities it may not; data classes it may touch; processors it may send data to |
| 6 | Handoffs | 5 | What the role receives, from whom, in what form; what it passes on, to whom, in what form; what triggers the handoff |
| 7 | Gates enforced | 6 | The gates this role runs, each with its pass criteria and check type |
| 8 | Failure routing | 6 | What the role does when a gate fails, when an input breaks a rule, when it meets an unknown |
| 9 | Approval boundaries | 3 (RACI) and 6 (human checks) | What the role may decide alone; what requires a Human; which Human |
| 10 | Escalation | 3 | The triggers and the person they escalate to |
| 11 | Data handling | 3.5 | Sensitivity class; redaction and minimization rules the role applies; retention rule for anything it keeps |
| 12 | Test cases assigned | 8A | The case IDs this role must pass before the packet can be marked Tested |
| 13 | Provenance and closing line | Workflow Record | The Workflow Record name and version; the artifact versions the packet was cut from; owner; date; and the mandatory session closing line the role's instructions must carry |

## Copy-ready template

```
BUILDER PACKET

1. Packet ID, version and status
   ID: BP-[INTAKE | PRODUCER | RED-TEAM]     Version: 0.1     Status: Draft

2. Role and purpose
   Role: …
   Purpose: Produces … so that [decision owner] can decide … (from the Target Statement)

3. Inputs (Stage 4 Input Rules)
   Accepted sources: …
   Formats and schema: …
   Required fields: …
   Forbidden fields and sources: …

4. Outputs (Stage 4 Output Skeleton)
   Sections and required fields: …
   Acceptance criteria: …

5. Tool permissions (Stage 7, Stage 3.5)
   Allowed capabilities: …
   Forbidden capabilities: …
   Data classes this role may touch: …
   Third-party processors this role may send data to: …

6. Handoffs (Stage 5)
   Receives: … from … as …
   Passes: … to … as …
   Handoff trigger: …

7. Gates enforced (Stage 6)
   Gate | Check type (auto / human) | Pass criteria
   …

8. Failure routing (Stage 6)
   On gate failure: …
   On input that breaks a rule: …
   On an unknown: write "Unknown / Insufficient data", then …

9. Approval boundaries (Stage 3 RACI, Stage 6 human checks)
   May decide alone: …
   Requires a Human: … (who: …)

10. Escalation (Stage 3)
   Triggers: …
   Escalate to: …

11. Data handling (Stage 3.5)
   Sensitivity class: …
   Redaction and minimization: …
   Retention: …

12. Test cases assigned (Stage 8A)
   …

13. Provenance and closing line
   Workflow Record: … v…
   Cut from: Target v… | Context Packet v… | Risk and RACI v… | Data Handling Review v… | Creases v… | Base A v… | Gates v… | Roles v…
   Owner: …     Date: …
   Every session run by this role ends with: "Final Liability rests with the Human."
```

## Completeness check

Run before a packet is handed to a builder, at Draft and again at Released.

- All thirteen fields present, in order, none reading "Unknown / Insufficient data" if the status is Released.
- Field 3 and field 4 restate the Stage 4 creases without adding to them. A packet is not the place to invent a new input rule.
- Field 5 lists at least one forbidden capability. A role with nothing forbidden has not been thought about.
- Field 6 names a receiving party for every output. An output nobody receives is either a gap in Base A or a deliverable the role should not be producing.
- Field 8 covers every gate in field 7. A gate with no fail routing is a gate that fails open.
- Field 9 names a Human for everything the role may not decide alone, and the Human named appears in the Stage 3 RACI.
- Field 12 lists at least one case per gate in field 7.
- Field 13 carries the closing line verbatim, and the artifact versions match the Workflow Record.

## From packet to GPT Builder

The packet is the specification. The GPT configuration is derived from it, not the other way round.

| GPT Builder setting | Take from |
|---|---|
| Name | Field 2, role |
| Description | Field 2, purpose |
| Instructions | Fields 2 to 11 and the closing line in field 13, in that order. Field 8 and field 9 are the part builders most often drop; they are the part the method exists for |
| Capabilities | Field 5. Enable only what is allowed; leave everything else off |
| Knowledge | Only files field 3 names as accepted sources and field 11 permits at that sensitivity class |
| Actions | None unless field 5 names a processor and field 11 permits it |
| Conversation starters | Optional; if used, phrase them as the handoff in field 6 ("Paste the validated notes from Intake") |

## Version and status rules

- **Draft** is the status a packet is born with, after Design Approval. It may be built into a GPT for testing only.
- **Tested** is recorded by whoever runs Stage 8 when every case in field 12 is at P on the built configuration. It is a note on the packet, not an approval.
- **Released** is recorded only when Release Approval is in the Workflow Record. Version moves to 1.0.
- Any change to any field is a fold: it is logged at Stage 9, the version increments, the status returns to Draft and the assigned cases are re-run. The invalidation table in [risk-and-approval-rules.md](risk-and-approval-rules.md) section 4 says which other approvals the change undoes.

A complete set of three packets, cut from a full run of the method on a fictional workflow, is in [worked-example.md](worked-example.md).

---

Final Liability rests with the Human.
