#!/usr/bin/env python3
"""Build and read Impact-to-Outcome maps as Obsidian canvases (JSON Canvas 1.0).

The map is the one from Jeff Gothelf's "Why you should map outcomes to impact
metrics": impact metrics at the top, lagging outcomes under them, leading
outcomes under those, arrows pointing up (child -> parent), one tree per impact
metric side by side, a legend column on the left.

Layout only: every piece of text comes from the input JSON, so the script is
language-agnostic (the legend strings can be overridden with "labels").
See references/input-schema.md for the input format.

Usage:
    python3 -I impact_map_canvas.py build INPUT.json OUTPUT.canvas
    python3 -I impact_map_canvas.py read  INPUT.canvas [OUTPUT.json]
"""
import hashlib
import json
import math
import re
import sys

W = 260              # node width
H_GAP = 40           # horizontal gap between sibling nodes of the same tree
TREE_GAP = 110       # horizontal gap between nodes of different trees
V_GAP = 100          # vertical gap between layers
LEGEND_GAP = 160     # gap between the legend column and the first tree
CHAR_W = 9.0         # rough pixels per character, to estimate node height
LINE_H = 24
PAD = 36
PARA_GAP = 12

COLORS = {"impact": "5", "lagging": "3", "leading": "2"}   # cyan, yellow, orange
TYPES = ("impact", "lagging", "leading")

DEFAULT_LABELS = {
    "impact_title": "Impact",
    "impact_question": "How do we know that our strategy has succeeded?",
    "lagging_title": "Outcome (Lagging)",
    "lagging_question": "What behaviors can we observe/measure that indicate we're going to achieve our impact metric?",
    "leading_title": "Outcome (Leading)",
    "leading_question": "What behaviors lead to the behavior that we want to see above?",
    "pattern": "[WHO] [DOES WHAT]",
}


def fail(msg):
    sys.exit("impact_map_canvas.py: " + msg)


def warn(msg):
    print("warning: " + msg, file=sys.stderr)


def hid(key):
    return hashlib.sha1(key.encode("utf-8")).hexdigest()[:16]


def est_height(text):
    cpl = max(10, int((W - PAD) / CHAR_W))
    paragraphs = [p for p in text.split("\n\n")]
    lines = 0
    for p in paragraphs:
        for line in p.split("\n"):
            lines += max(1, math.ceil(len(line) / cpl))
    h = PAD + lines * LINE_H + PARA_GAP * (len(paragraphs) - 1)
    return max(80, int(math.ceil(h / 10.0) * 10))


# ---------------------------------------------------------------- text <-> node

def node_text(n):
    """Title in bold, then the metric in italics, then 'baseline -> target'."""
    parts = ["**" + n["text"].strip() + "**"]
    tail = []
    metric = (n.get("metric") or "").strip()
    baseline = (n.get("baseline") or "").strip()
    target = (n.get("target") or "").strip()
    if metric:
        tail.append("*" + metric + "*")
    if baseline or target:
        tail.append((baseline or "?") + " → " + (target or "?"))
    if tail:
        parts.append("\n".join(tail))
    return "\n\n".join(parts)


def parse_node_text(text):
    """Inverse of node_text. Falls back to the first line when hand-edited."""
    lines = [l.strip() for l in text.strip().split("\n") if l.strip()]
    if not lines:
        return {"text": ""}
    first = lines[0]
    m = re.match(r"^\*\*(.*)\*\*$", first)
    out = {"text": (m.group(1) if m else first).strip()}
    for l in lines[1:]:
        mi = re.match(r"^\*(?!\*)(.*)\*$", l)
        if mi and "metric" not in out:
            out["metric"] = mi.group(1).strip()
        elif "→" in l and "baseline" not in out and "target" not in out:
            b, t = [s.strip() for s in l.split("→", 1)]
            if b and b != "?":
                out["baseline"] = b
            if t and t != "?":
                out["target"] = t
    return out


# ------------------------------------------------------------------- validation

def validate(data):
    nodes = data.get("nodes")
    if not isinstance(nodes, list) or not nodes:
        fail('"nodes" must be a non-empty list')
    by_id = {}
    for n in nodes:
        for k in ("id", "type", "text"):
            if not n.get(k):
                fail("every node needs id, type and text: %r" % (n,))
        if n["type"] not in TYPES:
            fail("node %s: type must be one of %s" % (n["id"], ", ".join(TYPES)))
        if n["id"] in by_id:
            fail("duplicate node id: " + n["id"])
        if n["id"].startswith("legend-"):
            fail('node ids cannot start with "legend-" (reserved)')
        by_id[n["id"]] = n
    for n in nodes:
        feeds = n.get("feeds") or []
        if n["type"] == "impact":
            if feeds:
                fail("impact node %s cannot have \"feeds\" (it is a root)" % n["id"])
            continue
        if not feeds:
            fail("node %s (%s) must feed at least one node (\"feeds\")" % (n["id"], n["type"]))
        for p in feeds:
            if p not in by_id:
                fail("node %s feeds unknown node %s" % (n["id"], p))
            pt = by_id[p]["type"]
            if n["type"] == "lagging" and pt != "impact":
                fail("lagging node %s must feed an impact node, not %s (%s)" % (n["id"], p, pt))
            if n["type"] == "leading" and pt == "impact":
                fail("leading node %s must feed a lagging or leading node, not impact %s" % (n["id"], p))
    if not any(n["type"] == "impact" for n in nodes):
        fail("at least one impact node is required")
    # cycles
    state = {}

    def visit(i):
        if state.get(i) == 1:
            fail("cycle in \"feeds\" involving node " + i)
        if state.get(i) == 2:
            return
        state[i] = 1
        for p in by_id[i].get("feeds") or []:
            visit(p)
        state[i] = 2
    for i in by_id:
        visit(i)
    for pair in data.get("related") or []:
        if len(pair) != 2 or pair[0] not in by_id or pair[1] not in by_id or pair[0] == pair[1]:
            fail("\"related\" must be pairs of two different node ids: %r" % (pair,))
    # soft checks
    children = {i: [] for i in by_id}
    for n in nodes:
        for p in n.get("feeds") or []:
            children[p].append(n["id"])
    for n in nodes:
        if n["type"] == "impact" and not children[n["id"]]:
            warn("impact \"%s\" has no lagging outcomes yet" % n["text"])
        if n["type"] == "lagging" and not children[n["id"]]:
            warn("lagging outcome \"%s\" has no leading outcomes yet" % n["text"])
    return by_id, children


# ----------------------------------------------------------------------- layout

def place(desired, seps):
    """Positions closest to `desired` (least squares) keeping order and min separations."""
    n = len(desired)
    off = [0.0] * n
    for i in range(1, n):
        off[i] = off[i - 1] + seps[i]
    t = [desired[i] - off[i] for i in range(n)]
    blocks = []
    for v in t:
        blocks.append([v, 1])
        while len(blocks) > 1 and blocks[-2][0] / blocks[-2][1] > blocks[-1][0] / blocks[-1][1]:
            s, c = blocks.pop()
            blocks[-1][0] += s
            blocks[-1][1] += c
    q = []
    for s, c in blocks:
        q += [s / c] * c
    return [q[i] + off[i] for i in range(n)]


def layout(nodes, by_id, children):
    parents = {n["id"]: list(n.get("feeds") or []) for n in nodes}
    roots = [n["id"] for n in nodes if n["type"] == "impact"]

    # layer = longest path from any impact node
    depth = {}

    def d(i):
        if i not in depth:
            depth[i] = 0 if not parents[i] else 1 + max(d(p) for p in parents[i])
        return depth[i]
    for i in by_id:
        d(i)
    n_layers = max(depth.values()) + 1

    # DFS order + primary tree of every node
    order, root_of = {}, {}

    def dfs(i, r):
        if i in order:
            return
        order[i] = len(order)
        root_of[i] = r
        for c in children[i]:
            dfs(c, r)
    for ri, r in enumerate(roots):
        dfs(r, ri)
    for i in by_id:                      # nodes unreachable from a root cannot exist (validated)
        order.setdefault(i, len(order))
        root_of.setdefault(i, 0)

    layers = [[] for _ in range(n_layers)]
    for i in sorted(by_id, key=lambda k: order[k]):
        layers[depth[i]].append(i)

    # barycenter sweeps (trees stay contiguous: root_of is the primary key)
    def reorder(layer_idx, neighbours):
        idx = {}
        for L in layers:
            for p, i in enumerate(L):
                idx[i] = p
        keyed = []
        for pos, i in enumerate(layers[layer_idx]):
            ns = neighbours(i)
            bary = sum(idx[x] for x in ns) / len(ns) if ns else pos
            keyed.append((root_of[i], bary, pos, i))
        keyed.sort()
        layers[layer_idx] = [k[3] for k in keyed]
    for _ in range(4):
        for li in range(1, n_layers):
            reorder(li, lambda i: parents[i])
        for li in range(n_layers - 2, 0, -1):
            reorder(li, lambda i: children[i])

    def seps_for(layer):
        out = [0.0]
        for a, b in zip(layer, layer[1:]):
            out.append(W + (TREE_GAP if root_of[a] != root_of[b] else H_GAP))
        return out

    x = {}
    for layer in layers:
        pos = 0.0
        for k, i in enumerate(layer):
            pos += seps_for(layer)[k] if k else 0
            x[i] = pos
    for _ in range(10):
        for li in range(1, n_layers):
            L = layers[li]
            des = [sum(x[p] for p in parents[i]) / len(parents[i]) for i in L]
            for i, v in zip(L, place(des, seps_for(L))):
                x[i] = v
        for li in range(n_layers - 2, -1, -1):
            L = layers[li]
            des = [sum(x[c] for c in children[i]) / len(children[i]) if children[i] else x[i] for i in L]
            for i, v in zip(L, place(des, seps_for(L))):
                x[i] = v
    return layers, x, depth


# ------------------------------------------------------------------------ build

def build(data):
    by_id, children = validate(data)
    nodes = data["nodes"]
    labels = dict(DEFAULT_LABELS)
    labels.update(data.get("labels") or {})
    legend = data.get("legend", True)

    layers, x, depth = layout(nodes, by_id, children)

    text = {n["id"]: node_text(n) for n in nodes}
    height = {i: est_height(t) for i, t in text.items()}

    legend_nodes = []
    if legend:
        lg = {
            "impact": "**%s**\n\n*%s*" % (labels["impact_title"], labels["impact_question"]),
            "lagging": "**%s**\n\n*%s*\n\n%s" % (labels["lagging_title"], labels["lagging_question"], labels["pattern"]),
            "leading": "**%s**\n\n*%s*\n\n%s" % (labels["leading_title"], labels["leading_question"], labels["pattern"]),
        }
        legend_nodes = [("legend-" + t, t, lg[t]) for t in TYPES]

    # vertical bands: one per layer
    band_h = []
    for li, L in enumerate(layers):
        hs = [height[i] for i in L]
        if legend and li < 3:
            hs.append(est_height(legend_nodes[li][2]))
        band_h.append(max(hs))
    band_top, y = [], 0
    for h in band_h:
        band_top.append(y)
        y += h + V_GAP

    min_left = min(x[i] for i in x) - W / 2
    x0 = (W + LEGEND_GAP if legend else 0) - min_left

    out_nodes, out_edges = [], []
    for li, L in enumerate(layers):
        for i in L:
            n = by_id[i]
            h = height[i]
            out_nodes.append({
                "id": hid("node:" + i), "type": "text", "text": text[i],
                "x": int(round(x[i] + x0 - W / 2)),
                "y": int(round(band_top[li] + (band_h[li] - h) / 2)),
                "width": W, "height": h, "color": COLORS[n["type"]],
            })
    if legend:
        for li, (lid, t, lt) in enumerate(legend_nodes):
            if li >= len(layers):
                break
            h = est_height(lt)
            out_nodes.append({
                "id": lid, "type": "text", "text": lt, "x": 0,
                "y": int(round(band_top[li] + (band_h[li] - h) / 2)),
                "width": W, "height": h, "color": COLORS[t],
            })

    for n in nodes:
        for p in n.get("feeds") or []:
            out_edges.append({
                "id": hid("edge:%s>%s" % (n["id"], p)), "fromNode": hid("node:" + n["id"]),
                "fromSide": "top", "toNode": hid("node:" + p), "toSide": "bottom", "toEnd": "arrow",
            })
    for a, b in data.get("related") or []:
        if depth[a] == depth[b]:
            left, right = (a, b) if x[a] <= x[b] else (b, a)
            fs, ts, fn, tn = "right", "left", left, right
        else:
            upper, lower = (a, b) if depth[a] < depth[b] else (b, a)
            fs, ts, fn, tn = "bottom", "top", upper, lower
        out_edges.append({
            "id": hid("rel:%s<>%s" % (a, b)), "fromNode": hid("node:" + fn), "fromSide": fs,
            "toNode": hid("node:" + tn), "toSide": ts, "fromEnd": "arrow", "toEnd": "arrow",
        })
    return {"nodes": out_nodes, "edges": out_edges}


# ------------------------------------------------------------------------- read

def read(canvas):
    """Rebuild the input model from a canvas (drawn by this script or by hand)."""
    nodes = [n for n in canvas.get("nodes", []) if n.get("type") == "text" and not str(n.get("id", "")).startswith("legend-")]
    others = [n for n in canvas.get("nodes", []) if n.get("type") != "text"]
    ids = {n["id"] for n in nodes}
    feeds, related = {i: [] for i in ids}, []
    for e in canvas.get("edges", []):
        a, b = e.get("fromNode"), e.get("toNode")
        if a not in ids or b not in ids:
            continue
        if e.get("fromEnd") == "arrow" and e.get("toEnd", "arrow") == "arrow":
            related.append((a, b))
        else:
            feeds[a].append(b)
    has_in = {p for ps in feeds.values() for p in ps}
    connected = {i for i in ids if feeds[i] or i in has_in} | {i for pair in related for i in pair}
    loose = [n for n in nodes if n["id"] not in connected]
    tree = [n for n in nodes if n["id"] in connected]

    def pos(n):
        return (n.get("y", 0), n.get("x", 0))
    roots = {n["id"] for n in tree if not feeds[n["id"]]}
    typ = {}
    for n in tree:
        i = n["id"]
        if i in roots:
            typ[i] = "impact"
        elif any(p in roots for p in feeds[i]):
            typ[i] = "lagging"
        else:
            typ[i] = "leading"
    counters = {"impact": 0, "lagging": 0, "leading": 0}
    prefix = {"impact": "i", "lagging": "l", "leading": "e"}
    newid = {}
    for t in TYPES:
        for n in sorted([n for n in tree if typ[n["id"]] == t], key=lambda n: (n.get("x", 0), n.get("y", 0))):
            counters[t] += 1
            newid[n["id"]] = "%s%d" % (prefix[t], counters[t])
    model_nodes = []
    for t in TYPES:
        for n in sorted([n for n in tree if typ[n["id"]] == t], key=lambda n: (n.get("x", 0), n.get("y", 0))):
            item = {"id": newid[n["id"]], "type": t}
            item.update(parse_node_text(n.get("text", "")))
            if t != "impact":
                item["feeds"] = [newid[p] for p in feeds[n["id"]]]
            model_nodes.append(item)
    model = {"nodes": model_nodes}
    if related:
        model["related"] = [[newid[a], newid[b]] for a, b in related]
    notes = []
    if loose:
        notes.append("%d node(s) not connected to the tree (they will be lost if the canvas is regenerated): %s" % (
            len(loose), "; ".join(repr(parse_node_text(n.get("text", ""))["text"]) for n in loose)))
    if others:
        notes.append("%d non-text node(s) (files, links, groups) are not part of the model and will be lost on regeneration" % len(others))
    return model, notes


# ------------------------------------------------------------------------- main

def load(path):
    try:
        with open(path, encoding="utf-8") as f:
            return json.load(f)
    except (OSError, ValueError) as e:
        fail("cannot read %s: %s" % (path, e))


def main():
    a = sys.argv[1:]
    if len(a) >= 3 and a[0] == "build" and len(a) == 3:
        canvas = build(load(a[1]))
        with open(a[2], "w", encoding="utf-8") as f:
            json.dump(canvas, f, ensure_ascii=False, indent="\t")
            f.write("\n")
        kinds = {t: 0 for t in TYPES}
        for n in load(a[1])["nodes"]:
            kinds[n["type"]] += 1
        print("wrote %s: %d impact, %d lagging, %d leading; %d canvas nodes, %d edges" % (
            a[2], kinds["impact"], kinds["lagging"], kinds["leading"], len(canvas["nodes"]), len(canvas["edges"])))
    elif len(a) in (2, 3) and a[0] == "read":
        model, notes = read(load(a[1]))
        for n in notes:
            warn(n)
        s = json.dumps(model, ensure_ascii=False, indent=2) + "\n"
        if len(a) == 3:
            with open(a[2], "w", encoding="utf-8") as f:
                f.write(s)
            print("wrote %s: %d nodes" % (a[2], len(model["nodes"])))
        else:
            sys.stdout.write(s)
    else:
        fail("usage: impact_map_canvas.py build INPUT.json OUTPUT.canvas | read INPUT.canvas [OUTPUT.json]")


if __name__ == "__main__":
    main()
