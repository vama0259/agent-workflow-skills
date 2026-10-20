# Agent Workflow Skills

Reusable agent skills by **Varun Malhotra** for multi-step work where an agent has to choose the right tool, keep track of what actually happened and leave the final call to a person.

The package has two groups:

- **[AI video production](#ai-video-production)**: a router plus five skills that pick and drive open-source video tools (HyperFrames, onetake, collage B-roll, Clawd animation, Lemo-Opuscar).
- **[Evidence-first agent supervisor](#evidence-first-agent-supervisor)**: coordinates research, authorized actions and human review across interrupted runs, using career operations as the example domain.

| Skill | Use it to |
| --- | --- |
| [`video-workflow`](skills/video-workflow/SKILL.md) | Pick the right video tool for a request, and chain tools when one is not enough. Start here. |
| [`video-hyperframes`](skills/video-hyperframes/SKILL.md) | Make promos, explainers, PR videos, captions, overlays, decks and batch renders as HTML with HeyGen's HyperFrames |
| [`video-onetake`](skills/video-onetake/SKILL.md) | Make 10-30 s premium 16:9 launch teasers with onetake (noncommercial use only) |
| [`video-collage-broll`](skills/video-collage-broll/SKILL.md) | Turn one voiceover line into a 9:16 paper-collage B-roll clip (paid MaxFusion MCP) |
| [`video-clawd-animation`](skills/video-clawd-animation/SKILL.md) | Paint a short character cartoon with Clawd or a new character |
| [`video-opuscar`](skills/video-opuscar/SKILL.md) | Direct a 30-60 s film in one of 51 code-rendered art styles with score and narration |
| [`career-supervisor`](skills/career-supervisor/SKILL.md) | Coordinate evidence-based opportunity research, outreach and application review |

## Install

```bash
npx skills add vama0259/agent-workflow-skills                                  # pick skills and agents interactively
npx skills add vama0259/agent-workflow-skills --list                           # list the skills
npx skills add vama0259/agent-workflow-skills --skill career-supervisor --agent claude-code
```

Install the whole video group:

```bash
npx skills add vama0259/agent-workflow-skills --agent claude-code \
  --skill video-workflow --skill video-hyperframes --skill video-onetake \
  --skill video-collage-broll --skill video-clawd-animation --skill video-opuscar
```

Replace `claude-code` with `codex`, `cursor` or another supported agent, or omit `--agent` to choose. For manual installation, copy a folder from `skills/` into your agent's skills directory, keeping any `references/` folder.

Installing these skills grants no account access. The video skills download upstream tools only when you use them.

### Video kit: everything local, loaded only on demand

Skills in `~/.claude/skills` load their descriptions into every session. To keep video tooling out of normal sessions, install it into a separate folder instead:

```bash
git clone https://github.com/vama0259/agent-workflow-skills.git
sh agent-workflow-skills/scripts/install-video-kit.sh        # builds ~/claude-video-kit (or pass a folder)
~/claude-video-kit/bin/claude-video                          # a Claude Code session with the kit loaded
```

The kit holds the six `video-*` skills plus all five upstream tools, pinned to the analysed commits:
- HyperFrames' skills
- onetake, without its demo films
- the collage B-roll skill
- the Clawd starter kit
- the Lemo-Opuscar library and skill

It adds about 100 MB and the upstream licence files. Heavy dependencies (npm packages, Python venvs, Chrome, voice models) still install on first use.

- **Normal sessions:** nothing loads, so there is no token cost.
- **Video sessions:** the launcher runs `claude --add-dir <kit>`, or you run `/add-dir ~/claude-video-kit` inside a session. That adds the skill descriptions, roughly 4,000 tokens, most of it HyperFrames' 21 skills.
- **Privacy and pinning:** prefer the launcher. It turns off HyperFrames telemetry, feedback reports and its skill auto-install, which would otherwise write to `~/.claude/skills`. It also points Lemo-Opuscar at the pinned library. With `/add-dir`, the `video-*` skills set the same variables on each command. But an upstream HyperFrames or Lemo-Opuscar skill that triggers on its own does not, and may install into `~/.claude/skills` or clone `~/lemo-opuscar`.

Re-running the installer from a newer checkout updates the kit in place. Delete the folder to remove it. The script needs `git` and a POSIX shell (macOS, Linux, or WSL or Git Bash on Windows).

## AI video production

The video skills don't contain the video tools. Each one tells the agent when to use a tool, how to install it at a pinned version, which gates to apply (licence, paid services, privacy, approvals) and what to deliver. The upstream projects keep their own code, licences and creative workflows.

### What to use when

| You want | Use |
| --- | --- |
| Captions or overlays on existing footage, a deck, a PR video, a promo from a URL, vertical or square formats, transparent overlays, batch renders | `video-hyperframes` |
| A ~5 s paper-collage visual metaphor for one script line | `video-collage-broll` |
| A hand-painted, textless character cartoon | `video-clawd-animation` |
| A premium 10-30 s 16:9 launch teaser, **noncommercial** | `video-onetake` |
| A 30-60 s film in a named art style, or a data, science or product story from real material | `video-opuscar` |
| Anything else custom or long | `video-hyperframes` (`/general-video`) |

Some requests need more than one tool. `video-workflow` hands MP4s between them:

```text
brief ─► video-workflow ─┬─► video-collage-broll ──┐  metaphor inserts
                         ├─► video-clawd-animation ┤  textless cartoon
                         ├─► video-opuscar ─────────┤  styled hero film
                         ├─► video-onetake ─────────┤  noncommercial teaser
                         │                          ▼
                         └─────────────► video-hyperframes ─► captions, titles, VO, music,
                                                              9:16 / 1:1 cut-downs ─► delivery
```

Example prompts:

- "Use video-workflow: a 30 s vertical explainer about why our API is fast, with captions and two collage B-roll inserts."
- "Make a 15-second Clawd cartoon of Clawd trying to catch a butterfly, then add a title card."
- "Make a 45-second film in the ukiyo-e style about the history of tea."

### Before you start

| | HyperFrames | onetake | Collage B-roll | Clawd animation | Lemo-Opuscar |
| --- | --- | --- | --- | --- | --- |
| Licence | Apache-2.0 | **PolyForm Noncommercial** | MIT | MIT | MIT; demo films CC BY 4.0 |
| Paid services | Optional (HeyGen cloud and media) | None | **Required** (MaxFusion) | None | None |
| Needs | Node 22+, FFmpeg, Chrome | Python 3, Playwright, ffmpeg, Node | MaxFusion MCP, ffmpeg | Node 22.12+, Chrome, ffmpeg, GPU recommended | Node 20+, Python 3.11+, ffmpeg; GPU for 3D |
| Output | 16:9, 9:16, 1:1, 4K, alpha | 16:9, up to 4K60 | 9:16, 720p, 5 s | 16:9, 1080p | 1080p24 default, other sizes on request |

Every tool needs a local shell. A chat-only surface can plan and write prompts but cannot render. HyperFrames sends anonymous telemetry by default, and `video-hyperframes` asks before any public feedback report or paid usage.

Read the [video tools analysis](skills/video-workflow/references/tool-analysis.md) for the evidence behind each routing rule: strengths, limits, maturity and the commit each project was analysed at.

## Evidence-first agent supervisor

I built the underlying career-supervisor workflow around a practical systems problem: an agent can find information and take actions, but it also needs to remember what actually happened. A draft is not a submission. A promise is not a received referral. A timeout does not tell you whether a message was sent.

This skill extracts the coordination pattern into an agent-neutral playbook. Career operations provide a concrete example domain. It is an engineering project release; all public demonstrations are synthetic. The package contains no executable send automation.

What it adds:

- One supervisor owns account operations and shared writes; optional workers return bounded evidence or isolated packets.
- An evidence ledger separates discovered leads, verified roles, uncertain sends, promises, received referrals, drafts and confirmed applications.
- Durable checkpoints preserve partial coverage and resume without blind retries.
- Capability adapters support connectors, browsers, local files or manual handoffs, with sequential operation when subagents are unavailable.
- A ranked review queue gives the user exact remaining actions. Final employer submissions stay with the user.

Start with the [skill](skills/career-supervisor/SKILL.md), [workflow](skills/career-supervisor/references/workflow.md), [synthetic demos](skills/career-supervisor/references/synthetic-demos.md), and [limits/cost explanation](skills/career-supervisor/references/limits-and-cost.md).

Example prompt: "Use career-supervisor to review these fictional records, reconcile history, and prepare a review queue. Do not send messages or submit applications."

See [the design story](docs/design-story.md) for how it was built. It is an instruction package distilled from an existing operational workflow, not a hosted service, a continuously running bot or a benchmarked productivity claim. No live tracker, private conversation, candidate resume or employer-specific facts are included.

## Validation

See [validation scope](docs/validation.md). Checks cover packaging, metadata and links, not live account integrations or video quality. No skill in this package has a measured benchmark.

## Discovery and compatibility

The [official skills CLI](https://github.com/vercel-labs/skills) supports these agent targets. Actual capabilities remain host-dependent; installation does not prove every integration works on every agent.

According to the [skills.sh FAQ](https://skills.sh/docs/faq), directory discovery uses aggregated CLI installation telemetry rather than a separate submission form. Public listing may lag publication and installation; do not interpret a successful install as a verified leaderboard listing.

## License

MIT for this package. The video tools the video skills install keep their own licences, listed above; in particular, onetake is free for noncommercial use only. Contributions should use synthetic fixtures and preserve the evidence, licence and human-action boundaries.
