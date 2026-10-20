---
name: video-onetake
description: Make 10-30 s premium 16:9 product or app launch teasers, and narrated feature demos up to ~60 s with the UI rebuilt from screenshots, using the onetake skill - kinetic type, carried beats, real motion blur, synthesised sound and a verification oracle against slideshow cuts. NONCOMMERCIAL ONLY under PolyForm Noncommercial 1.0.0. Use when video-workflow routes here or the user names onetake, and only after confirming the video is not for commercial use or the user holds an onetake Pro licence.
---

# onetake motion film

[onetake](https://github.com/feitangyuan/onetake) is an agent skill for short product motion films. The agent writes one HTML composition where every value is a pure function of time (`window.__seek(t)`), uses a library of about 39 measured moves (`lib/motion.js`), renders frame by frame in headless Chromium with averaged shutter motion blur, and checks the cut with an oracle (`verify_promo.py`). Output is H.264 MP4: 1920×1080 at 30 fps for drafts and 3840×2160 at 60 fps for finals. All visuals are procedural; there is no generative AI. Analysed at commit `4157581`.

## Licence gate (do this first)

onetake is **PolyForm Noncommercial 1.0.0**. The README says "Commercial use is not permitted" and points to the paid onetake Pro licence. A promo for a company's product, an ad, client work or a monetised channel is very likely commercial. Ask before installing:

- **Noncommercial** (personal project, study, hobby, nonprofit, education, research): continue.
- **Commercial, with an onetake Pro licence:** continue, and note the licence in the delivery.
- **Commercial, no licence:** stop. Route to `video-hyperframes` (`product-launch-video`) or `video-opuscar` instead.

Any copy of onetake must keep its licence and Required Notice. Don't vendor its files into other repositories.

## When to use

Use it for: launch, teaser or intro clips for an app, page, skill or feature; narrated 30-60 s feature demos with the UI rebuilt in HTML from screenshots, optionally in several languages; matching the feel of a reference clip; diagnosing why a motion video "reads like a slideshow".

Don't use it for long-form, talking heads, editing existing footage, or vertical formats (the template is fixed at 1920×1080 and vertical is undocumented). If the user names HyperFrames or Remotion, use that.

## Setup

```bash
git clone https://github.com/feitangyuan/onetake.git ~/.claude/skills/onetake     # Claude Code
git clone https://github.com/feitangyuan/onetake.git ~/.agents/skills/onetake     # Codex and other agents
git -C ~/.claude/skills/onetake checkout 415758128aa45cc54340df40d8109363447f582e  # optional: pin the analysed version
```

Requirements, which the repo lists but does not pin: python3 with `playwright`, `numpy`, `scipy`, `Pillow`, `matplotlib`, `fonttools`, `brotli` and `opencv-python`; Chromium for Playwright (`python3 -m playwright install chromium`); `ffmpeg` and `ffprobe` with libx264; `node` for library tests. Report missing system tools to the user rather than installing system software unasked.

Narration also needs `faster-whisper` and a Kokoro venv at `~/.cache/kokoro/venv` with model files at `~/.cache/kokoro/kokoro-v1.0.onnx` and `voices-v1.0.bin`. The repo does not explain where to download those, so ask the user to provide them or drop narration.

## Run

Follow the upstream `SKILL.md` protocol in order. Its hard rules come from rejected cuts.

1. Optional reference: `python3 scripts/analyze_ref.py ref.mp4 --out ana/`.
2. Offer three one-sentence concepts plus a look (`paper`, `dusk`, `tabletop`, `ultramarine`, `riso`, `ember`) and let the user choose.
3. Write a beat sheet. Shot lengths must vary by at least 4×, and every boundary names what carries over.
4. Footage: record real pages with `scripts/record_footage.py`, or rebuild the UI from screenshots with `lib/ui_kit.js`.
5. Compose: copy `templates/comp.html` and `lib/motion.js` into the film folder, apply a look with `python3 scripts/look.py apply <look> <film>/comp.html`, and check with `python3 scripts/probe.py <film>/comp.html`.
6. Look before rendering: `python3 scripts/stills.py comp.html --times 0.7,2.4,3.8 --out stills.png`.
7. Render a draft with `python3 scripts/render.py comp.html --out draft.mp4 --sfx sfx.wav`. Estimate time first: about 0.2 s per capture per browser, so one 15 s cut took about 103 s on 8 workers. Tell the user the estimate before long renders.
8. Sound: `python3 scripts/sfx_palette.py`. The upstream `dump_events.py` and `score.py` are referenced but **not shipped**, so use the palette, or a user-supplied score. Music must be royalty-free unless the user supplies and licenses it.
9. Verify: `python3 scripts/verify_promo.py draft.mp4 --comp comp.html`. Narrated cuts fail its audio check by design; say so rather than hiding it.
10. Only after the user accepts the draft, render the final with `--final` (4K60, much slower).

## Deliver

Deliver `draft.mp4` or `film.mp4` with its `.render.json`, the film folder (`comp.html`, `motion.js`, `look.js`), the sound file, and licence notes for any music or recorded sound effects. State that the film was made with onetake under its noncommercial licence, or under the user's Pro licence.
