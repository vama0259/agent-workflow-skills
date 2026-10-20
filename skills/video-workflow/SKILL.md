---
name: video-workflow
description: Route an AI video request to the right open-source production tool - HyperFrames, onetake, collage B-roll, Clawd animation or Lemo-Opuscar - and chain them when one tool is not enough. Use first whenever the user asks for a video, promo, explainer, launch clip, B-roll, cartoon, motion graphic, captions or a styled short film and has not already named the tool. Checks deliverable, format, commercial use, budget and machine before choosing, then hands off to the matching video-* skill.
---

# Video workflow router

Use this playbook to pick a tool, not to make the video. Each tool has its own skill in this package (`video-hyperframes`, `video-onetake`, `video-collage-broll`, `video-clawd-animation`, `video-opuscar`). They wrap independent upstream projects that change quickly and carry different licences. Read [the tool analysis](references/tool-analysis.md) when you need the evidence behind a routing rule.

If the user names a tool, use it. Still apply the gates below and say plainly if the request breaks one.

## 1. Capture the brief in one round

Ask only what the request leaves open, in a single message:

- **Deliverable:** new film, B-roll clip, edit of existing footage, captions or overlays, deck, or batch of templated renders.
- **Format:** aspect ratio (16:9, 9:16, 1:1), length, with or without narration, music and on-screen text.
- **Use:** personal, educational or nonprofit, or **commercial** (a company's product, ads, client work, monetised channel).
- **Budget:** whether paid generation services are acceptable.
- **Machine:** local shell with Node, Python, ffmpeg and Chrome; GPU or not.
- **Material:** URL, screenshots, footage, script, data, brand files, voice or music.

All five tools need a local shell with a real filesystem. A chat-only surface can plan the film and write prompts, but cannot render.

## 2. Gates, before choosing

| Gate | Rule |
| --- | --- |
| Commercial use | onetake is PolyForm Noncommercial. Do not route commercial work to it unless the user says they hold an onetake Pro licence. |
| Paid generation | The collage B-roll skill runs every image, video and voice through the MaxFusion MCP, a paid service. Get explicit approval of the spend first. |
| Existing footage | Only HyperFrames handles existing footage (captions, overlays, custom edits). The others make new films. |
| Photoreal or live-action | None of these tools shoots or generates photoreal footage, except the collage B-roll skill's AI-generated collage stills. Say so and offer a stylised alternative. |
| No GPU | Clawd animation watercolour fills and Lemo-Opuscar 3D or shader styles are slow without a GPU. Warn about render time before starting. |
| Text on screen | The Clawd animation guide forbids captions and lettering by design. If the user needs words on screen, plan a HyperFrames pass on top. |

## 3. Choose by deliverable

Use the first row that matches the deliverable, not a word mentioned in passing.

| The user wants | Use | Why |
| --- | --- | --- |
| Captions, lower-thirds or designed overlays on existing footage | `video-hyperframes` | Only tool with footage workflows |
| A slide deck, a GitHub PR explainer, a website or product promo from a URL | `video-hyperframes` | Dedicated upstream workflows |
| Vertical or square formats, transparent overlays, 4K, or batch renders from data | `video-hyperframes` | Presets, alpha output, `--batch` |
| One ~5 s editorial paper-collage visual metaphor for a voiceover line | `video-collage-broll` | Purpose-built, 9:16, 720p |
| A hand-painted character cartoon (Clawd or a new character), no dialogue | `video-clawd-animation` | Character rig and brush engine |
| A 10-30 s premium 16:9 launch teaser or a UI-rebuilt feature demo, **noncommercial** | `video-onetake` | Motion library, real motion blur, slideshow oracle |
| A 30-60 s film in a named art style, or a data, science or product explainer from real material | `video-opuscar` | 51 code-rendered styles with score and narration |
| Anything else custom, or longer than about 3 minutes | `video-hyperframes` (`/general-video`) | General composition fallback |

When two rows fit, prefer the tool with no paid service, then the permissive licence, then the shorter setup.

## 4. Chain tools when one is not enough

Hand off with files, not shared state: each tool writes an MP4 the next can place as a clip.

- **Explainer with metaphor B-roll:** script to `video-collage-broll` for the two or three most abstract lines, then `video-hyperframes` to assemble narration, captions, music and the clips.
- **Character short with titles:** `video-clawd-animation` for the textless cartoon, then `video-hyperframes` for title, captions and end card.
- **Launch package:** a hero film from `video-opuscar` (any use) or `video-onetake` (noncommercial), then `video-hyperframes` for 9:16 and 1:1 cut-downs and overlays.
- **Data story:** `video-opuscar` Evidence styles when the data is the picture; `video-hyperframes` when the data supports a narrated product or PR story.

Keep one project folder per film. Record which tool made each clip and under which licence, and keep upstream credits files with the delivery.

## 5. Hand off and report

Load the chosen skill and follow it. At delivery, tell the user the tool used, the output paths, remaining manual steps (approvals, licences for music or assets, any paid usage incurred) and what each tool could not do. Never claim a render succeeded without checking the output file exists and plays to the expected length.
