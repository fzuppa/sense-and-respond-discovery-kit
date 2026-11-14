---
name: impact-to-outcome-mapping
description: "Use to build, extend or review an Impact-to-Outcome map (Jeff Gothelf & Josh Seiden): a tree that links impact metrics (health of the business) to the lagging outcomes and leading outcomes (customer behaviors) that should move them, saved as an Obsidian canvas (.canvas). It interviews the user level by level — impact metrics, then lagging outcomes for each, then leading outcomes for each lagging — and offers suggestions at the outcome levels. Triggers: 'impact to outcome mapping', 'impact outcome map', 'map outcomes to impact metrics', 'outcome tree', 'impact metrics', 'lagging outcomes', 'leading outcomes', 'leading and lagging indicators', 'mapa de impacto a outcomes', 'mapear outcomes a métricas de impacto', 'mapa de outcomes', 'árbol de outcomes', 'draw/extend/review the impact map', 'help me write OKRs from outcomes' (the map comes first)."
---

# Impact-to-Outcome Mapping

Guides the user through building an **Impact-to-Outcome map** and saves it as an Obsidian canvas laid out like the diagram in Jeff Gothelf's post [Why you should map outcomes to impact metrics](https://jeffgothelf.com/blog/why-you-should-map-outcomes-to-impact-metrics/): impact metrics at the top, lagging outcomes under each, leading outcomes under those, arrows pointing up (child → parent), one tree per impact metric side by side, a legend column on the left.

This skill is part of the **Sense & Respond Product Discovery kit**. It works on its own; if the product has a Lean Product Canvas it can start from its Box 2. Self-contained: `references/` and `scripts/` (relative to this file) are all it needs, plus the project where it saves the canvas.

Read `references/method.md` before the first interview question: it has the definitions, the quality checks for each level and how to write suggestions. `references/input-schema.md` describes the JSON the script takes.

## The model

| Level | Canvas color | Question it answers | Node text |
|---|---|---|---|
| **Impact** | cyan | How do we know that our strategy has succeeded? | the business metric (Revenue, Profit Margin…) |
| **Outcome (Lagging)** | yellow | What behaviors can we observe/measure that indicate we're going to achieve our impact metric? | `[Who] [does what]` |
| **Outcome (Leading)** | orange | What behaviors lead to the behavior we want to see above? | `[Who] [does what]` |

- Leading outcomes can chain: a leading outcome can itself have an earlier leading outcome under it (Gothelf's diagram has two leading rows). All of them are orange.
- An outcome can feed more than one parent (in Gothelf's diagram "arrives via referral link" feeds two lagging outcomes), and two sibling outcomes can reinforce each other (a double-headed arrow).
- Every node can carry a **metric** (how it is measured) and an optional **baseline → target**. The user chose to be asked for the metric at every level.
- The map is a set of **hypotheses** about what drives what, not facts. Say so when it matters (first time, and when presenting the final map). Gothelf's advice for unclear journeys: make an informed guess and start running experiments, or bring in someone who can read the data.

## Output language

Same rule as the rest of the kit:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the current conversation.
3. If still unclear, ask before writing.

Node texts are written in that language. The legend on the canvas is in English by default; when the output language is different, translate it by passing `labels` in the JSON (see `references/input-schema.md`). The behavior format `[Who] [does what]` keeps its shape in any language.

## Output: one `.canvas`, no Markdown twin

The canvas is the only file and the source of truth. There is no `.md` copy. To work on an existing map, read it back with the script (`read`), change the JSON and rebuild (see "Resuming").

- **File name:** `impact-to-outcome-map <Product>.canvas`.
- **Folder** (resolve in this order, ask nothing if one applies):
  1. Search the project for existing `impact-to-outcome-map *.canvas` (`find . -iname "impact-to-outcome-map *.canvas"`) and use that folder.
  2. If the product has a `main-lean-product-canvas <Product>.md` or `.canvas`, use its folder.
  3. Otherwise ask where to save it (suggest the product's folder).

## Workflow

Ask **one question at a time**. Never fill a level for the user: suggestions are options, the user decides.

### 0. Identify the product and the file

- Ask what product or initiative the map is for, if it isn't clear.
- Resolve the folder and file name as above. If the canvas already exists, go to "Resuming" instead of starting over.

### 1. Context (once)

- **Lean Product Canvas.** If a main Lean Product Canvas exists for the product, read its Box 2 (Business Outcomes; in a `.canvas`, the text of that box) and offer it as the starting list of impact metrics. The user picks which ones to carry over.
- **Project material.** Ask once: *"Do you want me to look for related material in the project (notes, research, personas, problems) to ground the suggestions I make later?"* If yes, search by the product name and related terms and cite where each suggestion comes from. If no, work only from the conversation. Don't ask again for this map.

### 2. Impact metrics (level 1)

1. Ask: *"How will you know your strategy has succeeded? List the impact metrics, the measures of the health of the business."* (Suggest a Lean Product Canvas Box 2 carry-over if you found one.)
2. Run the impact checks from `references/method.md` (a business metric, not a behavior and not a feature; few of them). If one fails, explain why in one line and ask the user how to reword it. Never rewrite silently.
3. Confirm the final list before going on. Two or three is a healthy number; if there are more than four, say that the map will lose focus and ask whether to keep all.

No suggestions at this level: the impact metrics come from the business strategy, which only the user knows.

### 3. Lagging outcomes (level 2), once per impact metric

For each impact metric, in order:

1. Ask: *"What customer behaviors can we observe and measure that would tell us we're going to hit **<impact>**?"* Format `[Who] [does what]`.
2. **Offer suggestions** (the user asked for this at levels 2 and 3): ask *"Do you want suggestions?"*. Ask it **before** brainstorming alone, and again for each new impact metric (the answer can change). If yes, follow "Suggestions" in `references/method.md`: 3 to 5 options in `[Who] [does what]` format, each with a one-line reason and what it rests on; the user picks, edits or discards.
3. Run the outcome checks from `references/method.md`. A feature or a release ("launch the recommendation widget") is an output: ask what behavior it is meant to cause and use that.
4. Ask whether any of these lagging outcomes also feeds **another** impact metric (they then get several parents). Skip when there is only one impact metric.
5. Confirm the list for that impact metric.

### 4. Leading outcomes (level 3), once per lagging outcome

For each lagging outcome, in order (impact metric by impact metric):

1. Ask: *"What behaviors lead to **<lagging outcome>**?"* Same format. Same suggestions offer as in step 3.2.
2. Run the outcome checks. A leading outcome should happen earlier, more often and closer to something the team can influence than the outcome above it.
3. **Optional chain.** After the list for that lagging outcome, ask: *"Does any of these have an earlier behavior that leads to it (like 'logs in' before 'views product page')?"* If yes, repeat the question for that outcome, as many levels as the user wants. Stop when the behavior is something the team can influence directly. Don't push for depth.
4. Ask whether any leading outcome also feeds a second parent, and whether two siblings reinforce each other (these become `related` double arrows). Both questions only when the tree makes them plausible.

### 5. Measures (all levels)

Once the structure is confirmed, go level by level (impact, then lagging, then leading) and for each node ask:
- **Metric:** how would you measure it? (an event, a rate, a count; e.g. "% of sessions with add-to-cart"). If the user wants help, offer 2 or 3 metric names.
- **Baseline and target:** current value and desired value. Optional, and "unknown" is a valid answer.

Numbers are only the user's or come from a source they point to (cite it). **Never invent a baseline or a target**; a suggested *metric name* is fine, a suggested *value* is not. Leave blank what is unknown. The user can skip the leading level ("I'll measure those later").

### 6. Review and draw

1. Show the map as a nested list (impact → lagging → leading) with the metrics, and say which nodes still have no metric and which lagging outcomes have no leading outcome yet.
2. Offer the review from `references/method.md` ("Review") if the user wants a second look; don't rewrite their work, give specific guidance.
3. On confirmation, write the input JSON in a scratch directory **outside the vault** (a temp dir) and run the script from a neutral directory:

   ```bash
   python3 -I "<this skill's base directory>/scripts/impact_map_canvas.py" build input.json "<folder>/impact-to-outcome-map <Product>.canvas"
   ```

   If the canvas already exists, see "Resuming" for the overwrite rules.
4. Re-read the canvas with `read` and confirm the counts (impacts, lagging, leading) match what was agreed. You can't render the canvas, so say that the structure was verified, not how it looks.
5. Report in two or three lines: where the file is, that nodes are hypotheses to validate, and that regenerating the canvas redoes the layout (see "What the canvas does not carry").
6. Suggest the next step (Gothelf's prioritization): agree the strategy for the next 2-3 quarters, count the teams available, pick the same number of high-priority outcomes the teams can influence, and write the OKRs from them. This skill stops at the map; don't write OKRs unless asked.

## Resuming an existing map

Triggered by "extend the map", "add a lagging outcome to…", "review my map", or when the canvas for the product already exists.

1. **Read it:** `python3 -I <skill>/scripts/impact_map_canvas.py read "<canvas>" model.json` (scratch directory). Show the user the map as a nested list. The script infers the levels from the arrows, so it also reads a canvas drawn by hand (impact = a node with no outgoing arrow, lagging = feeds an impact, leading = the rest).
2. **Say what the script found beyond the tree:** it prints warnings for nodes not connected to the tree and for non-text nodes (files, links, groups). Those are lost on regeneration; tell the user and ask whether to keep going.
3. **Work on the model:** add or change nodes following the same questions (only the levels the user asks for), edit `model.json` and rebuild.
4. **Overwriting:** rebuilding overwrites the canvas, and with it any hand-made layout. Before writing, show what changes (nodes added, edited, removed) and ask for confirmation. If the user prefers, save the result with a `-v2` suffix instead.
5. **Hand-drawn maps that break the rules** (a business metric drawn as a lagging outcome, numbers inside the text, a feature as a node): apply the checks from `references/method.md` and give guidance. Don't fix silently.

## What the canvas does not carry

Say it the first time and whenever the user edits the canvas by hand:
- **Layout is regenerated.** Moving or resizing nodes in Obsidian is lost when the canvas is rebuilt. Text edits survive (they come back through `read`), as long as they keep the node format: a bold first line with the behavior, an italic line with the metric, a `baseline → target` line.
- **Extra nodes** (notes, files, groups) are not part of the model and are lost on rebuild.
- **Heights are estimated** from the text length. A long node may need a manual resize in Obsidian.
- **Rendering is not checked.** The script validates the structure (unique ids, valid parents, no cycles), not how it looks.

## What this skill does not do

- It does not decide the strategy or the impact metrics; it helps the user state them.
- It does not validate the hypotheses with data, and it does not prioritize or write OKRs.
- It does not keep a Markdown copy, and it does not edit the Lean Product Canvas.
- It does not produce Excalidraw or images; it only writes `.canvas` files.
