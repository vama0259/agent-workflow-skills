---
name: video-brand-kit
description: The default brand for every video (currently @omaiverse, set in brands/default). Closed brand kit and edit grammar for vertical AI reels, Shorts and TikToks - fixed fonts, colours, safe zones, frame layouts, transitions, caption style, sound and English voiceover rules - plus a checker that fails off-kit fonts or colours and mispronounced voiceovers. Use for any 9:16 reel or short-form content video, and whenever edits look sparse or generic, transitions feel random, or the voiceover sounds non-English (Hindi voice or phonemizer, mangled brand names). Works with video-hyperframes as the design spec (frame.md) and with any other editor as a written spec.
---

# Reel brand kit

**Every reel and video uses the default brand** named in [`brands/default`](brands/default), currently `omaiverse`, unless the person names another brand or says to use none. Start every reel with `reelkit.py init`, which copies the kit into the project, so no reel is built without it.

This skill makes every reel look and sound like one brand. The kit is a **closed set**: only the fonts, colours, layouts, transitions, captions and voices in [`assets/frame.md`](assets/frame.md) are allowed. If a reel seems to need something else, ask the person to add it to the kit; never improvise a one-off.

Files:

- [`assets/frame.md`](assets/frame.md): the kit. HyperFrames reads a `frame.md` at the project root as its normative design spec.
- [`assets/lexicon.json`](assets/lexicon.json): how brand and tool names are spoken.
- [`references/edit-grammar.md`](references/edit-grammar.md): script and beat sheet, the 8 layouts, the 8 recipes (layout + motion + transition + sound), caption rules and the pre-render checklist.
- [`references/voiceover.md`](references/voiceover.md): why voices came out half-Hindi, and the exact voice steps.
- [`references/reel-rebuild.md`](references/reel-rebuild.md): rebuilding a reel Om shares ("make the same"): teardown, Hinglish script, ElevenLabs voice, word-synced build, the rating loop, cover and caption.
- [`references/research.md`](references/research.md): sources and what was measured versus chosen.
- [`scripts/reelkit.py`](scripts/reelkit.py): `lint`, `speak` and `verify` (Python 3, standard library only). `--brand <name>` uses `brands/<name>/`.
- [`brands/omaiverse/`](brands/omaiverse/frame.md): the filled kit for @omaiverse, with six series and their [playbooks](brands/omaiverse/series.md). `assets/frame.md` is the blank default for other brands.

## 1. Set up the kit once

1. The brand in `brands/default` is the person's brand: its `frame.md`, `lexicon.json` and `series.md` apply to every reel. `reelkit.py` uses it whenever `--brand` is left out; `--brand none` uses the blank kit in `assets/`.
2. For a different brand, use its folder in `brands/` if one exists. Otherwise ask in one message for brand name, handle, CTA and whether to keep the default palette, then create `brands/<name>/` from `assets/frame.md`, with a `lexicon.json` that has `"extends": "../../assets/lexicon.json"`. Offer to change at most the accent colours (`volt`, `signal`); keep everything else unless they ask. Changes to the kit are the person's decision, made once, not per reel.

## 2. Every reel

1. **Start the project with the kit.** Pick the series from the brand's `series.md` (ask only if the topic does not make it clear), then:

   ```bash
   python3 <skill>/scripts/reelkit.py init <project> --series claude-skills
   ```

   This copies the brand's `frame.md` into the project, where HyperFrames reads it as the design spec (`video-hyperframes`), and writes a `STORYBOARD.md` with the series chip, colour, voice and call to action filled in. With HyperFrames, run `npx hyperframes init` first (it refuses a folder that is not empty), then `reelkit.py init` on the same folder. Read that series' playbook. With any other editor, follow `frame.md` as a written spec.
2. **Script:** follow `references/edit-grammar.md` §1: one idea, 20-45 s, a 6-word-max hook. English by default; Hinglish when the person asks, through ElevenLabs only. When the person shares a reel to recreate, follow `references/reel-rebuild.md` from the start.
3. **Beat sheet:** write `STORYBOARD.md` with one row per beat: time, words, layout (L1-L8), recipe (R1-R8), transition out (T1-T9), SFX, filling in the table `init` wrote. Check it against §7 of the edit grammar before building anything. Show it to the person for approval.
4. **Voice** (`references/voiceover.md`):

   ```bash
   python3 <skill>/scripts/reelkit.py speak script.txt --voice af_heart -o vo.txt
   npx hyperframes tts --text-file vo.txt --voice af_heart --lang en-us --output assets/vo.wav
   npx hyperframes transcribe assets/vo.wav --model small.en --json
   python3 <skill>/scripts/reelkit.py verify script.txt assets/transcript.json
   ```

   For the brand's ElevenLabs voice or a Hinglish script, use `speak --provider elevenlabs [--lang hinglish]` and ElevenLabs Speech-to-Text for the transcript. Never use a Hindi Kokoro voice (`hf_*`, `hm_*`) or `--lang hi` for English. Synthesise 1-3 sentences per call, never one caption at a time. Fix failures through the lexicon, then re-run.
5. **Build** with the kit's layouts and recipes only. Captions come from the original script and the transcript timings.
6. **Lint, then preview:**

   ```bash
   python3 <skill>/scripts/reelkit.py lint <project>
   npx hyperframes lint && npx hyperframes check --snapshots
   ```

   `reelkit.py lint` fails on fonts and colours outside the kit, text under 32 px and a wrong canvas. Look at the snapshots at phone size for empty stages and text in the reserved strips (top 250, bottom 350, right 120 px).
7. **Draft render, review, final render** as `video-hyperframes` describes.

## 3. Report

At delivery, list: the recipes and transitions used (3-5 kinds), the voice ID and language, the `verify` word error rate and any spans the person should listen to, `reelkit.py lint` and HyperFrames check results, and anything the kit could not express that the person may want to add. Say that pronunciation and loudness were machine-checked, not heard.
