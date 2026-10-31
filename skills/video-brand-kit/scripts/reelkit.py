#!/usr/bin/env python3
"""Keep a reel inside its brand kit. Standard library only.

  reelkit.py init   <project> --series KEY [--brand NAME]          start a reel: kit + storyboard in the project
  reelkit.py lint   <project> [--brand NAME | --kit frame.md]     off-kit fonts, colours, tiny text, wrong canvas
  reelkit.py speak  <script.txt> [--brand NAME] [--voice ID] [--lang L] [-o vo.txt]
  reelkit.py verify <script.txt> <transcript.json> [--brand NAME] [--max-wer 0.08]

--brand NAME uses brands/NAME/frame.md and brands/NAME/lexicon.json (which extends the default lexicon).
Without --brand, the brand named in brands/default is used; --brand none uses the blank kit in assets/.

Exit status: 0 pass, 1 problems found, 2 bad input.
"""
import argparse
import difflib
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
DEFAULT_KIT = os.path.join(HERE, "..", "assets", "frame.md")
DEFAULT_LEXICON = os.path.join(HERE, "..", "assets", "lexicon.json")
BRANDS = os.path.join(HERE, "..", "brands")
SKIP_DIRS = {"node_modules", "renders", ".git", "assets", ".media", "dist"}
CSS_GENERIC = {"inherit", "initial", "unset", "sans-serif", "serif", "monospace", "system-ui"}


def frontmatter(path):
    text = open(path, encoding="utf-8").read()
    m = re.match(r"---\n(.*?)\n---", text, re.S)
    if not m:
        sys.exit(f"✗ {path}: no frontmatter")
    return m.group(1)


def section(fm, name):
    m = re.search(rf"^{name}:\s*\n((?:[ \t]+.*\n?|\s*\n)*)", fm, re.M)
    return m.group(1) if m else ""


def kit_values(kit):
    fm = frontmatter(kit)
    colors = {v.lower() for v in re.findall(r'"(#[0-9A-Fa-f]{6})"', section(fm, "colors"))}
    fonts = set(re.findall(r'fontFamily:\s*"([^"]+)"', fm))
    canvas = re.search(r"canvas:\s*\{\s*width:\s*(\d+),\s*height:\s*(\d+)", fm)
    floor = re.search(r"floor:\s*\{\s*px:\s*(\d+)", fm)
    return {
        "colors": colors,
        "fonts": fonts,
        "canvas": (int(canvas.group(1)), int(canvas.group(2))) if canvas else None,
        "floor": int(floor.group(1)) if floor else 32,
    }


def hex6(token):
    h = token.lstrip("#").lower()
    if len(h) in (3, 4):
        h = "".join(c * 2 for c in h[:3])
    return "#" + h[:6]


def rgb_hex(r, g, b):
    return "#%02x%02x%02x" % (int(r), int(g), int(b))


def project_files(root):
    for dirpath, dirs, files in os.walk(root):
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS]
        for f in files:
            if f.endswith((".html", ".css", ".js", ".mjs")):
                yield os.path.join(dirpath, f)


def cmd_lint(args):
    kit = kit_values(args.kit)
    problems = []
    declared_faces = set()
    files = list(project_files(args.project))
    if not files:
        print(f"✗ no .html/.css/.js files under {args.project}")
        return 2
    for path in files:
        text = open(path, encoding="utf-8", errors="replace").read()
        declared_faces |= set(re.findall(r"@font-face\s*\{[^}]*font-family:\s*['\"]?([^;'\"]+)", text))
    allowed_fonts = kit["fonts"] | declared_faces if args.allow_font_face else kit["fonts"]
    for path in files:
        rel = os.path.relpath(path, args.project)
        for n, line in enumerate(open(path, encoding="utf-8", errors="replace"), 1):
            decls = re.findall(r"font-?[fF]amily['\"]?\s*[:=]\s*([^;}\n]+)", line)
            decls += re.findall(r"--[\w-]*font[\w-]*\s*:\s*([^;}\n]+)", line)
            for decl in decls:
                for fam in decl.split(","):
                    fam = fam.strip().strip("'\"` ")
                    if fam and fam.lower() not in CSS_GENERIC and not fam.startswith(("var(", "$", "{")) and fam not in allowed_fonts:
                        problems.append(f"{rel}:{n}: font '{fam}' is not in the kit")
            for tok in re.findall(r"#[0-9A-Fa-f]{3,8}\b", line):
                if len(tok) - 1 in (3, 4, 6, 8) and hex6(tok) not in kit["colors"]:
                    problems.append(f"{rel}:{n}: colour {tok} is not in the kit")
            for r, g, b in re.findall(r"rgba?\(\s*(\d+)[ ,]+(\d+)[ ,]+(\d+)", line):
                if rgb_hex(r, g, b) not in kit["colors"]:
                    problems.append(f"{rel}:{n}: colour rgb({r},{g},{b}) is not in the kit")
            for px in re.findall(r"font-?[sS]ize['\"]?\s*[:=]\s*['\"]?(\d+(?:\.\d+)?)px", line):
                if float(px) < kit["floor"]:
                    problems.append(f"{rel}:{n}: font size {px}px is under the {kit['floor']}px floor")
            if kit["canvas"]:
                for w, h in re.findall(r'data-width="(\d+)"\s+data-height="(\d+)"', line):
                    if (int(w), int(h)) != kit["canvas"] and os.path.basename(path) == "index.html":
                        problems.append(f"{rel}:{n}: canvas {w}×{h}, kit is {kit['canvas'][0]}×{kit['canvas'][1]}")
    for p in problems:
        print("✗", p)
    print(("✓ inside the kit" if not problems else f"{len(problems)} off-kit value(s)") + f" ({len(files)} files)")
    return 1 if problems else 0


# --- voice -----------------------------------------------------------------

EMOJI = re.compile("[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF‍️]")
DEVANAGARI = re.compile("[ऀ-ॿ]")
URL = re.compile(r"\bhttps?://\S+|\bwww\.\S+", re.I)
GOOD_VOICE = re.compile(r"^[ab][fm]_[a-z]+$")
BAD_VOICES = {"am_adam"}
SHORT_CHARS = 25


def load_lexicon(path):
    data = json.load(open(path, encoding="utf-8"))
    terms, keep, never = {}, set(), {}
    if data.get("extends"):
        terms, keep, never = load_lexicon(os.path.join(os.path.dirname(path), data["extends"]))
    terms.update(data.get("terms", {}))
    keep |= set(data.get("keep_as_written", []))
    never.update(data.get("never_write", {}))
    return terms, keep, never


def default_brand():
    try:
        return open(os.path.join(BRANDS, "default"), encoding="utf-8").read().strip() or None
    except OSError:
        return None


def resolve_brand(args):
    if not hasattr(args, "brand"):
        return
    if args.brand is None and getattr(args, "kit", DEFAULT_KIT) == DEFAULT_KIT:
        args.brand = default_brand()
    if not args.brand or args.brand == "none":
        return
    folder = os.path.join(BRANDS, args.brand)
    if not os.path.isdir(folder):
        raise ValueError(f"no brand folder {folder}")
    if hasattr(args, "kit") and args.kit == DEFAULT_KIT:
        args.kit = os.path.join(folder, "frame.md")
    if hasattr(args, "lexicon") and args.lexicon == DEFAULT_LEXICON and os.path.exists(os.path.join(folder, "lexicon.json")):
        args.lexicon = os.path.join(folder, "lexicon.json")


def kit_series(kit):
    """The series block of a kit: {key: {chip, color, cta, voice, ...}}."""
    series, key = {}, None
    for line in section(frontmatter(kit), "series").splitlines():
        m = re.match(r"^  ([\w-]+):\s*$", line)
        if m:
            key = m.group(1)
            series[key] = {}
            continue
        m = re.match(r"^    ([\w-]+):\s*(.*?)\s*(?:#.*)?$", line)
        if key and m:
            series[key][m.group(1)] = m.group(2).strip('"')
    return series


def cmd_init(args):
    series = kit_series(args.kit)
    if series and args.series not in series:
        print(f"✗ choose --series from: {', '.join(series)}")
        return 2
    os.makedirs(args.project, exist_ok=True)
    kit_text = open(args.kit, encoding="utf-8").read()
    open(os.path.join(args.project, "frame.md"), "w", encoding="utf-8").write(kit_text)
    print(f"✓ {args.project}/frame.md ← {os.path.relpath(args.kit, os.path.join(HERE, '..'))}")
    board = os.path.join(args.project, "STORYBOARD.md")
    if os.path.exists(board):
        print(f"- kept existing {board}")
        return 0
    s = series.get(args.series, {})
    lines = [
        f"# {s.get('chip', args.series).title()} reel",
        "",
        f"- Brand: {args.brand or 'none'} (frame.md in this folder is the kit; use nothing outside it)",
        f"- Series: {args.series} · chip \"{s.get('chip', '')}\" in {s.get('color', '')} · voice: {s.get('voice', '')}",
        f"- CTA: {s.get('cta', '')}",
        "- Length: 20-45 s · English · one idea · hook of 6 words max, on screen in frame 1",
        "",
        "| Time | Words (as written) | Layout L1-L8 | Recipe R1-R8 | Transition out | SFX |",
        "| --- | --- | --- | --- | --- | --- |",
        "| 0.0-1.5 | HOOK | | R1 | | |",
        "| | | | | | |",
        "| last 2 s | " + s.get("cta", "CTA") + " | | R8 | loop | |",
        "",
        "Checklist before the draft render: references/edit-grammar.md §7, then `reelkit.py lint`.",
        "",
    ]
    open(board, "w", encoding="utf-8").write("\n".join(lines))
    print(f"✓ {board}")
    return 0


def apply_terms(text, terms):
    for key in sorted(terms, key=len, reverse=True):
        text = re.sub(rf"(?<![\w.]){re.escape(key)}(?![\w])", terms[key], text)
    return text


def normalise(text):
    text = EMOJI.sub("", text)
    text = re.sub(r"\$(\d[\d,]*(?:\.\d+)?)(k|K)?\b", lambda m: m.group(1) + (" thousand" if m.group(2) else "") + " dollars", text)
    text = re.sub(r"(\d)\s*%", r"\1 percent", text)
    text = re.sub(r"\s&\s", " and ", text)
    text = re.sub(r"(\d)x\b", r"\1 times", text)
    text = re.sub(r"[*_#>`~|]", "", text)
    text = re.sub(r"[ \t]+", " ", text)
    return "\n".join(line.strip() for line in text.strip().splitlines())


def cmd_speak(args):
    terms, keep, never = load_lexicon(args.lexicon)
    raw = open(args.script, encoding="utf-8").read()
    errors, warnings = [], []
    if args.voice:
        if not GOOD_VOICE.match(args.voice):
            errors.append(f"voice '{args.voice}' is not an American (a*) or British (b*) English Kokoro voice")
        elif args.voice in BAD_VOICES:
            errors.append(f"voice '{args.voice}' is graded F+ in Kokoro VOICES.md; use af_heart, af_bella, bf_emma or am_michael")
        if args.voice.startswith("b") and args.lang == "en-us":
            warnings.append("British voice with --lang en-us; pass --lang en-gb")
    if args.lang not in ("en-us", "en-gb", "en"):
        errors.append(f"--lang {args.lang} is not English; the kit's voice language is en")
    for n, line in enumerate(raw.splitlines(), 1):
        if DEVANAGARI.search(line):
            errors.append(f"line {n}: Devanagari text in an English voiceover")
        if URL.search(line):
            errors.append(f"line {n}: URL; write how it is said (\"link in bio\", \"example dot com\")")
        for bad, why in never.items():
            if re.search(rf"(?<!\w){re.escape(bad)}(?!\w)", line):
                errors.append(f"line {n}: '{bad}' {why}")
        for tok in re.findall(r"\b[A-Z][A-Z0-9]{1,}\b", line):
            if tok not in keep and tok not in terms and tok not in never:
                warnings.append(f"line {n}: '{tok}' may be read letter by letter or as a word; add it to the lexicon")
    spoken = normalise(apply_terms(raw, terms))
    for n, line in enumerate(spoken.splitlines(), 1):
        if 0 < len(line.strip()) < SHORT_CHARS:
            warnings.append(f"line {n}: '{line.strip()}' is short for Kokoro; synthesise it together with its neighbours")
        if len(line) > 400:
            warnings.append(f"line {n}: {len(line)} characters; split into 1-3 sentence chunks so the voice does not rush")
    for w in warnings:
        print("!", w)
    for e in errors:
        print("✗", e)
    if errors:
        return 1
    if args.output:
        open(args.output, "w", encoding="utf-8").write(spoken + "\n")
        print(f"✓ wrote {args.output}")
    else:
        print(spoken)
    return 0


def words(text):
    text = text.lower().replace("’", "'")
    return re.findall(r"[a-z0-9]+(?:'[a-z]+)?", text)


def transcript_words(path):
    data = json.load(open(path, encoding="utf-8"))
    if isinstance(data, dict):
        data = data.get("words") or data.get("segments") or []
    return [str(w.get("text", w.get("word", ""))) for w in data if isinstance(w, dict)]


def cmd_verify(args):
    terms, _, _ = load_lexicon(args.lexicon)
    # Compare in spoken form, so "Claude" and "Clawd" or "$20" and "20 dollars" match.
    spoken = lambda text: words(normalise(apply_terms(text, terms)))
    expected = spoken(open(args.script, encoding="utf-8").read())
    heard = spoken(" ".join(transcript_words(args.transcript)))
    if not expected or not heard:
        print("✗ empty script or transcript")
        return 2
    sm = difflib.SequenceMatcher(a=expected, b=heard, autojunk=False)
    errors = 0
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal" or "".join(expected[i1:i2]) == "".join(heard[j1:j2]):
            continue  # also "comfyui" heard as "comfy ui"
        errors += max(i2 - i1, j2 - j1)
        print(f"✗ {op:7} script: {' '.join(expected[i1:i2]) or '—':30} heard: {' '.join(heard[j1:j2]) or '—'}")
    wer = errors / len(expected)
    ok = wer <= args.max_wer
    print(f"{'✓' if ok else '✗'} word error {wer:.1%} ({errors}/{len(expected)} words), limit {args.max_wer:.0%}")
    return 0 if ok else 1


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    init = sub.add_parser("init", help="start a reel project with the brand kit and a storyboard")
    init.add_argument("project")
    init.add_argument("--series", required=True)
    init.add_argument("--brand")
    init.add_argument("--kit", default=DEFAULT_KIT)
    lint = sub.add_parser("lint", help="find off-kit fonts, colours and sizes in a HyperFrames project")
    lint.add_argument("project")
    lint.add_argument("--kit", default=DEFAULT_KIT)
    lint.add_argument("--brand")
    lint.add_argument("--allow-font-face", action="store_true", help="also accept families declared with @font-face")
    speak = sub.add_parser("speak", help="turn a script into the text the voice reads")
    speak.add_argument("script")
    speak.add_argument("--voice")
    speak.add_argument("--lang", default="en-us")
    speak.add_argument("--lexicon", default=DEFAULT_LEXICON)
    speak.add_argument("--brand")
    speak.add_argument("-o", "--output")
    verify = sub.add_parser("verify", help="compare a voice transcript with the script")
    verify.add_argument("script")
    verify.add_argument("transcript")
    verify.add_argument("--lexicon", default=DEFAULT_LEXICON)
    verify.add_argument("--brand")
    verify.add_argument("--max-wer", type=float, default=0.08)
    args = p.parse_args()
    try:
        resolve_brand(args)
        return {"init": cmd_init, "lint": cmd_lint, "speak": cmd_speak, "verify": cmd_verify}[args.cmd](args)
    except (OSError, ValueError) as e:
        print(f"✗ {e}")
        return 2


if __name__ == "__main__":
    sys.exit(main())
