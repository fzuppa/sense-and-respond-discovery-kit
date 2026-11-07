# Friction Map Canvas (Claude Code skill)

Skill that turns a saved **Cognitive Friction Map (MFC)** into a visual Obsidian canvas (`.canvas`): the journey as a left-to-right flow, steps grouped into phases, each step's friction colored by severity (red / orange / yellow, uncolored when there is no MFC friction), and a bottom row with the legend, the ranked opportunities, the patterns that cut across the map and a link back to the `.md`.

Part of the **[Sense & Respond Product Discovery kit](../README.md)**.

It draws a map; it doesn't create one. The map comes from `/afpm:map-frictions` (the `afpm` plugin) or any file that follows the `cognitive-frictions` output format.

## Installation

### Option 1: with `npx skills` (recommended)

```bash
npx skills add fzuppa/sense-and-respond-discovery-kit/friction-map-canvas -g
```

### Option 2: manual

Copy this whole folder (`SKILL.md`, `README.md`, `scripts/`, `references/`) into:
- **A single project:** `.claude/skills/friction-map-canvas/` at the project's root.
- **All your projects:** `~/.claude/skills/friction-map-canvas/`.

Requires `python3` (standard library only). No build step.

## Usage

The skill is meant to run **by itself** at the end of a friction mapping: after `/afpm:map-frictions` saves its file, Claude writes the canvas next to it. You can also ask:

- "Draw the friction map"
- "Graficá el mapa de fricciones"
- "Regenerate the canvas for the Spotify journey"

To make it fire reliably in a given project, add one line to that project's `CLAUDE.md`:

```
After generating a friction map (/afpm:map-frictions or similar), always run the friction-map-canvas skill on the saved file.
```

## What you get

`<same name as the map>.canvas`, next to the `.md`:

- A title node, and one node per journey step in a row (wrapping into rows of 8 beyond 12 steps).
- One friction node under each step. Color = severity from the map. A step without MFC friction keeps a short note and no color.
- Phase groups around contiguous steps.
- Bottom row: legend, ranked opportunities, cross-cutting notes, and a file node pointing to the `.md`.

The `.md` stays the source of truth. The canvas is a summary: re-running the skill regenerates it and overwrites hand edits (the skill asks before overwriting an existing canvas).

## How it works

Claude reads the map and writes a small JSON ([`references/input-schema.md`](references/input-schema.md)) with the text of each node, copying numbers from the map and never inventing them. [`scripts/make_canvas.py`](scripts/make_canvas.py) does the layout (positions, sizes, colors, edges), validates ids and edge references, and writes the canvas. The script has no text of its own, so it works in any language.

[`references/example-spotify.json`](references/example-spotify.json) is the input of a real 11-step canvas (Spotify, "from free to Premium").

## Limits

- Obsidian only: it writes JSON Canvas 1.0, which Obsidian opens natively. It doesn't generate Excalidraw or images.
- Node heights are estimates from the text length; a very long text may need a manual resize.
- It can't render the canvas, so it validates structure, not looks.

## Language

Output language follows the kit-wide rule, in order:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the friction map itself.
3. If still unclear, ask before writing.

The kit's own instructions (this README, `SKILL.md`, reference files) are in English; only the content the skill generates adapts to the project's language.
