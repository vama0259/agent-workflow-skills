# Evidence-first Agent Supervisor

A reusable agent skill by **Varun Malhotra** for coordinating research, authorized actions and human review across interrupted runs.

I built the underlying career-supervisor workflow around a practical systems problem: an agent can find information and take actions, but it also needs to remember what actually happened. A draft is not a submission. A promise is not a received referral. A timeout does not tell you whether a message was sent.

This public package extracts the coordination pattern into an agent-neutral playbook. Career operations provide a concrete example domain. It is an engineering project release; all public demonstrations are synthetic.

## Install

```bash
npx skills add vama0259/agent-workflow-skills --skill career-supervisor
```

Select your agent interactively, or target one explicitly:

```bash
npx skills add vama0259/agent-workflow-skills --skill career-supervisor --agent claude-code
npx skills add vama0259/agent-workflow-skills --skill career-supervisor --agent codex
npx skills add vama0259/agent-workflow-skills --skill career-supervisor --agent cursor
```

For manual installation, copy `skills/career-supervisor/` into your agent's supported skill directory, including its references. The package contains no executable send automation. Installing it grants no account access or authorization.

## What it adds

- One supervisor owns account operations and shared writes; optional workers return bounded evidence or isolated packets.
- An evidence ledger separates discovered leads, verified roles, uncertain sends, promises, received referrals, drafts and confirmed applications.
- Durable checkpoints preserve partial coverage and resume without blind retries.
- Capability adapters support connectors, browsers, local files or manual handoffs, with sequential operation when subagents are unavailable.
- A ranked review queue gives the user exact remaining actions. Final employer submissions stay with the user.

Start with the [skill](skills/career-supervisor/SKILL.md), [workflow](skills/career-supervisor/references/workflow.md), [synthetic demos](skills/career-supervisor/references/synthetic-demos.md), and [limits/cost explanation](skills/career-supervisor/references/limits-and-cost.md).

Example prompt: "Use career-supervisor to review these fictional records, reconcile history, and prepare a review queue. Do not send messages or submit applications."

## Design and iteration

See [the design story](docs/design-story.md) and [validation scope](docs/validation.md). This is an instruction package distilled from an existing operational workflow, not a hosted service, a continuously running bot or a benchmarked productivity claim. No live tracker, private conversation, candidate resume or employer-specific facts are included.

## Discovery and compatibility

The [official skills CLI](https://github.com/vercel-labs/skills) supports these agent targets. Actual account capabilities remain host-dependent; installation does not prove every integration works on every agent.

According to the [skills.sh FAQ](https://skills.sh/docs/faq), directory discovery uses aggregated CLI installation telemetry rather than a separate submission form. Public listing may lag publication and installation; do not interpret a successful install as a verified leaderboard listing.

## License

MIT. Contributions should use synthetic fixtures and preserve the evidence and human-action boundaries.
