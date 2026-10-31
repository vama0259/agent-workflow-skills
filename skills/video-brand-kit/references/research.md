# Research notes

What the kit is based on, checked on 31 October 2026. "Measured" means it was run or read in source here; "upstream rule" means a rule written in HyperFrames' own skills; "house default" means a choice made for this kit that you should tune against your own analytics.

## Voiceover (measured)

- **HyperFrames picks the phonemizer from the voice ID.** `packages/cli/src/tts/manager.ts` maps the first letter of a Kokoro voice to a language (`a` en-us, `b` en-gb, `h` hi, …) and `af_heart` is the default voice. Read at commits `b7fa007` (the video kit's pin) and `a04b45a` (main on 31 October 2026).
- **Hindi phonemization of English, run with kokoro-onnx 0.6.1 and its bundled espeak-ng:** "10x" → `dˈʌs ˈɛks`, "50%" → `pəcˈaːs pətˈɪʃət`, "2026" → `dˈoː hˈʌɟaːɾ cʰəbbˈis`, and English words wrapped in `(en)…(hi)`. The tokenizer keeps `(` `)` and the letters as vocabulary tokens, so they reach the model.
- **English phonemization of the same words is correct**: "Hello" `həlˈoʊ`, "Claude" `klˈɔːd`, "transition" `tɹænsˈɪʃən`.
- **Lexicon entries** in `assets/lexicon.json` were each phonemized in en-us. Fixed by respelling: SaaS (was "saa es"), Veo (was "vee-oh"), Udio, Hailuo, DALL-E, UX (was "ux"), SEO, ROI, 9:16 (was read with a colon), 1080p, vs., e.g. Left as written because en-us is already right: AI, GPT, ChatGPT, LLM, API, Gemini, Midjourney, Kling, Perplexity and the others in `keep_as_written`. "A I" with a space is worse than "AI" (`ɐ ˈaɪ`). This was phonemes only: no audio was rendered or listened to.
- **Voice quality grades** from [Kokoro-82M VOICES.md](https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md): `af_heart` A, `af_bella` A-, `bf_emma` B-, `am_michael` / `am_fenrir` / `am_puck` C+, `am_adam` F+. Hindi voices `hf_alpha`, `hf_beta`, `hm_omega`, `hm_psi` (C) use espeak-ng `hi`. The same file says voices are weak under about 10-20 tokens and rush over about 400, which is why the kit chunks 1-3 sentences.
- **Kokoro's own pronunciation syntax** `[word](/phonemes/)` belongs to the [misaki](https://pypi.org/project/misaki/) front end. HyperFrames uses kokoro-onnx with espeak-ng instead, so the kit respells words in text, which works for every engine.
- **Cloud voices:** multilingual voices drifting into Hindi or Hinglish is a reported problem ([Vapi community thread](https://vapi.ai/community/m/1437389028428353546)); pinning the request language is the general fix. Exact parameter names vary by provider and model, so check current docs.

## Layout and safe zones (third-party, approximate)

There is no official Meta specification in the sources found. Guides agree on a 1080×1920 canvas and disagree on margins: top 108-269 px, bottom 280-450 px, right 60-120 px ([Hopper HQ](https://www.hopperhq.com/blog/instagram-reel-size/), [Socialync](https://www.socialync.io/tools/safe-zones/instagram-reels), [TryMyPost](https://www.trymypost.com/blog/instagram-reels-safe-zones-text-placement-2026)). The kit takes a conservative common reading, top 250, bottom 350, right 120, which leaves a 900×1320 information area. HyperFrames' caption rule places portrait captions about 600-700 px from the bottom (upstream rule, `embedded-captions/references/rail.md` at `b7fa007`). Check your own uploads in the app preview.

## Type (upstream rule + vendor guides)

- Montserrat, Inter and JetBrains Mono are bundled by HyperFrames (`references/format.md` at `a04b45a`) and are SIL Open Font Licence on Google Fonts, so they need no licence fee. If an older HyperFrames lint flags `font_family_without_font_face`, add an `@font-face` to the Google Fonts `.woff2` in `assets/fonts/`.
- Bold sans caption faces (Montserrat, Anton) and a 2-4 px or ~8-9% stroke are the common recommendation for reels; vendor guides quote caption heights of 6-9% of frame height ([Blitzcut](https://blitzcutai.com/blog/best-caption-fonts-reels-2026), [BurnSub preset](https://burnsub.pages.dev/styles/hormozi-bold-white)). Claimed watch-time lifts from word-by-word highlighting come from vendors and are unverified.

## Motion and transitions (upstream rules)

From HyperFrames `skills/hyperframes/references/motion.md` and `captions.md` at `a04b45a`: fast moves 0.3-0.6 s with motion blur at the fastest frame; arrivals on long ease-outs (`expo.out`), exits accelerate (`power3.in`); 3-5 transition kinds per film, each caused by something on screen; at most a third of seams hard cuts; no crossfades between worlds; whip 0.13-0.3 s, zoom-through 0.35 s, grow 0.65 s, dip 3 frames, blur swap 0.13-0.2 s; caption groups 2-3 words for high energy. The volt wipe, glitch, idle push and the caps per reel are house defaults.

## Hooks and pacing (practitioner consensus, not benchmarks)

Sources agree on text in the first frame, no slow intro or logo sting, pattern interrupts every few seconds and a loop at the end ([CapCut hooks guide](https://www.capcut.com/create/short-form-video-hooks), [skills.sh short-form-video](https://skills.sh/iart-ai/tiktok-video-skills/short-form-video), [dev.to hook engineering](https://dev.to/bulkdl/hook-engineering-the-science-of-the-first-3-seconds-in-short-form-video-2026-2jp9)). Specific retention percentages in those posts are uncited. The beat timings in `edit-grammar.md` are house defaults.

## Not done

No reel was rendered, no voice audio was synthesised or listened to, and no retention test was run. `reelkit.py` was tested on synthetic projects, scripts and transcripts.
