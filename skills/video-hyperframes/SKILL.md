---
name: video-hyperframes
description: Make, edit and render videos as HTML compositions with HeyGen's open-source HyperFrames (Apache-2.0) - product promos from a URL, PR explainers, faceless explainers, captions and overlays on existing footage, motion graphics, music-synced edits, decks, vertical or square formats, transparent overlays and batch renders. Use when video-workflow routes here or the user names HyperFrames. Installs the upstream plugin or skills, then gates telemetry, public feedback reports and paid HeyGen cloud or media usage behind the user's choice.
---

# HyperFrames video

[HyperFrames](https://github.com/heygen-com/hyperframes) turns HTML, CSS, media and seekable animations (GSAP, CSS, Lottie, Three.js and others) into deterministic video. It seeks each frame in headless Chrome and encodes with FFmpeg. Outputs: MP4, MOV (ProRes 4444 with alpha), WebM with alpha, GIF, PNG sequence. Presets cover 1920×1080, 1080×1920, 1080×1080 and 4K. Licence: Apache-2.0, no per-render fee. Analysed at commit `b7fa007` (plugin 0.8.181, pre-1.0, fast-moving).

This skill installs HyperFrames and adds guardrails. The upstream `hyperframes` router skill owns the creative workflow.

## When to use

Use it for: promos and site tours from a URL, GitHub PR or changelog videos, narrated explainers with invented visuals, captions or designed overlays on talking-head footage, short unnarrated motion graphics, beat-synced music videos, navigable decks, Remotion ports, and templated batches. It also assembles clips from the other `video-*` tools.

Don't use it for photoreal generated footage (it needs external media providers for that), NLE-style footage editing beyond the documented workflows, or screen recording.

## Setup

Requirements: Node.js 22+, FFmpeg and ffprobe, and the pinned Chrome build HyperFrames downloads.

```bash
# Claude Code plugin (recommended)
claude plugin marketplace add heygen-com/hyperframes
claude plugin install hyperframes@hyperframes

# Other agents: install the core skills only
npx skills add heygen-com/hyperframes     # choose the "Core Skills" group
```

Then check the machine. `doctor` always exits 0, so read `.ok`:

```bash
npx hyperframes doctor --json
npx hyperframes browser ensure            # if doctor reports no usable Chrome
```

Inside the Claude Code plugin, run the CLI through the plugin's pinned wrapper, as its own skill instructs (`node "<plugin root>/skills/hyperframes/scripts/plugin-cli.mjs" <command>`). Don't run `npx hyperframes skills --all` inside a HyperFrames source checkout.

## Guardrails to apply before the first render

Ask once, in the same round as the creative questions:

1. **Telemetry** is on by default: command names, render performance and a coarse system fingerprint, including the name of the coding agent. Offer `npx hyperframes telemetry disable`, or `HYPERFRAMES_NO_TELEMETRY=1` for this run.
2. **Feedback reports:** the upstream CLI skill sends a rating and "MISSING FEATURE" reports to a **public** channel after renders unless telemetry is disabled. Send them only if the user agrees. Never use `--file-issue` without explicit consent, because it publishes a reproduction.
3. **Usage reads:** `npx hyperframes usage --json` reads the existing Claude Code or Codex login to report remaining plan allowance. It is read-only; skip it if the user prefers.
4. **Paid paths:** local rendering is free. `npx hyperframes cloud render` and the `heygen` CLI for TTS, music, images and avatars use HeyGen credits beyond any free allowance. Name the cost and get approval before using them. Free local alternatives include Kokoro TTS.
5. **Desktop app prompts:** the upstream skill mentions the HyperFrames desktop app and its assistant at final review. Pass that on once, as information.

## Run

1. Load the upstream `hyperframes` router skill. It resumes project state, writes `BRIEF.md`, picks one workflow (`product-launch-video`, `faceless-explainer`, `pr-to-video`, `embedded-captions`, `talking-head-recut`, `motion-graphics`, `music-to-video`, `slideshow`, `remotion-to-hyperframes` or `general-video`) and installs it on demand.
2. Follow that workflow's interview, storyboard and review gates. The upstream rule is preview and approval before the delivery render.
3. Use the CLI loop the workflow names. Common commands:

   ```bash
   npx hyperframes init my-video --non-interactive [--resolution portrait]
   npx hyperframes lint
   npx hyperframes check --snapshots
   npx hyperframes preview --background          # Studio preview for review
   npx hyperframes render --quality draft --output renders/draft.mp4
   npx hyperframes render --quality delivery --output renders/final.mp4
   npx hyperframes render --format webm --output renders/overlay.webm   # alpha overlay
   ```

4. For renders longer than a few minutes, set `HYPERFRAMES_RENDER_DETACHED=1` so the render survives the agent process. Frames can use about 25 GB per minute at 1080p30 on some paths; check free disk first.
5. To assemble clips from other `video-*` tools, place their MP4s as media clips in a `general-video` composition and keep each clip's source credits.

## Deliver

Deliver the rendered file path (default `renders/`), the project folder (`index.html`, `compositions/`, `BRIEF.md`, `STORYBOARD.md`) and any credits for third-party registry blocks. Registry items can carry their own licences, for example GSAP's standard licence. Report paid usage incurred and what was left for the user to approve.
