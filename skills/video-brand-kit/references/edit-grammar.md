# Edit grammar for reels

How to turn a script into a reel that uses the whole frame and keeps moving. Values come from `assets/frame.md`; this file says how to combine them. Where a number is an upstream rule (HyperFrames' `skills/hyperframes/references/motion.md` and `captions.md` at commit `a04b45a`) it says so; the rest are house defaults to tune against your own retention graphs.

## 1. Script first

- **One idea per reel.** One promise in the hook, paid off by the end.
- **Length:** 20-45 s, about 55-110 spoken words at 2.5-2.8 words a second.
- **Every beat is concrete:** a tool name, a step, a number, a before/after or a result on screen. Cut any sentence that only says "this is amazing".
- **Write for the ear:** short sentences, no brackets, no URLs, no emoji, no Hindi words in an English script. Numbers as you would say them ("twenty dollars a month"); `reelkit.py speak` catches the common slips.
- **Hook patterns** (pick one, 6 words max on screen): result first ("This AI edited my reel in 9 seconds"), mistake ("Stop prompting ChatGPT like this"), number ("3 free AI tools that replace Canva"), contrast ("$0 vs $200 a month, same result"), secret ("Nobody uses this Claude feature").
- **CTA:** one line, last 1.5-2 s, then loop to frame 1. "Save this for later" or `brand.cta`.

## 2. Beat sheet

| Time | Beat | Job | Default recipe |
| --- | --- | --- | --- |
| 0-1.5 s | Hook | Stop the scroll: text and motion in frame 1 | R1 Hook slam |
| 1.5-5 s | Stakes | Why this matters to the viewer | R2 Stat punch or R5 Before/after |
| 5 s-end-4 s | Value, 3-6 beats of 3-6 s | One step or point per beat | R3 Tool demo, R4 List beat, R6 Prompt → result |
| last 2-4 s | Payoff | The result, shown | R7 Reveal |
| last 1.5-2 s | CTA | Follow / save, loops to hook | R8 End card |

Change something every 2-4 s inside a beat (zoom, chip, punch, b-roll). Write the beat sheet into `STORYBOARD.md` with, per beat: time range, spoken words, layout, recipe, transition out, SFX.

## 3. Layouts (the only frame layouts)

Every layout keeps the ground full-bleed and the stage filled. Zones are in `frame.md` (`head` 250-600, `stage` 600-1180, `caption` 1180-1420, `foot` 1420-1570).

| ID | Layout | Head | Stage | Caption | When |
| --- | --- | --- | --- | --- | --- |
| L1 | Full-bleed picture | optional title | b-roll or generated clip covers the whole canvas, 30-40% ink scrim behind text | yes | hook, mood, b-roll lines |
| L2 | Title over stage | hook or title, 2-3 lines | visual 900-960 px wide | yes | most value beats |
| L3 | Screen card | label chip with tool name | `screen-card` 900-960 px, cursor and zoom-ins on the action | yes | tool demos |
| L4 | Big number | label ("costs", "saves") | `stat` number, volt, 220-320 px | yes | stakes, results |
| L5 | List stack | title | up to 3 rows, each a chip + body line, staggered 0.06 s; the current row is paper, others mute | yes | "3 tools", steps |
| L6 | Split before/after | "BEFORE" / "AFTER" labels | two stacked halves 900×280 each, alert vs volt edge | yes | comparisons |
| L7 | Talking head + overlay | chip | person full-bleed; one card or number pops in at side, never over the face | yes | creator on camera |
| L8 | Prompt card | label "PROMPT" | `mono` text in a surface card, typed on at 30-40 characters/s, volt caret | caption off while the card is read | prompts, code |

Never use a layout that leaves the stage empty. If a line has no visual, use L4 (pull a number from it), L5 (list it) or L1 b-roll.

## 4. Recipes (combinations)

Each recipe is a fixed combination of layout, motion, transition and sound. Use these instead of inventing new ones.

| ID | Recipe | Build | Transition out | SFX |
| --- | --- | --- | --- | --- |
| R1 | Hook slam | L1 or L2. Hook words arrive one by one with `arrive` ease, scale 1.15 → 1, stagger 0.06; the key word is volt. Picture already moving at frame 0. | T2 whip or T3 zoom | whoosh on the cut |
| R2 | Stat punch | L4. Number counts up over 0.6 s on `expo.out`, lands with a T1 punch to 1.12 on the spoken number. | T5 volt wipe | pop on land |
| R3 | Tool demo | L3. Card arrives from 1.1 scale; camera pushes to the button being clicked (0.6 s, `camera` ease); chip with tool name in head. | T3 zoom through the clicked element, or T4 grow | click, whoosh |
| R4 | List beat | L5. Rows enter on the word that names them; the active row is paper, past rows go mute. | T5 volt wipe between items, max 2, then T2 | pop per row |
| R5 | Before/after | L6. "Before" half in, hold 0.4 s, "after" half in on the word "now"/"after". | T6 blur swap | none or soft pop |
| R6 | Prompt → result | L8 types the prompt, then the card becomes the result. | T6 blur swap from prompt to result, T8 glitch allowed once | keyboard ticks, then hit |
| R7 | Reveal | T7 dip, hold 0.3-0.75 s, result fills the stage at normal speed. | T1 punch into the result | riser into it, max 1 per reel |
| R8 | End card | `end-card` component; volt underline draws in 0.4 s; last frame matches the hook's ground so the loop is seamless. | loops to frame 1 | none |

## 5. Transitions

Use only `transitions` from `frame.md`, 3-5 kinds per reel, each caused by something on screen. From HyperFrames' measured rules: hard cuts belong inside a scene; at most a third of the seams between beats are hard cuts; worlds never crossfade; a fast move is 0.3-0.6 s and carries motion blur at its fastest frame; arrivals land on long ease-outs, exits accelerate. Cut on the beat of the music when there is music, and mirror the ease across a seam (`power3.in` out, `power3.out` or `expo.out` in).

Quick map from what the voice is doing to the seam:

| The voice... | Seam |
| --- | --- |
| stresses a word inside a sentence | T1 punch |
| moves to the next point | T2 whip |
| goes deeper into the thing on screen | T3 zoom or T4 grow |
| starts a new section or list item | T5 volt wipe (max 2) |
| compares or swaps content | T6 blur swap |
| is about to reveal the result | T7 dip |
| says the AI just did it | T8 glitch (max 1) |

## 6. Captions

From HyperFrames' caption rules, fixed to this kit: groups of 2-3 words (reel energy), one group visible at a time, starting 0.1-0.3 s in, each group ending with a hard kill. Size with `fitTextFontSize` at `maxWidth` 900, base 80, minimum 64. Centre in the caption zone (about 500-740 px from the bottom, inside the upstream 600-700 px portrait guidance). Never over a face. The spoken word turns volt and scales 1.08; at most one emphasis word per group.

## 7. Space and pacing checklist (before the draft render)

- [ ] Every frame: ground covers the full canvas, stage occupied by something ≥ 840 px wide.
- [ ] No text in the reserved strips (top 250, bottom 350, right 120). Check with `npx hyperframes check --snapshots` and look at the snapshots at phone size.
- [ ] Text readable in frame 1; no logo or greeting before the hook.
- [ ] Something changes every 2-4 s; no shot held over 4 s without motion inside it.
- [ ] 3-5 transition kinds, none banned, no kind 3 times in a row, ≤ 1/3 of seams hard cuts.
- [ ] One volt accent per frame; red only for "wrong/before".
- [ ] Captions match the voice word for word (after `reelkit.py verify`).
- [ ] `python3 scripts/reelkit.py lint <project>` passes: no off-kit fonts or colours.
