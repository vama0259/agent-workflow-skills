# Validation scope

Publication validation checks skill metadata, relative reference links, synthetic JSON, public-content sanitization, CLI discovery and an isolated project-scoped install. Installation checks packaging, not account integration or behavioral effectiveness.

The [synthetic scenarios](../skills/career-supervisor/references/synthetic-demos.md) cover history hydration, uncertain sends, model-limit recovery, promise/draft distinctions, missing capabilities and expired-role eligibility. They specify reviewable expected behavior and can be run without live accounts. They are not fabricated test transcripts or measured benchmarks.

Known limits: the playbook depends on the host following instructions, authorized tools returning useful evidence and the user supplying truthful configuration. Checkpoints cannot retroactively establish an unobserved external action. Account/provider usage is unavailable unless actual metering exposes it. Cross-agent live integrations have not been certified.

## Publication checks — 9 October 2026

- Bundled skill metadata validator: passed.
- Eleven repository-relative Markdown references and the synthetic JSON fixture: resolved and parsed successfully.
- Sanitization scan and content review: public files contain synthetic examples and no copied live messages, account IDs, resume links, local source paths or private employer facts.
- Official skills CLI: discovered one skill and completed a project-scoped copy install with Codex, Claude Code and Cursor selected. Its summary showed the shared `.agents/skills` copy and `.claude/skills` copy. This verifies packaging, not live host behavior.
- `skills find career-supervisor`: initially returned no listing. A subsequent browser check verified the live [skills.sh detail page](https://skills.sh/vama0259/agent-workflow-skills/career-supervisor), including the skill content and install command. Search indexing and install counts may update separately.

No automated behavioral benchmark was run for this release. The scenario fixtures and initial baseline review are documented without claiming measured improvement.

## Video skills checks — 20 October 2026

Scope: the six `video-*` skills are routing and setup instructions around five upstream projects. Checks cover packaging and the accuracy of what the skills say about those projects, not rendered output.

- Upstream review: each project was shallow-cloned at the commit listed in the [tool analysis](../skills/video-workflow/references/tool-analysis.md) and read without running its code. Install commands, flags, paths, licences, paid services and version requirements quoted in the skills were checked against the upstream README, skill files, licence and source at those commits.
- Metadata: all seven `SKILL.md` files parse as YAML, names match folders and descriptions are under 1,024 characters. The first CLI run skipped `video-onetake` because a colon in its description broke YAML parsing; the description was fixed and the check now uses a YAML parser.
- Links: 27 repository-relative Markdown links resolve. The tool analysis lives inside the router skill so its links survive installation.
- Official skills CLI: `skills add <repo> --list` discovered seven skills, and a project-scoped install with `--skill '*' -a claude-code` copied all seven into `.claude/skills`. This verifies packaging only.

- Video kit installer: `scripts/install-video-kit.sh` was run into a scratch folder on Linux.
  - It fetched all five upstream projects at the pinned commits in about 7 seconds.
  - It produced 30 skills in `<kit>/.claude/skills` (6 wrappers, 21 HyperFrames, onetake, collage B-roll, Lemo-Opuscar), the Clawd and Lemo-Opuscar tools, the licence files, the launcher and a README, about 100 MB in all. No onetake demo films were included.
  - A second run changed nothing.
  - Lemo-Opuscar's own `setup.sh`, given the kit's library path, used the pinned clone as it was. It neither cloned nor reset to `main`.
  - Not tested: macOS, and a real `claude --add-dir` session loading the kit. That loading behaviour comes from the Claude Code skills and permissions docs.

Not done: no video was rendered with any of the five tools, no paid service was called, and no upstream skill was run end to end. Upstream projects change quickly; re-check the pinned commits before relying on a detail.

## Reel brand kit checks — 31 October 2026

Scope: `video-brand-kit` is a design spec, a lexicon and a standard-library checker. Checks cover the claims it makes and the checker, not rendered reels.

- Upstream claims: HyperFrames was read at `b7fa007` (the video kit's pin) and `a04b45a` (main on 31 October 2026) for voice-to-language mapping, the default voice, `tts` flags, bundled fonts, `frame.md` handling, caption placement and transition rules. Kokoro voice grades come from its `VOICES.md`.
- Phonemizer: kokoro-onnx 0.6.1 with its bundled espeak-ng was run on the lexicon terms and test sentences in `en-us` and `hi`. The results behind each lexicon entry are in the skill's [research notes](../skills/video-brand-kit/references/research.md). No audio was synthesised or listened to.
- `reelkit.py`, run on synthetic inputs:
  - `lint` flagged an off-kit font, a hex colour, an `rgb()` colour and an 18 px size, and accepted kit colours written as `rgba()` and `#000`.
  - `speak` rejected a Hindi voice, `--lang hi`, `am_adam`, Devanagari, a URL and "A I". It applied the lexicon and the `$`, `%`, `&` and `x` rules.
  - `verify` passed a matching transcript (0%) and failed one with three wrong words (8.1%).
- Metadata: the new `SKILL.md` and `frame.md` frontmatter parse as YAML, and the relative links resolve.
- Packaging: `skills add <repo> --list` discovered eight skills including `video-brand-kit`, and `scripts/install-video-kit.sh` copied it, with its assets, references and script, into the kit.

Not done: no reel was rendered, and no retention or listening test was run. The safe-zone margins are a conservative reading of disagreeing third-party guides, not a Meta specification.

### omaiverse brand — 31 October 2026

- `brands/omaiverse/frame.md` parses as YAML: 14 colours and 6 series.
- WCAG contrast was computed for every text and ground pair. The AI Breakdown and tool chips use ink text on `signal` (4.7:1), because paper text would be 3.8:1. Every other series chip with ink text is 6.4:1 or higher.
- Brand lexicon: "omaiverse" as written phonemizes as "AH-may-verse", so it is respelled "Ohm AI verse". Niche terms were checked in en-us: IIT, IIM, NIT, OKR, IPO, EDM, USP, VIP, ESOPs, EBITDA, FAANG and CTC are respelled; SDE, MBA, LPA, GMAT, DSA, LeetCode and others are left as written. `reelkit.py speak --brand omaiverse` applied the brand terms and the default terms together, and rejected "APM".
- `reelkit.py lint --brand omaiverse` accepted the series colours and flagged an off-kit hex.
- Default brand: with no `--brand`, `reelkit.py` used `brands/default` (omaiverse): `speak` said "Ohm AI verse" and `lint` accepted the series colours. `--brand none` fell back to the blank kit. `init --series claude-skills` copied the brand's `frame.md` into a new project and wrote a storyboard with the Claude Skills chip, colour, voice and call to action; an unknown series was refused with the list of valid ones.
- Hinglish mode: `speak --lang hinglish` refused the Kokoro provider, accepted ElevenLabs with Devanagari, and kept rejecting Devanagari in English mode. `verify` compared a mixed Devanagari and Latin transcript at 4.3% word error with one flagged word. The ElevenLabs voice settings in `brands/omaiverse/frame.md` were copied from Om's local reel session; no ElevenLabs audio was generated here, because this cloud session cannot download ElevenLabs or OpenArt files.
- Om's voices (1 November 2026): "om Hindi Voice" (`k2wSOFjoeAf2dogWLjMV`, cloned from a 2:27 Hindi recording) and "Om Voice" (`OIuMZwCGrdCumuvntFIq`, from a 2:53 English recording) are both verified clones in Om's ElevenLabs account. Test lines were generated with `eleven_multilingual_v2` and transcribed back with ElevenLabs Speech-to-Text: every word matched except the plain-written brand name ("Omiverse", "OMAVERSE"); respelled "Ohm AI verse" it came back as "Om AI Verse". Both are now the brand voices in `brands/omaiverse/frame.md`. Listening was left to Om.
