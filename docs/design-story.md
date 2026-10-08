# From actions to evidence

The underlying workflow combined discovery, inbox checks, outreach, document preparation and a review queue. The reusable engineering problem was coordination: multiple sources and workers could describe the same opportunity, while an external action could finish even when its tool failed to return confirmation.

## Operational guidance, extracted

The source workflow already specified bounded research roles, a single account operator, historical deduplication, truthful candidate facts and human final submission. Its later refinements separated referral requests, promises and received referrals; prioritized unfinished packets and received links; and added daily funnels and periodic evidence reviews. These are documented design refinements, not measured performance gains.

The public version removes personal schedules, employer watchlists, account IDs, model choices, connector names, resume paths and exclusion lists. Users supply their own configuration. What remains is the coordination policy: evidence before promotion, partial coverage before totals, history before retries, and a named owner for every next action.

## Why one supervisor

Research can be parallel; sends and canonical state need ordered ownership. Optional workers return compact evidence or isolated packets. They do not independently message recipients or edit the shared tracker. Hosts without workers run the same roles sequentially.

This trades maximum parallelism for traceability. It also makes interruption manageable: the next run reads a durable checkpoint rather than reconstructing state from a long conversation.

## Why separate outcome dimensions

A single "done" flag collapses incompatible facts. A referral promise and a saved form can both represent progress without completing the application. The queue therefore tracks preparation state, referral stage and confirmed external outcomes separately. An uncertain send remains uncertain until history resolves it.

## Why adapters instead of dependencies

Account access, browsers, schedulers and model selection differ across agents. The playbook describes capabilities and fallbacks rather than requiring one provider. Missing access produces a truthful blocked item; it does not produce a fabricated empty result or an implicit new permission.

## What has and has not been established

The original operational guidance was ported and reviewed with synthetic scenarios. An initial baseline hypothetical review already reasoned correctly about history, uncertain sends, promises and drafts without this skill. There is no demonstrated benchmark uplift, measured token saving or controlled comparison. The value claimed is packaging and maintaining reusable operational constraints.

Next useful work would be repeatable host-specific offline evaluations and measured representative runs, followed by narrow corrections supported by observed failures. Live user data belongs outside this repository.
