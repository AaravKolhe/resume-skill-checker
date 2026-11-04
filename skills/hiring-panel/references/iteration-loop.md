# Evidence-based revision loop

This extends the seven-persona panel into a bounded improvement process. Preserve the role/posting, factual source, reviewer rubrics, and user formatting constraints throughout. Do not reinterpret the task as maximizing a numerical ATS score.

## Baseline and success criteria

Review the current resume once with all seven perspectives and preserve it as round 0. Build the required/preferred job-evidence table if a posting exists. Track each supported finding with a stable ID; do not treat a renamed or reworded finding as a new improvement.

The default target requires all of these on the SAME evaluated version:

1. The automated screen returns PASS, based on an inspected final document with no unresolved material parsing or layout issues.
2. The interview-gate manager returns INTERVIEW OR the day-one manager returns HIRE.
3. Factual audit passes: no invented claims, unanswered material facts, visible `[ADD: ...]` prompts, or unresolved submission blockers. All explicitly required job criteria are mapped; no unresolved material required-evidence gap or confirmed mandatory-qualification mismatch may be hidden behind positive votes.

The other perspectives may still return MAYBE or decline. Disclose their concerns rather than claiming unanimous HIRE. Their supported material objections still require resolution even if the target voters are positive. Without a posting, label any success "role-level simulated review target met; exact job match unverified." If the user explicitly sets another target, record it, but keep factual integrity and submission-readiness checks separate and mandatory for claiming the resume ready.

If the baseline already meets the target, do not introduce gratuitous content changes. Produce a requested LaTeX version if necessary and re-review the actual final output after conversion.

## Each revision round

Default budget: at most THREE revised versions after round 0. Respect a user-specified smaller budget; if the user requests more, record that explicit finite budget. "Until it passes" alone does not authorize an endless loop. Compiler repair attempts are technical retries within a round, not new content rounds.

1. Choose the highest-impact supported findings that can be fixed with existing evidence. Revise wording, relevant ordering, supported terminology, and layout. Show which source facts support each substantive edit. Preserve the one-line entries, three bullets per list, and balanced spacing unless the user overrides them.
2. Audit new factual claims and the job-evidence table against the original and explicit clarifications. An unsupported required skill cannot be created by inserting its keyword. Do not delete a meaningful requirement, essential fact, or unresolved prompt merely to turn a failure into PASS. A prompt may be removed only when answered or when its optional proposed claim is omitted and the underlying gap is honestly retained in the report.
3. Apply the latest-edit verification procedure in `ats-checks.md`: compile/export the current saved source, establish PDF freshness, inspect it, and run PDF extraction checks with a new audit filename. Record document identity (path plus hash or immutable snapshot). Refresh expected-field strings only for justified edits, preserving the meaning and metrics being tested. If required inspection is unavailable, mark it unverified rather than claiming target completion.
4. Run ALL seven perspectives against this version, using fresh contexts when supported. Supply the same target, rubric, and appropriate extraction/layout evidence; give the recruiter only this version's top third. Do not send prior verdicts, round number, desired outcome, or an instruction to be more favorable. The coordinator sees previous rounds; reviewers do not. If fresh independent contexts are unavailable, label the sequential or mixed execution honestly.
5. Save the complete results, changes, evidence mapping, and resolved/remaining/new findings. Compare material findings, not just votes: improved votes with unchanged evidence do not demonstrate progress.

Do not retry an unchanged resume to obtain favorable votes. A failed tool call may be retried once without treating it as another opinion. Missing reviewers or checks must be disclosed; a missing target reviewer cannot be presumed favorable. Restore accidental factual regressions before proceeding.

## Stop and select the final version

Stop at the first qualifying version. Otherwise stop when:

- **Needs user facts:** remaining material problems require facts or clarification. Complete independent edits first, then ask focused questions; retain visible prompts where needed. Do not run cosmetic rounds against a known factual blocker.
- **No actionable progress:** no supported change remains, or two consecutive revised versions resolve no material findings or evidence gaps. Preserve disagreements; do not lower standards or rerun unchanged content.
- **Verification unavailable:** essential parsing/layout checks cannot be completed after their bounded retries. Deliver an explicitly unverified draft.
- **Round limit:** three revision rounds have completed (or the explicit user budget is exhausted).

Choose the strongest supported version, prioritizing factual integrity and submission readiness, then fewer material findings and better evidenced job alignment, then clarity. Never combine a favorable screen from one version with a HIRE from another. If restoring an earlier snapshot, restore its exact content and cite that snapshot's reviews; any further change requires new verification. Keep all losing rounds visible in the report.

In `PANEL.md`, include a table: round, document identity, major changes, screen verdict, interview-manager verdict, day-one verdict, remaining five-persona concerns, factual/readiness status, resolved finding IDs, and remaining blockers. Include the selected round, actual stop reason, and next factual questions. State which checks were completed and which were unverified. Never label "target met" when stopping for missing facts, unavailable checks, stalled progress, or the budget limit.

When the user later supplies facts, record them as explicit clarifications and continue from the saved selected version. Retain prior rounds and allocate a fresh bounded revision budget; do not restart by erasing history.

Before delivering the selected version, apply the final parsing gate in `structured-parser.md`. Panel success does not bypass this gate; formatting repairs require new current-version audits. Preserve PARTIAL or UNVERIFIED parsing independently from favorable content votes.
