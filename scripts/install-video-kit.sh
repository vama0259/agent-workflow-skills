#!/bin/sh
# Install the video-* skills and the five upstream video tools into one separate
# folder. Claude Code loads it only when asked, so normal sessions pay nothing.
#
#   sh scripts/install-video-kit.sh [kit folder]     default: $VIDEO_KIT or ~/claude-video-kit
#
# Use it with the launcher this writes (<kit>/bin/claude-video, which runs
# `claude --add-dir <kit>`), or run `/add-dir <kit>` inside a session.
# Heavy dependencies (npm packages, Python venvs, Chrome, voice models, sample
# libraries) are not installed here; each tool installs what it needs on first use.
set -eu

KIT=${1:-${VIDEO_KIT:-$HOME/claude-video-kit}}
case "$KIT" in /*) ;; *) KIT=$(pwd)/$KIT ;; esac
case "$KIT" in / | "$HOME" | "$HOME"/) echo "✗ choose a dedicated folder for the kit, not $KIT"; exit 1 ;; esac
REPO_DIR=$(cd "$(dirname "$0")/.." && pwd)
SKILLS=$KIT/.claude/skills
TOOLS=$KIT/tools
CACHE=$KIT/.cache

# Upstream commits analysed in skills/video-workflow/references/tool-analysis.md
HYPERFRAMES_SHA=b7fa007bf3cfb03a62bbb5460009c7e628e3bb2d # CLI 0.8.181
ONETAKE_SHA=415758128aa45cc54340df40d8109363447f582e
COLLAGE_SHA=2e9b8a93a2834e4d670700ab9e4827a8baf3b668
CLAWD_SHA=0ac8bf2b31942376cb6b8c4074715595d512acd2
OPUSCAR_SHA=b5e8ef93930b6d828f352055a689320f138237b1

command -v git >/dev/null 2>&1 || { echo "✗ git is required"; exit 1; }
[ -d "$REPO_DIR/skills/video-workflow" ] || { echo "✗ run this from a checkout of agent-workflow-skills"; exit 1; }
mkdir -p "$SKILLS" "$TOOLS" "$CACHE" "$KIT/bin" "$KIT/licenses"

# fetch OWNER/REPO SHA DEST [sparse pattern...]
# Pinned and shallow; only the checked-out paths are downloaded. Re-running at a
# new commit updates in place and keeps untracked files (venvs, node_modules).
fetch() {
  repo=$1 sha=$2 dest=$3
  shift 3
  short=$(printf %.7s "$sha")
  if [ ! -d "$dest/.git" ]; then
    mkdir -p "$dest"
    git -C "$dest" init -q
    git -C "$dest" remote add origin "https://github.com/$repo.git"
  fi
  if [ "$(git -C "$dest" rev-parse -q --verify HEAD 2>/dev/null || true)" = "$sha" ]; then
    echo "= $repo $short"
    return 0
  fi
  if [ $# -gt 0 ]; then
    git -C "$dest" config core.sparseCheckout true
    printf '%s\n' "$@" >"$dest/.git/info/sparse-checkout"
  fi
  git -C "$dest" fetch -q --depth 1 --filter=blob:none origin "$sha"
  git -C "$dest" checkout -q FETCH_HEAD
  echo "↓ $repo $short"
}

# copy_skill SRC_DIR NAME: replace one skill folder in the kit
copy_skill() {
  rm -rf "${SKILLS:?}/$2"
  cp -R "$1" "$SKILLS/$2"
}

# 1. This package's router and wrappers
for dir in "$REPO_DIR"/skills/video-*/; do
  copy_skill "${dir%/}" "$(basename "$dir")"
done
cp "$REPO_DIR/LICENSE" "$KIT/licenses/agent-workflow-skills-LICENSE"
echo "✓ video-* skills from $REPO_DIR"

# 2. HyperFrames: all published skills, so its router never installs workflows
#    into ~/.claude/skills (the launcher also sets HYPERFRAMES_SKIP_SKILLS=1)
fetch heygen-com/hyperframes "$HYPERFRAMES_SHA" "$CACHE/hyperframes" '/skills/' '/LICENSE' '/CREDITS.md'
for dir in "$CACHE"/hyperframes/skills/*/; do
  if [ -f "$dir/SKILL.md" ]; then copy_skill "${dir%/}" "$(basename "$dir")"; fi
done
cp "$CACHE/hyperframes/LICENSE" "$KIT/licenses/hyperframes-LICENSE"
cp "$CACHE/hyperframes/CREDITS.md" "$KIT/licenses/hyperframes-CREDITS.md"

# 3. onetake (PolyForm Noncommercial): the skill, without its demo films
fetch feitangyuan/onetake "$ONETAKE_SHA" "$SKILLS/onetake" '/*' '!*.mp4' '!*.gif' '!/assets/'
cp "$SKILLS/onetake/LICENSE" "$KIT/licenses/onetake-LICENSE"

# 4. Collage B-roll: one prompt-only skill (needs the paid MaxFusion MCP to run)
fetch MegaTroll222/VOX-COLLAGE-BROLL "$COLLAGE_SHA" "$CACHE/collage" '/SKILL.md' '/LICENSE'
mkdir -p "$SKILLS/collage-broll-explainers"
cp "$CACHE/collage/SKILL.md" "$SKILLS/collage-broll-explainers/SKILL.md"
cp "$CACHE/collage/LICENSE" "$KIT/licenses/collage-broll-LICENSE"

# 5. Clawd animation: a starter kit copied into a new folder per film
fetch JohnHeibel/ClaudeAnimationBase "$CLAWD_SHA" "$TOOLS/ClaudeAnimationBase"
cp "$TOOLS/ClaudeAnimationBase/LICENSE" "$KIT/licenses/ClaudeAnimationBase-LICENSE"

# 6. Lemo-Opuscar: the style library, pinned (its setup.sh leaves an unmanaged
#    clone as it is), plus its skill. Same sparse paths as upstream's setup.sh.
fetch lemomo-ai/lemo-opuscar "$OPUSCAR_SHA" "$TOOLS/lemo-opuscar" '/*' '!/styles/*/demo/' '!/styleboard/' \
  '!/docs/frames/' '!/docs/cover.jpg' '!/docs/opuscar98.jpg' '!/styles/*/poster.jpg'
copy_skill "$TOOLS/lemo-opuscar/plugin/skills/lemo-opuscar" lemo-opuscar
cp "$TOOLS/lemo-opuscar/LICENSE" "$KIT/licenses/lemo-opuscar-LICENSE"

# Launcher: loads the kit for one session, with HyperFrames telemetry and skill
# auto-install off and Lemo-Opuscar pointed at the pinned library.
cat >"$KIT/bin/claude-video" <<EOF
#!/bin/sh
# Start Claude Code with the video kit loaded for this session only.
export VIDEO_KIT='$KIT'
export LEMO_OPUSCAR_HOME='$TOOLS/lemo-opuscar'
export HYPERFRAMES_NO_TELEMETRY=1 HYPERFRAMES_SKIP_SKILLS=1
exec claude --add-dir '$KIT' "\$@"
EOF
chmod +x "$KIT/bin/claude-video"

cat >"$KIT/README.md" <<EOF
# Claude video kit

Installed from agent-workflow-skills by scripts/install-video-kit.sh. Normal
Claude Code sessions don't load anything from this folder.

- Start a video session: \`$KIT/bin/claude-video\` (any \`claude\` flags work).
  Prefer this: it turns off HyperFrames telemetry and skill auto-install and
  points Lemo-Opuscar at the pinned library.
- Add it to a running session: \`/add-dir $KIT\`. Only the video-* skills then
  set those variables on each command, so start requests with video-workflow.
- Start with: "Use video-workflow: <what you want>".

| Folder | Contents |
| --- | --- |
| .claude/skills/video-* | Router and wrappers from agent-workflow-skills |
| .claude/skills/hyperframes*, media-use, figma and other workflows | HyperFrames skills @ $(printf %.7s "$HYPERFRAMES_SHA") (Apache-2.0) |
| .claude/skills/onetake | onetake @ $(printf %.7s "$ONETAKE_SHA") (PolyForm Noncommercial: noncommercial use only) |
| .claude/skills/collage-broll-explainers | Collage B-roll @ $(printf %.7s "$COLLAGE_SHA") (MIT; needs paid MaxFusion) |
| .claude/skills/lemo-opuscar, tools/lemo-opuscar | Lemo-Opuscar @ $(printf %.7s "$OPUSCAR_SHA") (MIT) |
| tools/ClaudeAnimationBase | Clawd starter kit @ $(printf %.7s "$CLAWD_SHA") (MIT) |
| licenses/ | Upstream licence and credits files |

Update: re-run the installer from a newer checkout. Remove: delete this folder.
EOF

echo
echo "✓ Video kit ready in $KIT"
echo "  Start a video session:  $KIT/bin/claude-video"
echo "  Optional shortcut:      alias claude-video='$KIT/bin/claude-video'   (add to your shell profile)"
