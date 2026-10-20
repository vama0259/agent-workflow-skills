---
name: video-clawd-animation
description: Author and render a short hand-painted 2D character cartoon - Clawd, the Claude Code mascot, or a new character - with the MIT ClaudeAnimationBase starter kit (p5.js + p5.brush in headless Chrome, 1920x1080 H.264). Use when video-workflow routes here or the user wants a painted, textless character animation, mascot short, music-synced loop or GIF frames. Sets up the kit, follows its ANIMATION_GUIDE.md, and self-reviews with contact sheets before the final render.
---

# Clawd character animation

[ClaudeAnimationBase](https://github.com/JohnHeibel/ClaudeAnimationBase) is a starter kit, not a library. It provides the Clawd character (5 drawn views, 31 emotions, dances, hats and emotes), painting and timing helpers on p5.js 2.3 and p5.brush 2.2, a scrubbing studio page and a headless renderer. Every frame is a pure function of time, painted on a flat 2D WEBGL canvas with paper texture and boiling ink lines. Output: 1920×1080 H.264 MP4 at 24 fps by default (`--fps` overrides). Licence: MIT. Analysed at commit `0ac8bf2`. It ships no `SKILL.md`; its `ANIMATION_GUIDE.md` is written for the model and is the source of truth.

## When to use

Use it for 10-30 s character-driven cartoons, mascot or brand shorts, music-synced loops and GIF frame sequences in a hand-painted look.

Don't use it for text-heavy explainers, captions, UI demos, data visualisation, 3D, photoreal output, dialogue or lip-sync, long-form, or vertical video: the canvas is hard-coded to 1920×1080. For titles or captions, render the cartoon here and add text in `video-hyperframes`.

## Setup

Requirements: Node.js 22.12 or newer (required by the locked `puppeteer-core` 25.11), Google Chrome or Chromium, and `ffmpeg` on `PATH`. puppeteer-core downloads no browser.

```bash
git clone https://github.com/JohnHeibel/ClaudeAnimationBase.git my-animation
cd my-animation
git checkout 0ac8bf2b31942376cb6b8c4074715595d512acd2   # optional: pin the analysed version
npm install
```

**In the video kit** (`VIDEO_KIT` is set, or `<kit>/bin/claude-video` sits three folders above this skill), copy the pinned kit for each film instead of cloning, then install as above:

```bash
cp -R "<kit>/tools/ClaudeAnimationBase" my-animation && rm -rf my-animation/.git
cd my-animation && npm install
```

Run every command from the project root, because paths are relative to it. If Chrome is not in a standard location, pass `--chrome=<path>` or set `CHROME_PATH`; the renderer also finds Playwright's Chromium.

Pick render flags for the machine:

- **Dedicated GPU:** defaults.
- **No GPU:** add `--soft-gl` (software WebGL). Watercolour fills then take seconds per frame, so warn the user and offer to replace fills with cheaper strokes.
- **Headless Linux with an NVIDIA GPU:** add `--gpu-angle=gl-egl` or `--gpu-angle=vulkan`. `node gpu_probe.mjs <chrome path>` shows which renderer each flag set gets.

On Linux the renderer always starts Chrome with `--no-sandbox`. The studio page loads a Google Fonts stylesheet and the renderer waits for the network to go idle, so fully offline runs may stall or lose the font.

## Run

1. Read `ANIMATION_GUIDE.md` in full before drawing anything. The user decides what the film is about; the guide decides how it is made. Where they conflict, the user's request wins.
2. Write `STORYBOARD.md`: logline, world, motif, arc, then shots with time ranges, transitions and what each shot should read as. Show it to the user if they want to approve the storyboard first.
3. Set `duration` and `bpm` in `src/config.js`.
4. Create `src/scenes/<name>.js` ending in `shots([...])`, and swap the `demo.js` script tag in `studio.html` for it. Don't copy the demo's story.
5. Follow the guide's hard rules: paint only through `paint()` and `inkLine()`, flat 2D, no text unless the user insists, something happens in every shot, a transition at every seam, every frame a pure function of `t` (use `hash()` and `boilSeed()`, never `Math.random`).
6. Review your own work before rendering the whole film:

   ```bash
   node render.mjs --sheet=0.1,0.8,1.6 --cols=6 --w=320 --out=out/check/sheet.jpg
   node render.mjs --strip=2.1:2.6 --cols=6 --w=320 --out=out/check/strip.jpg
   node render.mjs --sheet=2.3,2.4 --crop=760,420,500,400 --w=500 --out=out/check/face.jpg
   ```

   Look at the images, fix timing and readability, and repeat.
7. Render the film:

   ```bash
   node render.mjs --clip --out=out/video.mp4                                  # one worker
   node render.mjs --frames --workers=4 && node render.mjs --encode --out=out/video.mp4   # parallel, resumable
   ```

   Add `--audio=assets/song.mp3` to mux music, using only audio the user supplied or licensed.

## Deliver

Deliver `out/video.mp4`, `STORYBOARD.md` and the scene source. For a GIF, render a PNG loop with `--loop=<name> --png` and encode it with ffmpeg, because the kit has no GIF encoder. Keep the MIT notice if you redistribute the kit's code.
