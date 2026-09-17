# Changelog

All notable changes to this repository are documented here. Versioning follows [Semantic Versioning](https://semver.org/). The README and this file version in lockstep; prior versions are superseded, never silently overwritten.

## v1.2.0 (2026-09-17)

Method reference and build kit. An external review of v1.1.3, received 17 September 2026, made six recommendations, all of which were checked against the repository bytes and all of which held. This release ships the documentation side of all six and stages the instruction-level changes as a tested-before-deployed candidate. Minor rather than patch: five companion files and a check script are new, and the README's method reference changes in substance. The production mirror is unchanged byte for byte.

### Added
- **`builder-packet-template.md`.** The thirteen required fields of a Builder Packet, each tied to the stage that produces it; a copy-ready template; a completeness check; the mapping from packet fields to GPT Builder settings; the Draft, Tested and Released status rules. Until now the deployed text promised packets "with all required fields" and defined none.
- **`worked-example.md`.** The whole method run by hand on one fictional workflow, public meeting notes to a reviewed action list: every stage artifact, four approvals of record, three Draft packets, a Stage 8 test that failed (a hedged suggestion read as an assignment), the Refactor and Expose folds that fixed it, the re-test at 5 of 5, Release Approval and the Workflow Record at close. It is not a transcript of the live GPT and says so.
- **`risk-and-approval-rules.md`.** How Impact and Likelihood combine (a 3 × 3 matrix with two floors, stated as the author's judgment); which unknowns block a stage gate and which are carried; the four approvals of record and the five elements each must have; what changes reopen which stages and invalidate which approvals; a Workflow Record template.
- **`regression-suite.md`.** Thirteen cases replacing the three quick self-tests: the three former cases renumbered RS-01 to RS-03, the six the review asked for (incomplete context, conflicting requirements, instructions embedded in source material, a failed gate, a changed approved input, an incomplete packet) as RS-04 to RS-09 and four rules the deployed block already states as RS-10 to RS-13. Each case carries setup, prompt, expected behavior, pass criteria and its basis, marked where the basis is a candidate fold rather than the deployed text. **No run is recorded.** The results log is empty and says so; the review did not test the live GPT and neither did this release.
- **`candidate-instructions.md`.** The deployed block with folds 1, 2, 5, 6, 7 and 8 applied as exact replacements, 7,797 characters against a GPT Builder ceiling reported at 8,000, the deployment procedure and a unified diff generated from the bytes. **Not deployed.** The mirror in the README stays verbatim until the candidate passes the regression suite on the live configuration. Fold 2, the scope hard stop, is the maintainer's own proposal of 14 July 2026 rather than the review's, included so that the candidate is the whole pending fold set; strike it from the candidate before deployment if it is to be tested on its own.
- **`tools/check_release.py`.** Release consistency check, Python 3 only, no dependencies. Version and date lockstep across the README masthead, footer and How to Cite block, the newest changelog entry and `CITATION.cff`; each companion masthead naming a release that exists in the changelog, with its date, and naming this release where the file changed since the last tag (the substance test, which needs git and says NOT CHECKED without it); internal links and heading anchors outside fenced blocks; the thirteen packet fields in the template against every packet in the example and the candidate's compact packet line; the deployed block's character count and SHA-256 against the figures the README states; the candidate block's size and stated size; and its diff against a fresh one. Exits non-zero on any failure and refuses to pass when an input is missing. Proved before release by breaking each condition it tests and watching it fail, then repairing and watching it pass; the controls are recorded in the maintainer's completion record for this session.

### Changed
- **Masthead carries two dates.** The documentation release (v1.2.0 · 17 September 2026) and the deployed instructions' last verified date (14 July 2026) now version separately, and the "Maintenance and release checks" section says which moves when.
- **"The method in brief" corrected.** The heading line read "Ten gated stages" over a twelve-entry list. It now reads twelve gated steps: ten numbered stages and two checkpoints. Stage 5 states the canonical flow (intake → draft → self-check → review → finalize) with the revision loop and the final approval; Stage 7.5 states that packets are generated at Draft; Stage 8 gains release approval (8C). List separators changed from spaced dashes to colons, house style.
- **New section "Approvals and the export sequence"** naming ready to export (Design Approval at 7.5) and ready to use (Release Approval after Stage 8), the four approvals of record, the invalidation rule and the deployment status of each. The earlier Stage 7.5 checklist asked for gates "tested" and a "sign-off captured" before any test had run; that circularity is recorded here rather than silently corrected.
- **New section "Build kit"** listing every file and what it is for.
- **Rebuild guide** now points at the regression suite; the three self-tests are RS-01 to RS-03 there and are not restated.
- **Deployment notes and proposed folds** gains folds 5 to 8 (Stage 5 flow; export and validation sequence; packet fields; risk matrix, approval of record and invalidation rule), states which folds are text and which are tests or configuration and names the candidate file. Folds 1 to 4 stand as written on 14 July 2026, except that fold 2's reference to self-test B now reads RS-02.
- **New section "Maintenance and release checks"** with the check script's invocation and the rule for behavioral changes: candidate tested on the live configuration first, mirror refreshed in the next release, never the other way round.
- **Production mirror section** now states the deployed block's character count (5,956) and SHA-256, which the check script recomputes from the bytes on every run.
- **Regulatory and standards note** re-dated to 17 September 2026 on a review of every file in this release, including the five new ones. No alignment claim is made anywhere; the worked example relies on no legal rule and says so.
- `CITATION.cff` and the How to Cite block moved to v1.2.0 in lockstep. Header and footer version lines likewise. Companion files carry "last changed in v1.2.0" rather than a lockstep version, on the account's practice that a version line records the release in which a file's substance last changed.

### Unchanged
- **The production mirror.** The Instructions block is byte for byte the text supplied from GPT Builder on 14 July 2026, and the name, description, capabilities, conversation starters and actions are as recorded then. The live GPT was not changed in this release and no claim is made about how it behaves on the new cases.
- The live-version link's verification date (14 July 2026). Not re-verified in this release; chatgpt.com is not reachable from the environment the release was prepared in.
- `LICENSE`, byte for byte.

### Verified (2026-09-17, KST)
- `python3 tools/check_release.py` passes on the release bytes: 5 companion files each naming v1.2.0 as the release that last changed them, every internal link and anchor resolving, 3 packets carrying all 13 fields in order, deployed block at 5,956 characters with the stated SHA-256, candidate block at 7,797 characters with a matching diff.
- The deployed block extracted from this README is identical to the block extracted from the v1.1.3 README.
- Each of the six review claims was re-read against the v1.1.3 bytes before any edit: the twelve-entry list under "Ten gated stages"; the Stage 5 prose against the Stage 5 template; the Stage 7.5 items "Gates defined & tested?" and "Sign-off captured?" against Stage 8; "all required fields" with no field defined; the three self-tests; the changelog's "second occurrence" of a lockstep lag. All six held.

## v1.1.3 (2026-09-06)

Citation infrastructure, doctrine citation line and lockstep maintenance. Session C of the September 2026 improvement pack, one patch release per repository across all 21 public repositories.

- **`CITATION.cff` added** in the house form settled at D-C1: no `type` field, `version` and `date-released` in lockstep with the README, `license` as the SPDX identifier for this repository's licence, `abstract` taken from this repository's ECOSYSTEM.md role line rather than newly written.
- **How to Cite block** aligned to this release and pointing at `CITATION.cff`.
- **Doctrine citation line added** to the Part of the ecosystem section. This repository restates a doctrine and cited DOCTRINE.md nowhere, which is the Class E2 finding the new guards report.
- **Lockstep lag corrected, second occurrence.** The closing version block read `v1.1.1 · 30 July 2026` against a masthead of `v1.1.2`. Found by reading in Session C, not by any guard.
- All other files in this repository are unchanged byte for byte.

## v1.1.2 (2026-08-13)

License metadata sweep. An `SPDX-License-Identifier: CC-BY-NC-SA-4.0` line and the canonical Creative Commons legal code are now carried inside the existing license file. The filename is unchanged and the human-readable summary is retained above the legal code.

- The primary audience is automated intake and provenance tooling, which reads the SPDX tag rather than prose. Automated license detection previously reported nothing across all twenty-one repositories in this account.
- No change to the licence in force. The identifier records what was already true.

## v1.1.1 (2026-07-30)

Patch release. Trademark rendering only.

### Changed
- Trademark rendering corrected to the canonical closed-up form GRCnext™. The retired spaced form "GRC next" is withdrawn from repository prose. One occurrence, in the grc line of the Part of the ecosystem section.
- Header and footer version lines updated in lockstep.

### Unchanged
- The method, the fold vocabulary and the production-mirror instruction block.

## v1.1.0 (2026-07-14)

First versioned release under the repository improvement program. The pre-existing README is treated as implicit v1.0.0.

### Added
- Version, date and license header; version and license footer.
- Deployed-configuration section mirroring the production GPT verbatim as of 14 July 2026: name, description, no conversation starters, four enabled capabilities, no actions and the full Instructions text as supplied from GPT Builder.
- "Deployment notes and proposed folds" section recording four observations about the production configuration (Target Statement phrasing inconsistency, implicit rather than explicit scope hard stop, all capabilities enabled, no conversation starters), each typed with the method's own fold vocabulary.
- Doctrine connections section: stage gates as Informed Intent, the "Unknown / Insufficient data" rule as Slow AI, the mandatory closing line as Final Liability rests with the Human.
- "When to use this" positioning against slow-ai-kitchen and the AI-Impact-Assessment-Tool.
- Regulatory and standards note dated 14 July 2026: no alignment claims are made; governance vocabulary is generic.
- "Base A" defined as the conservative baseline workflow every design starts from.
- "Part of the ecosystem" section linking the canonical ECOSYSTEM.md and four nearest neighbors.
- CHANGELOG.md and LICENSE (CC BY-NC-SA 4.0) added to the repository.

### Changed
- Instructions block replaced with the deployed text supplied from GPT Builder on 14 July 2026. The prior block differed materially from production: it contained a SCOPE / HARD BOUNDARIES section with an explicit deliverable-refusal rule, an explicit stage-enforcement sentence, MANDATORY-labeled progress-marker and end-of-session headings and a different export-phase closing sentence, none of which appear in the deployed instructions; section ordering also differed. Divergences the repo should push back into production are logged as proposed folds instead of being restated as fact.
- Builder setup notes rewritten as a rebuild guide that matches production exactly; the prior text claimed pasting the block would recreate "most of" the behavior, which is inconsistent with a verbatim mirror. The prior tool-configuration advice (consider disabling browsing/actions) contradicted the deployed configuration and now lives in the proposed-folds section as an Audit fold.
- Unicode mathematical-bold heading ("𝗢𝗿𝗶𝗴𝗮𝗺𝗶 𝗠𝗲𝘁𝗵𝗼𝗱") replaced with standard markdown; the special characters broke screen readers, in-page search, copy-paste and anchor links.
- Opening five-step summary replaced with a faithful listing of all stages including 3.5 and 7.5.
- Explanatory prose (what, how, why) moved to the top of the README and edited to house style.
- Short description updated to the deployed text ("Guides users step-by-step through the Origami Method to design safe, repeatable AI workflows.").
- Quick self-test B expectation reworded to match what the deployed instructions actually guarantee (redirection per the role definition rather than a scripted refusal).

### Verified (2026-07-14, KST)
- Live GPT link resolves; page title confirms "Origami Workflow Guide".
- Deployed name, description, conversation starters, capabilities and Instructions text supplied by the maintainer from GPT Builder on 14 July 2026.
- Repository reviewed for regulatory or standards alignment claims: none present; no currency note required.

Final Liability rests with the Human.
