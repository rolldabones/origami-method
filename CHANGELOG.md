# Changelog

All notable changes to this repository are documented here. Versioning follows [Semantic Versioning](https://semver.org/). The README and this file version in lockstep; prior versions are superseded, never silently overwritten.

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
