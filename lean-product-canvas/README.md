# Lean Product Canvas (Claude Code skill)

Skill for filling in, selecting between options for, and reviewing the 8 boxes of the [Lean Product Canvas](https://jeffgothelf.com/blog/the-lean-product-canvas/) by talking to Claude — no copy-pasting prompts by hand. It manages three related artifacts per product: a single **main canvas** (`main-lean-product-canvas <Product>.md`), any number of **problem canvases** (`lean-product-canvas-<problem-name>.md`), one per experiment within that product, and a backlog of **problem records** (one Business Problem Statement per identified problem, in the product's problems folder). See [Main canvas vs. problem canvas](#main-canvas-vs-problem-canvas) and [Problem records](#problem-records-identified-problems) below.

Part of the **[Sense & Respond Product Discovery kit](../README.md)**.

Self-contained: all the logic and prompts live inside this folder, it doesn't depend on any other file in the project where it's installed. Output language follows the kit-wide rule — see [Language](#language) below.

## Installation

### Option 1: with `npx skills` (recommended)

Using the [`skills`](https://github.com/vercel-labs/skills) CLI, which installs into whatever agent you're using (Claude Code, Cursor, Codex, and many more):

```bash
npx skills add fzuppa/sense-and-respond-discovery-kit/lean-product-canvas
```

To install it at the user level (available in all your projects) instead of just this one:

```bash
npx skills add fzuppa/sense-and-respond-discovery-kit/lean-product-canvas -g
```

`npx skills add` installs the skill (`SKILL.md` + `references/` + `scripts/`) — that's all this skill needs, since it's auto-triggered by Claude recognizing Lean Product Canvas requests in conversation. No slash command to register.

### Option 2: manual

1. Copy this whole folder (`SKILL.md`, `README.md`, `references/`, and `scripts/`) into Claude Code's skills folder:
   - **For a single project:** paste it into `.claude/skills/lean-product-canvas/` at that project's root.
   - **For all your projects:** paste it into `~/.claude/skills/lean-product-canvas/` (user-level skills).
2. No build step. The canvas conversion needs `python3` (standard library only).

## Usage

Just ask Claude, in natural language, something like:

- "Help me fill in the main Lean Product Canvas for product X"
- "Help me fill in a Lean Product Canvas for problem Y"
- "Generate options for box 1"
- "I have several options for box 5, help me choose"
- "Review my box 3"
- "I want to write a new problem for product X" / "List the problems of product X"
- "Turn the Markdown of product X into a canvas" / "Convert the canvas back to Markdown"

The skill guides you box by box, asking for the information it needs, showing you the generated results, and asking for your confirmation before saving each summary to the canvas file.

The first time it's used for a product, it creates that product's main canvas. From then on, requests about a specific problem/experiment inside that product create or resume a problem canvas instead — see [Main canvas vs. problem canvas](#main-canvas-vs-problem-canvas).

The first time it's used in a new project, it'll ask which folder to save canvas files in. Subsequent uses reuse that same folder automatically (it finds it by looking for existing `main-lean-product-canvas *.md` / `.canvas` and `lean-product-canvas-*.md` / `.canvas` files).

## Markdown, Canvas, or both

When you start a new canvas, Claude asks how you want to keep it:

| Choice | What you get |
|---|---|
| **Markdown** | `<name>.md`, the classic file. |
| **Canvas** | `<name>.canvas`, an [Obsidian canvas](https://obsidian.md/canvas) laid out like the official Lean Product Canvas (v3): boxes 1, 3, 6 on the left, 5 and 7 in the middle, 2, 4, 8 on the right, with the color coding of the official version (boxes 1-4 red, 5 cyan, 6-8 green; a box that is still pending stays uncolored). |
| **Both** | The two files side by side with the same base name. The `.md` is the source of truth and the canvas is regenerated from it after each saved box. |

You can also **convert at any time**: "turn the Markdown into a canvas" or "convert the canvas to Markdown". Box titles and text are copied verbatim in both directions, so a round trip changes nothing. Claude never overwrites a file silently: if the target exists, it shows which boxes differ and asks first. In **Both** mode, if you edited one of the files by hand, it detects the difference before saving the next box and asks which version wins.

What the canvas doesn't carry: box positions and sizes you change in Obsidian are lost when it is regenerated, extra nodes you add are not carried back to the Markdown, and the header's `Date:` is the generation date (`Iteration:` stays blank). Node heights are estimated from the text length, so a very long box may need a manual resize. Problem records are always Markdown.

The conversion is done by [`scripts/lpc_canvas.py`](scripts/lpc_canvas.py) (`to-canvas`, `to-md`, `compare`), Python standard library only. Claude runs it for you; you can also run it by hand:

```bash
python3 -I scripts/lpc_canvas.py to-canvas "main-lean-product-canvas Acme.md" "main-lean-product-canvas Acme.canvas"
python3 -I scripts/lpc_canvas.py to-md "main-lean-product-canvas Acme.canvas" "main-lean-product-canvas Acme.md"
python3 -I scripts/lpc_canvas.py compare "main-lean-product-canvas Acme.md" "main-lean-product-canvas Acme.canvas"
```

## Main canvas vs. problem canvas

This skill produces two kinds of files for the same 8-box methodology:

- **Main canvas** (`main-lean-product-canvas <Product>.md`) — exactly one per product. Captures the overarching opportunity: why the product should exist, its top-level outcomes, its core audience, and its primary hypothesis.
- **Problem canvas** (`lean-product-canvas-<problem-name>.md`) — one per specific problem/experiment inside that product, created after the main canvas exists. Its Box 3 (Proto-Personas) is offered for reuse from the main canvas instead of being generated from scratch, and its Box 6/8 are scoped to that specific experiment rather than the whole product.

Box 1 also supports two formats depending on the situation: the classic **Business Problem Statement** (for an existing product/situation) or the **Business Opportunity Statement** (for something genuinely new, with no baseline) — see `SKILL.md` for how the skill picks between them.

## Problem records (identified problems)

When you want to write down a problem of a product that already exists, Claude interviews you one question at a time — what the product was designed to achieve, how you observed it isn't meeting that goal, what it costs the business, what customer behavior would change if it were solved — and writes a **Business Problem Statement** plus the evidence and open assumptions behind it. The result is saved as `<problem-name>.md` in the product's problems folder, next to the canvas files (e.g. `Products/Acme/Problems/`).

- **The folder name follows the output language:** `Problems` in English, `Problemas` in Spanish, and so on. If a problems folder already exists in another language, it's reused — it's recognized by `type: problem` in its files' frontmatter.
- Each record has a `status`: `identified`, `selected` (promoted to a problem canvas, whose Box 1 starts pre-filled with the record's statement) or `discarded`.
- Ask "list the problems" to see the backlog, or let Claude help you pick which one to work on first with the Box 1 Selection prompt.

Always a Business Problem Statement — records are for products that already exist. See `SKILL.md` → "Capturing a problem" and `references/capture_problem.md`.

## MVPs (running an experiment)

Once a canvas's Box 8 (Least Amount of Work to Learn It) is filled in, you can ask Claude to turn it into an **MVP** — a folder that tracks the actual execution of that experiment. MVPs live in a shared `MVPs/` folder next to the canvas files (e.g. `Products/Acme/MVPs/`), numbered sequentially and named after the risk they test, e.g. `MVPs/#1-Some-Risk-From-Box-7/`. Each MVP folder starts with a single `Summary.md` recording the source canvas's Box 7 (what to learn) and Box 8 (how) — later, whoever runs the experiment adds their own results file. See `SKILL.md` → "Creating an MVP" for the exact naming/derivation rules.

## Language

Output language follows this rule, in order:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the current conversation.
3. If still unclear, ask before writing.

The skill's own instructions (`SKILL.md`, this README, the prompts in `references/`) are written in English — that doesn't change; only the **content it generates** (the canvas file, the conversation) adapts to the detected language.

## Structure

```
lean-product-canvas/
├── SKILL.md              # instructions Claude follows
├── README.md              # this file
├── scripts/
│   └── lpc_canvas.py                            # Markdown <-> Obsidian canvas conversion
└── references/
    ├── box1_business_problem_statement.md
    ├── capture_problem.md                       # interview guide for problem records
    ├── box1_business_opportunity_statement.md   # alternate Box 1, for brand-new products
    ├── box2_business_outcomes.md
    ├── box3_users_proto_personas.md
    ├── box4_user_outcomes_benefits.md
    ├── box5_solutions_features.md
    ├── box6_hypotheses.md
    ├── box7_most_important_thing_to_learn.md
    └── box8_least_amount_of_work_to_learn_it.md
```

Each file in `references/` contains the Generation, Selection (when applicable), and Review prompts for that canvas box.
