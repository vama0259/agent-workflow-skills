# Video tools analysis

This note compares the five open-source video projects the `video-*` skills wrap. It records what each project is, what it needs, where it fits and what to watch for. The [`video-workflow`](../SKILL.md) router turns it into routing rules.

Scope: each repository was shallow-cloned and read on 20 October 2026, without running its code. Claims come from each project's README, skill files, licence and source at the commit listed. These projects change quickly, so re-check before relying on a detail.

| Project | Commit analysed | Licence | Wrapper skill |
| --- | --- | --- | --- |
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | `b7fa007` (2026-10-20), plugin 0.8.181 | Apache-2.0 | [`video-hyperframes`](../../video-hyperframes/SKILL.md) |
| [feitangyuan/onetake](https://github.com/feitangyuan/onetake) | `4157581` (2026-10-12) | PolyForm Noncommercial 1.0.0 | [`video-onetake`](../../video-onetake/SKILL.md) |
| [MegaTroll222/VOX-COLLAGE-BROLL](https://github.com/MegaTroll222/VOX-COLLAGE-BROLL) | `2e9b8a9` (2026-07-17) | MIT | [`video-collage-broll`](../../video-collage-broll/SKILL.md) |
| [JohnHeibel/ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) | `0ac8bf2` (2026-09-24) | MIT | [`video-clawd-animation`](../../video-clawd-animation/SKILL.md) |
| [lemomo-ai/lemo-opuscar](https://github.com/lemomo-ai/lemo-opuscar) | `b5e8ef9` (2026-10-19), package 0.1.0 | MIT (code), CC BY 4.0 (demo films) | [`video-opuscar`](../../video-opuscar/SKILL.md) |

## At a glance

| | HyperFrames | onetake | Collage B-roll | Clawd animation | Lemo-Opuscar |
| --- | --- | --- | --- | --- | --- |
| Makes | Any HTML-composed video: promos, explainers, captions, overlays, decks | 10-30 s launch teasers; demos up to ~60 s | One 5 s collage metaphor clip | Hand-painted character cartoon | 30-60 s film in one of 51 styles |
| Engine | HTML + GSAP and other adapters, headless Chrome, FFmpeg | One HTML composition, move library, headless Chromium with motion blur | MaxFusion image, video and speech generation, ffmpeg | p5.js + p5.brush on WEBGL, puppeteer, ffmpeg | Canvas, WebGL or three.js pages, Playwright, Python audio, ffmpeg |
| Format | 16:9, 9:16, 1:1, 4K; MP4, MOV/WebM with alpha, GIF | 16:9 only; 1080p30 draft, 4K60 final | 9:16, 720p | 16:9, 1080p, 24 fps | 1080p24 default; other sizes on request |
| Generative AI | Optional (HeyGen media, local models) | None | All of it | None | None |
| Audio | Placed audio, TTS via HeyGen or Kokoro | Synthesised effects; Kokoro narration | Optional MaxFusion voice | Muxed user track | Original score, effects, Kokoro or edge-tts narration |
| Text on screen | Yes | Yes (kinetic type) | Forbidden | Forbidden by default | Yes, with subtitles |
| Paid services | Only cloud render and HeyGen media | None | MaxFusion, required | None | None |
| GPU | Helpful, optional | Not stated | No | Strongly recommended | For 3D and shader styles |
| Agent packaging | Claude Code plugin, 21 skills, router | Single skill (git clone) | Single prompt-only skill | None (guide only) | Claude Code plugin, 1 skill + library |
| Maturity | Large, active, pre-1.0, fast churn | Solo, "lite" library, case sources withheld | 1 commit, no code | Small v1.0.0, no tests | Early 0.1.0, single author |

## HyperFrames

**What it is.** HeyGen's framework for writing video as HTML. A composition marks clips with timing attributes; animation runs on a paused, seekable timeline. The renderer seeks each frame in headless Chrome and encodes with FFmpeg, so output is deterministic and suits CI and batch jobs.

**Strengths.** It covers the most kinds of deliverable, through a router skill and specialised workflows (product launch from a URL, faceless explainer, PR to video, embedded captions, talking-head recut, motion graphics, music to video, slideshow, Remotion port, general video). It is the only one of the five that works with existing footage, renders transparent overlays and offers vertical, square and 4K presets, batch rendering and Lambda or Cloud Run scaling. It also has a catalogue of about 400 registry blocks, website capture, and lint and browser-check gates.

**Weaknesses.** It is heavy (Chrome, FFmpeg, up to ~25 GB of frames per minute at 1080p30 on some paths) and pre-1.0 with very fast releases. Generated footage needs external providers.

**Watch for.** Anonymous telemetry is on by default and records the coding agent's name. The upstream skills send post-render feedback to a public channel unless telemetry is off. `usage --json` reads the local Claude Code or Codex login. Cloud rendering and HeyGen media cost credits. The upstream router presents itself as the mandatory entry point for any video request, so with several video tools installed, route explicitly with `video-workflow`.

## onetake

**What it is.** A skill for short product motion films built from the product itself: one HTML composition where everything is a function of time, about 39 measured moves (enter, carry, contact, camera, fluid), UI recorded from real pages or rebuilt from screenshots, shutter motion blur, synthesised sound, and a verification oracle that rejects slideshow-like cuts.

**Strengths.** It is the most opinionated about motion craft. It enforces rhythm (shot lengths varying by at least 4×) and "carry" between beats, renders real motion blur up to 4K60, needs no API keys, and supports narrated, multilingual versions of the same film.

**Weaknesses.** It is 16:9 only and needs a multi-round protocol (concepts, drafts, verification). Some referenced scripts (`dump_events.py`, `score.py`) are not shipped, the narration models must be placed by hand, and dependencies are unpinned.

**Watch for.** **PolyForm Noncommercial.** The README states commercial use is not permitted without the paid Pro licence. Because its purpose is product promos, most company use is likely commercial. This is the most important routing constraint across the five tools.

## Collage B-roll (VOX-COLLAGE-BROLL)

**What it is.** A prompt-only skill, ported from pyang5166's Chinese original, that turns one spoken line into a 9:16, 5 s paper-collage clip assembling itself from an empty colour field. Three approval gates: metaphor, still, motion.

**Strengths.** It has a distinctive editorial look and a strict style system with colour meanings. The gates stop money being spent on rejected ideas, and it includes a QA and repair playbook. It makes good inserts for explainers and social video.

**Weaknesses.** It is locked to one paid MCP (MaxFusion) and one video model with no fallback, 720p only. It offers no layer control, no editable timeline and no text. It has a single commit, no code and no tests.

**Watch for.** Every generation costs money and prices aren't stated, so approve spend first. Rights to outputs follow the generation providers' terms. The upstream install fetches from `main`; the wrapper pins a commit.

## Clawd animation (ClaudeAnimationBase)

**What it is.** A starter kit for hand-painted cartoons starring Clawd, the Claude Code mascot. It includes a character rig with five views and 31 emotions, p5.brush painting helpers, a scrubbing studio page and a headless renderer with contact-sheet, strip and crop modes for self-review.

**Strengths.** It has a unique watercolour-and-ink look with boiling linework, deterministic, parallel and resumable rendering, and a model-facing guide that encodes animation principles and a storyboard-first workflow.

**Weaknesses.** It is fixed at 1920×1080, has no text or dialogue by design, and has no GIF encoder. Without a GPU it renders at seconds per frame. It uses global-scope scripts and has no tests or `SKILL.md`.

**Watch for.** Chrome is started with `--no-sandbox` on Linux. Crop expressions are evaluated in the page. The studio page fetches a web font, so offline renders may stall. It needs Node 22.12+.

## Lemo-Opuscar

**What it is.** A library of 51 film styles (Evidence, Hand-drawn, East Asian, Print, Graphic, Info and Keynote, Cartoon, Games, Cinema, 3D). The agent directs and codes the whole film: picture, original score from free sample libraries, procedural effects, narration checked by speech recognition, subtitles and a −14 LUFS master.

**Strengths.** It has the widest stylistic range and a strong directing doctrine (treatment first, cue maps, readability checks). Evidence styles build data, science and product stories from real material. Everything is fully editable code with no generation costs, and it is bilingual English and Chinese. Users can make a style their own.

**Weaknesses.** It is slow (30-60 minutes of agent time per film) and token-heavy. Optional downloads run from 0.35 GB to over 2 GB. It is tuned for one model family and developed on macOS.

**Watch for.** The plugin hard-resets its library clone to upstream `main` on each run, so pin by working in your own clone. `edge-tts` sends narration text to Microsoft. Some per-style packages carry other licences.

## Recommendations

1. **Default to HyperFrames** for general, commercial, footage-based, vertical or batch work. Install it alongside the others even if another tool makes the hero film, because it is the assembly layer.
2. **Use Lemo-Opuscar** when the look is the point, or when real data or material should carry the story. Allow for the time.
3. **Use onetake** only for noncommercial launch teasers where motion craft matters most, or when the user holds a Pro licence.
4. **Use Collage B-roll** for a few high-value metaphor inserts, with spend approved, then assemble them in HyperFrames.
5. **Use Clawd animation** for character shorts and mascot moments; add any text in HyperFrames.
6. Pin versions for anything repeatable, keep upstream credits files with deliveries, and route through `video-workflow` when several of these skills are installed. Their own descriptions overlap: HyperFrames calls its router the mandatory entry point for any video request, and onetake claims launch clips unless the user names another framework.
