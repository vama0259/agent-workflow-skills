---
version: 1
name: Reel Brand Kit (9:16 AI content)
description: >
  Closed design system for vertical AI reels and shorts. Dark "ink" ground, one volt accent,
  Montserrat for everything loud, Inter for support, JetBrains Mono for prompts and code.
  Every frame uses the full 1080×1920 canvas for picture and keeps information inside the
  safe area. Only the fonts, colours, layouts, transitions and voices listed here are allowed.
unit: the frame, 1080×1920 at 30 fps (1080×1080 and 1920×1080 cut-downs documented in the prose)
principle: closed set · fill the frame · one idea per beat · the voice is the clock

brand:
  name: "YOUR BRAND"          # replace once; used on the end card
  handle: "@yourhandle"       # end card and optional footer watermark
  cta: "Follow for daily AI workflows"
  language: en                # every reel is English unless the person says otherwise

canvas: { width: 1080, height: 1920, fps: 30 }

safe:                         # information stays inside; picture fills the whole canvas
  left: 60
  right: 960                  # 120 px reserved for the like / comment / share column
  top: 250                    # account name, audio label, top bar
  bottom: 1570                # 350 px reserved for caption, audio and comment row

zones:                        # y ranges inside the safe area
  head:    { y: [250, 600],   use: "hook, title, section label" }
  stage:   { y: [600, 1180],  use: "the visual: screen card, b-roll, diagram, number" }
  caption: { y: [1180, 1420], use: "spoken captions only" }
  foot:    { y: [1420, 1570], use: "source chip, handle watermark, small CTA" }

colors:
  ink: "#0A0A0F"        # ground
  surface: "#16161D"    # cards, screen frames
  line: "#2A2A35"       # hairlines, grid, card borders
  paper: "#F4F4EF"      # primary text
  mute: "#9A9AA6"       # secondary text, captions not yet spoken
  volt: "#D4FF3A"       # THE accent: active caption word, key number, CTA. Max ~10% of a frame
  signal: "#7B61FF"     # AI / tool accent: chips, cursor glow, UI highlights
  alert: "#FF5A4E"      # wrong, before, don't. Never decorative
  stroke: "#000000"     # caption outline and text shadow only

typography:
  # Montserrat, Inter and JetBrains Mono are bundled with HyperFrames (no @font-face needed
  # for the bundled weights) and are SIL Open Font Licence, free for commercial use.
  hook:      { fontFamily: "Montserrat", px: 144, min: 112, weight: 900, lineHeight: 0.95, tracking: "-0.02em", upper: true, maxWords: 6, maxLines: 3 }
  title:     { fontFamily: "Montserrat", px: 96,  min: 80,  weight: 900, lineHeight: 1.0,  tracking: "-0.01em", upper: true, maxWords: 8 }
  stat:      { fontFamily: "Montserrat", px: 320, min: 220, weight: 900, lineHeight: 0.9,  tracking: "-0.04em", note: "one number fills the stage" }
  caption:   { fontFamily: "Montserrat", px: 80,  min: 64,  max: 96, weight: 800, lineHeight: 1.05, upper: true, stroke: "8% of font size, {colors.stroke}" }
  body:      { fontFamily: "Inter", px: 46, min: 40, weight: 600, lineHeight: 1.25 }
  label:     { fontFamily: "Inter", px: 32, weight: 700, tracking: "0.08em", upper: true }
  mono:      { fontFamily: "JetBrains Mono", px: 38, min: 32, weight: 500, lineHeight: 1.35, note: "prompts, code, model names in chips" }
  floor:     { px: 32, note: "nothing on screen is smaller than 32 px" }

spacing:
  gutter: 60px          # = safe.left
  gap: 32px
  card-pad: 40px
  radius: 32px          # cards and screen frames
  chip-radius: 999px

components:
  screen-card:
    description: "UI capture or screen recording in a surface card: width 900-960 px, radius 32, 2 px line border, 0 0 120px signal at 25% glow. Fills the stage; never smaller than 840 px wide."
  chip:
    description: "Pill, label type, ink text on volt (key fact) or on signal (tool name). Height 64 px."
  caption-group:
    description: "2-3 words, centred in the caption zone, paper with stroke; the spoken word turns volt and scales 1.08; emphasis words (numbers, tool names, 'free', 'never') scale 1.15."
  grain:
    description: "Ground is never flat: ink plus a 3% film grain and a slow 40 s drifting radial glow of signal at 12%, or a 72 px line grid at 40% opacity."
  end-card:
    description: "Handle in title type, brand.cta in body type, a volt underline that draws in 0.4 s. 1.5-2 s, then the reel loops to frame 1."

motion:
  arrive: { ease: "expo.out", duration: 0.45 }
  exit:   { ease: "power3.in", duration: 0.25 }
  camera: { ease: "power2.inOut" }
  stagger: 0.06          # per word or list item
  idle-push: "every shot pushes 1.00 → 1.04 across its length; nothing is ever fully still"
  hold-before-payoff: [0.3, 0.75]

transitions:              # the only seams allowed between beats. Use 3-5 kinds per reel.
  T1-punch:   { duration: 0,    build: "hard cut to the same shot scaled 1.12 (or back to 1.0)", use: "emphasis inside a beat, on the stressed word" }
  T2-whip:    { duration: 0.2,  build: "outgoing x 0 → -1080, incoming 1080 → 0, 18 px horizontal blur at the fastest frame, power3.in / expo.out, whoosh SFX", use: "next point, change of topic" }
  T3-zoom:    { duration: 0.35, build: "an on-screen element scales 8% → 250% with power3.in; its fill becomes the next ground", use: "going deeper: tool → feature, step → detail" }
  T4-grow:    { duration: 0.65, build: "a card grows past the frame, power2.inOut, radius 32 → 0; surroundings blur 15 px and fade in 0.3 s", use: "demo → close-up, overview → item" }
  T5-volt-wipe: { duration: 0.3, build: "a full-height volt bar sweeps left → right and reveals the next beat; max 2 per reel", use: "section change, list item 1 → 2 → 3" }
  T6-blur-swap: { duration: 0.28, build: "out: opacity 0 + 8 px blur in 0.15 s; in: blur 0 in 0.13 s; the ground never cuts", use: "swap content on the same stage: before/after, prompt → result" }
  T7-dip:     { duration: 0.1,  build: "outgoing frame darkens 40% for 3 frames, then hard cut", use: "right before the payoff or reveal" }
  T8-glitch:  { duration: 0.2,  build: "6 frames of RGB split (signal / volt channels, ±12 px) and 2 slice offsets; max 1 per reel", use: "the 'AI just did it' moment only" }
  banned: ["crossfade between scenes", "spin", "cube", "page curl", "star or shape wipes", "zoom blur on every cut", "the same transition 3 times in a row", "power2.out 0.5 s on everything"]

sound:
  music-under-voice: 0.14   # volume
  loudness: "-14 LUFS integrated, true peak <= -1 dBTP"
  sfx: { whoosh: "T2, T3", pop: "chip or list item enters", riser: "max 1, into the payoff", click: "cursor clicks in screen demos" }

voice:
  language: en
  provider-order: ["kokoro (local, free)", "heygen or elevenlabs, only with the person's approval of the cost"]
  kokoro:
    default: af_heart        # American English female, grade A in Kokoro VOICES.md
    alternates: [af_bella, bf_emma, am_michael, am_fenrir, am_puck]
    lang: en-us              # en-gb with a b* voice
    speed: [1.0, 1.1]
    banned: ["hf_alpha", "hf_beta", "hm_omega", "hm_psi", "any voice not starting a_ or b_", "am_adam (grade F+)", "--lang hi or any non-English --lang"]
  chunk: "1-3 sentences per TTS call (about 100-300 characters); never one short phrase per call, never over 400"
  lexicon: lexicon.json
  verify: "transcribe the rendered voice and run reelkit.py verify; fail over 8% word error"
---

# Reel Brand Kit

This file is the brand. The frontmatter is normative: quote hex values, families, weights,
durations and voice IDs exactly. Nothing outside it goes on screen or into the voice. If a
reel seems to need something the kit does not have, ask the person to add it to the kit
first; do not improvise one-off fonts, colours or transitions.

## The look in one line

Black-ink ground that is never flat, paper-white heavy caps, one volt-green accent that
always means "this is the important word", violet for anything that is AI or a tool, red
only for mistakes. Picture fills the whole 1080×1920 canvas; words live inside the safe area.

## Do

- Fill the frame. The ground (ink + grain or grid) covers the whole canvas, and the stage zone
  is always occupied by something at least 840 px wide: a screen card, a number, a diagram,
  b-roll. Empty stage for more than 0.5 s is a bug, except the deliberate hold before a payoff.
- Put readable text in the first frame. The hook sits in the head zone at frame 0, already
  in motion. No logo sting, no greeting, no "hey guys".
- One idea per beat, one accent per frame. Volt marks at most one word or number at a time.
- Change something every 2-4 s: layout, zoom, a T1 punch, a chip, b-roll. Use the layouts in
  `references/edit-grammar.md`.
- Let the voice time the picture: text lands on the word that says it.

## Don't

- No fonts other than Montserrat, Inter and JetBrains Mono. No emoji as icons. No stock
  "tech" blue gradients. No drop shadows except the caption stroke.
- No text in the reserved strips: top 250 px, bottom 350 px, right 120 px.
- No crossfades between scenes and nothing from the banned transition list.
- No Hindi or Hinglish in an English voiceover script, and no Hindi Kokoro voice for English.

## Cut-downs

- 1:1 (1080×1080): head zone y 60-300, stage y 300-860, captions y 860-1020; same type scale × 0.85.
- 16:9 (1920×1080): captions 100 px from the bottom, stage is the full frame, type scale × 0.75.
