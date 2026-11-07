---
name: friction-map-canvas
description: "Use whenever a Cognitive Friction Map (MFC) has been produced or saved, to turn it into a visual Obsidian canvas (.canvas): the journey steps as a flow, grouped into phases, with each step's friction colored by severity, plus the ranking and cross-cutting patterns. Run it as the last step after /afpm:map-frictions or after any friction map saved in product/journeys/, without waiting to be asked. Also use when the user asks to draw, visualize, chart or graph a friction map, or says 'friction map canvas', 'mapa de fricciones en canvas', 'graficá el mapa de fricciones', 'MFC canvas'."
---

# Friction Map Canvas

Turns a saved **Cognitive Friction Map (MFC)** into an Obsidian canvas: the journey as a left-to-right flow, steps grouped into phases, one friction node under each step colored by severity, and a bottom row with the legend, the ranked opportunities and the patterns that cut across the map.

This skill is part of the **Sense & Respond Product Discovery kit**. It does not create the map: it only draws one that already exists. The map comes from `/afpm:map-frictions` (or any file that follows the `cognitive-frictions` output format).

## When it runs

- **Automatically, as the last step of a friction mapping.** As soon as a friction map file is saved (for example `product/journeys/{YYYY-MM-DD-HHMM}-{slug}.md`), run this skill on it. Don't ask first; tell the user at the end that the canvas exists.
- **On request**, for an existing map ("draw the friction map", "regenerate the canvas").
- If there is no friction map file yet, say so and point to `/afpm:map-frictions`. Never invent a map to draw.

## Output language

Same rule as the rest of the kit:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the friction map itself (the canvas text must match the `.md` it comes from).
3. If still unclear, ask before writing.

The script is layout-only and language-agnostic: every piece of text on the canvas comes from the input JSON you write.

## Workflow

1. **Read the map.** Read the friction map `.md` completely: header (actor, goal, source), the step list, the per-step frictions, the ranking and any cross-cutting patterns or caveats.

2. **Write the input JSON** following `references/input-schema.md`, in a scratch directory outside the vault (for example a temp dir), never inside the user's notes. Rules:
   - **Copy, don't invent.** Every number, count, percentage and quote on the canvas must already be in the map. If the map says "not yet measured", the canvas says so too.
   - **One node per step, short.** The friction node holds: categories in bold, severity and rank, a one-line problem, the key evidence numbers, and a caveat if the map has one. Aim for 250-350 characters. The `.md` keeps the detail.
   - **Steps without friction stay on the map.** Give them a `note` with a one-line reason (bug, policy, business model) and the number that shows why. Don't give them a severity color: a canvas where every step is colored hides the real bottlenecks.
   - **Phases**: group contiguous steps into 3-5 phases that name a stage of the journey. Every step should belong to one.
   - **Severity** is the one in the map (`high|medium|low`, or `alta|media|baja`). Do not re-score.
   - **Ranking** must match the map's ranked list, including tie-break notes.
   - `source_file` is the vault-relative path of the `.md`, so the canvas links back to it.

3. **Run the script** from a neutral directory:

   ```bash
   python3 -I "<this skill's base directory>/scripts/make_canvas.py" input.json "<path to the map>.canvas"
   ```

   Save the canvas **next to the `.md`, with the same base name** (`…/2026-11-07-1023-de-gratis-a-premium.md` → `…/2026-11-07-1023-de-gratis-a-premium.canvas`). The script validates unique ids and edge references and prints the node/edge counts.

4. **Check the result.** Re-read the canvas as JSON and confirm it parses and has one friction node per step. If the user has Obsidian open, they can look at it; you can't render it, so don't claim how it looks.

5. **Report in two or three lines:** where the canvas is, that the `.md` stays the source of truth, and that re-running the skill regenerates it (changes made by hand in the canvas are overwritten).

## If a canvas already exists

If the `.canvas` next to the map already exists, ask before overwriting: the user may have moved nodes by hand. If they say yes, overwrite; otherwise save with a `-v2` suffix.

## Layout facts (so you can set expectations)

- Up to 12 steps fit in one row; beyond that the script wraps to rows of 8 (override with `steps_per_row`). A phase that crosses a row break is drawn as two groups with the same label.
- Node heights are estimated from the text length. Very long texts may still need a manual resize in Obsidian.
- Colors use the canvas presets, so the actual tones follow the user's Obsidian theme: red = high, orange = medium, yellow = low, none = no MFC friction.

## What this skill does not do

- It does not analyze the journey, score severity or propose solutions. That is the friction mapping.
- It does not edit the `.md` map.
- It does not produce Excalidraw or images. It only writes `.canvas` files.
