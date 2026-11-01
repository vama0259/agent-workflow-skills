# Rebuilding a reference reel

How to turn a reel Om likes into an omaiverse reel: same structure and pacing, original Hinglish or English script, omaiverse look. This follows the `explainer-reel-rebuild` pipeline that Om's local session proved on the Uber driver-matching reel (1 November 2026), with the brand kit added. That session's render engine lives on Om's Mac; this file is the playbook, so any session that has a shell and network access can follow it.

## Guardrails (override everything below)

- Never name or hint at Om's employer, its internal systems or clients.
- Never claim Om built projects he didn't; share learning and opinions, sparingly.
- Never publish without Om's explicit yes for that post.
- Ask before any OpenArt spend (for example lip-sync at about 20 credits a second). The default pipeline spends nothing.
- Copy the reference's structure, pacing and transition types, never its script, graphics or footage. Delete the downloaded reference when the teardown is written.

## 0. Can this session reach what it needs?

Rebuilding needs `www.instagram.com` (download), ElevenLabs (voice and speech-to-text) and a local renderer. A network-restricted cloud session fails at step 1. Check once with `yt-dlp`; if it is blocked, say so and give Om the one action that fixes it: run the job on his Mac, connect a Mac folder through Remote Control, or attach the MP4 (an iPhone screen recording works). Don't try workarounds through other tools.

## 1. Read the reference

```bash
yt-dlp -o 'ref.%(ext)s' --no-playlist '<url>'       # one attempt; on a login wall or 429, ask Om for the file
```

- **Cuts:** ffmpeg scene detection (`select='gt(scene,0.08)'`, then drop cuts within 0.25 s of each other).
- **Look:** frames at `fps=1/3` tiled into grids. Actually view them.
- **Words:** ElevenLabs Speech-to-Text (`scribe_v1`, word timestamps). Instagram reels carry no captions.
- **Teardown spec**, written to `TEARDOWN.md`: each shot with time range, scene type, on-screen text, transition out; the UI system (cards, maps, pins, captions); the beat map; the palette. Then map every element to the kit: scene types to layouts L1-L8, transitions to T1-T9, their captions to the kit's caption style, their colours to the series colour and volt.

## 2. Script and voice (the voice drives the edit)

- Pick the series from `brands/omaiverse/series.md` (most explainers are AI Breakdown, SDE & AI Jobs or MBA & Business) and run `reelkit.py init <dir> --series <key>`.
- **Write to the target length, never translate.** Hindi runs about 58% longer than English for the same sentence (6.3 s became 10 s). Keep tech words in English (driver, route, ETA, model, prompt): shorter, and how Indian creators speak.
- **Mixed script for the voice:** Devanagari for Hindi words, Latin for English words.
- **Voice of record:** ElevenLabs "Ayush — Creator" (`00KdCZfPLQodWob7wL6g`), model `eleven_v3`, stability 0.45, similarity 0.75, style 0, speed 1.08. It is in `brands/omaiverse/frame.md`.
- Check and prepare the text: `reelkit.py speak script.txt --lang hinglish --provider elevenlabs -o vo.txt`.
- **Pronunciation check:** run the voice back through ElevenLabs Speech-to-Text, then `reelkit.py verify script.txt transcript.json`. Every English term must survive.

## 3. Build

Build in HyperFrames with the project's `frame.md` from `init`, or in the local engine on Om's Mac. Either way:

1. **Variety like the reference.** Alternate scene types (for example map, street, phone UI, top-down, big number); never two shots of the same type in a row. One reused backdrop reads as boring.
2. **Every visual beat lands on the word that names it.** Key events to word timestamps, never to shot-relative timers.
3. **Om's persona** is a real, non-talking clip of him, in the bottom-left corner (the right side sits under Instagram's buttons), on screen 2-4 s, then slides out. No cycling stills, no looped talking mouth. True lip-sync costs OpenArt credits: quote and ask first.
4. **Hook:** a question headline from frame 1 that works muted, plus motion in the first second, with the series chip.
5. **Close:** a takeaway line people would save, then the end card with the series CTA, held about 2 s over silent padding.
6. **Safe area:** information inside x 60-960, clear of the top 250 and bottom 350 px (the kit's zones).
7. Hindi text on screen goes through the browser (HyperFrames or Chrome sprites); Pillow cannot shape Devanagari.
8. Render 4-8 test frames and look at them before any full render.
9. No generated music: Om adds a native Instagram track.

## 4. Rate it honestly, then loop

Score 1-10 as a muted thumb-scroller, from frames of the encoded file: Hook (first 1.5 s), Polish, Clarity, Sync, Save/share, Variety against the reference. Say plainly whether you would scroll past. Fix the weakest score and repeat until all are 8 or higher. The Uber reel went from 3/5/6/7/5 to all 8s in five versions.

## 5. Cover and caption

- **Cover:** the kit's cover template (series chip, 2-4 word title with one volt word, wordmark), a clean scene frame and Om cut out, all inside y 480-1440 for the profile grid.
- **Caption:** hook line, takeaway, `Comment [KEYWORD] 👇 full guide DM mein 📩`, then 6-8 hashtags. A comment-for-guide CTA needs a real guide and an auto-DM tool behind it: flag that to Om every time.

## 6. Deliver

Two versions of the reel (with and without burned-in captions), the cover and the caption `.txt`. On Om's Mac, copy them to `~/Desktop/reel content/<YYYY-MM-DD>/`; in a cloud session, put them where Om can open them and send them. Report the scores, the voice ID, the `verify` result and anything left for Om.
