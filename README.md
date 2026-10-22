# Hiring Panel for Codex

A Codex adaptation of [Alex Chen's hiring-panel skill](https://github.com/alexyc9381/hiring-panel-skill), based on commit `3ec597eb85a904efd17f9171e18f1b8d9dfe4e1a`, under the MIT license.

The skill runs seven review perspectives, merges their findings, rewrites the resume using supplied facts, and re-screens the draft. It uses isolated Codex subagents where supported and permitted, batches work to fit available slots, and clearly labels a sequential fallback. No API key or external resume-scoring service is required.

## Install and use

Copy `skills/hiring-panel` into your Codex skills directory (`$CODEX_HOME/skills`, or `~/.codex/skills` when unset). Preserve the included LICENSE. Open a new Codex chat if the skill is not yet listed.

Example:

```text
$hiring-panel C:\Users\you\Documents\resume.pdf
Target: Senior product designer at a fintech startup.
Job posting: [paste the posting here]
```

Pasted resume text works too. The skill writes `PANEL.md` and an editable LaTeX project at `resume/main.tex` into a new `.hiring-panel/<date>-<name>/` directory in the working workspace. It compiles `resume/main.pdf` when a compiler is available, or opens the project in Codex's LaTeX editor for a live PDF preview. It reports any compilation or visual checks it could not complete. Unknown facts stay as visible `[ADD: ...]` placeholders, with questions in the report.

The bundled template uses a single column, Times-style serif text, a centered contact header, thin section rules, compact bullets, and right-aligned dates. Supplied reference resumes guide the final layout. Ask for another format to override the LaTeX default. The public template contains no personal resume data.

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
