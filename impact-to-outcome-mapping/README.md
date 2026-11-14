# Impact-to-Outcome Mapping (Claude Code skill)

Skill that guides you through building an **Impact-to-Outcome map** (Jeff Gothelf & Josh Seiden) and saves it as an Obsidian canvas (`.canvas`), laid out like the diagram in [Why you should map outcomes to impact metrics](https://jeffgothelf.com/blog/why-you-should-map-outcomes-to-impact-metrics/): impact metrics on top, lagging outcomes under them, leading outcomes at the bottom, one tree per impact metric, a legend on the left.

Part of the **[Sense & Respond Product Discovery kit](../README.md)**.

## Installation

### Option 1: with `npx skills` (recommended)

```bash
npx skills add fzuppa/sense-and-respond-discovery-kit/impact-to-outcome-mapping -g
```

### Option 2: manual

Copy this whole folder (`SKILL.md`, `README.md`, `scripts/`, `references/`) into:
- **A single project:** `.claude/skills/impact-to-outcome-mapping/` at the project's root.
- **All your projects:** `~/.claude/skills/impact-to-outcome-mapping/`.

Requires `python3` (standard library only). No build step.

## Usage

Just talk to Claude:

- "Help me map outcomes to impact metrics for `<product>`"
- "Armemos el mapa de impacto a outcomes de `<producto>`"
- "Add a lagging outcome to the impact map"
- "Review my impact map"

Claude asks one question at a time:

1. **Impact metrics** (level 1): how will you know your strategy succeeded?
2. **Lagging outcomes** (level 2), for each impact metric: which customer behaviors indicate you'll reach it?
3. **Leading outcomes** (level 3), for each lagging outcome: which behaviors lead to it? You can chain them as deep as you want, like Gothelf's diagram.
4. **Measures** at every level: metric, and optionally baseline → target.

At levels 2 and 3 Claude asks whether you want suggestions. They are hypotheses, and nothing goes into the map until you pick it. If the product has a Lean Product Canvas, its Box 2 (Business Outcomes) is offered as the starting list of impact metrics.

## What you get

`impact-to-outcome-map <Product>.canvas`, in the product's folder:

- Impact nodes in cyan, lagging outcomes in yellow, leading outcomes in orange, arrows from child to parent.
- Outcomes with more than one parent, and double-headed arrows between outcomes that reinforce each other.
- Each node: the behavior in bold, the metric in italics, `baseline → target` when known.
- A legend column with the three questions from Gothelf's diagram.

The canvas is the only file and the source of truth. Claude can read it back to extend or review the map. Rebuilding redoes the layout, so manual positioning is lost; text edits survive.

## How it works

Claude interviews you and writes a small JSON ([`references/input-schema.md`](references/input-schema.md)). [`scripts/impact_map_canvas.py`](scripts/impact_map_canvas.py) validates it (ids, parents, cycles), lays out the tree (layers, centered parents, trees side by side) and writes the canvas. The `read` command does the reverse, and it also understands canvases drawn by hand. The script has no text of its own except an English legend that can be overridden, so it works in any language.

[`references/example-gothelf.json`](references/example-gothelf.json) draws Gothelf's own example (Revenue and Profit Margin). [`references/method.md`](references/method.md) has the definitions, the quality checks for each level, how suggestions are written and how a review goes.

## Limits

- Obsidian only: it writes JSON Canvas 1.0. No Excalidraw, no images.
- Node heights are estimated from the text length; a long node may need a manual resize.
- It can't render the canvas, so it validates structure, not looks.
- The map is a set of hypotheses. The skill doesn't validate them with data, prioritize or write OKRs.

## Language

Output language follows the kit-wide rule, in order:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the current conversation.
3. If still unclear, ask before writing.

The kit's own instructions (this README, `SKILL.md`, reference files) are in English; only the content the skill generates adapts to the project's language.
