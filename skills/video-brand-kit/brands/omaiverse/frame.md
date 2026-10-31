---
version: 1
name: omaiverse — Reel Brand Kit
description: >
  Closed brand kit for @omaiverse, an AI content creator on Instagram covering six series:
  AI Breakdown, Claude Skills, SDE & AI Jobs, MBA & Business, Lifestyle and Clubs.
  One look across all of them: ink ground that is never flat, heavy paper-white Montserrat
  caps, a volt accent that always marks the one important word, and one colour per series
  used only for that series' tag. Only the values in this file go on screen or into the voice.
unit: the frame, 1080×1920 at 30 fps
principle: one brand, six series · closed set · fill the frame · one idea per beat · the voice is the clock

brand:
  name: "omaiverse"
  handle: "@omaiverse"
  platform: instagram
  creator: "AI content creator"
  say-it: "Ohm AI verse"                # how the voice says the brand (see lexicon.json)
  cta: "Follow @omaiverse for more"     # default; each series has its own below
  language: en

wordmark:
  text: "omaiverse"
  build: "lowercase Montserrat 900, tracking -0.03em; the letters 'ai' are volt, the rest paper. On a light or volt ground: all ink, 'ai' on a volt highlight block."
  clear-space: "the height of the 'o' on every side"
  min-px: 48
  watermark: "optional: foot zone, right edge at x 960, 40 px, paper at 40% opacity; never during the hook or end card"
  never: ["outline or gradient on the wordmark", "a robot, brain or sparkle icon", "any other company's logo as part of the brand"]

canvas: { width: 1080, height: 1920, fps: 30 }

safe:
  left: 60
  right: 960
  top: 250
  bottom: 1570

zones:
  head:    { y: [250, 600],   use: "series bar and chip, hook, title" }
  stage:   { y: [600, 1180],  use: "the visual: screen card, footage, chart, number" }
  caption: { y: [1180, 1420], use: "spoken captions only" }
  foot:    { y: [1420, 1570], use: "source chip, watermark, small CTA" }

cover:                                   # the reel cover, so the profile grid reads as one brand
  size: [1080, 1920]
  title-band: { y: [480, 1440], note: "survives the 3:4 profile grid crop and a 1:1 crop; check in the app" }
  build: "series chip at top of the title band, 2-4 word title in hook type, one visual behind at 60% brightness, wordmark 56 px at the bottom of the band"
  rule: "every cover in a series uses the same chip, position and type; only the title and visual change"

colors:
  ink: "#0A0A0F"
  surface: "#16161D"
  line: "#2A2A35"
  paper: "#F4F4EF"
  mute: "#9A9AA6"
  volt: "#D4FF3A"       # THE accent, every series: active caption word, key number, wordmark 'ai'
  signal: "#7B61FF"     # AI / tool UI accents; also the AI Breakdown series colour
  alert: "#FF5A4E"      # wrong, before, don't. Never decorative
  stroke: "#000000"     # caption outline only
  # series colours: ONLY the series chip, the 6 px series bar and the cover chip
  clay: "#FF8A4C"       # Claude Skills
  cyan: "#3DD6FF"       # SDE & AI Jobs
  gold: "#FFC145"       # MBA & Business
  mint: "#6EE7B7"       # Lifestyle
  magenta: "#FF3DCB"    # Clubs

series:
  ai-breakdown:
    chip: "AI BREAKDOWN"
    color: signal
    chip-text: ink          # ink on signal 4.7:1; paper would be 3.8:1
    voice: narrated
    cta: "Follow @omaiverse for daily AI breakdowns"
  claude-skills:
    chip: "CLAUDE SKILLS"
    color: clay
    chip-text: ink
    voice: narrated
    cta: "Follow @omaiverse for a new Claude skill every week"
  sde-ai-jobs:
    chip: "SDE & AI JOBS"
    color: cyan
    chip-text: ink
    voice: narrated
    cta: "Follow @omaiverse to land your next tech role"
  mba-business:
    chip: "BUSINESS BREAKDOWN"
    color: gold
    chip-text: ink
    voice: narrated
    cta: "Follow @omaiverse for business, broken down"
  lifestyle:
    chip: "LIFESTYLE"
    color: mint
    chip-text: ink
    voice: own voice or music-led
    cta: "Follow @omaiverse for the life behind the screen"
  clubs:
    chip: "CLUBS"
    color: magenta
    chip-text: ink
    voice: music-led, minimal captions
    cta: "Follow @omaiverse for the nights out"

series-bar:
  build: "6 px bar at y 250, x 60 → 960, in the series colour; fills left to right with the reel's progress"

typography:
  # Montserrat, Inter and JetBrains Mono: bundled with HyperFrames, SIL Open Font Licence.
  hook:      { fontFamily: "Montserrat", px: 144, min: 112, weight: 900, lineHeight: 0.95, tracking: "-0.02em", upper: true, maxWords: 6, maxLines: 3 }
  title:     { fontFamily: "Montserrat", px: 96,  min: 80,  weight: 900, lineHeight: 1.0,  tracking: "-0.01em", upper: true, maxWords: 8 }
  stat:      { fontFamily: "Montserrat", px: 320, min: 220, weight: 900, lineHeight: 0.9,  tracking: "-0.04em" }
  caption:   { fontFamily: "Montserrat", px: 80,  min: 64,  max: 96, weight: 800, lineHeight: 1.05, upper: true, stroke: "8% of font size, {colors.stroke}" }
  wordmark:  { fontFamily: "Montserrat", px: 72,  min: 48, weight: 900, tracking: "-0.03em", upper: false }
  body:      { fontFamily: "Inter", px: 46, min: 40, weight: 600, lineHeight: 1.25 }
  label:     { fontFamily: "Inter", px: 32, weight: 700, tracking: "0.08em", upper: true }
  mono:      { fontFamily: "JetBrains Mono", px: 38, min: 32, weight: 500, lineHeight: 1.35 }
  floor:     { px: 32 }

spacing:
  gutter: 60px
  gap: 32px
  card-pad: 40px
  radius: 32px
  chip-radius: 999px

components:
  series-chip:
    description: "Pill, label type, series colour fill, chip-text colour, height 64 px, top-left of the head zone. Enters with the hook and stays for the whole reel."
  screen-card:
    description: "UI capture in a surface card, 900-960 px wide, radius 32, 2 px line border, soft signal glow. Never smaller than 840 px wide."
  chip:
    description: "Pill, label type: ink on volt for a key fact, ink on signal for a tool name."
  source-chip:
    description: "Foot zone, label type in mute: 'Source: <name>, <month year>'. Required on every salary, market or company number."
  caption-group:
    description: "2-3 words, centred in the caption zone, paper with stroke; spoken word turns volt and scales 1.08."
  grain:
    description: "Ground is ink plus 3% grain and a slow drifting radial glow of the series colour at 10%, or a 72 px line grid at 40%."
  footage-grade:
    description: "Real footage (Lifestyle, Clubs): blacks lifted to ink, highlights capped at paper, saturation -10%; Clubs push shadows toward magenta and signal, Lifestyle stays warm and natural. A 30-40% ink scrim behind any text."
  end-card:
    description: "Wordmark 96 px, the series CTA in body type, a volt underline drawn in 0.4 s; 1.5-2 s, last frame matches the hook ground so the reel loops."

motion:
  arrive: { ease: "expo.out", duration: 0.45 }
  exit:   { ease: "power3.in", duration: 0.25 }
  camera: { ease: "power2.inOut" }
  stagger: 0.06
  idle-push: "every shot pushes 1.00 → 1.04 across its length"
  hold-before-payoff: [0.3, 0.75]
  beat-cut: "music-led reels (Lifestyle, Clubs) cut on the beat and change layout on the bar"

transitions:
  T1-punch:   { duration: 0,    build: "hard cut to the same shot scaled 1.12 (or back to 1.0)", use: "emphasis on the stressed word" }
  T2-whip:    { duration: 0.2,  build: "outgoing x 0 → -1080, incoming 1080 → 0, 18 px horizontal blur at the fastest frame, power3.in / expo.out, whoosh", use: "next point" }
  T3-zoom:    { duration: 0.35, build: "an on-screen element scales 8% → 250% with power3.in; its fill becomes the next ground", use: "going deeper" }
  T4-grow:    { duration: 0.65, build: "a card grows past the frame, power2.inOut, radius 32 → 0; surroundings blur 15 px", use: "overview → detail" }
  T5-volt-wipe: { duration: 0.3, build: "a full-height volt bar sweeps left → right; max 2 per reel", use: "section change, list item" }
  T6-blur-swap: { duration: 0.28, build: "out: opacity 0 + 8 px blur in 0.15 s; in: blur 0 in 0.13 s; the ground never cuts", use: "before/after, prompt → result" }
  T7-dip:     { duration: 0.1,  build: "outgoing frame darkens 40% for 3 frames, then hard cut", use: "right before the payoff" }
  T8-glitch:  { duration: 0.2,  build: "6 frames of RGB split (signal / volt, ±12 px) and 2 slice offsets; max 1 per reel; AI series only", use: "the 'AI just did it' moment" }
  T9-flash:   { duration: 0.1,  build: "3 frames of paper-white flash at 70% on the beat drop; Clubs only, max 3 per reel", use: "beat drop between footage shots" }
  banned: ["crossfade between scenes", "spin", "cube", "page curl", "star or shape wipes", "zoom blur on every cut", "the same transition 3 times in a row", "power2.out 0.5 s on everything"]

sound:
  music-under-voice: 0.14
  loudness: "-14 LUFS integrated, true peak <= -1 dBTP"
  sfx: { whoosh: "T2, T3", pop: "chip or list item enters", riser: "max 1, into the payoff", click: "cursor clicks", typing: "prompt cards" }
  licensed-music: "for trending or club tracks, export with voice and ambient only and add the track in Instagram's editor, so it stays licensed"

voice:
  language: en
  provider-order: ["kokoro (local, free)", "heygen or elevenlabs, only with Om's approval of the cost", "Om's own recorded voice"]
  kokoro:
    default: af_heart
    alternates: [af_bella, bf_emma, am_michael, am_fenrir, am_puck]
    lang: en-us
    speed: [1.0, 1.1]
    banned: ["hf_alpha", "hf_beta", "hm_omega", "hm_psi", "any voice not starting a_ or b_", "am_adam (grade F+)", "--lang hi or any non-English --lang"]
  one-voice-rule: "pick one narrator voice for all narrated series and keep it; the voice is part of the brand"
  chunk: "1-3 sentences per TTS call (about 100-300 characters)"
  lexicon: lexicon.json
  verify: "transcribe the rendered voice and run reelkit.py verify --brand omaiverse; fail over 8% word error"
---

# omaiverse brand kit

The frontmatter is normative: quote hex values, families, weights, durations and voice IDs
exactly. Nothing outside it goes on screen or into the voice. If a reel needs something the
kit lacks, ask Om to add it here first.

Each series has a playbook in [`series.md`](series.md). Shared rules (layouts L1-L8, recipes
R1-R8, beat sheet, caption rules, checklist) are in the skill's
`references/edit-grammar.md`; this kit adds T9-flash for Clubs and the series system.

## The look in one line

Ink ground that is never flat, heavy paper-white caps, volt green on the one word that matters,
a coloured series tag so viewers know in a second which show they are watching, and the
`om·ai·verse` wordmark with the "ai" lit up.

## Series system

- The **volt accent never changes** between series; it is the brand.
- The **series colour** appears only in the series chip, the 6 px series bar and the cover chip.
  It is never used for body text, captions or backgrounds.
- Every reel opens with its series chip in the head zone and ends on the series CTA.
- Lifestyle and Clubs are footage-first: full-bleed real footage with `footage-grade`, fewer
  words, captions only where words are spoken. The four knowledge series are narrated and use
  screen cards, numbers and lists to fill the stage.

## Do

- Fill the frame: full-bleed ground or footage, and an occupied stage at least 840 px wide.
- Text readable in frame 1; the hook is already moving. No logo intro, no "hey guys".
- One idea per beat, one volt accent per frame, something changes every 2-4 s.
- Cite every salary, market size, funding or company number in a source chip with month and year.
- Show real product UI in screen cards (Claude, ChatGPT, job portals); keep the omaiverse
  wordmark as the only brand mark.

## Don't

- No fonts other than Montserrat, Inter and JetBrains Mono. No emoji as icons. No stock blue
  "tech" gradients. No other company's logo or colours as omaiverse branding.
- No text in the reserved strips: top 250 px, bottom 350 px, right 120 px.
- No crossfades and nothing from the banned transition list.
- No Hindi or Hinglish in an English voiceover script, and no Hindi Kokoro voice.
- In Clubs and Lifestyle, no identifiable stranger as the focus of a shot without their OK,
  and no copyrighted track burned into the export.
