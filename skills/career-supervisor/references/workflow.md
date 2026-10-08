# Run structure and evidence ledger

## Configure once, read compact state each run

Keep a private user configuration outside the installed skill: truthful candidate facts, role families, locations, employer preferences/exclusions, permitted communication channels, authorization scope, timezone, packet sources, canonical tracker pointer and run caps. No public template grants outreach authority. Timing and alternate-contact rules are user preferences, not universal defaults.

The supervisor plans bounded coverage and owns accounts and shared writes. A portal scout verifies official openings; a hiring-signal scout returns relevant post evidence and requested contact route; a packet builder prepares truthful role-specific materials; a recorder merges verified outcomes sequentially. These are roles, not always-running services. Use separate output paths for workers and await completion before merging. Sequential execution is fully supported.

## A bounded run

1. Hydrate history and reconcile uncertain outcomes. Read current queue, dated evidence, previous sends and authoritative receipts before producing totals or sending.
2. Consume a dated discovery handoff if configured. Rotate unprocessed official sources rather than repeat every search. Persist actual coverage by source/date, including incomplete groups.
3. Check changed relevant conversations within authorized access. Record check failures separately from successful empty results. Prioritize received instructions, referral links and deadlines.
4. Discover a bounded set of roles and hiring signals. Prefer verified fit and evidenced freshness; broaden only within user-selected locations and eligibility. Keep talent pools distinct from vacancies. Respect an author's requested route, including forms-only or no-DM instructions.
5. Verify the strongest leads against official sources and user facts. Classify eligible, conditional, user-requested stretch, excluded or unverified. Recheck stale or uncertain live status before role-specific action. For expired openings, find a separately verified replacement or report the expiry.
6. Prepare highest-priority packets and only explicitly authorized individualized outreach. Check history immediately before account actions; do not manufacture volume to meet a cap. Requests involving unknown personal facts, sensitive documents, offers or commitments go to the user.
7. Verify outcomes, merge sequentially, checkpoint and deliver the review queue. Do not count unfinished groups as complete.

An illustrative configuration might cap a run at 8 searches, 5 detail fetches and 2 packets, with zero sends until authorized. These values are examples to tune, not recommended capacity, quotas or cost predictions. Cache dated evidence only while relevant; an unchanged cache cannot prove an opening is still live.

## Records and deduplication

Deduplicate roles by employer plus official requisition, falling back to normalized official URL. Strip tracking parameters but preserve identity-bearing job IDs. Deduplicate posts by permalink and sends by recipient + role + channel. Count employer applications once by requisition/application ID, even when receipts repeat across channels.

Suggested queue fields: `key`, `company`, `title`, `requisition_id`, `official_url`, `source_url`, `checked_at`, `posted_evidence`, `live_status`, `requirements`, `fit`, `gaps`, `state`, `packet_paths`, `contact_candidates`, `sent_evidence`, `next_action`, `next_action_owner`, `human_fields`, `draft_status`, `deadline_evidence`.

Queue states: `discovered`, `verifying`, `qualified`, `outreach_ready`, `outreach_sent`, `preparing`, `ready_for_user`, `blocked`, `submitted_confirmed`, `closed`. Log `send_unconfirmed` separately on uncertain send outcomes; do not promote to `outreach_sent` without proof. Track referral stages independently: `unknown`, `requested`, `promised`, `received`, `declined`. Preserve stage evidence and transition time.

Use append-only dated action events alongside a small current queue. Each confirmed external action needs timestamp/timezone, role key, channel and proof reference. Store only relevant private conversation evidence in the user's private workspace. Never publish account identifiers or message contents from live operations.

If a workbook is locked, preserve it and write a dated verified copy with an explicit canonical pointer update where permitted. Do not silently switch trackers or discard history. JSON or CSV is acceptable if no spreadsheet capability exists.

## Review and iteration

Rank ready items by verified fit, deadline, received referral and remaining completion effort. Show direct form URL, packet links, honest gaps, referral stage, retained draft status and exact fields the user must resolve. Count sent events, replies, promised/received referrals, prepared forms and confirmed submissions separately.

If the user requests a periodic review, use observed counts and denominators, and acknowledge small samples. A generic rejection does not prove a skills gap or its cause. Improve positioning from concrete JD evidence and existing truthful content. No success-rate or efficiency claim follows from merely installing this playbook.
