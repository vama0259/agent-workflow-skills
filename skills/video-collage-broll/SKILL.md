---
name: video-collage-broll
description: Turn one ~5 s voiceover line or abstract idea into a 9:16 editorial halftone paper-collage B-roll clip, optionally voiced, using the MIT collage-broll-explainers skill (VOX-COLLAGE-BROLL) on the paid MaxFusion MCP. Use when video-workflow routes here or the user asks for collage B-roll, paper-collage or halftone-collage visuals or a script line as a visual metaphor. Confirms the paid spend first and keeps the upstream three-gate approval flow.
---

# Collage B-roll clip

[VOX-COLLAGE-BROLL](https://github.com/MegaTroll222/VOX-COLLAGE-BROLL) ships one prompt-only skill, `collage-broll-explainers`. It is an English port of pyang5166's `gbro-collage-broll`. It turns a single line into one visual metaphor of 3-6 objects: black-and-white halftone photo cut-outs and coloured cardstock on a flat colour field, assembling itself from an empty frame in stop-motion. Output: 9:16, 5 s, 720p MP4, silent by default, with an optional fitted voiceover. Licence: MIT. Analysed at commit `2e9b8a9`. The repo has no code or tests; all imagery is AI-generated through MaxFusion.

## Spend and access gate (do this first)

Every image, video and voice call goes through the **MaxFusion MCP** (`https://mcp.maxfusion.ai/mcp`), a paid service. The repo states no prices. Before anything else:

1. Tell the user it needs a MaxFusion account and that each still, video and voiceover uses paid generation. Get explicit approval.
2. Check whether the MaxFusion tools are already connected in this session. If not, the user connects it: in Claude Code, `claude mcp add --transport http maxfusion https://mcp.maxfusion.ai/mcp`, then authenticate on first use; in claude.ai, add it as a custom connector. Don't continue until it is connected.
3. Without MaxFusion, the upstream README describes a bring-your-own-keys route (a Google AI Studio key for images and the video model, an ElevenLabs key for voice), but you would have to write those scripts. Offer it as a project, not a quick fallback.

The video model is locked upstream to `gemini-omni-flash` with no fallback. Rights to generated outputs follow MaxFusion's and the model providers' terms, which the repo does not cover.

## When to use

Use it for short abstract lines in explainers, opinion pieces or vertical social videos, alone or as a batch sharing one look. Typical request: *make a collage B-roll for: "Nobody misses washing dishes by hand."*

Don't use it when the user needs exact layer or occlusion control, camera moves, an editable timeline, separate transparent layers, a real person or presenter, or only a prompt. For assembled explainers, make the clips here and assemble them in `video-hyperframes`.

## Setup

**In the video kit** (`VIDEO_KIT` is set, or `<kit>/bin/claude-video` sits three folders above this skill), `collage-broll-explainers` is already installed at the analysed commit; skip the download. The spend gate still applies.

Otherwise, install the upstream skill pinned to the analysed commit, rather than the moving `main` branch the README uses:

```bash
mkdir -p ~/.claude/skills/collage-broll-explainers
curl -fsSL -o ~/.claude/skills/collage-broll-explainers/SKILL.md \
  https://raw.githubusercontent.com/MegaTroll222/VOX-COLLAGE-BROLL/2e9b8a93a2834e4d670700ab9e4827a8baf3b668/SKILL.md
```

Local requirements: `ffmpeg` and `ffprobe`, plus file access for frame preparation, QA and voiceover fitting. A sandbox without local downloads can still run the three gates, but frame prep falls back to prompt-only colour matching and self-QA and voiceover fitting are skipped. Tell the user if that applies.

## Run

Load `collage-broll-explainers` and keep its three gates. Each gate is a stop for user approval, and the stops are what keep rejected ideas from costing money.

1. **Gate 1, metaphor only:** propose the meaning, emotion, proposition, objects, colour and assembly order. Generate nothing.
2. **Gate 2, still:** write `visual-spec.json`, generate one 9:16 still, run still QA and a contact sheet, then stop for approval.
3. **Gate 3, motion:** build the last frame from the approved still and a solid-colour first frame with ffmpeg, upload both, generate the 5 s clip, strip audio, and run the QA and repair playbook (first-frame purity, end-frame match, no invented lettering).
4. **Optional voice:** list the user's MaxFusion voices, generate the line, trim silence, fit it into 4-5 s, and mux without re-encoding the video.

Projects go to `~/collage-broll-projects/YYYY-MM-DD-<title>/` unless the user chooses another folder.

## Deliver

Deliver `final-5s-noaudio.mp4` or `final-5s-voiced.mp4`, the contact sheets and QA notes, a one-sentence explanation of each metaphor, and the MaxFusion job and asset IDs. Report how many paid generations ran, including retries.
