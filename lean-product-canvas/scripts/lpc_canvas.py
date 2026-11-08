#!/usr/bin/env python3
"""Convert a Lean Product Canvas between Markdown and an Obsidian .canvas (JSON Canvas 1.0).

The Markdown file is the one the skill writes: an H1 "# <Prefix> — <Initiative>",
an optional preamble line (e.g. "Source problem: [[...]]"), and eight sections
"## N. <Box title>". The canvas lays the eight boxes out like the official Lean
Product Canvas (v3): boxes 1/3/6 on the left, 5 (tall) and 7 in the middle,
2/4/8 on the right. Box text is copied verbatim in both directions.

Commands (run with `python3 -I`):
    lpc_canvas.py to-canvas  MD CANVAS [--date YYYY-MM-DD] [--link NAME] [--strings FILE]
    lpc_canvas.py to-md      CANVAS MD  [--h1-prefix TEXT]
    lpc_canvas.py compare    MD CANVAS   (exit 0 if identical, 1 if they differ)

Existing output files are overwritten: the caller decides when that is OK.
When to-md replaces an existing Markdown it keeps that file's title prefix
(it may be translated); for a new file pass --h1-prefix, or it defaults to
"Main Lean Product Canvas" (file name starting with "main-") or "Lean Product Canvas".
"""
import argparse
import datetime
import json
import math
import re
import secrets
import sys

COL_W, GAP = 820, 20
CHAR_W, LINE_H, PAD = 8.5, 26, 50

STRINGS = {
    "title": "Lean Product Canvas (v3)",
    "initiative": "Title of initiative:",
    "date": "Date:",
    "iteration": "Iteration:",
    "footer": "CC BY-NC-SA · Lean Product Canvas (v3) by Sense & Respond · www.senseandrespond.co/the-lean-product-canvas",
    "data": "Data:",
    "questions": {
        "1": "What is the most important problem your business needs to focus on right now?",
        "2": "How will you know you solved the business problem? What will you measure?",
        "3": "Which users and customers (i.e., personas) should you focus on first?",
        "4": "Why would your users seek out your product or service? What benefit would they gain from using it? What is their Job To Be Done? What are they trying to do?",
        "5": "What can we make that will solve our business problem and meet the needs of our customers at the same time?",
        "6": "We believe that [business outcome] will be achieved if [user] attains [benefit] with [feature].",
        "7": "What's the most important thing we need to learn first?",
        "8": "What's the least amount of work we need to do to learn the next most important thing?",
    },
}
# Official v3 colour coding: 1-4 red, 5 cyan, 6-8 green. Pending boxes stay uncoloured.
COLORS = {1: "1", 2: "1", 3: "1", 4: "1", 5: "5", 6: "4", 7: "4", 8: "4"}
PENDING_RE = re.compile(r"^_[^_\n]{2,30}_$")
FOOTER_MARK = "senseandrespond.co/the-lean-product-canvas"


def fail(msg):
    sys.exit("lpc_canvas.py: " + msg)


def load_strings(path):
    s = json.loads(json.dumps(STRINGS))
    if path:
        with open(path, encoding="utf-8") as f:
            extra = json.load(f)
        for k, v in extra.items():
            if k == "questions":
                s["questions"].update({str(i): t for i, t in v.items()})
            else:
                s[k] = v
    return s


# ---------- Markdown <-> model ----------

def parse_md(text):
    h1 = re.search(r"^# (.+)$", text, re.M)
    if not h1:
        fail("the Markdown has no '# ' title line")
    title = h1.group(1).strip()
    prefix, initiative = "", title
    for sep in (" — ", " - "):
        if sep in title:
            prefix, initiative = title.rsplit(sep, 1)
            break
    first = re.search(r"^## \d\. ", text, re.M)
    if not first:
        fail("the Markdown has no '## N. <box>' sections")
    preamble = text[h1.end():first.start()].strip()
    boxes = {}
    for m in re.finditer(r"^## (\d)\. (.+?)\n(.*?)(?=^## \d\. |\Z)", text, re.M | re.S):
        boxes[int(m.group(1))] = (m.group(2).strip(), m.group(3).strip())
    missing = [i for i in range(1, 9) if i not in boxes]
    if missing:
        fail("boxes missing in the Markdown: %s" % missing)
    return {"prefix": prefix.strip(), "initiative": initiative.strip(),
            "preamble": preamble, "boxes": boxes}


def model_to_md(model, prefix):
    head = "# %s — %s" % (prefix, model["initiative"]) if prefix else "# " + model["initiative"]
    out = [head, ""]
    if model["preamble"]:
        out += [model["preamble"], ""]
    for n in range(1, 9):
        title, body = model["boxes"][n]
        out += ["## %d. %s" % (n, title), body, ""]
    return "\n".join(out).rstrip("\n") + "\n"


# ---------- canvas <-> model ----------

def new_id(used):
    while True:
        i = secrets.token_hex(8)
        if i not in used:
            used.add(i)
            return i


def est_height(text, width, minimum):
    cpl = max(10, int((width - 40) / CHAR_W))
    lines = sum(max(1, math.ceil(len(l) / cpl)) for l in text.split("\n"))
    return max(minimum, int(math.ceil((PAD + lines * LINE_H) / 10.0) * 10))


def model_to_canvas(model, s, date, link):
    used = set()
    texts, heights = {}, {}
    for n in range(1, 9):
        title, body = model["boxes"][n]
        texts[n] = "## %d. %s\n*%s*\n\n%s" % (n, title, s["questions"][str(n)], body)
        heights[n] = est_height(texts[n], COL_W, 300)

    r1 = max(heights[1], heights[2], 340)
    r2 = max(heights[3], heights[4], 300)
    if r1 + GAP + r2 < heights[5]:
        r2 += heights[5] - (r1 + GAP + r2)
    r3 = max(heights[6], heights[7], heights[8])

    X = [0, COL_W + GAP, 2 * (COL_W + GAP)]
    Y2 = r1 + GAP
    Y3 = r1 + GAP + r2 + GAP
    total_w, total_h = 3 * COL_W + 2 * GAP, Y3 + r3
    pos = {
        1: (X[0], 0, COL_W, r1), 2: (X[2], 0, COL_W, r1),
        3: (X[0], Y2, COL_W, r2), 4: (X[2], Y2, COL_W, r2),
        5: (X[1], 0, COL_W, r1 + GAP + r2),
        6: (X[0], Y3, COL_W, r3), 7: (X[1], Y3, COL_W, r3), 8: (X[2], Y3, COL_W, r3),
    }

    init_text = "%s\n**%s**" % (s["initiative"], model["initiative"])
    if model["preamble"]:
        init_text += "\n\n" + model["preamble"]
    hdr_h = est_height(init_text, 1300, 100)
    y_hdr = -70 - hdr_h
    half = (hdr_h - 10) // 2

    nodes = [{"id": new_id(used), "type": "group", "x": -20, "y": -20,
              "width": total_w + 40, "height": total_h + 40}]
    nodes += [
        {"id": new_id(used), "type": "text", "x": 0, "y": y_hdr, "width": 640, "height": 100,
         "text": "# " + s["title"]},
        {"id": new_id(used), "type": "text", "x": 680, "y": y_hdr, "width": 1300, "height": hdr_h,
         "text": init_text},
        {"id": new_id(used), "type": "text", "x": 2020, "y": y_hdr, "width": total_w - 2020,
         "height": half, "text": "%s %s" % (s["date"], date)},
        {"id": new_id(used), "type": "text", "x": 2020, "y": y_hdr + half + 10,
         "width": total_w - 2020, "height": half, "text": s["iteration"]},
    ]
    for n in range(1, 9):
        x, y, w, h = pos[n]
        node = {"id": new_id(used), "type": "text", "x": x, "y": y, "width": w, "height": h,
                "text": texts[n]}
        if not PENDING_RE.match(model["boxes"][n][1]):
            node["color"] = COLORS[n]
        nodes.append(node)
    footer = s["footer"] + ("\n%s [[%s]]" % (s["data"], link) if link else "")
    nodes.append({"id": new_id(used), "type": "text", "x": 0, "y": total_h + 50,
                  "width": 1500, "height": 90, "text": footer})

    ids = [n["id"] for n in nodes]
    assert len(ids) == len(set(ids)), "duplicate ids"
    return {"nodes": nodes, "edges": []}


def canvas_to_model(path):
    with open(path, encoding="utf-8") as f:
        data = json.load(f)
    boxes, initiative, preamble, skipped = {}, "", "", []
    for n in data.get("nodes", []):
        if n.get("type") != "text":
            continue
        t = n.get("text", "")
        m = re.match(r"^## (\d)\. ([^\n]+)(?:\n(.*))?$", t, re.S)
        if m and 1 <= int(m.group(1)) <= 8:
            num, rest = int(m.group(1)), (m.group(3) or "")
            # drop the guiding question the layout adds: an italic line followed by a blank line
            q = re.match(r"^\*[^*\n][^\n]*\*[ \t]*\n\n(.*)$", rest, re.S)
            body = (q.group(1) if q else rest).strip()
            if num in boxes:
                print("warning: box %d appears twice, keeping the first one" % num, file=sys.stderr)
                continue
            boxes[num] = (m.group(2).strip(), body)
        elif n.get("y", 0) < 0:
            hm = re.match(r"^[^\n]+\n\*\*(.+?)\*\*(?:\n\n(.*))?$", t, re.S)
            if hm and not initiative:
                initiative, preamble = hm.group(1).strip(), (hm.group(2) or "").strip()
        elif FOOTER_MARK not in t:
            skipped.append(t.strip().split("\n")[0][:40])
    missing = [i for i in range(1, 9) if i not in boxes]
    if missing:
        fail("boxes not found in the canvas: %s" % missing)
    if not initiative:
        fail("could not find the title-of-initiative node (a header node with the name in **bold**)")
    if skipped:
        print("note: %d node(s) that are not numbered boxes were not carried over: %s"
              % (len(skipped), "; ".join(skipped)), file=sys.stderr)
    return {"prefix": "", "initiative": initiative, "preamble": preamble, "boxes": boxes}


# ---------- commands ----------

def cmd_to_canvas(a):
    s = load_strings(a.strings)
    with open(a.md, encoding="utf-8") as f:
        model = parse_md(f.read())
    canvas = model_to_canvas(model, s, a.date or datetime.date.today().isoformat(), a.link)
    with open(a.canvas, "w", encoding="utf-8") as f:
        json.dump(canvas, f, ensure_ascii=False, indent=2)
    pending = sum(1 for n in range(1, 9) if PENDING_RE.match(model["boxes"][n][1]))
    print("canvas written: %d nodes, %d of 8 boxes filled" % (len(canvas["nodes"]), 8 - pending))


def cmd_to_md(a):
    model = canvas_to_model(a.canvas)
    prefix = a.h1_prefix
    if prefix is None:
        # keep the title prefix of the Markdown being replaced (it may be translated)
        try:
            with open(a.md, encoding="utf-8") as f:
                prefix = parse_md(f.read())["prefix"] or None
        except (OSError, SystemExit):
            prefix = None
    if prefix is None:
        name = a.md.replace("\\", "/").rsplit("/", 1)[-1].lower()
        prefix = "Main Lean Product Canvas" if name.startswith("main-") else "Lean Product Canvas"
    with open(a.md, "w", encoding="utf-8") as f:
        f.write(model_to_md(model, prefix))
    pending = sum(1 for n in range(1, 9) if PENDING_RE.match(model["boxes"][n][1]))
    print("markdown written: 8 boxes, %d filled" % (8 - pending))


def cmd_compare(a):
    with open(a.md, encoding="utf-8") as f:
        m1 = parse_md(f.read())
    m2 = canvas_to_model(a.canvas)
    same = True
    if m1["initiative"] != m2["initiative"]:
        same = False
        print("initiative: differs (md: %r, canvas: %r)" % (m1["initiative"], m2["initiative"]))
    if m1["preamble"] != m2["preamble"]:
        same = False
        print("preamble: differs")
    for n in range(1, 9):
        if m1["boxes"][n] == m2["boxes"][n]:
            print("box %d: same" % n)
        else:
            same = False
            what = "title" if m1["boxes"][n][0] != m2["boxes"][n][0] else "content"
            print("box %d: differs (%s)" % (n, what))
    sys.exit(0 if same else 1)


def main():
    p = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = p.add_subparsers(dest="cmd", required=True)
    c = sub.add_parser("to-canvas")
    c.add_argument("md"), c.add_argument("canvas")
    c.add_argument("--date"), c.add_argument("--link"), c.add_argument("--strings")
    c.set_defaults(fn=cmd_to_canvas)
    m = sub.add_parser("to-md")
    m.add_argument("canvas"), m.add_argument("md")
    m.add_argument("--h1-prefix")
    m.set_defaults(fn=cmd_to_md)
    k = sub.add_parser("compare")
    k.add_argument("md"), k.add_argument("canvas")
    k.set_defaults(fn=cmd_compare)
    a = p.parse_args()
    a.fn(a)


if __name__ == "__main__":
    main()
