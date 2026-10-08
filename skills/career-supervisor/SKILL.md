---
name: career-supervisor
description: Coordinate evidence-based opportunity research, authorized outreach, application preparation and review queues with resumable state and human final submission.
---

# Evidence-first Agent Supervisor

Use this playbook for supervised career operations. It supplies coordination instructions, not account access, a scheduler or permission to contact anyone. The user defines candidate facts, scope, recipients, exclusions, budgets and authorized actions. Final employer application submission remains the user's action.

Read the user's current preferences, compact checkpoint, current queue and relevant historical tracker before acting. Empty new state does not mean empty history. If configuration is missing, do useful public research or prepare a synthetic demonstration; request only facts needed for the next dependent action.

Read [workflow](references/workflow.md) for run structure and state semantics; [capability adapters](references/adapters.md) when mapping tools or recovering from missing access; [limits and cost](references/limits-and-cost.md) when budgeting or encountering interruption. Use [synthetic demos](references/synthetic-demos.md) for offline review, never as real candidate facts.

## Operational invariants

- One supervisor owns account interactions, external sends, queue merges and canonical tracker writes. Optional workers research or prepare isolated packets only when delegation is available and authorized. Otherwise execute their roles sequentially. Never create independent account operators.
- Official employer evidence establishes title, requisition, location, requirements and live status. Search snippets and hiring posts are leads. Preserve unknown recency, eligibility and deadline as unknown. A repost is not an official posting date.
- Assess requirements against user-confirmed facts. Keep internships separate from full-time tenure; do not invent experience, skills, metrics, relationships, notice periods or work authorization. Mark concrete gaps and conditional eligibility.
- Before every authorized send, inspect relevant role history and actual recipient/channel conversations. Respect declines, exclusions and pending invitations. Use only published or person-provided professional email addresses. Contact caps are ceilings, not targets.
- Verify actual sent content and attachments. A timeout is `send_unconfirmed`; inspect history before considering a retry. Never treat an unsuccessful inbox check as no replies.
- A request, promise, received referral, prepared portal draft and confirmed application are separate outcomes. Only an actual receipt or portal confirmation supports `submitted_confirmed`; do not submit on the user's behalf.
- Preserve canonical resume facts, requested content and tracker history. Prepare each packet in an isolated role directory. Save supported portal drafts or deliver an answer sheet; leave unknown facts, attestations, terms, commitments and final submission to the user.
- Checkpoint partial coverage, evidence and next cursor after meaningful work. On interruption, resume from persisted state and reconcile uncertain external actions first. Report failures and blocked access honestly.

## Run outcome

Advance received referrals and unfinished ready packets before speculative outreach. Deliver a ranked review queue with evidence, packet links, retained draft status, exact remaining fields and next action owner. Separate new changes from cumulative totals, unique contacts from channel send events, and confirmed from uncertain outcomes. Keep unchanged scheduled runs quiet unless the user requested periodic updates. Scheduling must be configured separately with explicit authorization.
