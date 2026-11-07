# Input schema for `scripts/make_canvas.py`

A single JSON file. All text is free Markdown and ends up verbatim on the canvas, so write it in the language of the friction map. Use real line breaks (`\n` inside the JSON string), never the literal characters `\\n`.

```json
{
  "title": "Product: journey name",
  "subtitle": "Cognitive friction map (MFC) · actor · evidence in one line",
  "steps_per_row": 8,
  "phases": [
    { "label": "Phase name", "steps": [1, 3] }
  ],
  "steps": [
    {
      "name": "1. Step name",
      "friction": {
        "severity": "high",
        "text": "**Evaluator** · severity **high** (#1)\n\nOne-line problem.\n\nKey evidence numbers · caveat."
      }
    },
    {
      "name": "2. A step with no MFC friction",
      "note": "**No MFC friction**\nOne-line reason.\n\nThe number that shows why."
    }
  ],
  "legend": "**Legend**\n\n🔴 High severity\n🟠 Medium\n🟡 Low\n⚪ No MFC friction",
  "ranking": "**Ranked opportunities**\n\n1. Step 11: ...\n2. Step 5: ...",
  "notes": [
    { "color": "purple", "width": 520, "text": "**Cross-cutting pattern**\n\n..." }
  ],
  "source_file": "Products/Spotify/product/journeys/2026-11-07-1023-slug.md"
}
```

## Fields

| Field | Required | Meaning |
|---|---|---|
| `title`, `subtitle` | no | Header node at the top-left. |
| `steps` | **yes** | The journey steps in order. Each has a `name` and either a `friction` (a step with MFC friction) or a `note` (a step without). |
| `steps[].friction.severity` | yes, if `friction` | `high`/`medium`/`low` (also `alta`/`media`/`baja`). Sets the node color: red, orange, yellow. Any other value leaves the node uncolored. |
| `steps[].friction.text` | yes, if `friction` | Body of the friction node. Aim for 250-350 characters. |
| `steps[].note` | no | Body of the node for a step without friction. Left uncolored. |
| `phases` | no | Contiguous 1-based step ranges drawn as cyan groups. A range outside `1..N` aborts the script. |
| `steps_per_row` | no | Defaults to all steps in one row up to 12 steps, and to 8 per row beyond that. |
| `legend` | no | Text node with the color legend, bottom-left. |
| `ranking` | no | Text node (green) with the ranked opportunities. |
| `notes` | no | Extra text nodes in the bottom row. `color`: `red`, `orange`, `yellow`, `green`, `cyan`, `purple` (default `purple`). `width` default 520. |
| `source_file` | no | Vault-relative path of the `.md` map, shown as a file node in the bottom row. |

## Example

`example-spotify.json` is the input behind a real canvas: an 11-step journey ("from free to Premium"), four phases, six frictions and five steps without friction. Run it to see the layout:

```bash
python3 -I scripts/make_canvas.py references/example-spotify.json /tmp/example.canvas
```

(Its `source_file` points to a note in the author's vault, so that node will show as a missing file anywhere else.)
