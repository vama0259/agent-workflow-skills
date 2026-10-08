# Capability adapters

The skill uses ordinary Markdown instructions. Claude Code, Codex, Cursor and other agents that load Agent Skills can interpret it, but their available tools and permissions differ. Installation is not end-to-end compatibility certification.

| Needed capability | Available adapter | Fallback |
| --- | --- | --- |
| Public discovery | Agent's search connector or web search | User-supplied official links; report incomplete discovery |
| Official verification | Fetch/browser over employer sources | Manual verification queue with unverified status |
| Relevant inbox history | Authorized account connector | Signed-in browser if permitted; otherwise user checks, no inferred absence of replies |
| Outreach | Authorized send connector with verification | Supported signed-in UI; otherwise prepare a draft only |
| Packet preparation | Existing resume/document tools | Markdown answer sheet and change suggestions; no fabricated compiled PDF |
| Shared state | Local JSON/CSV or existing tracker integration | Compact user-owned checkpoint document |
| Worker delegation | Agent-native subagents, explicitly authorized | Sequential role execution with the same single-writer rule |
| Scheduled wakes | User-configured host scheduler | User-triggered runs; no background execution implied |

Choose the least complex available adapter that preserves authorization and evidence. No named connector, model, cloud service or paid subscription is required by the instructions. A browser is not permission to bypass login, CAPTCHA, restrictions or attestations. Stop at access barriers and record the blocker.

Lower-cost models are optional for bounded extraction if the host supports them and the user permits model selection. Provide only assigned sources, relevant facts, dedupe slice and output schema. Escalate a concrete ambiguity when useful; do not assume a particular model is available or cheaper. Do not change providers, disclose private context or purchase credits as an implicit fallback.
