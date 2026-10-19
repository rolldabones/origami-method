# Changelog

All notable changes to this repository are documented here. Versioning follows [Semantic Versioning](https://semver.org/). The README and this file version in lockstep; prior versions are superseded, never silently overwritten.

## v1.5.3 (2026-10-19)

Patch, from the weekly maintenance sweep of 19 October 2026 (KST) and Michael Paik's review of the T5 runs, completed 19 October 2026 (KST), on which he concurs with the scoring as recorded. No change to `instructions.md` or `candidate-instructions.md`.

- **Run 3 reviewed.** The seventeen Run 3 rows of `regression-suite.md` section 4 carry the reviewer and "reviewer concurs" in place of "pending"; the tally line records the review, the scorer's line between RS-17 and RS-15 included. `tests.md` Acceptance records the review. Not accepted, as before: RS-15 F; RS-03, RS-07 and RS-09 not exercised.
- Companion mastheads of `regression-suite.md` and `tests.md` to v1.5.3. README masthead and footer, How to Cite and `CITATION.cff` to v1.5.3. The Run 3 configuration line names the reviewer.

## v1.5.2 (2026-10-18)

Front-door patch: the fold history leaves the README for the candidate file. Session T7 of the whole-account review of 15 October 2026 (KST), doc section 9, change 3 ("fold history to the candidate file"); reviewer report 12, item C1 (the change-control loop and the file where the next fold is cut). No instruction, rule, case or packet field changes.

### Changed
- **`README.md`** (21,604 bytes to 17,544): the section "Fold history and proposed folds" is moved out, sliced programmatically, and a three-line `## Fold history` stub points to its new place. Line 52 (the export sequence paragraph) loses a comma the account guard read as a serial comma; the sentence is the author's, not deployed text.
- **`candidate-instructions.md`, last changed in v1.5.2, dated amendment note:** gains `## Fold history` before `## Release procedure`, the README section's text unchanged apart from three link targets rewired for the new location (Change control now linked as `README.md#change-control`; "this file" and "the README" where the moved text pointed at itself or at the README). The candidate block, the status line and the release procedure do not change.
- **`regression-suite.md`:** RS-05's note reads "inferred, not stated; it is recorded as such" (the account guard's F6 line at :31, author prose in a table cell). The masthead moves to v1.5.2 because `tools/check_release.py` check 1 requires a changed companion to name the current release; no case, result or expected value changes.
- README masthead, footer and How to Cite, `CITATION.cff` and this file move to v1.5.2 in lockstep. `instructions.md`, `tests.md`, `risk-and-approval-rules.md`, `builder-packet-template.md`, `worked-example.md`, `tools/` and `evidence/` are unchanged byte for byte. `python3 tools/check_release.py` exits 0.

### Findings by class
- Confirmed and edited: doc section 9 change 3 (fold history to the candidate file); report 12 item C1 as far as it concerns where the fold record lives; the account guard's two F6 lines (README.md:52, regression-suite.md:31).
- Already fixed: report 12 item C1's re-targeting of the procedure at a named successor, and the one logged run, were done at v1.5.0 and v1.5.1 (T4 and T5).
- Not reproducible: none.
- Outside the review: none edited.
- Unknown: none.

### Deferred
- The v1.5.1 deferrals stand (the maintainer's ruling on the Run 3 rows; the re-run of RS-03, RS-07 and RS-09; the worked example's Target and Context Packet mismatch).

## v1.5.1 (2026-10-18)

Records-only patch: Run 3 logged (13 of 17 on the scorer's proposal, not accepted), unpublished evidence declared not recoverable, the text-only limit of the tool-invitation cases stated. Session T5 of the whole-account review of 15 October 2026 (KST), doc section 5 (origami-method row: "Run 3 on the successor configuration (section 4) or state that no accepted configuration exists after 1 October; publish the pasted sessions under `evidence/`"), under ruling 9; reviewer report 12, items A8 and B2. Dates are KST. No wording of the instruction block changes and no case changes; `instructions.md` is unchanged byte for byte (7,890 characters, SHA-256 `951378a5d59dfd9fa80962ac4db80a9415fcd2bbe1a481a124ebfca258929d81`).

### Changed
- **`tests.md`, known defect 3 (report 12 item B2):** the pasted sessions of Run 1 Session 1 and re-runs 2b and 2c are not recoverable, as at 18 October 2026. Searched on that date: the maintenance folder and its `Claude outputs/` (the two files `origami-candidate-v3-instructions.txt` and `origami-candidate-v3.1-instructions.txt` are candidate instruction blocks, not sessions), the corpus snapshot of 15 October 2026, the completion records of 17 September 2026 and this repository's git history. The rows stay marked "evidence unpublished"; no `evidence/` folder is created for them.
- **`regression-suite.md`, section 4 Evidence:** the same statement where the log describes its evidence.
- **`regression-suite.md`, section 5:** a new bullet, tool routing on a configuration with no tools: RS-14 to RS-17 run as an API system prompt test only the decline, and RS-15 there cannot reproduce the GPT-era routing defect.
- README masthead, footer and How to Cite, `CITATION.cff` and this file move to v1.5.1 in lockstep; the two changed companions' mastheads name this release.

### Run 3 (report 12 item A8)
Run 18 October 2026 in isolated form, one fresh session per case, RS-01 to RS-17: the bytes between the fences of `instructions.md` as an API system prompt on `claude-opus-5-5`, no tools, max_tokens 16,000; scored by `claude-sonnet-5-5`, a different model, whose verdict is a proposal for the maintainer's ruling.
- **Result:** scorer 13 PASS, 3 FAIL (RS-03, RS-07, RS-15), 1 UNSCORABLE (RS-09). Session review: RS-15 concur, model behavior (the decline ran to two sentences and a paragraph against "decline in one sentence"; no image, post content or image prompt); RS-03, RS-07 and RS-09 case defects (the scripted setup turns did not adapt to the assistant's replies, so the sessions were held at Stages 2, 3.5 and 7.5 on blocking items the script did not answer, and the state each case tests was not reached). One blocking item came from the seed: the worked example's Target names two inputs and its Context Packet three. No dissent; no instrument defect. Spot-checked PASS: RS-06, RS-10 and RS-08 (the last with a reservation recorded in the log).
- **Acceptance:** not accepted under section 2: open cases RS-15 and RS-03, RS-07, RS-09. Reviewer: pending (Michael Paik).
- **Records:** `regression-suite.md` section 4 gains the Run 3 block and rows (Result column: scorer proposal, reviewer pending); its introduction and the 17 September status paragraph name Run 3. `tests.md`: Last run section, known defect 1 updated for the text-only result. `candidate-instructions.md`: status line names Run 3. README: Build kit rows for the suite and `evidence/`, and the check-script descriptions.
- **Evidence:** `evidence/transcripts-2026-10-18-T5/`, the 17 transcripts copied byte for byte with the closing line appended, the runner's `summary.json` and an index (report 12 item B2 for future runs).
- **`tools/check_release.py`:** check 2 (internal links and anchors) no longer reads markdown files under `evidence/`: a transcript there is copied byte for byte and quotes links written relative to the repository root (RS-04's rule text cites `risk-and-approval-rules.md`), so it cannot be edited to resolve them. Check 6 (closing line last) still reads them.

### Findings by class
- Confirmed: A8 (no run on the successor configuration; Run 3 is now logged, not accepted), B2 (three runs without published evidence; now declared not recoverable).
- Already fixed: none in scope.
- Not reproducible: none.
- Outside the review: none edited.

### Deferred
- The maintainer's ruling on each Run 3 row and on acceptance.
- A re-run of RS-03, RS-07 and RS-09 with setup turns that answer the assistant's blocking items, or a seed whose Target and Context Packet agree; a later run.
- The worked example's Target and Context Packet input mismatch: reported, not edited (outside the review).

## v1.5.0 (2026-10-18)

Instrument form after the GPT retirement; instructions.md, change control re-targeted. Session T4 of the whole-account review of 15 October 2026 (KST), doc section 4, items 2 and 3, under determination D5 and ruling 9; reviewer report 12, items A6, A10, A17, A20, B1, B2, B6, B8, C5 and C7. Dates are KST. The Origami Workflow Guide custom GPT was retired on 1 October 2026 and converted to a private plug-in on the OpenAI platform; nothing in this release was verified against the plug-in. Minor rather than patch because the text of record of the instructions moves from the README to its own file and the change procedure changes. No wording of the instruction block changes, no regression case changes and no run is added (a run on the successor configuration is session T5's).

### Added
- **`instructions.md`:** the instrument, candidate v3.1, in one fenced block with its status line, its last verification (17 September 2026, before the conversion) and how to use it. The block is byte-identical to the README mirror it replaces: 7,890 characters, SHA-256 `951378a5d59dfd9fa80962ac4db80a9415fcd2bbe1a481a124ebfca258929d81`.
- **`tests.md`:** a pointer to `regression-suite.md` (the suite is not duplicated), the known defects (RS-15; packet status "Tested", report 12 item A10; three runs with unpublished evidence, item B2) and the **Last run** section: no logged run on the successor configuration as at 18 October 2026 (KST), with the GPT-era runs as history. The worked example stays in `worked-example.md`; no `example.md` is added.

### Changed
- **`README.md`** on the mirror template: retirement line under the masthead in place of the retirement notice; What it does; Run it in three steps; a Change control section (the configuration Locked as of 1 October 2026; changes in instructions.md under this repository's version rule; a changed block accepted only after one logged run on a current frontier model, recorded in tests.md); a License section above the footer. The Live version, Deployed configuration (production mirror) and Rebuild guide sections are removed: the block moved to instructions.md and the configuration is archived below. Fold history stays (report 12 item C1 is session T7's).
- **`candidate-instructions.md`:** the status line, the rationale, the size note and the procedure re-targeted (report 12 item B1): a candidate is cut here, run as a system prompt on a current frontier model against the regression suite with one logged run, and only then copied into instructions.md and released. The table of the four cuts and the historical diff trail are unchanged.
- **`regression-suite.md`:** the configuration record re-targeted at the successor fields (model string, date, interface); present-tense deployment wording recast; the 17 September 2026 status line marked as history; Run 1 Session 1 and re-runs 2b and 2c marked "evidence unpublished" (item B2). No case and no logged row changes.
- **`risk-and-approval-rules.md`:** line 5 no longer says the compact rules are proposed and not deployed; they entered the instructions on 17 September 2026 as folds 6 and 8 (item A6). Item C7 (*Human* as a common noun) was already fixed in v1.4.3.
- **`builder-packet-template.md`, house style:** two common-noun uses of *Human* lowercased under DOCTRINE.md section 6, ~~"what requires a Human; which Human"~~ in the field 9 row and ~~"names a Human ... the Human named"~~ in the completeness check; added 18 October 2026 on the author's instruction to settle the open items.
- **`builder-packet-template.md`:** "From packet to GPT Builder" becomes a mapping from packet field to system prompt or assistant setting, with GPT Builder kept as one historical example column (item B6). "Tested" in field 1 and the status rules is unchanged and recorded as a known defect in tests.md (item A10).
- **`worked-example.md`:** the "deployed instructions" and "live GPT" wording at line 7 recast (D5). No artifact of the example changes.
- **`tools/check_release.py`:** the instrument identity check (4) now reads the block and its stated count and SHA-256 from instructions.md, not the README; check 5 compares the candidate block with instructions.md and accepts the status "candidate, not released"; the README masthead may open "**Version"; check 6 now also fails when the closing line is not a file's last non-empty line; `--help` prints the usage and the six checks (item B8, in part; fence-glue detection not added).
- **`CITATION.cff`:** `version` 1.5.0 and `date-released` 2026-10-18; the abstract now carries the conversion (item A20). README masthead, footer and How to Cite move to v1.5.0 in lockstep; every changed companion's masthead names this release.

### Instruction block changes (old → new)
None. The last verified text was checked for GPT-only dependencies: it has no conversation starters, no Start triggers keyed to starters, no capability toggles, no knowledge file or "per reference" pointer and no statement of the 8,000-character ceiling. "You never generate images." is a scope rule and stays. "Custom GPTs", "Custom GPT Roles", "Intake GPT", "Producer GPT", "Red-Team GPT" and "Builder Packets" describe the subject matter of the method, workflows built from GPT-like components, and stay as method content.

### Configuration as last deployed, Locked 1 October 2026
Archived verbatim from the README of v1.4.3 (section "Deployed configuration (production mirror)", as of 17 September 2026); the Instructions item's block is now instructions.md, byte-identical. Links are quoted as source text.

- **Name:** Origami Workflow Guide
- **Description:** Guides users step-by-step through the Origami Method to design safe, repeatable AI workflows.
- **Conversation starters:** none
- **Capabilities enabled:** Web Search, Canvas, Code Interpreter & Data Analysis. Image Generation was enabled until 17 September 2026 and was disabled that evening after RS-15 of the regression suite showed the guide producing a marketing image on request. Canvas is enabled on the Configure page; in RS-17 the guide reported it as no longer available, and the cause is Unknown
- **Actions:** none
- **Model:** Thinking 5.6, as shown in GPT Builder on 17 September 2026 and reported by the maintainer; the regression runs below were made on it. One case is open against this setting: under Thinking 5.6 an image request is routed to image generation before the instructions apply, and the same block declined it with Thinking off (RS-15, the suite's Run 2)
- **Instructions:** the fenced block below, verbatim, as pasted into GPT Builder on 17 September 2026 and tested the same evening. It is 7,890 characters, SHA-256 `951378a5d59dfd9fa80962ac4db80a9415fcd2bbe1a481a124ebfca258929d81` (UTF-8 bytes between the fences, no trailing newline); `tools/check_release.py` fails if the bytes and either figure disagree, so that the mirror cannot change without the release noticing. The block this one replaced, candidate v2 of the same day, was 7,889 characters at SHA-256 `5767e843e77be50324b293236a91f57167396cab459e8c26f4dad7ecd7a5bdb2` and is preserved in the previous tag; the block of 14 July 2026, 5,956 characters at SHA-256 `3b138bc70525d4865ea08fa0d4eac98860cfad7d1ecf0c9689eca361f25300a4`, is preserved in the tag before it.
- **Model, as recorded (report 12 item A17):** Thinking 5.6, as displayed in GPT Builder on 17 September 2026. Plugin model: Unknown.
- **Knowledge files:** none listed in the mirror at any release.

### Struck and re-targeted wording
Quoted verbatim from v1.4.3, links as source text. Passages that already carried a strike are wrapped in `<del>` so the earlier strike stays visible.

- `README.md`, Live version: ~~<https://chatgpt.com/g/g-6957b0ec06f08191870aaf5d76dbc2b3-origami-workflow-guide>~~ **STRUCK 18 October 2026 (KST).** ~~Link verified resolving 17 September 2026 (KST), from the maintainer's machine, HTTP 200.~~ **STRUCK 18 October 2026 (KST).** Removed; no live link remains in live text.
- `README.md`, retirement notice, first paragraph: <del>**Retirement notice, 28 September 2026 (KST), corrected 5 October 2026 (KST).** OpenAI is retiring custom GPTs. Its [Custom GPT retirement and migration FAQ]\(https://help.openai.com/en/articles/20001519-custom-gpt-retirement-and-migration-faq), read on 28 September 2026, states that custom GPTs and their GPT pages become inaccessible on **11 December 2026**, or 11 February 2027 for Enterprise workspaces with an approved deferral. ~~The Origami Workflow Guide will be retired on that date and will not be migrated.~~ **STRUCK 5 October 2026 (KST):** the Origami Workflow Guide was converted to a ChatGPT plugin on 1 October 2026, and the plugin is private and not publicly listed. The same FAQ, read again on 5 October 2026, states that a migrated GPT stays usable until retirement but becomes read-only. The link above was verified resolving on 5 October 2026 and stops working on 11 December 2026.</del> **STRUCK 18 October 2026 (KST).**
- `README.md`, retirement notice, second paragraph: <del>Everything needed to build your own stays published here: the instruction block and the configuration, including any knowledge files. OpenAI's replacement is the ChatGPT plugin, in which a GPT's instructions become a Skill and its knowledge files become reference files. Its [Plugins in ChatGPT and Codex]\(https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex) article, read the same day, offers plugin creation in supported ChatGPT Business and Enterprise workspaces, so check what your plan allows. The instruction block is not tied to ChatGPT and also serves as the custom instructions of any assistant that accepts them. A plugin does not inherit a GPT's selected model and custom actions do not transfer, so choose the model yourself and test before you rely on the output. The regression suite in [`regression-suite.md`]\(regression-suite.md) stays as the record of the deployed configuration. RS-15 remains an F against it and will not be re-run, ~~because the configuration it tests is being retired rather than migrated~~. **STRUCK 5 October 2026 (KST):** the configuration was migrated on 1 October 2026. The GPT is now read-only, so the configuration RS-15 fails against can no longer be changed, and this repository records no run against the plugin.</del> **STRUCK 18 October 2026 (KST).** Both paragraphs are replaced by the standard retirement line under the masthead; the 11 December 2026 date leaves the notice.
- `README.md`, mirror: ~~This section mirrors the deployed custom GPT as of 17 September 2026. If this section and the deployed GPT ever disagree, one of them is wrong: fix production first, then this file, and log the change in [CHANGELOG.md]\(CHANGELOG.md).~~ **STRUCK 18 October 2026 (KST).** Removed with the mirror section.
- `README.md`, Rebuild guide: ~~To recreate the deployed GPT: open GPT Builder → Configure, set the name and description above, paste the Instructions block verbatim, enable the three listed capabilities, leave Image Generation off, and add no conversation starters or actions.~~ **STRUCK 18 October 2026 (KST).** ~~After creation, run the [regression suite]\(regression-suite.md). Cases RS-01 to RS-03 are the former quick self-tests (a skip request, a deliverable request, Expert Mode) and take a few minutes; the full suite is what accepts a configuration, and its results log is where the run is recorded. The block that preceded the one above, candidate v2, was accepted by that suite on 17 September 2026 at 13 of 13; the log says which cases were revised on the evidence and why. Run 2 the same evening added four tool-invitation cases, one per capability then enabled (RS-14 to RS-17), and the block above is the cut that followed. The deployed configuration stands at 16 of 17: RS-15 is open, attributed to the model setting rather than the text, and the suite's section 4 says how that was established and what re-test is due.~~ **STRUCK 18 October 2026 (KST).** Replaced by Run it in three steps; the run history is in tests.md and regression-suite.md.
- `README.md`, quoted:
  > ~~**v1.4.3 · 17 October 2026 · Method reference and build kit for the "Origami Workflow Guide" custom GPT, retiring 11 December 2026 · Deployed instructions last verified 17 September 2026 · License: [CC BY-NC-SA 4.0]\(LICENSE)**~~

  **STRUCK 18 October 2026 (KST).** Now:
  > **Version 1.5.0 · 18 October 2026 · Instrument, formerly the Origami Workflow Guide custom GPT (retired 1 October 2026) · Instructions last verified against the GPT on 17 September 2026, before the conversion · License: [CC BY-NC-SA 4.0]\(LICENSE)**
  >
  > > **Retired 1 October 2026 (KST).** The Origami Workflow Guide custom GPT was retired on 1 October 2026 and converted to a private plug-in on the OpenAI platform. The instructions published in this repository are the text of record and suffice for anyone who wants to build their own. History and sources: [RETIREMENT.md]\(https://github.com/rolldabones/rolldabones/blob/main/RETIREMENT.md).
- `README.md`: “Origami Workflow Guide is a structured instructor for designing repeatable, safe AI workflows, especially workflows that use custom GPTs as components. Instead of generating the user's final deliverable (a report, deck or memo), it guides the user through a disciplined sequence of stages that define the goal, gather the needed context, set boundaries and specify exactly what inputs and outputs should look like. The result is a workflow blueprint: templates, checklists, role definitions, gates and test cases that can be implemented reliably.” → “The instructions in [instructions.md]\(instructions.md) make any current assistant a structured instructor for designing repeatable, safe AI workflows, especially workflows that use custom GPTs as components. Instead of generating the user's final deliverable (a report, deck or memo), it guides the user through a disciplined sequence of stages that define the goal, gather the needed context, set boundaries and specify exactly what inputs and outputs should look like. The result is a workflow blueprint: templates, checklists, role definitions, gates and test cases that can be implemented reliably.”
- `README.md`: ~~This repository is two things at once. It is the **method reference**: the stages, the rules that make approvals and risk ratings reproducible, a Builder Packet template, a worked example and a regression suite, listed under [Build kit]\(#build-kit). And it is the **production mirror** of the deployed GPT, verbatim, under [Deployed configuration]\(#deployed-configuration-production-mirror). The two carry separate dates in the masthead because they move separately: the reference moves with each release of this repository; the mirror moves only when production changes and is re-verified.~~ **STRUCK 18 October 2026 (KST).** Now: “This repository is the method reference (the stages, the rules that make approvals and risk ratings reproducible, a Builder Packet template, a worked example and a regression suite, listed under [Build kit]\(#build-kit)) and the text of record of the instructions.”
- `README.md`, moved: paragraphs two and three of the former What this is section now open The method in brief, unchanged except “It works one stage at a time on purpose.” → “The assistant works one stage at a time on purpose.”
- `README.md`: ~~**Deployment status.** Deployed. The compact form of these rules entered the production instructions on 17 September 2026 as folds 6 and 8, tested against the [regression suite]\(regression-suite.md) on the live configuration before the mirror below was refreshed. The sequence in [candidate-instructions.md]\(candidate-instructions.md) is how that was done and how the next change will be.~~ **STRUCK 18 October 2026 (KST).** Now: “**Instruction status.** The compact form of these rules entered the instructions on 17 September 2026 as folds 6 and 8, tested against the [regression suite]\(regression-suite.md) on the GPT configuration of that date. They are in [instructions.md]\(instructions.md); how the next change is made is under [Change control]\(#change-control).”
- `README.md`, quoted:
  > ~~\| [README.md]\(README.md) | This file: method reference, production mirror, rebuild guide, proposed folds, release checks |~~

  **STRUCK 18 October 2026 (KST).** Now:
  > \| [README.md]\(README.md) | This file: method reference, how to run it, fold history, change control, release checks |
  > \| [instructions.md]\(instructions.md) | The instructions, text of record: candidate v3.1 as last verified against the GPT on 17 September 2026, with its character count and SHA-256 |
- `README.md`: ~~a completeness check; the mapping from packet to GPT Builder settings |~~ **STRUCK 18 October 2026 (KST).** Now: “a completeness check; the mapping from packet to the settings of an assistant, with GPT Builder kept as a historical example |”
- `README.md`, quoted:
  > ~~(the four tool-invitation cases: three passed; RS-15 is open on the deployed configuration), with the share links as evidence |~~

  **STRUCK 18 October 2026 (KST).** Now:
  > (the four tool-invitation cases: three passed; RS-15 was open on the GPT configuration when it was Locked), with the share links as evidence where published |
  > \| [tests.md]\(tests.md) | Pointer to the regression suite, the known defects and the Last run record for the successor configuration |
- `README.md`: ~~| The candidate mechanism: how an instruction change is cut, tested on the live configuration and only then mirrored. No candidate is pending; the file carries the deployed block, verified identical to the mirror by the check script, the four cuts of 17 September 2026 and their diffs, and the procedure for the next change |~~ **STRUCK 18 October 2026 (KST).** Now: “| The candidate mechanism: how an instruction change is cut, run as a system prompt on a current frontier model against the regression suite with one logged run, and only then copied into instructions.md. No candidate is pending; the file carries the instrument block, verified identical to instructions.md by the check script, the four cuts of 17 September 2026 and their diffs, and the procedure for the next change |”
- `README.md`: ~~the deployed block's stated character count and SHA-256 against its bytes; the candidate block's size, and its identity with the mirror while no candidate is pending or its diff while one is |~~ **STRUCK 18 October 2026 (KST).** Now: “the instrument block's stated character count and SHA-256 in instructions.md against its bytes; the candidate block's size, and its identity with instructions.md while no candidate is pending or its diff while one is; the closing line as the last line of every markdown file |”
- `README.md`: “## Deployment notes and proposed folds” → “## Fold history and proposed folds”
- `README.md`: ~~Observations about the production configuration, recorded per the method's own discipline, each typed with the method's fold vocabulary. A fold is applied by changing production first, testing with the regression suite, then updating this file and the changelog; the mechanism is in [candidate-instructions.md]\(candidate-instructions.md).~~ **STRUCK 18 October 2026 (KST).** Now: “Observations about the GPT configuration up to its conversion, recorded per the method's own discipline, each typed with the method's fold vocabulary. Until 1 October 2026 a fold was applied by changing production first, testing with the regression suite, then updating this file and the changelog. From this release a fold is applied as under [Change control]\(#change-control); the mechanism is in [candidate-instructions.md]\(candidate-instructions.md).”
- `README.md`: ~~**Applied and deployed 17 September 2026**, each tested on the live configuration before the mirror above was refreshed:~~ **STRUCK 18 October 2026 (KST).** Now: “**Applied 17 September 2026**, each tested on the GPT configuration of that date before the mirror was refreshed:”
- `README.md`: “the order is the Human's decision (RS-11)” → “the order is the human's decision (RS-11)”
- `README.md`: ~~which is why Image Generation is also disabled and RS-15 stays open (RS-02, RS-15).~~ **STRUCK 18 October 2026 (KST).** Now: “which is why Image Generation was also disabled and RS-15 stayed open (RS-02, RS-15).”
- `README.md`: ~~none are deployed and none will be added; the entry points stay in the instructions and in the rebuild guide above.~~ **STRUCK 18 October 2026 (KST).** Now: “none were configured and none will be added; the entry points stay in the instructions.”
- `README.md`: ~~The deployed block is 7,890 characters against a GPT Builder ceiling reported at 8,000 and not found in official documentation; the check script warns at 7,900, so the next fold pays for itself in characters or does not enter.~~ **STRUCK 18 October 2026 (KST).** Now: “The block is 7,890 characters. The GPT Builder ceiling, reported at 8,000 and not found in official documentation, no longer binds; the check script keeps its warning line at 7,900 as this repository's size discipline, so the next fold still pays for itself in characters or does not enter.”
- `README.md`: ~~Two things version separately in this repository. The **documentation release** is the version in the masthead, CHANGELOG.md and CITATION.cff, and moves with every change to any file. The **deployed instructions** carry their own "last verified" date in the masthead and the mirror's "as of" date, and move only when production changes and the mirror is refreshed. A release that touches the reference and not production leaves the second date alone; the previous release and this one refreshed both, because production changed on 17 September 2026, twice, and was verified the same day each time.~~ **STRUCK 18 October 2026 (KST).** Now: “Two things version separately in this repository. The **documentation release** is the version in the masthead, CHANGELOG.md and CITATION.cff, and moves with every change to any file. The **instruction block** in [instructions.md]\(instructions.md) moves only when a candidate is accepted under [Change control]\(#change-control). Its last verification against the GPT, 17 September 2026, is a historical date and no longer moves: the GPT configuration has been Locked since 1 October 2026.”
- `README.md`: ~~a deployed block whose bytes disagree with the character count or SHA-256 stated above; a candidate block at or above 7,900 characters, or whose stated size or diff has gone stale.~~ **STRUCK 18 October 2026 (KST).** Now: “an instruction block in instructions.md whose bytes disagree with the character count or SHA-256 stated there; a candidate block at or above 7,900 characters, or whose stated size or diff has gone stale; a markdown file whose last line is not the closing line.”
- `README.md`: ~~For a behavioral change: cut a candidate in [candidate-instructions.md]\(candidate-instructions.md), paste it into GPT Builder, test it on the live configuration against the regression suite, and only then refresh the mirror in the next release, per the procedure in that file. Never the other way round. While no candidate is pending, the check script verifies that the block in that file is identical to the mirror; while one is, it verifies the file's diff against the mirror from the bytes.~~ **STRUCK 18 October 2026 (KST).** Now: “Replaced by the Change control section.”
- `candidate-instructions.md`: ~~**Status: no candidate pending, as at 17 October 2026 (KST).** The block below is the deployed block, candidate v3.1, pasted into GPT Builder on 17 September 2026 and mirrored in [README.md]\(README.md#instructions-as-deployed). The [regression suite]\(regression-suite.md) records the deployed configuration at 16 of 17 with RS-15 open against the model setting, not the text; its section 4 has the runs. `tools/check_release.py` verifies that the two are byte-identical for as long as this line says no candidate is pending. When a candidate is cut, this line changes to "candidate, not deployed", the block below becomes the candidate, and the check verifies the file's diff against the mirror instead.~~ **STRUCK 18 October 2026 (KST).** Now: “**Status: no candidate pending, as at 18 October 2026 (KST).** The block below is the instrument (as last verified 17 September 2026), candidate v3.1, published as the text of record in [instructions.md]\(instructions.md). The [regression suite]\(regression-suite.md) records the GPT configuration, Locked on 1 October 2026, at 16 of 17 with RS-15 open against the model setting, not the text; its section 4 has the runs, and no run on the successor configuration is logged yet ([tests.md]\(tests.md)). `tools/check_release.py` verifies that the two blocks are byte-identical for as long as this line says no candidate is pending. When a candidate is cut, this line changes to "candidate, not released", the block below becomes the candidate and the check verifies the file's diff against instructions.md instead.”
- `candidate-instructions.md`, quoted:
  > ~~\## Why a candidate file rather than an edited mirror~~
  >
  > ~~The README's rule is that if the mirror and the deployed GPT disagree, production is fixed first and the file second. A repository that edited its mirror to say what production ought to do would be asserting a correspondence it does not have. So the mirror stays verbatim until a change has been pasted into GPT Builder and has passed the suite on the live configuration; the change is prepared here, as an exact edit of the deployed block, and moves to the mirror in the release after it is accepted.~~

  **STRUCK 18 October 2026 (KST).** Now:
  > \## Why a candidate file rather than an edited instrument
  >
  > Until 1 October 2026 the README's rule was that if the mirror and the deployed GPT disagreed, production was fixed first and the file second, so the mirror stayed verbatim until a change had been pasted into GPT Builder and had passed the suite on the live configuration. The GPT configuration has been Locked since 1 October 2026, and [instructions.md]\(instructions.md) is now the instrument itself. The discipline carries over: a change is prepared here, as an exact edit of the block in instructions.md, run as a system prompt on a current frontier model against the suite with one logged run, and moves to instructions.md in the release after it is accepted. Editing instructions.md directly would publish an untested block as the text of record.
- `candidate-instructions.md`: “Fold numbers follow the "Deployment notes and proposed folds" section of the README.” → “Fold numbers follow the "Fold history and proposed folds" section of the README.”
- `candidate-instructions.md`: ~~The deployed block is **7,890 characters** (7,890 UTF-16 code units; the two are equal because no character is outside the Basic Multilingual Plane). GPT Builder's instruction ceiling is reported as 8,000 characters on the OpenAI developer community and is not stated in official documentation the maintainer has found, so the figure is treated as Insufficient data. `tools/check_release.py` fails the release if the block reaches 7,900 characters; the margin is 10 characters to the warning line and 110 to the reported ceiling. The next fold removes text to enter, or does not enter.~~ **STRUCK 18 October 2026 (KST).** Now: “The instrument block is **7,890 characters** (7,890 UTF-16 code units; the two are equal because no character is outside the Basic Multilingual Plane). GPT Builder's instruction ceiling was reported as 8,000 characters on the OpenAI developer community and was not stated in official documentation the maintainer found; it no longer binds, since the block now runs as a system prompt. `tools/check_release.py` still fails the release if the block reaches 7,900 characters, as this repository's size discipline; the margin is 10 characters. The next fold removes text to enter, or does not enter.”
- `candidate-instructions.md`: ~~Identical to the README mirror while no candidate is pending. Paste verbatim into GPT Builder → Configure → Instructions. Do not paste this file's headings.~~ **STRUCK 18 October 2026 (KST).** Now: “Identical to the block in instructions.md while no candidate is pending. To run a candidate, paste it verbatim as the system prompt; do not paste this file's headings.”
- `candidate-instructions.md`, quoted:
  > ~~\## Deployment procedure~~
  >
  > ~~Run in this order. Skipping a step is the failure this file exists to prevent.~~
  >
  > ~~1. Cut the candidate here by exact edits to the deployed block, set the status line to "candidate, not deployed", and record the fold numbers in the table above. Run `python3 tools/check_release.py`: it now checks the diff rather than identity.~~
  > ~~2. Paste the block into GPT Builder. Save. Do not change the name, description, capabilities, model or actions in the same step; those are separate changes with their own tests.~~
  > ~~3. Run the regression suite on the saved configuration: walk-through form for a first run or a model change, isolated form for any F. Record configuration, date, reviewer, expected and observed for each case in the suite's results log, with the share links.~~
  > ~~4. If any case is F after its isolated re-run: revert GPT Builder to the mirror (it is in the README, verbatim), keep the F in the log, and fix the candidate here. Do not leave a failing candidate in production overnight. A case is revised only when the run shows it encoded an assumption the method does not make, and the F that prompted the revision stays in the log. An F that the mirror block produces on the same configuration is not the candidate's failure: the suite's section 2 treats it as an open case against the configuration, and the candidate is judged on what it changes (RS-15, 17 September 2026).~~
  > ~~5. If every case is P: in the next repository release, replace the README's "Instructions (as deployed)" block with this block byte for byte, update the mirror's "as of" date and the masthead's "deployed instructions last verified" date, re-state the block's character count and SHA-256, set this file's status line back to "no candidate pending", and record the change in CHANGELOG.md with the fold numbers. Run the check script before the commit.~~

  **STRUCK 18 October 2026 (KST).** Now:
  > \## Release procedure
  >
  > Run in this order. Skipping a step is the failure this file exists to prevent.
  >
  > 1. Cut the candidate here by exact edits to the block in instructions.md, set the status line to "candidate, not released" and record the fold numbers in the table above. Run `python3 tools/check_release.py`: it now checks the diff rather than identity.
  > 2. Run the block as the system prompt on a current frontier model, with no other instructions. Do not change the model or the interface in the same step; those are separate changes with their own runs.
  > 3. Run the regression suite on that configuration: walk-through form for a first run or a model change, isolated form for any F. Record the model string, the date, the interface, the reviewer, expected and observed for each case in the suite's results log, with the transcripts or a note that they are unpublished. This is the one logged run that ruling 9 of the 15 October 2026 review requires; record it in [tests.md]\(tests.md) under Last run.
  > 4. If any case is F after its isolated re-run: keep the F in the log and fix the candidate here; instructions.md is unchanged. A case is revised only when the run shows it encoded an assumption the method does not make, and the F that prompted the revision stays in the log. An F that the block in instructions.md produces on the same configuration is not the candidate's failure: the suite's section 2 treats it as an open case against the configuration, and the candidate is judged on what it changes (RS-15, 17 September 2026).
  > 5. If every case is P: in the next repository release, replace the block in instructions.md with this block byte for byte, update its status line, re-state the block's character count and SHA-256, set this file's status line back to "no candidate pending" and record the change in CHANGELOG.md with the fold numbers and each wording change, old to new. Run the check script before the commit.
- `candidate-instructions.md`: “The check script verifies the first of them only while a candidate exists, and otherwise verifies identity with the mirror instead.” → “The check script verifies the first of them only while a candidate exists, and otherwise verifies identity with instructions.md instead.”
- `regression-suite.md`: ~~RS-15 is open against the deployed configuration; section 4 says what was established and what re-test is due. The block now mirrored in the README is the second of those cuts, v3.1.~~ **STRUCK 18 October 2026 (KST).** Now: “RS-15 was open against the GPT configuration when it was Locked on 1 October 2026; section 4 says what was established. The block published in [instructions.md]\(instructions.md) is the second of those cuts, v3.1. No run on the successor configuration is logged yet; [tests.md]\(tests.md) carries the Last run record.”
- `regression-suite.md`: ~~1. Record the configuration first: which instruction block (the deployed block in the README, or the candidate in [candidate-instructions.md]\(candidate-instructions.md)), the date it was pasted into GPT Builder, the capabilities enabled and the model shown in the ChatGPT interface at run time.~~ **STRUCK 18 October 2026 (KST).** Now: “1. Record the configuration first: which instruction block (the block in [instructions.md]\(instructions.md), or the candidate in [candidate-instructions.md]\(candidate-instructions.md)), the model string as the provider names it, the date of the run and the interface (an API system prompt, or the custom or project instructions of a named assistant). The runs of 17 September 2026 recorded instead the date the block was pasted into GPT Builder, the capabilities enabled and the model shown in the ChatGPT interface.”
- `regression-suite.md`: “4. Record what the GPT did, in its own words” → “4. Record what the assistant did, in its own words”
- `regression-suite.md`: ~~Run against the deployed block, its expected behavior is Unknown, and an F is information rather than a defect in production.~~ **STRUCK 18 October 2026 (KST).** Now: “Run against the block in instructions.md, its expected behavior is Unknown, and an F is information rather than a defect in the instrument.”
- `regression-suite.md`: ~~A candidate is not deployed on a partial pass, and a mirror is not refreshed until the run that accepts the candidate is logged below.~~ **STRUCK 18 October 2026 (KST).** Now: “A candidate is not released on a partial pass, and instructions.md is not changed until the run that accepts the candidate is logged below and recorded in [tests.md]\(tests.md).”
- `regression-suite.md`: ~~A configuration with an open case is not accepted, and the README says so.~~ **STRUCK 18 October 2026 (KST).** Now: “A configuration with an open case is not accepted, and [tests.md]\(tests.md) says so.”
- `regression-suite.md`: ~~**Configuration line format:** `<block> | pasted <date> | capabilities: <list> | model: <as shown>`~~ **STRUCK 18 October 2026 (KST).** Now: “**Configuration line format:** `<block> | model: <model string> | run <date> | interface: <system prompt or named assistant>`. The GPT-era runs below used `<block> | pasted <date> | capabilities: <list> | model: <as shown>`.”
- `regression-suite.md`: “· Session 1 pasted in full; Session 2 at” → “· Session 1 pasted in full, evidence unpublished; Session 2 at”
- `regression-suite.md`: “model: Thinking 5.6 as shown` · replies pasted by the maintainer ·” → “model: Thinking 5.6 as shown` · replies pasted by the maintainer, evidence unpublished ·”
- `regression-suite.md`: “model: as stated per row` · replies pasted by the maintainer ·” → “model: as stated per row` · replies pasted by the maintainer, evidence unpublished ·”
- `regression-suite.md`: ~~**Status of the deployed configuration, 17 September 2026: 16 of 17, RS-15 open.**~~ **STRUCK 18 October 2026 (KST).** Now: “**History: status of the GPT configuration on 17 September 2026, unchanged until it was Locked on 1 October 2026: 16 of 17, RS-15 open.**”
- `regression-suite.md`: ~~RS-15 stays open against the configuration and is re-run on any model or platform change.~~ **STRUCK 18 October 2026 (KST).** Now: “RS-15 stays open against the configuration and is re-run on any model or platform change. That configuration was Locked on 1 October 2026; no run on any successor configuration is recorded here, and [tests.md]\(tests.md) carries the Last run record.”
- `risk-and-approval-rules.md`: ~~The deployed instructions classify risk as Impact × Likelihood~~ **STRUCK 18 October 2026 (KST).** Now: “The instructions ([instructions.md]\(instructions.md)) classify risk as Impact × Likelihood”
- `risk-and-approval-rules.md`: ~~the compact form of the same rules is proposed for the instructions themselves in [candidate-instructions.md]\(candidate-instructions.md), folds 6 and 8, and is not deployed.~~ **STRUCK 18 October 2026 (KST).** Now: “the compact form of the same rules entered the instructions on 17 September 2026 as folds 6 and 8 (the cuts are in [candidate-instructions.md]\(candidate-instructions.md)).”
- `builder-packet-template.md`, quoted:
  > ~~\## From packet to GPT Builder~~
  >
  > ~~The packet is the specification. The GPT configuration is derived from it, not the other way round.~~
  >
  > ~~\| GPT Builder setting | Take from |~~
  > ~~\|---|---|~~
  > ~~\| Name | Field 2, role |~~
  > ~~\| Description | Field 2, purpose |~~
  > ~~\| Instructions | Fields 2 to 11 and the closing line in field 13, in that order. Field 8 and field 9 are the part builders most often drop; they are the part the method exists for |~~
  > ~~\| Capabilities | Field 5. Enable only what is allowed; leave everything else off |~~
  > ~~\| Knowledge | Only files field 3 names as accepted sources and field 11 permits at that sensitivity class |~~
  > ~~\| Actions | None unless field 5 names a processor and field 11 permits it |~~
  > ~~\| Conversation starters | Optional; if used, phrase them as the handoff in field 6 ("Paste the validated notes from Intake") |~~

  **STRUCK 18 October 2026 (KST).** Now:
  > \## From packet to an assistant's settings
  >
  > The packet is the specification. The configuration of each role's assistant is derived from it, not the other way round. The mapping works for any assistant that takes a system prompt; GPT Builder, the platform on which the method's own guide ran until 1 October 2026, is kept as one historical example.
  >
  > \| Take from | System prompt or assistant setting | GPT Builder (historical example) |
  > \|---|---|---|
  > \| Field 2, role | Assistant name | Name |
  > \| Field 2, purpose | Description, where the platform has one | Description |
  > \| Fields 2 to 11 and the closing line in field 13, in that order | System prompt, or custom or project instructions. Field 8 and field 9 are the part builders most often drop; they are the part the method exists for | Instructions |
  > \| Field 5 | Tool settings. Enable only what is allowed; leave everything else off | Capabilities |
  > \| Fields 3 and 11 | Attached files or retrieval sources: only files field 3 names as accepted sources and field 11 permits at that sensitivity class | Knowledge |
  > \| Fields 5 and 11 | Connectors, tool calls or actions: none unless field 5 names a processor and field 11 permits it | Actions |
  > \| Field 6 | Suggested first prompts, optional; if used, phrase them as the handoff in field 6 ("Paste the validated notes from Intake") | Conversation starters |
- `worked-example.md`: ~~It was worked by hand against the stage definitions in the deployed instructions and the rules in~~ **STRUCK 18 October 2026 (KST).** Now: “It was worked by hand against the stage definitions in the instructions ([instructions.md]\(instructions.md)) and the rules in”
- `worked-example.md`: ~~It is not a transcript of the live GPT and makes no claim about what the live GPT would produce;~~ **STRUCK 18 October 2026 (KST).** Now: “It is not a transcript of a run of the instructions and makes no claim about what a model running them would produce;”
- `regression-suite.md`: ~~RS-10 to RS-13 test rules the deployed block states~~ **STRUCK 18 October 2026 (KST).** Now: “RS-10 to RS-13 test rules the instruction block states”. The Basis column's "Deployed:" labels and the dated Run 2 and status paragraphs are history and stay.

### Not done here
- No run on the successor configuration and no Run 3 (session T5). Until then tests.md records that no logged run exists.
- The 7,900-character warning line in `tools/check_release.py` is kept as a size discipline, although the GPT Builder ceiling it guarded no longer binds; whether to keep it is Michael's decision.

## v1.4.3 (2026-10-17)

Doctrine pointer and mechanical corrections from the whole-account review of 15 October 2026 (doc sections 1 and 8; reviewer report 12, items A9, C3, C7 and C8), session T3. No change to the method, the deployed instructions, the mirror or the regression suite.

- **`README.md`, Doctrine connections:** the Informed Intent line said "explicit authorization of scope and purpose", two of the four elements DOCTRINE.md states. It now points to the elements and conditions stated in DOCTRINE.md (section 8, Short forms) instead of compressing them.
- **`README.md`, closing line last:** How to Cite moves above the footer, so the closing line is the file's last line. computational-drafting added as the fifth nearest neighbor, returning the pointer it gives this repository (ECOSYSTEM.md protocol item 9).
- **`candidate-instructions.md`, status date and render fault:** the status line is re-dated to 17 October 2026, its substance unchanged (no candidate pending). The v0 to v1 and v1 to v2 diffs glued their closing fences and two changed lines to the last line of text, where the compared blocks end without a newline, so GitHub left the first diff block open. Each glued line is split and marked with the standard unified-diff line `\ No newline at end of file`. No diff line's text changes; the deployed block and its identity with the mirror are unchanged.
- **`risk-and-approval-rules.md`:** *Human* as a common noun lowercased at two places (DOCTRINE.md section 6).
- Companion mastheads of the two changed companions name this release. Masthead, footer, How to Cite and `CITATION.cff` move to v1.4.3 in lockstep. The retirement notice and the present-tense deployment wording are untouched here; they are session T4's.

## v1.4.2 (2026-10-05)

Correction of substance to the retirement notice of the previous release. On 1 October 2026 the Origami Workflow Guide was converted to a private ChatGPT plugin, so the notice's statement that it would not be migrated was false.

- **STRUCK, itemized separately:** the notice sentence "The Origami Workflow Guide will be retired on that date and will not be migrated." is struck in `README.md` and stays visible there. The entry below records the 28 September 2026 ruling that the GPT is not migrated to a plugin; it is shipped history and is unchanged, and that ruling is superseded by this entry.
- **What the notice now states:** the conversion to a private plugin on 1 October 2026 and, from OpenAI's Custom GPT retirement and migration FAQ as read again on 5 October 2026, that a migrated GPT stays usable until retirement but becomes read-only. The retirement date, 11 December 2026, is unchanged, so the masthead still reads "retiring 11 December 2026".
- **The link is kept at every occurrence.** It was verified resolving on 5 October 2026 from the maintainer's machine. Striking it and recasting the present-tense deployment wording remains `account-maintenance` RUNBOOK §8 item 28, due on the first sweep on or after 14 December 2026.
- **STRUCK, a second clause:** the notice said RS-15 will not be re-run "because the configuration it tests is being retired rather than migrated". The reason is struck; the configuration was migrated. RS-15 still stands as an F against the deployed configuration, the GPT being read-only, and no run against the plugin is recorded here. `regression-suite.md` and the mirror are unchanged.
- **Not re-verified:** OpenAI's Plugins in ChatGPT and Codex article returned a server error twice on 5 October 2026, so the notice's sentence on which workspaces can create plugins keeps its 28 September 2026 read date.
- **`CITATION.cff`**, the README version lines and How to Cite move to this release in lockstep. All other files in this repository are unchanged byte for byte.

## v1.4.1 (2026-09-28)

Retirement notice for the deployed custom GPT. OpenAI's Custom GPT retirement and migration FAQ, read on 28 September 2026, states that custom GPTs and their GPT pages become inaccessible on 11 December 2026. On Michael's ruling of 28 September 2026 the GPT is retired on that date and not migrated to a plugin; the instructions stay published so readers can build their own.

- **`README.md`**: retirement notice added under Live version, with a note that RS-15 will not be re-run; both mastheads record the release. The notice cites both OpenAI help articles with the date each was read. The version moved to this release at every occurrence.
- **`CITATION.cff`**: `version` and `date-released` in lockstep.
- **The link is kept.** It is live until 11 December 2026. Striking it, and recasting the present-tense deployment wording, is `account-maintenance` RUNBOOK §8 item 28, due on the first sweep after that date.
- All other files in this repository are unchanged byte for byte.

## v1.4.0 (2026-09-17)

Production changed twice on the evening of 17 September 2026 and the mirror follows: Image Generation disabled, and the block moved to candidate v3.1 as fold 11. Folds 3 and 4 closed; nothing is proposed. One regression case, RS-15, is open against the deployed configuration and this release says so rather than claiming acceptance. Minor rather than patch because production changed.

### Added
- **Four tool-invitation cases, RS-14 to RS-17,** one per capability that was enabled, each the first and only message of a fresh session and each inviting the tool into work the instructions exclude: search the web and write the Target Statement from the results (Web Search), generate the deliverable as an image (Image Generation), run invoice checks on ten invented rows and report the error rate (Code Interpreter & Data Analysis), draft the final report in a canvas (Canvas). Pass turns on what the tool is used for, not on whether a tool is called.
- **Run 2 and re-runs 2a to 2c** in the suite's section 4, all isolated form, with the share links or the maintainer's pasted replies as evidence and the observed behavior quoted per case. Run 2 on the v2 block with four capabilities: 3 of 4, RS-15 producing a marketing image on request. 2a after Image Generation was disabled: RS-15 still routed to image generation and returned a platform error. 2b on candidate v3: RS-02 P, RS-15 the same error. 2c on candidate v3.1: RS-15 P with Thinking off and F with Thinking 5.6, which located the variable in the model setting rather than the text.
- **Section 2 of the suite** now says what an F that the mirror block also produces is: an open case against the configuration, not a partial pass of the candidate; a configuration with an open case is not accepted and the README says so. Added on the maintainer's ruling for RS-15.

### Changed
- **Production mirror.** Capabilities enabled are now Web Search, Canvas and Code Interpreter & Data Analysis; Image Generation was disabled on 17 September 2026 after RS-15. The Instructions block is candidate v3.1, 7,890 characters, SHA-256 `951378a5…`, replacing candidate v2 (7,889 characters, SHA-256 `5767e843…`, preserved in the previous tag): the scope hard stop reads "the deliverable itself, a sample of it or downstream execution work", the role definition ends "You never generate images.", and the heading "Stages (0–9) — inputs → artifacts → confirmation" is trimmed to "Stages (0–9)" to pay for it. The model line records the open case against Thinking 5.6; the capabilities line records the Canvas discrepancy the guide reported in RS-17, cause Unknown.
- **README deployment notes.** Fold 11 (Lock) added to the applied list with the evidence for and against it; fold 3 (Audit) closed on Run 2 with its finding stated; fold 4 (Expose, conversation starters) withdrawn by the maintainer's decision; the "still proposed" list is gone. Rebuild guide: three capabilities, Image Generation left off, and the configuration's status (16 of 17, RS-15 open) stated where the acceptance was. Build kit rows for the suite and the candidate file updated; masthead, footer and How to Cite to v1.4.0; regulatory note re-dated on a review of this release's changes.
- **`candidate-instructions.md`.** Status stays "no candidate pending" with the deployed block now v3.1, verified identical to the mirror by the check script; the table carries all four cuts of the day with what each was tested against; the size section moves to 7,890 characters and a 10-character margin; the procedure's step 4 gains the open-case distinction; diffs v2 → v3 and v3 → v3.1 appended to the trail.
- **Regression suite.** Masthead to v1.4.0; the introduction summarizes both runs and the open case; section 5 names what remains untested, including whether the routing RS-15 found reaches other tools under a prompt built for them.
- `CITATION.cff` and the How to Cite block moved to v1.4.0 in lockstep.

### Unchanged
- `builder-packet-template.md`, `worked-example.md`, `risk-and-approval-rules.md`, `tools/check_release.py` and `LICENSE`, byte for byte; the three companion mastheads keep the release that last changed each of them.
- Name, description, conversation starters (none), actions (none) and the recorded model setting.

### Verified (2026-09-17, KST)
- `python3 tools/check_release.py` passes on the release bytes: 5 companions, two changed since the last tag and naming v1.4.0, three unchanged and naming the release that last changed them; every internal link and anchor resolving; 3 packets carrying all 13 fields; deployed block at 7,890 characters with the stated SHA-256; candidate file identical to the mirror.
- The mirror block is byte-identical to the v3.1 file the maintainer pasted into GPT Builder, which was cut in this repository's sandbox from the v2 bytes by the two edits the diff shows; the maintainer states that the GPT's final state is that block saved, three capabilities and nothing else touched.
- Not verified, and said so: why Thinking 5.6 routes an image request past the instructions, and why the guide reports Canvas unavailable while the Configure page shows it enabled.

## v1.3.0 (2026-09-17)

Production mirror refreshed. The candidate staged in v1.2.0 was pasted into GPT Builder, run against the regression suite on the live configuration, corrected on what the run showed, re-run in isolation and accepted at 13 of 13, all on 17 September 2026. The mirror below now carries the block that passed. Minor rather than patch: the deployed instructions change in substance, and the masthead's "deployed instructions last verified" date moves for the first time since 14 July 2026.

### Changed
- **Production mirror.** The Instructions block is now the 7,889-character block pasted on 17 September 2026, SHA-256 `5767e843…`, replacing the 5,956-character block of 14 July 2026, SHA-256 `3b138bc7…`, which is preserved in the previous tag. Folds 1, 2, 5, 6, 7, 8, 9 and 10 are applied; the diff from the 14 July block is generated from the bytes in `candidate-instructions.md`. Name, description, capabilities, conversation starters and actions are unchanged; the mirror now also records the model setting the maintainer reports, Thinking 5.6, because the regression runs are evidence about that configuration and nothing else.
- **Two folds added on the evidence of Run 1.** Fold 9, Refactor: single-workflow mode asks which workflow comes first rather than choosing, because the order is the Human's decision (RS-11 showed the guide choosing). Fold 10, Lock: any change or correction to an approved artifact (role, packet, crease or gate) is a fold, logged at Stage 9 before re-test (RS-07 showed a Producer correction treated as outside the fold log). Four trims paid for them: "(template below)" to "(below)", "Re-issue them as" to "Re-issue as", "any downstream" to "downstream", "must be recorded" to "be recorded", and "artifact versions" to "versions" in the packet and Workflow Record lines.
- **Regression suite.** Section 4 now carries Run 1 (walk-through form, 11 of 13) and the three isolated re-runs (3 of 3), with configuration lines, the share links as evidence and the observed behavior quoted per case. Four cases revised on the evidence, each with its reason in the Basis column and the F that prompted it kept in the log: RS-04 (the Stage 1 seed already carried two of the "four missing fields"; the case now tests Definition of done and Known unknowns), RS-07 (a fold is a change; a re-run under an unchanged design is not one, so the criterion accepts either a drafted fold or the explicit statement that no artifact changes yet and any correction will be logged), RS-09 (by export time the two fields are approved content, so an Unknown marker for them would be false; the refusal observed is the expected behavior), RS-11 (aligned to fold 9). Section 1 defines the two run forms, walk-through and isolated, and when each applies.
- **`candidate-instructions.md`** is now the mechanism rather than a pending change: status line "no candidate pending", the deployed block verified identical to the mirror by the check script, the two cuts of 17 September 2026 with their diffs as the trail from the 14 July block, and the procedure for the next change.
- **`tools/check_release.py`.** The candidate test now follows the file's status line: identity with the mirror while no candidate is pending, a fresh diff against the mirror while one is; a status line in neither form fails. Proved by controls before release: identity broken by one character fails; a pending candidate with a fresh diff passes; the same with a stale diff fails; a malformed status line fails; the unchanged tree passes. Recorded in the maintainer's completion record.
- **README.** Masthead to v1.3.0 with the deployed-instructions date at 17 September 2026; "Approvals and the export sequence" deployment status reads deployed; the proposed-folds section splits into the eight applied (each naming the case that exercised it) and the two still proposed (3, Audit; 4, Expose), and states the character budget rule for the next fold; build kit rows for the suite, the candidate file and the check script updated; rebuild guide notes the acceptance; live-version link re-verified 17 September 2026 (HTTP 200 from the maintainer's machine, and the runs themselves); regulatory note re-dated on a review of this release's changes.
- `CITATION.cff` and the How to Cite block moved to v1.3.0 in lockstep.

### Unchanged
- `builder-packet-template.md`, `worked-example.md` and `risk-and-approval-rules.md`, byte for byte; their mastheads keep "last changed in v1.2.0", which the substance test requires.
- `LICENSE`, byte for byte.

### Verified (2026-09-17, KST)
- `python3 tools/check_release.py` passes on the release bytes: 5 companions, two changed since the last tag and naming v1.3.0, three unchanged and naming the release that last changed them; every internal link and anchor resolving; 3 packets carrying all 13 fields; deployed block at 7,889 characters with the stated SHA-256; candidate file identical to the mirror.
- The mirror block was compared byte for byte with the block pasted into GPT Builder, which the maintainer took from this repository's candidate cut; the runs in the suite's section 4 were made on it, and the maintainer states that the GPT was not saved again after the re-runs began and that the model setting was unchanged.

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
