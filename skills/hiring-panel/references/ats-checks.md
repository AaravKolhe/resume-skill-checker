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

## 4. Report independently

- **Parsing:** checked with no observed issues / issues found / unverified; name the file, extractor, visual check, and limitations.
- **Job evidence:** criterion-by-criterion results, with required and preferred separated; unavailable without a posting.
- **Submission readiness:** ready for user review / needs facts or fixes / unverified. Visible placeholders are unfinished even if parsing is clean.

Give before/after comparisons only for checks actually performed on both versions. A model screen's PASS means no material obstacle found in inspected evidence, not a guarantee of employer acceptance. User confirmation of facts and any portal-specific requirements can still be outstanding.
