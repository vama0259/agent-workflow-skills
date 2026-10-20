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

## Video skills checks — 20 October 2026

Scope: the six `video-*` skills are routing and setup instructions around five upstream projects. Checks cover packaging and the accuracy of what the skills say about those projects, not rendered output.

- Upstream review: each project was shallow-cloned at the commit listed in the [tool analysis](../skills/video-workflow/references/tool-analysis.md) and read without running its code. Install commands, flags, paths, licences, paid services and version requirements quoted in the skills were checked against the upstream README, skill files, licence and source at those commits.
- Metadata: all seven `SKILL.md` files parse as YAML, names match folders and descriptions are under 1,024 characters. The first CLI run skipped `video-onetake` because a colon in its description broke YAML parsing; the description was fixed and the check now uses a YAML parser.
- Links: 27 repository-relative Markdown links resolve. The tool analysis lives inside the router skill so its links survive installation.
- Official skills CLI: `skills add <repo> --list` discovered seven skills, and a project-scoped install with `--skill '*' -a claude-code` copied all seven into `.claude/skills`. This verifies packaging only.

- Video kit installer: `scripts/install-video-kit.sh` was run into a scratch folder on Linux.
  - It fetched all five upstream projects at the pinned commits in about 7 seconds.
  - It produced 30 skills in `<kit>/.claude/skills` (6 wrappers, 21 HyperFrames, onetake, collage B-roll, Lemo-Opuscar), the Clawd and Lemo-Opuscar tools, the licence files, the launcher and a README, about 100 MB in all. No onetake demo films were included.
  - A second run changed nothing.
  - Lemo-Opuscar's own `setup.sh`, given the kit's library path, used the pinned clone as it was. It neither cloned nor reset to `main`.
  - Not tested: macOS, and a real `claude --add-dir` session loading the kit. That loading behaviour comes from the Claude Code skills and permissions docs.

Not done: no video was rendered with any of the five tools, no paid service was called, and no upstream skill was run end to end. Upstream projects change quickly; re-check the pinned commits before relying on a detail.
