# Voiceover: English that sounds like English

The voice settings in `assets/frame.md` (`voice:`) are mandatory. This file explains why and gives the exact steps.

## Why the voice came out "not English, not Hindi"

Checked on 31 October 2026 against HyperFrames at commit `a04b45a` and `kokoro-onnx` 0.6.1, the free local voice path HyperFrames uses (`npx hyperframes tts`):

1. **The voice ID picks the language.** HyperFrames infers the phonemizer language from the first letter of the Kokoro voice ID (`packages/cli/src/tts/manager.ts`): `a` American English, `b` British English, `h` **Hindi**, and so on. Choosing a Hindi voice (`hf_alpha`, `hf_beta`, `hm_omega`, `hm_psi`), for example to get an "Indian" sound, or passing `--lang hi`, sends English text through the Hindi phonemizer.
2. **The Hindi phonemizer garbles English.** Run through espeak-ng `hi`, numbers become Hindi words: "10x" → *dus ex*, "50%" → *pachaas pratishat*, "2026" → *do hazaar chhabbees*. English stretches get wrapped in `(en)…(hi)` language-switch markers, and kokoro-onnx keeps `(`, `)`, `e`, `n`, `h`, `i` as valid phoneme tokens, so stray sounds are spoken around English words. The result is the mixed, half-Hindi speech you heard.
3. **The same text in English mode is correct.** With `en-us`, espeak-ng gives "Hello" /həlˈoʊ/, "Claude" /klˈɔːd/ and "transition" /tɹænsˈɪʃən/.
4. **Short lines sound worse.** Kokoro's `VOICES.md` says voices are weak under about 10-20 tokens and rush over about 400. Synthesising one caption or one phrase at a time makes the voice unstable.
5. **Some voices are poor.** `am_adam`, which HyperFrames lists among its curated voices and uses in its help examples, is graded F+ in `VOICES.md`. `af_heart` is A, `af_bella` A-, `bf_emma` B-, and `am_michael`, `am_fenrir` and `am_puck` C+, the best male voices.

Cloud voices fail in a related way: multilingual models (HeyGen, ElevenLabs) guess the language from the text and the voice. An Indian-accented or Hindi-trained voice with code-mixed or ambiguous text can drift into Hindi. Pin the language to English in the request (HeyGen `language`, ElevenLabs `language_code` on models that support it; check the provider's current docs) and choose a voice whose listed language is English.

## Steps, every time

1. **Write the script in English only.** No Devanagari, no Hinglish words, no emoji, no URLs.
2. **Make the spoken version:**

   ```bash
   python3 <skill>/scripts/reelkit.py speak script.txt --voice af_heart -o vo.txt
   ```

   It applies `assets/lexicon.json` (brand and tool names, units, abbreviations), turns `$20` into "20 dollars", `%` into "percent", `&` into "and", strips emoji, and fails on Devanagari, URLs, a banned voice or a non-English language. It warns about unknown all-caps acronyms and lines too short for Kokoro. Captions use the original `script.txt`; only the voice reads `vo.txt`.
3. **Synthesise in chunks of 1-3 sentences** (about 100-300 characters), never per caption:

   ```bash
   npx hyperframes tts --text-file vo.txt --voice af_heart --lang en-us --speed 1.05 --output assets/vo.wav
   ```

   In the video kit, prefix the pinned form from `video-hyperframes`. Always pass `--lang en-us` (or `en-gb` with a `b*` voice) so a wrong voice cannot switch the phonemizer.
4. **Verify by listening with a machine, then a human:**

   ```bash
   npx hyperframes transcribe assets/vo.wav --model small.en --json
   python3 <skill>/scripts/reelkit.py verify script.txt assets/transcript.json
   ```

   `verify` aligns the transcript with the script and reports word error rate and every mismatch. Over 8% fails: fix the lexicon or the script and re-synthesise only the bad chunk. A misheard brand name can be the transcriber, not the voice, so listen to each flagged span before changing anything. Say in the delivery note that pronunciation was machine-checked.
5. **Add a word for good:** put it in `assets/lexicon.json` with a respelling that you checked, never a one-off edit to the script.

## Accent

Kokoro has no Indian-English voice: its Indian voices are Hindi. For an Indian-English accent, use a paid provider voice listed as English (India) with the language pinned to English, with the person's approval of the cost. Run `verify` on it like any other voice.

## Hinglish with ElevenLabs

When Om asks for Hindi-English, use ElevenLabs only, never Kokoro. For omaiverse, every narrated reel uses Om's own cloned voices, through the Zapier ElevenLabs connection: "om Hindi Voice" (`k2wSOFjoeAf2dogWLjMV`) for Hindi-English, and "Om Voice" (`OIuMZwCGrdCumuvntFIq`) for English. The model and settings are in `brands/omaiverse/frame.md`.

Tested 1 November 2026 with `eleven_multilingual_v2`, transcribed back with ElevenLabs Speech-to-Text:
- **Hindi clone, Hindi-English line:** every Hindi and English word came back correctly (driver, ETA, distance, AI, breakdowns, follow) in 10.4 s.
- **English clone, English line:** every word came back correctly, including "40 LPA" and "SDE".
- **Brand name:** written as "omaiverse" it was heard as "Omiverse" (Hindi clone) and "OMAVERSE" (English clone); respelled "Ohm AI verse" it was heard as "Om AI Verse". Always run `reelkit.py speak` so the lexicon respells it.

- Write Hindi words in Devanagari and English words in Latin script; keep tech words in English.
- `reelkit.py speak script.txt --lang hinglish --provider elevenlabs -o vo.txt` checks it. It refuses Hinglish with Kokoro and warns if there is no Devanagari.
- Transcribe with ElevenLabs Speech-to-Text (`scribe_v1`, word timestamps), then `reelkit.py verify`, which compares Devanagari and Latin words alike.
- Hindi takes about 58% longer to say than the same English sentence, so write to the target length rather than translating.
