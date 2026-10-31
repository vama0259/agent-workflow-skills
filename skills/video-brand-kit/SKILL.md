---
name: video-brand-kit
description: Closed brand kit and edit grammar for vertical AI reels, Shorts and TikToks - fixed fonts, colours, safe zones, frame layouts, transitions, caption style, sound and English voiceover rules - plus a checker that fails off-kit fonts or colours and mispronounced voiceovers. Use for any 9:16 reel or short-form content video, and whenever edits look sparse or generic, transitions feel random, or the voiceover sounds non-English (Hindi voice or phonemizer, mangled brand names). Works with video-hyperframes as the design spec (frame.md) and with any other editor as a written spec.
---

# Reel brand kit

This skill makes every reel look and sound like one brand. The kit is a **closed set**: only the fonts, colours, layouts, transitions, captions and voices in [`assets/frame.md`](assets/frame.md) are allowed. If a reel seems to need something else, ask the person to add it to the kit; never improvise a one-off.

Files:

- [`assets/frame.md`](assets/frame.md): the kit. HyperFrames reads a `frame.md` at the project root as its normative design spec.
- [`assets/lexicon.json`](assets/lexicon.json): how brand and tool names are spoken.
- [`references/edit-grammar.md`](references/edit-grammar.md): script and beat sheet, the 8 layouts, the 8 recipes (layout + motion + transition + sound), caption rules and the pre-render checklist.
- [`references/voiceover.md`](references/voiceover.md): why voices came out half-Hindi, and the exact voice steps.
- [`references/research.md`](references/research.md): sources and what was measured versus chosen.
- [`scripts/reelkit.py`](scripts/reelkit.py): `lint`, `speak` and `verify` (Python 3, standard library only).

## 1. Set up the kit once

1. If the person has not filled in `brand:` (name, handle, CTA) in their copy of the kit, ask in one message for those three values and whether to keep the default palette. Offer to change at most the accent colours (`volt`, `signal`); keep everything else unless they ask.
2. Keep their filled kit somewhere stable (their brand folder or this skill's `assets/`). Changes to the kit are the person's decision, made once, not per reel.

## 2. Every reel

1. **Copy the kit into the project:** `assets/frame.md` → `<project>/frame.md`, so HyperFrames uses it (`video-hyperframes`). With any other editor, follow it as a written spec.
2. **Script:** follow `references/edit-grammar.md` §1. English only, one idea, 20-45 s, a 6-word-max hook.
3. **Beat sheet:** write `STORYBOARD.md` with one row per beat: time, words, layout (L1-L8), recipe (R1-R8), transition out (T1-T8), SFX. Check it against §7 of the edit grammar before building anything. Show it to the person for approval.
4. **Voice** (`references/voiceover.md`):

   ```bash
   python3 <skill>/scripts/reelkit.py speak script.txt --voice af_heart -o vo.txt
   npx hyperframes tts --text-file vo.txt --voice af_heart --lang en-us --output assets/vo.wav
   npx hyperframes transcribe assets/vo.wav --model small.en --json
   python3 <skill>/scripts/reelkit.py verify script.txt assets/transcript.json
   ```

   Never use a Hindi Kokoro voice (`hf_*`, `hm_*`) or `--lang hi` for English. Synthesise 1-3 sentences per call, never one caption at a time. Fix failures through the lexicon, then re-run.
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
