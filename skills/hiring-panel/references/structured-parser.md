# Structured parser check for every final resume

Run this after each generated or edited PDF, including narrow follow-ups. Pair it with the latest-edit hash/compile procedure, text audit and visual inspection. This checks whether entries are assigned to the right fields; finding their words somewhere in extracted text is insufficient.

## Tested layout
Use the bundled Latin Modern Roman template, Unicode mapping, standard section headings, employer then actual role, and uniform 6pt gaps between entries within sections. Put Skills last. Do not enable pdfinterwordspaceon: OpenResume removes separate whitespace items, which can concatenate words. Keep course codes in descriptions rather than inside role titles. Use plain metric names where math extraction is unreliable. Retain three single-line bullets per list and verify real rendered fit. Preserve supplied titles, dates and claims.

## Local setup
Use an existing verified local installation when available. Otherwise obtain a separate checkout of https://github.com/xitanggg/open-resume at commit `4f8255a2c763479837f69f1dccf2a3338730cd79` in a private work/cache directory. Follow normal network/install permissions. Record the actual commit with `git rev-parse HEAD`. Do not copy upstream source into this skill or the public skill repository. OpenResume is AGPL-3.0; retain its license in the separate checkout.

In a separate dependency directory install `typescript@5.0.4` and `pdfjs-dist@3.7.107` using npm with `--ignore-scripts --no-audit --no-fund`. The adapter uses the standard PDF.js build for text extraction, so optional native canvas builds are unnecessary. No full Next.js app install or hosted resume upload is needed. Keep dependency folders out of the skill package.

## Expectations and execution
Create `expected-structure.json` FROM THE INTENDED SOURCE before reading parser output. Supported top-level keys: `profile`, `educations`, `workExperiences`, `projects`, `sectionNames`. Provide name/contact fields, each school's name/degree/date, every employer/title/date, every project/date, and expected descriptions. Include all entries in each array; array length and order are checked. Objects may omit optional keys. A descriptions array of three empty objects checks only count; prefer actual source-supported bullet strings to verify ownership/content. Do not derive expectations from observed parser output or omit failed fields to force success.

Run:

```text
node <skill>/scripts/check_openresume.cjs <current.pdf> <openresume-checkout> <dependency-directory> <new-audit.json> <expected-structure.json>
```

The adapter transpiles unmodified upstream parser functions into `<new-audit.json>.modules`, reads the PDF locally, and writes fields, sections, mismatches and PDF hash. Use new output paths for retries. Exit0 means compared expectations matched, 1 means mismatches, 2 means setup/execution failed. Pair the recorded PDF hash with the verified source/export manifest. Review all fields and section boundaries, not just the exit code. Skills/Leadership/Honors must also be checked in the returned sections and full extraction because the adapter does not fully extract those fields.

Fix supported formatting defects and rerun within the three-repair limit. Never change truthful job titles, remove relevant entries, hide text or weaken expectations merely to satisfy the parser. If a dictionary lacks an actual title (for example Handyman), preserve it and report that field mismatch. OpenResume's schema lacks dedicated Leadership/Honors fields; distinguish that limitation from entries being incorrectly merged into paid jobs. Missing candidate location/summary is not an error if not supplied or required.

## End-of-run repair loop

Run this after final content selection and all panel-driven edits, before handing over any resume. It also applies to follow-up edits. Compiler/layout repairs are not a reason to skip re-parsing. Use up to three formatting repair cycles after the initial check; do not ask permission between already authorized local repairs.

1. Freeze the intended fields and entry ownership from the source. Expectations must include exact contact fields, every school, employer, actual title, project, dates, and complete bullet text associated with each entry. Empty object placeholders or counts alone are insufficient for final verification. Include section boundaries and check all skills and leadership/honors text in the returned sections. Record intentional absent optional fields such as location; never invent them.
2. Compile/export the selected source and record source/PDF hashes. Run both text extraction and the structured parser. Review actual parsed values beside expected values, including lost spaces, swapped employer/title fields, merged/split entries, incorrect dates and bullets belonging to the wrong entry. Match the user's named parser when supplied; use the local OpenResume test by default.
3. For each discrepancy, diagnose its cause using actual output and, when available, parser rules. Repair formatting only where supported: font names/encoding, normal word spaces, conventional headings, employer/title ordering, section separation and consistent entry gaps. Preserve facts and the user's layout constraints. Do not rename a real role, add hidden keywords, omit facts, or modify parser code/expectations to manufacture success.
4. Rebuild after every repair and repeat BOTH extraction and structured checks, with a new audit filename. Render all pages and inspect the latest PDF for wrapping, clipping and spacing. Save each attempt's source/PDF identity, mismatches, change made and outcome. If repair introduces a content change, re-audit that fact and the relevant job evidence; full content-rebuild rounds retain their seven-reviewer requirement.
5. Stop successfully only when intended fields and entry ownership match, the visual/text checks are complete, and the source/PDF have not changed since checking. Otherwise stop at three repair cycles, two consecutive cycles without resolving a discrepancy, unavailable tools, or a proven parser dictionary/schema limitation that formatting cannot fix. Do not repeatedly reparse an unchanged file. Keep the best fact-preserving version and list each remaining mismatch.
6. Save `final-parsing-review.md` beside the final PDF: actual vs expected fields, attempt history, tested parser/version, source/PDF hashes, checked/unchecked areas and one status below. Link it in PANEL.md. Check hashes immediately before delivery; changes reopen the gate.

Final parsing status is separate from the hiring-panel content verdict:
- **VERIFIED:** every required comparison and visual/text check completed with no unresolved interpretation discrepancy.
- **PARTIAL:** checks ran but at least one field is still missing, misassigned or unsupported by the parser's schema/dictionary. State the exact limitation and whether the text is nevertheless visible. Do not label the resume fully ATS-verified or submission-verified.
- **UNVERIFIED:** the current export or necessary check could not be obtained/executed.

A favorable interview recommendation or another extractor recovering the words cannot erase a structured field failure. For example, an empty Handyman title remains a documented PARTIAL result even when the PDF shows the title. A material required field failure needs user attention before submission. If a portal allows manual correction, mention that option without claiming it has been corrected.

## Report honestly
Save source/PDF identity, upstream commit and dependency versions, expectations, full audit, field discrepancies and visual results with the current round. Report structured parsing as checked/no material issues, issues found, or unverified. Never claim every ATS accepts the resume. The local pinned parser can differ from the live website. If the user supplies a failing output from another parser, investigate its actual rules rather than assuming this test supersedes it. If local setup is unavailable, complete independent content/text checks and explicitly mark structured verification unverified; do not silently skip it or treat a model review as a parser execution.

No resume data is uploaded by this helper. External uploads need separate user authorization.
