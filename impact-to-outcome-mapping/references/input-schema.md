# Input schema — `impact_map_canvas.py build`

A JSON file the skill writes in a scratch directory (outside the user's notes) before running the script. All text comes from here: the script has none of its own except the English legend, which you can override.

```json
{
  "nodes": [
    {"id": "i1", "type": "impact", "text": "Revenue",
     "metric": "Monthly recurring revenue", "baseline": "1.2M", "target": "1.5M"},
    {"id": "l1", "type": "lagging", "text": "Customer adds item to cart",
     "metric": "% of sessions with add-to-cart", "baseline": "3%", "target": "4.5%",
     "feeds": ["i1"]},
    {"id": "e1", "type": "leading", "text": "Customer views product page", "feeds": ["l1"]},
    {"id": "e2", "type": "leading", "text": "Customer logs in", "feeds": ["e1"]}
  ],
  "related": [["e1", "e3"]],
  "labels": {"impact_title": "Impacto"},
  "legend": true
}
```

## Fields of a node

| Field | Required | Meaning |
|---|---|---|
| `id` | yes | Unique within the file. Any string except one starting with `legend-`. Not shown on the canvas. |
| `type` | yes | `impact`, `lagging` or `leading`. |
| `text` | yes | The node title. Impact: the metric name. Outcomes: `[Who] [does what]`. Behavior only, no numbers. |
| `feeds` | yes, except for `impact` | List of parent ids. Rules below. |
| `metric` | no | How it is measured (shown in italics). Leave out if unknown. |
| `baseline`, `target` | no | Current and desired value, shown as `baseline → target` (`?` for the missing side). **Never invent them.** |

**Rules for `feeds`** (the script rejects anything else):
- `impact` has no `feeds`. It is a root.
- `lagging` feeds one or more `impact` nodes.
- `leading` feeds `lagging` or `leading` nodes (a chain of leading nodes is fine), never an impact directly.
- No cycles. Several parents are allowed.

## Other keys

- `related`: list of pairs of node ids that reinforce each other, drawn as a double-headed arrow (like "views product page" ⇄ "clicks related item link" in Gothelf's diagram). Works best for two nodes on the same row.
- `legend`: `true` (default) draws the legend column on the left; `false` omits it.
- `labels`: overrides for the legend text, to translate it. Keys: `impact_title`, `impact_question`, `lagging_title`, `lagging_question`, `leading_title`, `leading_question`, `pattern` (the `[WHO] [DOES WHAT]` hint). Anything left out stays in English.

## What the script draws

- **Rows** are layers: impact on top, lagging below, leading below that. A node's row is the longest path to any impact node, so a chain of leading outcomes goes down one row per step. Arrows run child → parent (from the top of the child to the bottom of the parent).
- **Columns:** one tree per impact metric, side by side, with extra space between trees. Each parent is centered over its children; an outcome with several parents is placed between them.
- **Colors** use the canvas presets, so the tones follow the user's Obsidian theme: impact `5` (cyan), lagging `3` (yellow), leading `2` (orange).
- **Node text:** `**title**`, a blank line, then `*metric*` and `baseline → target` lines when present. `read` parses exactly this shape, so keep it if you edit nodes by hand.
- **Ids** on the canvas are derived from the input ids, so rebuilding the same map produces the same ids.

## Commands

```bash
python3 -I impact_map_canvas.py build input.json "out.canvas"   # JSON -> canvas
python3 -I impact_map_canvas.py read  "map.canvas" [model.json]  # canvas -> JSON (stdout if no file)
```

`build` validates ids, types, parents and cycles; it prints warnings for impacts without lagging outcomes and lagging outcomes without leading ones, and the counts of what it wrote. `read` renumbers the ids (`i1…`, `l1…`, `e1…`, left to right), infers levels from the arrows and warns about nodes it can't carry (disconnected or non-text).

Run both from a neutral directory (not inside the vault or a downloaded folder).
