# Limits, interruption and cost

This instruction package has no metered backend and makes no calls by itself. The agent host, models, tools and optional services determine usage and charges. A subscription fee is not a per-run token price and does not establish unlimited capacity.

## Before and during a run

Set user-chosen caps for searches, detail fetches, conversation checks, packets, workers and elapsed time. Reuse compact state and dated evidence, batch independent reads and avoid loading full history when a relevant slice suffices. Record actual tool/query counts and coverage. Record tokens, currency and cost only when authoritative usage metadata supplies them; otherwise mark them unavailable.

If a rate limit, quota, tool failure or model interruption occurs:

1. Persist completed records, current step, pending items, source coverage and next cursor when execution still permits. Keep durable incremental checkpoints so abrupt termination does not depend on a final save.
2. Mark any external action without confirmation as uncertain. Do not retry a send until relevant history resolves it; if access remains unavailable, keep it blocked.
3. Record the actual failure and reset time only if supplied. Never turn blocked discovery into zero opportunities or a failed inbox read into no replies.
4. Use an available fallback only within existing permissions and privacy constraints. Otherwise wait for limits to reset or request the missing decision. Do not automatically switch provider, spend money or create accounts.
5. On resume, re-read checkpoint and authorization, reconcile uncertain actions, refresh stale role evidence and continue the next incomplete item. Preserve prior confirmed outcomes and prevent duplicate sends.

## Honest estimates

For a user-reported budget of approximately ₹2,000/month for ChatGPT, report that as a personal budget estimate only. The exact plan, taxes, billing amount, model allowances and reset behavior require current account/provider information. This repository does not claim to run an unlimited agent on that budget.

Illustration only: ₹2,000 / 30 days ≈ ₹67/day is an accounting allocation, **not measured daily agent usage**. Dividing that by a chosen number of runs is not a provider per-run price and cannot predict quota consumption. For an independently billed API, estimate input tokens × current input rate plus output tokens × current output rate and tool charges, clearly stating assumptions, currency conversion and tax exclusions. Do not apply API pricing to a ChatGPT subscription.

Measure a small representative run only when host metering is available. Record plan/date, workload, observed usage and remaining limits; then revise caps from evidence. No measured token savings, per-run cost or benchmark uplift is claimed here.
