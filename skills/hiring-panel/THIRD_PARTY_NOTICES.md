# Third-party sources

The core seven-perspective workflow is adapted from Alex Chen's hiring-panel skill:
https://github.com/alexyc9381/hiring-panel-skill
Its MIT license is retained in `LICENSE`.

ATS guidance is adapted from Paramchoudhary/ResumeSkills:
https://github.com/Paramchoudhary/ResumeSkills
Source commit: `74ae19e7c62b0516d1c298328e5544976c12da5d`.
Reviewed components: `skills/resume-ats-optimizer/SKILL.md`, `skills/resume-formatter/SKILL.md`, `skills/resume-tailor/SKILL.md`, and `skills/job-description-analyzer/SKILL.md`.
Its MIT notice is retained in `licenses/ResumeSkills-LICENSE.txt`.

This integration adapts parsing/formatting checks, required/preferred criteria mapping, and truthful keyword tailoring. It intentionally omits upstream hiring statistics, universal pass thresholds, keyword-frequency quotas, invented example accomplishments, and predictions of ATS acceptance. Existing user formatting preferences take precedence over upstream defaults. No other upstream skills or installers are executed or required.
