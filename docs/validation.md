# Validation scope

Publication validation checks skill metadata, relative reference links, synthetic JSON, public-content sanitization, CLI discovery and an isolated project-scoped install. Installation checks packaging, not account integration or behavioral effectiveness.

The [synthetic scenarios](../skills/career-supervisor/references/synthetic-demos.md) cover history hydration, uncertain sends, model-limit recovery, promise/draft distinctions, missing capabilities and expired-role eligibility. They specify reviewable expected behavior and can be run without live accounts. They are not fabricated test transcripts or measured benchmarks.

Known limits: the playbook depends on the host following instructions, authorized tools returning useful evidence and the user supplying truthful configuration. Checkpoints cannot retroactively establish an unobserved external action. Account/provider usage is unavailable unless actual metering exposes it. Cross-agent live integrations have not been certified.

## Publication checks — 9 October 2026

- Bundled skill metadata validator: passed.
- Eleven repository-relative Markdown references and the synthetic JSON fixture: resolved and parsed successfully.
- Sanitization scan and content review: public files contain synthetic examples and no copied live messages, account IDs, resume links, local source paths or private employer facts.
- Official skills CLI: discovered one skill and completed a project-scoped copy install with Codex, Claude Code and Cursor selected. Its summary showed the shared `.agents/skills` copy and `.claude/skills` copy. This verifies packaging, not live host behavior.
- `skills find career-supervisor`: initially returned no listing. A subsequent browser check verified the live [skills.sh detail page](https://skills.sh/vama0259/agent-workflow-skills/career-supervisor), including the skill content and install command. Search indexing and install counts may update separately.

No automated behavioral benchmark was run for this release. The scenario fixtures and initial baseline review are documented without claiming measured improvement.
