---
name: lean-product-canvas
description: "Use when working on a Lean Product Canvas (LPD): filling in a box through guided questions, choosing between generated options, or reviewing an already-written box. Covers the product's main canvas, per-problem canvases for experiments within it, and a backlog of identified problems (problem records, each written as a Business Problem Statement). Triggers: 'Lean Product Canvas', 'LPD', 'box 1..8', 'business problem statement', 'business opportunity statement', 'business outcomes', 'proto-persona', 'JTBD', 'canvas hypotheses', 'main canvas', 'help me fill in the canvas', 'review my box', 'I have several options for box', 'write/log/record a problem', 'new problem for <product>', 'problems backlog', 'list the problems'. A canvas can be kept as Markdown, as an Obsidian canvas (.canvas) laid out like the official Lean Product Canvas, or both, and converted from one to the other. Also triggers on: 'as a canvas', 'canvas view', 'draw the lean product canvas', 'turn the markdown into a canvas', 'convert the canvas to markdown'."
---

# Lean Product Canvas (LPD)

Guide for filling in, selecting between options for, and reviewing the 8 boxes of the [Lean Product Canvas](https://jeffgothelf.com/blog/the-lean-product-canvas/) — either for a product's **main canvas** or for a specific **problem/experiment** within that product — using the prompts packaged in `references/` (relative to this file). Self-contained skill: it doesn't depend on any folder outside the skill itself, only on the project where it's invoked, to save its results. The only code it ships is `scripts/lpc_canvas.py` (Python standard library), used to convert between Markdown and an Obsidian canvas — see "Output format: Markdown, Canvas, or both".

This skill is part of the **Sense & Respond Product Discovery kit**. It's typically used after `market-research` has produced context on users/market, and feeds the canvas boxes (Users, Solutions) from that research when available.

## Output language

Follow these rules, in order:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the current conversation (the language the user is writing in).
3. If still unclear, ask before writing.

The box titles and prompt templates in `references/` are written in English — treat them as the canonical version and translate them naturally into the detected output language, both when talking to the user and when writing to the canvas file. When translating, keep the required format's structure intact (bracketed placeholders, overall sentence shape) — e.g. Box 1's statement or Box 2's `[Who][Does What][To What Extent]` format.

**Canvas principle (repeat it when relevant):** AI-generated outputs are assumptions that must be validated, not facts to accept.

## The 8 boxes

| # | Section name in the file | Prompts file | Available modes |
|---|------|---------------------|--------------------|
| 1 | Business Problem Statement *(or Business Opportunity Statement — see "Choosing the Box 1 format" below)* | `box1_business_problem_statement.md` / `box1_business_opportunity_statement.md` | Generate, Select, Review |
| 2 | Business Outcomes | `box2_business_outcomes.md` | Generate, Select, Review |
| 3 | Users (Proto-Personas) | `box3_users_proto_personas.md` | Generate, Review |
| 4 | User Outcomes & Benefits (JTBD) | `box4_user_outcomes_benefits.md` | Generate, Review |
| 5 | Solutions / Features | `box5_solutions_features.md` | Generate, Select, Review |
| 6 | Hypotheses | `box6_hypotheses.md` | Generate, Select, Review |
| 7 | Most Important Thing to Learn | `box7_most_important_thing_to_learn.md` | Generate, Review |
| 8 | Least Amount of Work to Learn It | `box8_least_amount_of_work_to_learn_it.md` | Generate, Select, Review |

Use the English section name above as the canonical title for the `## N. <name>` header in the canvas file, translated into the detected output language when that isn't English (e.g. in Spanish: "1. Enunciado del Problema de Negocio (Business Problem Statement)" — keep the original English name in parentheses so the section stays traceable across languages). When the output language is English, just use the plain English name, no parentheses needed.

All files live in `references/`, relative to this file (SKILL.md). Boxes 3, 4, and 7 don't have a Selection prompt — they produce a single synthesized artifact, not multiple options to compare — if the user asks to "select" for one of these boxes, explain this and offer to refine the result with targeted questions instead, or move to Review.

## Related artifacts: main canvas, problem canvases, and problem records

This skill produces three kinds of files for the same underlying methodology:

- **Main canvas** — exactly **one per product**. Captures the overarching opportunity: why this product should exist, its top-level outcomes, its core audience, and the primary hypothesis driving it.
- **Problem canvas** — **one per specific problem/experiment** being tackled inside that product, created after the main canvas exists. Each one works through the same 8 boxes, but scoped to that particular problem instead of the whole product.
- **Problem record** — **one per identified problem** of an existing product, stored in the product's problems folder (see "Capturing a problem" below). It's a lightweight backlog entry: a Business Problem Statement plus the evidence and assumptions behind it, not an 8-box canvas. A record can later be promoted to a problem canvas, which starts with Box 1 already written.

### File naming

- Main canvas: `main-lean-product-canvas <Product>.md` (e.g. `main-lean-product-canvas Acme Wellness.md`)
- Problem canvas: `lean-product-canvas-<problem-name>.md` (e.g. `lean-product-canvas-onboarding-drop-off.md`)
- Problem record: `<problem-name>.md` inside the problems folder (e.g. `Problems/onboarding-drop-off.md`). `<problem-name>` is short, kebab-case, in the output language.

Main and problem canvases can also exist as an Obsidian canvas, with the same base name and the extension `.canvas` (e.g. `main-lean-product-canvas Acme Wellness.canvas`) — see "Output format: Markdown, Canvas, or both". Problem records are always Markdown.

Main and problem canvases live in the same boards folder (see "Finding or defining the boards folder" below). The problems folder is a subfolder of it.

### Deciding which one to create or work on

1. **Identify the product** the user is talking about (ask if unclear).
2. **Look for an existing main canvas** for that product (`main-lean-product-canvas <Product>.md` or `.canvas`) in the boards folder (a canvas moved into an MVP folder counts, see "Creating an MVP").
   - **Not found** → this is the first canvas for this product. It becomes the **main canvas**.
   - **Found** → the main canvas already exists.
     - If the user is explicitly asking to revisit/review the main canvas itself, work on that file.
     - Otherwise, this is a **problem canvas**: ask for the name of the problem/experiment (if not already clear from the conversation) and create/resume `lean-product-canvas-<problem-name>.md`.
3. Either way, the file's internal structure (the 8 boxes, `_Pending_` scaffold, box-by-box flow) is the same — only the file name and the per-box nuances below differ.

### Finding or defining the boards folder

This skill doesn't assume any fixed folder structure — it adapts to whatever project it's used in:

1. **Look for a folder already in use.** Before asking anything, search the current project for existing files matching `main-lean-product-canvas *.md` / `.canvas` or `lean-product-canvas-*.md` / `.canvas` (e.g. with `find . \( -iname "main-lean-product-canvas *.md" -o -iname "lean-product-canvas-*.md" -o -iname "main-lean-product-canvas *.canvas" -o -iname "lean-product-canvas-*.canvas" \)`). If you find any, the folder containing them is the boards folder — use it without asking again. The exception: a canvas that was moved into an MVP folder (`<boards folder>/MVPs/#N-…/`, see "Creating an MVP") still belongs to the boards folder that contains `MVPs/`, so when a match sits inside an `MVPs/#N-…/` folder, the boards folder is the parent of `MVPs/`, not the MVP folder. This makes the folder choice persist automatically once a project has used the skill before.
2. **If none is found** (first use of the skill in this project), ask the user which folder to save this project's canvas files in (suggest `Lean Product Canvas Boards/` as a default if they have no preference). Create the folder if it doesn't exist.

The problems folder lives inside the boards folder (e.g. `Products/Acme/Problems/`). Its name follows the output-language rule and is the translation of "Problems" (English: `Problems`, Spanish: `Problemas`, Portuguese: `Problemas`, French: `Problèmes`, …). Because the language can differ between sessions, **look for an existing problems folder before creating one**: any subfolder of the boards folder whose files have `type: problem` in their frontmatter, whatever language its name is in, is the problems folder — reuse it as-is and never create a second one or rename it. Only when there's none, create it with the name in the current output language, and do it the first time a problem is saved.

### The file scaffold

With the folder determined, each canvas file (main or problem) has this same structure (shown here with English section names — translate per the output-language rule above):

```markdown
# Main Lean Product Canvas — <Product>

## 1. Business Problem Statement
_Pending_

## 2. Business Outcomes
_Pending_

## 3. Users (Proto-Personas)
_Pending_

## 4. User Outcomes & Benefits (JTBD)
_Pending_

## 5. Solutions / Features
_Pending_

## 6. Hypotheses
_Pending_

## 7. Most Important Thing to Learn
_Pending_

## 8. Least Amount of Work to Learn It
_Pending_
```

A problem canvas uses the identical scaffold, just titled `# Lean Product Canvas — <Problem>` instead.

- **Product / problem name:** if it isn't clear from the conversation context, ask "What's the product called?" (for a main canvas) or "What's this problem/experiment called?" (for a problem canvas) before creating or looking up the file.
- **Creation:** if the corresponding file doesn't exist yet in the boards folder determined above, create it with the full scaffold above (all 8 boxes as `_Pending_`) before filling in the first box. If the user chose a canvas (see "Output format: Markdown, Canvas, or both"), the scaffold is created as a `.canvas` as well, or only as a `.canvas` through a scratch working copy.
- **Content of each section:** only the **concise summary** of that box (see below) — not the full detail of the conversation, no confidence levels, no lists of pending research. That detail lives in the conversation, not in the file.

### Per-box differences between the main canvas and a problem canvas

The 8 boxes mean the same thing in both artifacts, scoped differently:

- **Box 1 (Business Problem Statement / Business Opportunity Statement):** in either artifact, first determine which format fits — see "Choosing the Box 1 format" below.
- **Box 2 (Business Outcomes):** in the **main canvas**, these are the product's high-level/strategic outcomes (company- or product-wide metrics). In a **problem canvas**, they're scoped to that specific problem/experiment.
- **Box 3 (Users / Proto-Personas):** in the **main canvas**, these are the product's core personas, meant to be reused. In a **problem canvas**, before generating new personas, check whether the product's main canvas already has Box 3 filled in — if so, show it to the user and offer to reuse it as-is (or adapt it) instead of generating from scratch.
- **Box 6 (Hypotheses):** in the **main canvas**, this is the overarching hypothesis for the whole product opportunity. In a **problem canvas**, it's the hypothesis for that specific experiment.
- **Box 8 (Least Amount of Work to Learn It):** in the **main canvas**, the output of this box identifies the direction for the product's first MVP/experiment. Depending on scope, that can become either the seed for a new problem canvas (when the experiment needs its own full canvas — new users, new hypotheses, etc.) or, more directly, an **MVP folder** (see "Creating an MVP" below) when the experiment can just be run and documented without a new canvas. In a **problem canvas**, it's the concrete experiment for that problem, and the same MVP-creation option applies there too.
- **Boxes 4, 5, 7:** no structural difference — just naturally scoped to the whole product (main canvas) or to the specific problem (problem canvas).

### Choosing the Box 1 format

Before generating Box 1 (in either the main canvas or a problem canvas), ask the user — unless already obvious from context — whether this product/situation already exists in some form, or is genuinely new with no existing baseline to observe:

- **Existing product/situation** → use `box1_business_problem_statement.md` (Business Problem Statement).
- **Genuinely new, no baseline** → use `box1_business_opportunity_statement.md` (Business Opportunity Statement).

Per Gothelf's own guidance: try the Business Problem Statement first — most situations, even ones that feel "new," turn out to be improving something that already exists. Only use the Business Opportunity Statement if the Problem Statement genuinely doesn't fit.

This choice doesn't apply to problem records: they're always Business Problem Statements, because a record describes a problem of a product that already exists (see "Capturing a problem").

## Output format: Markdown, Canvas, or both

Any canvas (main or problem) can be kept in one of three forms. Problem records are always Markdown and don't follow this section.

| Choice | Files | Source of truth |
|---|---|---|
| **Markdown** | `<name>.md` | the `.md` |
| **Canvas** | `<name>.canvas` | the `.canvas` |
| **Both** | `<name>.md` and `<name>.canvas`, side by side, same base name | the `.md`; the canvas is regenerated from it |

The `.canvas` is an Obsidian canvas (JSON Canvas 1.0) laid out like the official Lean Product Canvas (v3): boxes 1, 3, 6 on the left; 5 (tall) and 7 in the middle; 2, 4, 8 on the right; a header with title, initiative, date and iteration; a footer with the license credit. Boxes 1-4 are red, 5 cyan, 6-8 green, as in the official color-coded version; a box that is still pending stays uncolored, so progress is visible. Each box holds its title, the official guiding question in italics, and the box content.

### When to ask, and how to detect the choice

- **New canvas** (neither `<name>.md` nor `<name>.canvas` exists): ask once, before the research-scope question: *"Do you want this canvas as Markdown, as a canvas, or both?"* Don't assume a default; you may mention what the product's other canvases use. The answer applies to that canvas for the rest of the work, so don't ask again.
- **Existing canvas**: infer it from the files, don't ask. Only `.md` → Markdown. Only `.canvas` → Canvas. Both → Both.
- The user can change their mind at any time ("also give me the canvas", "I only want the canvas now"): that's a conversion, see below. Never delete the user's files to match a choice; if they want only one form, they delete the other.

### The conversion script

`scripts/lpc_canvas.py` (relative to this file; Python standard library) converts between the two forms. Run it with `python3 -I`, from a neutral directory, passing paths as arguments:

| Command | What it does |
|---|---|
| `to-canvas MD CANVAS [--date YYYY-MM-DD] [--link NAME] [--strings FILE]` | Lays the Markdown out as a canvas. `--link` adds a `[[link]]` to the Markdown in the footer (pass the `.md` base name in Both mode, omit it in Canvas mode). `--date` defaults to today. |
| `to-md CANVAS MD [--h1-prefix TEXT]` | Writes the Markdown back from the canvas. If `MD` already exists its title prefix is kept; for a new file it defaults to "Main Lean Product Canvas" (file name starting with `main-`) or "Lean Product Canvas". |
| `compare MD CANVAS` | Prints, box by box, whether the two agree. Exit code 0 if identical, 1 if they differ. |

Box titles and content are copied verbatim both ways, so a canvas → Markdown → canvas round trip changes nothing. Both commands **overwrite their output file**: you decide when that is OK, following the rules below.

**Output language.** The box titles come from the Markdown headings, already translated. When the output language isn't English, also translate the canvas chrome: write a small JSON file in a scratch directory with the keys you need (`initiative`, `date`, `iteration`, `data`, and `questions` with keys `"1"`..`"8"` for the guiding questions) and pass it with `--strings`. Anything you leave out stays in English. `to-md` doesn't need it: it drops the guiding question whatever its language.

### How each choice works

- **Markdown:** exactly as described in the rest of this skill.
- **Both:** the `.md` is the source of truth.
  1. Before saving a box, run `compare`. If the files differ, someone edited one of them by hand: show which boxes differ and ask which version wins (canvas → Markdown with `to-md`, or Markdown → canvas with `to-canvas`). Never decide silently, and never write the new box until that is resolved.
  2. Save the box to the `.md` following the usual confirmation rules.
  3. Regenerate the canvas with `to-canvas` (with `--link`).
- **Canvas only:** there is no `.md` in the project. Keep a **working copy** of the Markdown in a scratch directory outside the project (a temp dir), named after the canvas so the title prefix is right (`main-lean-product-canvas <Product>.md`).
  - **New canvas:** write the scaffold (all boxes `_Pending_`) to the working copy and run `to-canvas` to create the canvas.
  - **Every time you read or save a box:** first refresh the working copy from the canvas with `to-md` (this picks up anything the user changed by hand), apply the change to the working copy, then run `to-canvas`. This is also how you read boxes you need as context (Box 3 for reuse, Box 7 and 8 for an MVP).
  - Never leave the working copy inside the user's project.

### Converting an existing canvas

On requests like "turn the markdown into a canvas" or "convert the canvas to markdown":
1. Find the source file. If only one form exists, that's the source. If both exist, run `compare` and ask which one is the source.
2. If the target file doesn't exist, convert and report. If it exists, run `compare`, show which boxes differ, and ask before overwriting.
3. Report where the file is. After a Markdown → canvas conversion the canvas is in **Both** mode from then on.

### What the canvas does not carry

Say this when it matters (the first conversion, or when the user edits the canvas by hand):
- **Layout is regenerated.** Moving or resizing boxes in Obsidian is lost the next time the canvas is regenerated. Text edits are not lost (see the rules above), but they only reach the `.md` when it is refreshed with `to-md`.
- **Extra nodes** the user adds to the canvas (notes, links) are not carried back to the Markdown. `to-md` prints a note listing them.
- **The `Date:` in the header** is the generation date, and `Iteration:` is left blank: the Markdown doesn't store either.
- **Rendering is not checked.** Node heights are estimated from the text length; a very long box may need a manual resize in Obsidian.

## Capturing a problem

Use this when the user wants to write down, log, or record a problem of a product that already exists ("I want to write a new problem for Acheev", "log this problem", "new problem for X"). It produces a **problem record** in the product's problems folder — not a canvas. Always a Business Problem Statement (`references/box1_business_problem_statement.md`); don't ask which Box 1 format to use. If the situation described has no existing product or service to observe, say that capturing doesn't fit and offer to start a canvas instead, where the Opportunity Statement is available.

### Flow

1. **Identify the product** (ask if unclear) and resolve the boards folder and problems folder per "Finding or defining the boards folder". If the product has no boards folder yet, resolve it by that section's rules.
2. **Interview the user, one question at a time**, following `references/capture_problem.md`. The questions map one-to-one onto the slots of the Business Problem Statement; don't draft anything until every slot has an answer. If the user's description is a solution in disguise ("they need a report"), ask what problem that solution would solve before continuing. If an answer is missing or unsure, record it as unknown/`unverified` — never invent evidence.
3. **Draft the statement** in the exact format of the Box 1 template, translated per the output-language rule, and show it to the user together with the evidence table and the open assumptions. Offer a Box 1 Review (`## REVIEW PROMPT`) before saving; run it only if the user accepts.
4. **Confirm the problem name** (short, kebab-case) before creating the file — never create it silently with a name the user hasn't seen.
5. **Save** to `<problems folder>/<problem-name>.md` with the format below. If a file with that name already exists, show the old content next to the new and ask before overwriting.
6. **Suggest the next step:** capture another problem, or promote this one to a canvas (see below).

### Problem record format

Frontmatter keys and values stay in English (`type`, `status`, `identified`…) so the folder can be found and filtered regardless of language; the headings and everything else are translated per the output-language rule (shown here in English):

```markdown
---
type: problem
product: <Product>
status: identified
date: <YYYY-MM-DD>
---

# <Problem name>

## Business Problem Statement
<statement in the exact Box 1 format>

## Who suffers it
<persona/segment, and the situation in which it shows up>

## Evidence
| Signal | Provenance | Source |
|---|---|---|
| … | real / survey / secondary / synthetic / unverified | <who, when, file> |

## Open assumptions
- <what has to be true for this to be the real problem, and what would test it>
```

Unlike a canvas box, a record **does** keep evidence and assumptions: that's what makes the backlog usable when deciding which problem to work on first.

`status` values: `identified` (default), `selected` (promoted to a canvas — add `canvas: [[lean-product-canvas-<name>]]` to the frontmatter), `discarded` (add a `reason:` line to the frontmatter; a discarded problem is product memory too).

### Listing and prioritizing

When the user asks to see the problems ("list the problems", "what problems do we have for X?"), read the files in the problems folder and show a table with name, status, and one line of each statement. If they want help choosing which to work on, use the Box 1 Selection prompt over the `identified` records. Never choose for them.

Box 1 Selection also feeds this backlog: when a Selection leaves non-chosen statements as backlog, offer to save each one as a problem record (`identified`) — only after the user confirms, and still asking for the evidence of each, since a generated statement is an assumption.

### Promoting a problem to a canvas

When the user decides to work on a recorded problem:
1. Create `lean-product-canvas-<problem-name>.md` in the boards folder with the standard scaffold, plus a line `Source problem: [[<path to the record>]]` under the title. Ask for the output format first (see "Output format: Markdown, Canvas, or both"); the `Source problem:` line travels into the canvas header.
2. Pre-fill Box 1 with the record's statement and ask the user to confirm it; don't regenerate it, and skip the Box 1 format question and the research-scope question (the record's evidence is the starting context). Everything from Box 2 on follows the normal flow.
3. Update the record: `status: selected` and `canvas: [[…]]`.

## Creating an MVP

An MVP is the concrete execution of the experiment described in a canvas's **Box 8** (Least Amount of Work to Learn It), built to de-risk the assumption stated in that canvas's **Box 7** (Most Important Thing to Learn). A single canvas (main or problem) can spawn more than one MVP over time — e.g. a cheap first spike, then a follow-up experiment — each tracked as its own folder. This is lighter-weight than a full problem canvas: use it when the experiment doesn't need its own set of users/hypotheses/etc., just a place to run the test and record the result.

### Where MVPs live

One shared `MVPs/` folder per product, inside that product's boards folder (e.g. `Products/Acheev/MVPs/`). All MVPs for that product live here regardless of which canvas (main or a specific problem canvas) they came from. A canvas that hasn't spawned an MVP stays in the boards folder itself; once it spawns one, the canvas lives inside that MVP's folder (see "Moving the canvas into the MVP"). The MVP's `Summary.md` also records which source canvas/box it came from. Create the `MVPs/` folder the first time an MVP is created for that product.

### Folder naming

`#<N>-<Kebab-Case-Name>` — e.g. `#1-AI-Powered-Product-Matching-Engine-can-accurately-identify`.

- **`<N>`:** the next sequential integer across the whole `MVPs/` folder. Scan existing subfolders for the current highest `#N-` prefix and increment by 1 (start at `1` if `MVPs/` doesn't exist yet or is empty).
- **`<Kebab-Case-Name>`:** derived from the source canvas's Box 7 text — strip a leading framing phrase ("Whether ", "Whether the "), keep the first natural clause (up to the first comma, em-dash, or parenthetical aside), preserve the original word casing, and join words with hyphens instead of spaces. **Always show the derived name to the user before creating the folder** so they can adjust it — never create it silently with a name they haven't seen and approved. In the same message, tell them that the canvas files will move into that folder.

### Contents

Inside the new MVP folder, create `Summary.md`, containing the Box 7 and Box 8 content of the source canvas as of that moment, verbatim (if the canvas exists only as a `.canvas`, read the boxes by converting it with `to-md` into a scratch directory), each under its own heading, plus a link back to the source canvas. It is a snapshot: it keeps the boxes as of that moment and is not updated if the canvas changes later.

```markdown
# MVP #<N> — <Name>

Source: [[<source canvas base name>]]

## Most Important Thing to Learn
<verbatim Box 7 content from the source canvas>

## Least Amount of Work to Learn It
<verbatim Box 8 content from the source canvas>
```

The link is by name, not by path, so it keeps working wherever the canvas lives. Besides `Summary.md` and the moved canvas files (next section), don't create any other file (no `Final Report.md`, no results template, no `_Pending_` scaffolding) — those are written later by whoever actually runs the experiment. This skill only scaffolds the starting point.

### Moving the canvas into the MVP

Whenever an MVP is created, the source canvas **moves into the MVP's folder**, so the experiment travels with the canvas it came from. It applies to main canvases and problem canvases alike.

1. **What moves:** every file of that canvas that exists: `<name>.md`, `<name>.canvas`, or both (Both mode), keeping their names. The problem record, if the canvas came from one, never moves: it stays in the problems folder, and its `canvas:` link is by name, so it still resolves.
2. **How:** once the folder exists, `Summary.md` is written and the name was approved, move the files with `mv`. It's a move, not a copy, so there is still a single version of the canvas. If a file with that name already exists in the MVP folder, stop and ask.
3. **Fix path links:** moving files outside Obsidian doesn't update links. Before moving, search the project for wikilinks that point to the canvas by path (anything like `[[<folders>/<name>`); after moving, rewrite them to the new location. Links by name keep working and are left alone. Tell the user what you changed.
4. **The canvas stays editable there:** later work on its boxes (a pending box, a hand edit, converting between Markdown and Canvas) happens on the moved files, which are found through the rule in "Finding or defining the boards folder".
5. **A second MVP from the same canvas:** if the source canvas already lives inside an MVP folder, don't move it again silently. Ask which of these they want and do exactly that: move it to the new MVP; copy it, so each MVP keeps its own copy and the original stays; or leave it where it is and only link to it from the new `Summary.md`.
6. **Report** the new location of the canvas files and which links were updated.

### Trigger

- On explicit request ("create an MVP", "let's run an experiment for this", "spin up an MVP from box 8").
- Also offer it as an option right after Box 8 is saved/confirmed for any canvas (main or problem), alongside the existing suggestion to seed a new problem canvas — see step 9 of "General flow" below. When you offer it, mention that creating an MVP also moves the canvas into the new folder.

## General flow

0. **If the user wants to write down or list problems** (not work on a canvas box), follow "Capturing a problem" instead of the steps below.
1. **Identify the product, whether this is the main canvas or a problem canvas, and the box.** Follow "Deciding which one to create or work on" above to resolve the file. If the user doesn't specify the box, look at that file (if it exists) and suggest the first box still `_Pending_` as the next step — but if the user asks for a specific different box, address that without insisting on order.
2. **Ask about research scope, only when starting Box 1 of a new canvas** (the file doesn't exist yet, or exists but Box 1 is still `_Pending_`). Before touching the Generation prompt, explicitly ask the user — don't assume any default:
   - **Use related project information:** search (grep/find by the product/problem name and related terms) for prior notes, previous canvases, competitor analysis (e.g. a `market-research` output), or other existing material in the project, and use it as context/evidence when generating, citing where each piece of data comes from.
   - **Go straight to Box 1:** don't search for anything beyond this conversation; start the Generation prompt with only what the user tells you.
   For subsequent boxes of the same canvas, there's no need to repeat this question — the context already gathered (or the decision not to gather it) applies to the whole canvas, unless the user asks otherwise.
2b. **Ask for the output format, only when creating a new canvas** (neither the `.md` nor the `.canvas` exists): Markdown, Canvas, or both, per "Output format: Markdown, Canvas, or both". For an existing canvas, infer it from the files instead of asking. If the user asks to convert between forms, follow "Converting an existing canvas" instead of the box flow.
3. **On Box 1, resolve the format** per "Choosing the Box 1 format" above before generating anything.
4. **On Box 3 of a problem canvas**, check the product's main canvas for existing proto-personas first, per "Per-box differences" above.
5. **Detect the mode** from the language of the request (see table below). No exact command needed.
6. **Execute the mode**, following the corresponding prompt's instructions to the letter (see "How to execute each mode").
7. **Offer to save the summary.** When the user reaches a result they're satisfied with for that box (typically after Generate+Select, or after incorporating Review feedback), draft a concise summary and show it to them before writing it to the file.
8. **Save with confirmation.** If the box already has content other than `_Pending_` in the file, show the old summary next to the new one and explicitly ask whether to confirm the replacement before overwriting. Never overwrite silently. Saving follows the canvas's output format: in Both mode, check `compare` first and regenerate the canvas after saving; in Canvas mode, go through the working copy (see "Output format: Markdown, Canvas, or both").
9. **Suggest the next step.** After saving, indicate which box is next pending, leaving it open for the user to choose a different one. If Box 8 just got filled in (main canvas or problem canvas), suggest its output as the natural starting point for either a new problem canvas (if the experiment needs its own full canvas) or, more directly, an MVP folder (see "Creating an MVP" above; it also moves the canvas into the new folder) — whichever fits the scope of the experiment.

### Detecting the requested mode

| Signal in the user's request | Mode | Section of the prompts file to use |
|---|---|---|
| "help me fill in/think through/put together box N", "I don't know where to start with...", "give me options for..." | **Generate** | `## GENERATION PROMPT` |
| "I have these options, help me choose", "I generated several versions of box N", "which one should I pick?" | **Select** | `## SELECTION PROMPT` (if it exists for that box) |
| "review my box N", "how does this look?", "give me feedback on..." | **Review** | `## REVIEW PROMPT` |
| "I want to write/log/record a problem", "new problem for <product>", "list the problems" | **Capture** (no canvas box) | `references/capture_problem.md` — see "Capturing a problem" |

If the request is ambiguous, ask which mode they want before assuming one.

### How to execute each mode

In every case: read the corresponding `box{N}_*.md` file — for Box 1, whichever of `box1_business_problem_statement.md` or `box1_business_opportunity_statement.md` applies per "Choosing the Box 1 format" — locate the section for the detected mode, and **act it out yourself following those instructions** (don't just paste the raw prompt for the user to copy elsewhere — you are the AI that prompt describes).

- **Generate:** the prompt has placeholders in brackets (e.g. `[DESCRIBE YOUR SITUATION]`, `[PASTE YOUR BOX 1 PROBLEM STATEMENT]`). Before generating, resolve those placeholders:
  - If the data is already in the canvas file (e.g. a previous box's summary, or the main canvas's proto-personas when generating Box 3 of a problem canvas), use it directly without asking again.
  - If it isn't available, ask the user explicitly.
  - With placeholders resolved, generate content following exactly the format and number of options the prompt asks for (2-3, 5, etc.), including assumptions and validation evidence when the prompt calls for it — that's for the conversation, not for the file.
- **Select:** ask the user for the options if you didn't generate them yourself earlier in the same thread. Follow the prompt's question guide and decision framework exactly as written. Non-negotiable rule inherited from the prompt: **never choose for the user** — guide them with questions and trade-offs, and wait for their explicit decision.
- **Review:** ask for the box's current content if it isn't already in the canvas file or the conversation. Follow the prompt's review criteria (format adherence, clarity, risky assumptions, etc.). Non-negotiable rule inherited from the prompt: **don't rewrite the user's work** — give them specific guidance so they can improve it themselves.

### Writing the concise summary

When saving to the file, condense the final result agreed with the user into 2-6 lines or bullets, in that box's own required format (the same format used by the Generation prompt — e.g. the `[Our service/product] was designed to...` format for Box 1, or `[Who][Does What][To What Extent]` for Box 2). Don't include confidence levels, lists of assumptions, or pending research — that was resolved (or discussed) during the conversation.

Example summary for Box 1 (target format in the file, English output):

```markdown
## 1. Business Problem Statement
Our expense-tracking app was designed so users could log expenses in under 10 seconds.
We've observed, through drop-off on the quick-entry screen (60% don't complete logging),
that users aren't meeting that goal, which is causing low recurring app usage. How might
we improve the quick-entry flow so users are more successful logging expenses, as
determined by reducing drop-off to under 20%?
```
