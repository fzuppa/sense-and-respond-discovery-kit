#!/usr/bin/env python3
"""Build an Obsidian .canvas (JSON Canvas 1.0) from a friction map described in JSON.

Layout only: every piece of text comes from the input file, so the script is
language-agnostic. See references/input-schema.md for the input format.

Usage:
    python3 -I make_canvas.py INPUT.json OUTPUT.canvas
"""
import json
import math
import secrets
import sys

PITCH = 340          # horizontal distance between step columns
W = 280              # width of step and friction nodes
STEP_H = 100         # height of step nodes
GAP_STEP_FR = 90     # vertical gap between a step node and its friction node
GROUP_PAD = 25       # padding inside phase groups
ROW_GAP = 160        # vertical gap between rows of steps (when wrapping)
BOTTOM_GAP = 80      # gap between the last row and the bottom notes
CHAR_W = 8.5         # rough pixels per character, to estimate text node height
LINE_H = 26
BOX_PAD = 40

SEVERITY_COLOR = {
    "high": "1", "alta": "1", "alto": "1",
    "medium": "2", "media": "2", "medio": "2",
    "low": "3", "baja": "3", "bajo": "3",
}
NOTE_COLORS = {"red": "1", "orange": "2", "yellow": "3", "green": "4", "cyan": "5", "purple": "6"}

ids = set()


def new_id():
    while True:
        i = secrets.token_hex(8)
        if i not in ids:
            ids.add(i)
            return i


def est_height(text, width=W, minimum=120):
    cpl = max(10, int((width - BOX_PAD) / CHAR_W))
    lines = sum(max(1, math.ceil(len(line) / cpl)) for line in text.split("\n"))
    h = BOX_PAD + lines * LINE_H
    return max(minimum, int(math.ceil(h / 10.0) * 10))


def fail(msg):
    sys.exit("make_canvas.py: " + msg)


def main():
    if len(sys.argv) != 3:
        fail("usage: make_canvas.py INPUT.json OUTPUT.canvas")
    with open(sys.argv[1], encoding="utf-8") as f:
        data = json.load(f)

    steps = data.get("steps")
    if not steps:
        fail("input needs a non-empty 'steps' list")
    n = len(steps)

    per_row = data.get("steps_per_row") or (n if n <= 12 else 8)
    rows = [list(range(i, min(i + per_row, n))) for i in range(0, n, per_row)]

    nodes, edges = [], []
    group_nodes = []   # collected first so they sit in the lowest layer
    body_nodes = []

    # Title
    title = data.get("title", "")
    subtitle = data.get("subtitle", "")
    body_nodes.append({
        "id": new_id(), "type": "text", "x": 0, "y": -200, "width": 900, "height": 110,
        "text": "# " + title + ("\n" + subtitle if subtitle else ""),
    })

    # Phases -> list of (label, first_idx, last_idx) 0-based, validated
    phases = []
    for p in data.get("phases", []):
        a, b = p["steps"]
        if not (1 <= a <= b <= n):
            fail("phase '%s' has an invalid step range %s" % (p.get("label"), p["steps"]))
        phases.append((p["label"], a - 1, b - 1))

    step_ids = [None] * n
    friction_ids = [None] * n
    row_bottoms = []
    y0 = 0

    for r, row in enumerate(rows):
        fr_heights = []
        for idx in row:
            fr = steps[idx].get("friction")
            fr_heights.append(est_height(fr["text"]) if fr else est_height(steps[idx].get("note", ""), minimum=120))
        row_fr_max = max(fr_heights) if fr_heights else 120
        fr_y = y0 + STEP_H + GAP_STEP_FR

        for col, idx in enumerate(row):
            x = PITCH * col
            step = steps[idx]
            sid = new_id()
            step_ids[idx] = sid
            body_nodes.append({
                "id": sid, "type": "text", "x": x, "y": y0, "width": W, "height": STEP_H,
                "text": "**%s**" % step["name"],
            })
            fr = step.get("friction")
            if fr:
                text = fr["text"]
                color = SEVERITY_COLOR.get(str(fr.get("severity", "")).lower())
            else:
                text = step.get("note", "")
                color = None
            fid = new_id()
            friction_ids[idx] = fid
            node = {
                "id": fid, "type": "text", "x": x, "y": fr_y, "width": W,
                "height": fr_heights[col], "text": text,
            }
            if color:
                node["color"] = color
            body_nodes.append(node)
            edge = {
                "id": new_id(), "fromNode": sid, "fromSide": "bottom",
                "toNode": fid, "toSide": "top", "toEnd": "none",
            }
            if color:
                edge["color"] = color
            edges.append(edge)

        # phase groups for this row (a phase that crosses a row break is split)
        group_h = STEP_H + GAP_STEP_FR + row_fr_max + 2 * GROUP_PAD
        for label, a, b in phases:
            seg = [i for i in row if a <= i <= b]
            if not seg:
                continue
            c0, c1 = row.index(seg[0]), row.index(seg[-1])
            group_nodes.append({
                "id": new_id(), "type": "group",
                "x": PITCH * c0 - GROUP_PAD, "y": y0 - GROUP_PAD,
                "width": PITCH * (c1 - c0) + W + 2 * GROUP_PAD, "height": group_h,
                "label": label, "color": "5",
            })

        row_bottoms.append(y0 - GROUP_PAD + group_h)
        y0 = row_bottoms[-1] + ROW_GAP + GROUP_PAD

    # Arrows between consecutive steps
    for i in range(n - 1):
        same_row = (i // per_row) == ((i + 1) // per_row)
        edges.append({
            "id": new_id(), "fromNode": step_ids[i], "fromSide": "right" if same_row else "bottom",
            "toNode": step_ids[i + 1], "toSide": "left" if same_row else "top", "toEnd": "arrow",
        })

    # Bottom row: legend, ranking, notes, source file
    by = row_bottoms[-1] + BOTTOM_GAP
    x = 0
    boxes = []
    if data.get("legend"):
        boxes.append(("text", {"text": data["legend"]}, 340, None))
    if data.get("ranking"):
        boxes.append(("text", {"text": data["ranking"]}, 600, "4"))
    for note in data.get("notes", []):
        boxes.append(("text", {"text": note["text"]}, note.get("width", 520),
                      NOTE_COLORS.get(note.get("color", "purple"), "6")))
    if data.get("source_file"):
        boxes.append(("file", {"file": data["source_file"]}, 460, None))
    for kind, payload, width, color in boxes:
        height = est_height(payload["text"], width=width, minimum=200) if kind == "text" else 300
        node = {"id": new_id(), "type": kind, "x": x, "y": by, "width": width, "height": height}
        node.update(payload)
        if color:
            node["color"] = color
        body_nodes.append(node)
        x += width + 60

    nodes = group_nodes + body_nodes

    # Validation
    node_ids = {nd["id"] for nd in nodes}
    all_ids = [nd["id"] for nd in nodes] + [e["id"] for e in edges]
    if len(all_ids) != len(set(all_ids)):
        fail("duplicate ids")
    for e in edges:
        if e["fromNode"] not in node_ids or e["toNode"] not in node_ids:
            fail("dangling edge " + e["id"])

    with open(sys.argv[2], "w", encoding="utf-8") as f:
        json.dump({"nodes": nodes, "edges": edges}, f, ensure_ascii=False, indent=2)

    print("%d nodes, %d edges, %d row(s)" % (len(nodes), len(edges), len(rows)))


if __name__ == "__main__":
    main()
