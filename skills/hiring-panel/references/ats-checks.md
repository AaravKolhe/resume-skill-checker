# ATS parsing and evidence checks

Adapted from the MIT-licensed ResumeSkills ATS optimizer, formatter, resume tailor, and job-description analyzer; see `../THIRD_PARTY_NOTICES.md`. Integrate these checks into the existing panel, not a separate installation of all upstream skills.

## 1. Check the submission format and document

Follow the employer's stated file-type and size requirements when supplied. Use a text-based PDF by default; if a portal explicitly requires DOCX, explain the requirement and produce that format when supported. Do not imply every ATS accepts or prefers the same file type.

Inspect text extraction AND rendered pages. Look for image-only pages, password restrictions, omitted text, interleaved reading order, damaged glyphs, merged names/titles/dates, overlapping content, and text hidden in graphics. A local extraction failure is an input or export problem to investigate, not evidence the candidate is unqualified. Use a second available extractor to investigate discrepancies rather than immediately blaming the PDF. Confirm apparent replacement characters in the saved UTF-8 text rather than trusting terminal display encoding.

Prefer a single column with recognizable headings (Education, Experience, Projects, Technical Skills), common readable fonts, simple bullets, and consistent dates. Put name, email, phone, and supplied profile links in the main document body, not running headers/footers or graphics. A centered contact block at the top of the body is fine. Thin section rules, bold/italic text, and right-aligned dates are acceptable only when the final extraction retains their intended order and associations. Do not infer tables or parsing failures from alignment alone.

Keep the user's three-bullet, one-line, and balanced-spacing preferences. Do not conceal required evidence, invent facts, shrink type below 10 pt, or clip content to meet them. Explain an unresolved conflict. Do not use invisible text, keyword dumps, or repeated terms to game screening. Keep actual dates and titles; never conceal gaps by silently removing date precision.

## 2. Map the posting to evidence

For each distinct substantive requirement, quote the posting and classify it as explicitly required, explicitly preferred, or unspecified. Repetition alone does not make a phrase mandatory. Separate tools/methods, credentials/education, experience, responsibilities, and job-relevant collaboration evidence. Respect alternatives such as "Python OR R" and compound requirements such as "Python AND SQL" rather than scoring every occurrence.

Use a table in `PANEL.md`:

| Posting criterion and classification | Resume quote/location | Evidence status | Truthful edit or question |
|---|---|---|---|
| Exact posting excerpt | Original/final section and line | Exact wording / supported equivalent / partial evidence / not evidenced / confirmed gap | Supported wording or missing fact to ask for |

Not evidenced is not equivalent to not qualified. A projected outcome is not an achieved result; coursework, exposure, and proficiency are not interchangeable. Never infer certification, seniority, years of experience, or eligibility from keyword overlap. Do not classify a strong match as overqualified or discourage applying solely on a heuristic threshold.

Use the posting's exact wording only where the underlying facts support it. Expand a relevant acronym once if its meaning is established. Place terms naturally in Skills and relevant accomplishment bullets; add a summary only when it improves the user's resume, not to satisfy a keyword quota. Show consequential before/after edits and the source facts supporting them. Preserve factual metrics; never estimate accomplishments to fill gaps.

Report required and preferred evidence separately. Do not produce a proprietary-looking ATS score, pass probability, predicted ranking, or an 80% passing threshold. If the user specifically requests a number, provide only a transparent evidence-coverage count with the listed denominator and treatment of partial/alternative criteria; label it a local descriptive measure, not an ATS result. With no posting, skip job-specific coverage entirely.

## 3. Verify the final PDF

Create `expected-fields.json` as a JSON array of strings taken from the intended resume: name, supplied contact fields, headings, each employer/title, dates, credentials, key metrics, and important supported job terms. Do not derive this list from the extracted PDF, which would conceal omissions. Keep it inside the run directory. Run the bundled helper with the available Python environment (requires `pypdf`):

```text
python <skill-directory>/scripts/check_pdf_text.py <run>/resume/main.pdf --expect-json <run>/expected-fields.json --output <run>/pdf-text-check.json
```

The helper normalizes Unicode, whitespace, and case for field matching. It reports blank pages, replacement characters, visible `[ADD: ...]` markers, absent expected fields, and encrypted inputs. Exit 0 means its limited checks found no issues; 1 means findings need review; 2 means it could not run. It does NOT detect every reading-order problem, wrapping, layout defect, qualification mismatch, or invisible-text technique. Manually inspect page order, field associations and all three bullets per list. Short substring matches are not proof of a complete qualification. Never describe this helper as an ATS emulator.

Correct confirmed extraction/layout errors and rerun checks on the final version, up to three repair attempts. Use a new numbered audit filename for each run; the helper refuses to overwrite existing files. Never alter source facts just to satisfy a string check. If an expected field is absent due to an extractor quirk, record the exact discrepancy and the corroborating evidence; do not silently erase the failing expectation. If no saved PDF is available, preserve source and mark the PDF check unverified.

## Latest-edit verification (every resume edit)

Treat one saved revision as the unit of verification, not each keystroke. Apply this procedure after content edits, formatting changes, compiler repairs that alter source, and later follow-up corrections, even outside a full rebuild. A new edit invalidates all earlier PASS/readiness results for the current document. Do not rerun all seven reviewers for a narrow edit unless requested; rerun the automated screen and factual/job-evidence checks affected by that edit.

1. Save the current source and preserve an immutable snapshot. Record its absolute path and SHA-256, plus hashes of included local source/style/assets when applicable. Prepare expected fields from the intended current content, never from extracted output.
2. Compile that saved version. Prefer the existing editor and its supported export/download capability. If it produces only a preview, proactively discover an available export mechanism rather than immediately requesting an upload. When export is unavailable and separate compilation is permitted, use a local TeX engine with shell escape disabled on the same saved source and dependencies, writing only to a private audit directory. Keep the existing editor open. Honor explicit restrictions against separate compilation or replacement documents; ask only for the specific missing export/permission when required. Never silently install a compiler or upload personal data to an external conversion service.
3. Establish that the PDF came from this compilation/export. Record the compile/export outcome, source identity, PDF absolute path and SHA-256 together in a new audit manifest. A filename, recent timestamp, old sibling `main.pdf`, or an unrelated PDF is insufficient evidence of correspondence. If that relationship cannot be established, mark freshness unverified and do not audit it as the latest edit.
4. Run `check_pdf_text.py` on that PDF using the current expected fields and a new output filename. Inspect extracted reading order and field associations; render and inspect every page for wrapping, overlap, clipping, spacing, and three-item lists. Reassess required/preferred job evidence against the current posting without inventing a score. A helper exit 0 is only a text-check result, not the whole screen verdict.
5. Fix supported defects within the existing three-repair limit. Each saved repair restarts verification on its new identity. Immediately before delivery, rehash the source/dependencies and PDF. If any changed during checking, invalidate the audit and verify the new saved version; do not attach the previous result to it. If ongoing changes prevent a stable audit within the repair limit, report that blocker.
6. Save a current-version screen result linking source/PDF identities, extraction audit, visual findings, job-evidence status and readiness. Report PASS only when the latest version's required checks are complete and no material obstacle remains; REJECT for evidenced material obstacles; UNVERIFIED for missing evidence. State the exact failed/unavailable step and attempted fallback. Ask for an exported current PDF only after available permitted export/compile options have been attempted or ruled out. Never present an earlier PASS as current.

The manifest and hashes establish which files were checked; they do not themselves prove that a PDF matches its source. The observed compile/export operation supplies that link. This is an agent workflow whenever the skill edits a resume, not a background watcher for edits made outside a running task.

## Structured field assignment

For every generated or revised PDF, also follow `structured-parser.md`. Verify actual jobs/projects and their associated fields against expectations, not merely the presence of words somewhere in the PDF. Include this result in the current-version manifest and invalidate it on edits. A text-helper pass cannot override a structured parser failure.

After final content selection, complete the end-of-run repair loop in `structured-parser.md`; record its VERIFIED/PARTIAL/UNVERIFIED status separately from a simulated hiring verdict. Unresolved field assignment errors cannot be overridden by successful text extraction.

## 4. Report independently

- **Parsing:** checked with no observed issues / issues found / unverified; name the file, extractor, visual check, and limitations.
- **Job evidence:** criterion-by-criterion results, with required and preferred separated; unavailable without a posting.
- **Submission readiness:** ready for user review / needs facts or fixes / unverified. Visible placeholders are unfinished even if parsing is clean.

Give before/after comparisons only for checks actually performed on both versions. A model screen's PASS means no material obstacle found in inspected evidence, not a guarantee of employer acceptance. User confirmation of facts and any portal-specific requirements can still be outstanding.
