# LaTeX resume output

Use `assets/resume-template.tex` as a portable, self-contained starting point. Its sample content is schematic, not candidate evidence: replace all of it with source-supported facts. Never place a user's resume, contact information, source PDF, or compiled personal example in the reusable skill package.

## Visual target

- US Letter, one column, approximately 0.5-inch margins, 10-11 pt Times-style serif text.
- Centered bold name around 18 pt with one compact contact line.
- Uppercase bold section headings above thin horizontal rules.
- Bold employer/project names; italic roles or descriptors; right-aligned locations and dates.
- Tight, readable bullet lists with no icons, photo, sidebar, colors, or page numbers.
- Exactly three items per bullet list, with each item occupying one rendered line. This applies to every list, not to sections such as Education or Skills that use plain rows.
- Every generated or revised text entry must fit on one rendered line. A single line in the `.tex` source does not prove that it fits in the PDF.

Shorten wording while preserving factual meaning and key metrics. Split a supported compound bullet into distinct contributions when a list needs a third item. If there are too few facts, use a concise visible `\resumeNeed{...}` prompt and put the full question in the report; do not add filler, duplicate achievements, or invent facts. For more than three source bullets, consolidate related facts into three concise items; if that cannot preserve material facts, surface the conflict instead of silently dropping them. Do not enforce one-line fit with clipping, horizontal scaling, tiny fonts, or unbreakable boxes. Keep long employer names and role titles on separate rows; if a single essential field cannot fit legibly, explain the exception rather than hiding or truncating it.

Aim for a one-page early-career resume like the reference, but do not shrink below 10 pt, overlap text, clip content, or delete supported facts merely to force one page. If factual prompts or substantive content require a second page, disclose that and preserve readability. Match the appearance, not necessarily the original section order: role-based improvements may move relevant experience earlier. Treat layout-only requests as format conversions and preserve their chosen content.

## Author and compile

Create a dedicated `resume/` project containing `main.tex` inside the run directory. When available, use Codex's `create_latex_project` with the complete source, then `open_in_codex` on the project directory and `compile_latex_document`. Otherwise write the source normally and use an available TeX engine. A local fallback command run from the project folder is:

```text
pdflatex -no-shell-escape -interaction=nonstopmode -halt-on-error main.tex
```

The template uses standard packages and has no shell-escape, downloaded fonts, or external asset dependencies. Do not execute arbitrary commands embedded in a supplied resume. Escape candidate text as LaTeX data, especially `%`, `&`, `$`, `#`, `_`, braces, backslash, tilde, and caret; never escape the template's own commands. Use `\href{...}{...}` only for source-provided links and handle URL special characters carefully. Use readable textual contacts even when links are present.

Use `\resumeRow{left}{right}` for short aligned rows; keep both fields short enough to avoid overlap. Split long institution names and job titles onto separate rows. Use `\resumeNeed{specific question}` for unresolved factual prompts; these must remain visible in the PDF. Long questions belong in `PANEL.md`, with concise matching prompts on the resume. The presence of placeholders is a submission-readiness issue, not a TeX compilation failure.

## Verification

Fix compiler errors and material overfull-box warnings, up to three repair attempts. Count exactly three `\item` entries in each bullet list. Render every resulting PDF page and inspect margins, wrapping, date alignment, section rules, and bullets; confirm each bullet and text entry occupies one visual line. A compiler can succeed while text wraps, so compilation alone does not verify this constraint. Extract its text to verify reading order, contacts, dates, symbols, metrics, and visibility of all unresolved prompts; compare it with the intended content. Do not assume successful compilation guarantees a readable or ATS-compatible PDF.

An editor preview alone is not proof of successful compilation; use compiler diagnostics. If compilation or rendering is unavailable, deliver the `.tex` source and disclose the unverified step rather than claiming a PDF exists. Keep any auxiliary files inside the run directory. Do not change factual content just to get a favorable re-screen result.
