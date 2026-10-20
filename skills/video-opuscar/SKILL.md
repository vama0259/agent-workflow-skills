---
name: video-opuscar
description: Direct a 30-60 s film rendered entirely in code in one of the 51 styles of the MIT Lemo-Opuscar library (watercolor, ukiyo-e, risograph, blueprint, pixel RPG, satellite briefing, teardown, lidar survey and more), with original score, TTS narration and subtitles, and no generative video or API keys. Use when video-workflow routes here or the user wants a styled promo, explainer or data, science or product story from real material, or asks which film styles exist. Not for editing existing footage.
---

# Lemo-Opuscar styled film

[Lemo-Opuscar](https://github.com/lemomo-ai/lemo-opuscar) is a library of 51 film styles for coding agents. Each style has a `STYLE.md` (look, colour, type, motion, camera grammar, sound palette, pitfalls) and a demo film. The agent directs the film and writes everything as code: canvas, WebGL or three.js pages rendered frame by frame through headless Chromium, a score from free sample libraries or synthesis, procedural sound effects, TTS narration checked by speech recognition, and a loudness-normalised mix. No video generation, no stock footage. Output: 1920×1080 at 24 fps by default (other sizes such as 1080×1920 on request), −14 LUFS, burned-in subtitles plus an `.srt`. Licence: MIT for code and docs, CC BY 4.0 for demo films; films users make are theirs. Analysed at commit `b5e8ef9` (package 0.1.0).

## When to use

Use it for: a film in a named art style; a styled promo, launch, explainer or title sequence; data, science or product stories from real material (satellite imagery, laser scans, CAD, archive scans) with the Evidence styles; making a style the user's own; answering "which styles are there?". Bilingual English and Chinese.

Don't use it for editing or converting existing video, photoreal or live-action looks, quick turnaround (a film takes an agent about 30-60 minutes and a fair amount of tokens), or chat-only surfaces without a shell. Upstream tunes the styles for Claude Opus 5.5 and warns other models may not reproduce them well.

Style families: Evidence (satellite-briefing, briefing-board, lidar-survey, white-model, data-physical, teardown, microscope, archive-lighttable), Hand-drawn, East Asian, Print, Graphic, Info and Keynote, Cartoon, Games, Cinema and 3D. Read `styles/README.md` in the library for the full list and use cases.

## Setup

Requirements: Node 20+, `ffmpeg`, Python 3.11+ (or `uv`) and `git`. Kokoro TTS needs Python 3.11-3.13. Developed on macOS (Apple silicon); Linux should work; Windows needs WSL. 3D and shader styles want a GPU.

```bash
# Claude Code plugin (recommended)
claude plugin marketplace add lemomo-ai/lemo-opuscar
claude plugin install lemo-opuscar@lemolab
```

On first use the plugin's `setup.sh` clones the library to `~/lemo-opuscar` (override with `LEMO_OPUSCAR_HOME`). On every later run it **hard-resets that clone to upstream `main`**. To pin a version instead, clone the repo yourself, check out the analysed commit and work inside it; the setup script uses a clone the user is standing in as it is:

```bash
git clone https://github.com/lemomo-ai/lemo-opuscar.git && cd lemo-opuscar
git checkout b5e8ef93930b6d828f352055a689320f138237b1
claude
```

Install tiers, which the agent runs and the user should hear about in the one round of questions:

- **Core:** about 350 MB (Playwright headless shell, three.js, numpy and audio packages).
- **Voice:** about 0.55 GB, plus a 354 MB Kokoro model and a ~145 MB Whisper model on first use.
- **Music:** instrument sample libraries of 70-400 MB each, about 1.4 GB for all.
- **Per-style extras:** for example a ~970 MB background-removal model for briefing-board.

No API keys or paid services are needed.

## Guardrails

- **Privacy:** Chinese narration can use `edge-tts`, which sends the narration text to Microsoft. Use offline Kokoro unless the user agrees.
- **System software:** report missing Node, ffmpeg or Python in the question round instead of installing system software yourself, as the library instructs.
- **Licences:** some per-style packages carry other licences (for example `occt-import-js` is LGPL-2.1 for teardown). Keep the film's `CREDITS` file with the delivery.
- **Copyright:** respect the library's copyright red lines in `DIRECTOR.md`. Use only material the user owns or that is licensed for reuse.

## Run

1. Load the upstream `lemo-opuscar` skill. It runs `setup.sh`, starts `setup.sh deps` early in the background, and hands you to the library's `AGENTS.md`.
2. Find the style (or help the user choose), then ask the one round of questions: topic, length, language, voice, music, their own photos, logos or data, and whether they want to see a storyboard.
3. Write `TREATMENT.md` with three candidate structures and your choice **before** opening the style's demo. Use the demo only to learn techniques, never its story.
4. Build in the project folder (`<name>/` where the user started, or `films/<name>/` in a clone), run tools from the library with absolute project paths, and use the checks the library provides: stills and contact sheets, reading-time check, ASR check of every narration line, and loudness in the mux step.
5. Render with the film's one-command `build.sh`.

## Deliver

Deliver `<name>.mp4`, `poster.jpg`, `<name>.srt`, `TREATMENT.md`, `CREDITS`, the source with `build.sh`, and `FACTS.md` for Evidence styles. Films are the user's own: no LemoLab credit or watermark.
