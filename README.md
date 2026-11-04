# Hiring Panel for Codex

A Codex adaptation of [Alex Chen's hiring-panel skill](https://github.com/alexyc9381/hiring-panel-skill), based on commit `3ec597eb85a904efd17f9171e18f1b8d9dfe4e1a`, under the MIT license.

The skill runs seven review perspectives, merges their findings, rewrites the resume using supplied facts, and re-screens the draft. It uses isolated Codex subagents where supported and permitted, batches work to fit available slots, and clearly labels a sequential fallback. No API key or external resume-scoring service is required.

Full rebuilds now automatically iterate through up to three revision rounds, rechecking the PDF and all seven perspectives after each revision. The target is a verified screen PASS plus an interview-manager INTERVIEW or day-one-manager HIRE on the same version, with no material factual or submission blockers. It stops early for success, missing facts, stalled progress, or unavailable verification, and retains the round history and best supported version. It never invents qualifications or repeatedly samples unchanged text to force a favorable verdict. These are simulated reviews, not real hiring decisions.

## Install and use

Copy `skills/hiring-panel` into your Codex skills directory (`$CODEX_HOME/skills`, or `~/.codex/skills` when unset). Preserve the included LICENSE. Open a new Codex chat if the skill is not yet listed.

Example:

```text
$hiring-panel C:\Users\you\Documents\resume.pdf
Target: Senior product designer at a fintech startup.
Job posting: [paste the posting here]
```

Pasted resume text works too. The skill writes `PANEL.md` and an editable LaTeX project at `resume/main.tex` into a new `.hiring-panel/<date>-<name>/` directory in the working workspace. It compiles `resume/main.pdf` when a compiler is available, or opens the project in Codex's LaTeX editor for a live PDF preview. It reports any compilation or visual checks it could not complete. Unknown facts stay as visible `[ADD: ...]` placeholders, with questions in the report.

The bundled template uses a single column, Latin Modern Roman serif text, a centered contact header, thin section rules, compact bullets, and right-aligned dates. Supplied reference resumes guide the final layout. Ask for another format to override the LaTeX default. The public template contains no personal resume data.

Uniform item and list spacing, with evenly distributed section spacing, balances the top and bottom margins of a full one-page resume.

Generated or revised bullets and text entries fit on one rendered line, and every bullet list has exactly three items. The skill splits existing compound statements where useful and uses visible factual prompts when evidence is missing; it never invents achievements to fill a list. It checks bullet counts and visual wrapping before delivery, or reports when rendering could not be verified.

## Changes from the Claude Code version

- Codex `$hiring-panel` invocation and `agents/openai.yaml` UI metadata.
- LaTeX resume template with compilation, visual inspection, and PDF text-extraction checks.
- Removed Claude-specific `argument-hint` and fixed five-at-once scheduling.
- Explicit reviewer isolation, concurrency limits, failure handling, and honest single-agent fallback.
- Evidence citations, factual rewrite audit, and tracking for issues that require user input.
- Clear distinction between an ATS-style text simulation and testing a real ATS or final document layout.
- Source credit in the report and bundled license, without a promotional footer on the candidate's resume.

The seven perspectives and rewrite workflow come from the original project. This adaptation is not affiliated with OpenAI or Anthropic. Model reviews do not guarantee interviews or jobs.

Codex format reference: [Build skills](https://learn.chatgpt.com/docs/build-skills).

## Integrated ATS checks

Version 1.4 adapts the ATS optimizer, formatting, truthful tailoring, and job-description analysis guidance from [ResumeSkills](https://github.com/Paramchoudhary/ResumeSkills). It adds a required/preferred evidence table and separates PDF parsing, job evidence, and submission readiness. No extra skills need to be installed. Attribution and the upstream MIT notice are bundled with the skill.

The local `scripts/check_pdf_text.py` helper requires Python and `pypdf`. It checks the generated PDF against a source-derived expected-fields list, flags missing text and unfinished prompts, and writes a JSON audit in the private run folder. This is a limited extraction check, not an actual ATS simulator or guarantee of acceptance. The skill retains one-line entries, three bullets per list, and balanced spacing.

Example: `$hiring-panel Review my resume against this posting, check ATS readability, and build the LaTeX resume.` Attach the resume and paste the posting. Without a posting, it checks formatting and extraction but cannot evaluate job-specific keyword coverage.

### Checks after every edit

Version 1.5.1 requires a fresh ATS-readability screen after every resume edit, including small follow-ups and formatting changes. It compiles/exports the latest saved source, records source and PDF identities, checks text extraction and every rendered page, and invalidates earlier results if either file changes. It tries available permitted export or compilation options before asking you to upload a PDF. If verification is blocked, it names the missing check instead of carrying forward an old PASS. Narrow edits run the screen; full rebuild rounds retain all seven perspectives. This runs during skill use, not as a background file watcher.

### Structured parser verification

Version 1.6 uses the layout tested with OpenResume: Latin Modern Roman, standard headings, employer-first entries, clear entry gaps, and Skills last. Every generated or revised resume requires a local structured check of schools, jobs, projects, dates and word spacing alongside PDF extraction and visual review. The included adapter uses a separately downloaded, pinned OpenResume checkout; it does not upload resumes or bundle OpenResume code. See `skills/hiring-panel/references/structured-parser.md` for setup and commands. Dictionary/schema limitations are reported explicitly instead of changing real titles or claiming universal ATS acceptance.

### Final parsing repair loop

Version 1.6.1 checks the selected final PDF after all content edits, compares parsed fields and bullet ownership against the intended resume, and automatically repairs supported layout defects and reparses (up to three repair cycles). It saves `final-parsing-review.md` with each attempt and remaining mismatches. Fully VERIFIED requires correct field interpretation plus text and visual checks on the same version. Dictionary/schema limitations remain PARTIAL; missing checks remain UNVERIFIED. Favorable panel votes never override parsing errors.
