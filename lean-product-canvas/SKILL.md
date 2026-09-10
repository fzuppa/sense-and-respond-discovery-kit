---
name: lean-product-canvas
description: "Use when working on a Lean Product Canvas (LPD): filling in a box through guided questions, choosing between generated options, or reviewing an already-written box. Triggers: 'Lean Product Canvas', 'LPD', 'box 1..8', 'business problem statement', 'business outcomes', 'proto-persona', 'JTBD', 'canvas hypotheses', 'help me fill in the canvas', 'review my box', 'I have several options for box'."
---

# Lean Product Canvas (LPD)

Guide for filling in, selecting between options for, and reviewing the 8 boxes of the [Lean Product Canvas](https://jeffgothelf.com/blog/the-lean-product-canvas/) for an opportunity, using the prompts packaged in `references/` (relative to this file). Self-contained skill: it doesn't depend on any folder outside the skill itself, only on the project where it's invoked, to save its results.

This skill is part of the **Sense & Respond Product Discovery kit**. It's typically used after `market-research` has produced context on users/market, and feeds the canvas boxes (Users, Solutions) from that research when available.

## Output language

Follow these rules, in order:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the current conversation (the language the user is writing in).
3. If still unclear, ask before writing.

The box titles and prompt templates in `references/` are written in English — treat them as the canonical version and translate them naturally into the detected output language, both when talking to the user and when writing to the LPD file. When translating, keep the required format's structure intact (bracketed placeholders, overall sentence shape) — e.g. Box 1's statement or Box 2's `[Who][Does What][To What Extent]` format.

**Canvas principle (repeat it when relevant):** AI-generated outputs are assumptions that must be validated, not facts to accept.

## The 8 boxes

| # | Section name in the file | Prompts file | Available modes |
|---|------|---------------------|--------------------|
| 1 | Business Problem Statement | `box1_business_problem_statement.md` | Generate, Select, Review |
| 2 | Business Outcomes | `box2_business_outcomes.md` | Generate, Select, Review |
| 3 | Users (Proto-Personas) | `box3_users_proto_personas.md` | Generate, Review |
| 4 | User Outcomes & Benefits (JTBD) | `box4_user_outcomes_benefits.md` | Generate, Review |
| 5 | Solutions / Features | `box5_solutions_features.md` | Generate, Select, Review |
| 6 | Hypotheses | `box6_hypotheses.md` | Generate, Select, Review |
| 7 | Most Important Thing to Learn | `box7_most_important_thing_to_learn.md` | Generate, Review |
| 8 | Least Amount of Work to Learn It | `box8_least_amount_of_work_to_learn_it.md` | Generate, Select, Review |

Use the English section name above as the canonical title for the `## N. <name>` header in the LPD file, translated into the detected output language when that isn't English (e.g. in Spanish: "1. Enunciado del Problema de Negocio (Business Problem Statement)" — keep the original English name in parentheses so the section stays traceable across languages). When the output language is English, just use the plain English name, no parentheses needed.

All files live in `references/`, relative to this file (SKILL.md). Boxes 3, 4, and 7 don't have a Selection prompt because they produce a single synthesized artifact, not multiple options to compare — if the user asks to "select" for one of these boxes, explain this and offer to refine the result with targeted questions instead, or move to Review.

## Output file

Each opportunity has a single `LPD <Opportunity>.md` file (e.g. `LPD Acme Corp.md`) inside a boards folder of the current project.

### Finding or defining the boards folder

This skill doesn't assume any fixed folder structure — it adapts to whatever project it's used in:

1. **Look for a folder already in use.** Before asking anything, search the current project for existing files matching `LPD *.md` (e.g. with `find . -iname "LPD *.md"`). If you find any, the folder containing them is the boards folder — use it without asking again. This makes the folder choice persist automatically once a project has used the skill before.
2. **If none is found** (first use of the skill in this project), ask the user which folder to save this project's LPD files in (suggest `Lean Product Canvas Boards/` as a default if they have no preference). Create the folder if it doesn't exist.

With the folder determined, each opportunity's file has this structure (shown here with English section names — translate per the output-language rule above):

```markdown
# LPD <Opportunity>

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

- **Opportunity name:** if it isn't clear from the conversation context, ask "What's the opportunity called?" before creating or looking up the file.
- **Creation:** if `LPD <Opportunity>.md` doesn't exist yet in the boards folder determined above, create it with the full scaffold above (all 8 boxes as `_Pending_`) before filling in the first box.
- **Content of each section:** only the **concise summary** of that box (see below) — not the full detail of the conversation, no confidence levels, no lists of pending research. That detail lives in the conversation, not in the file.

## General flow

1. **Identify opportunity and box.** If the user doesn't specify the box, look at the LPD file (if it exists) and suggest the first box still `_Pending_` as the next step — but if the user asks for a specific different box, address that without insisting on order.
2. **Ask about research scope, only when starting Box 1 of a new opportunity** (the LPD file doesn't exist yet, or exists but Box 1 is still `_Pending_`). Before touching the Generation prompt, explicitly ask the user — don't assume any default:
   - **Use related project information:** search (grep/find by the opportunity name and related terms) for prior notes, previous canvases, competitor analysis (e.g. a `market-research` output), or other existing material in the project, and use it as context/evidence when generating, citing where each piece of data comes from.
   - **Go straight to Box 1:** don't search for anything beyond this conversation; start the Generation prompt with only what the user tells you.
   For subsequent boxes of the same opportunity, there's no need to repeat this question — the context already gathered (or the decision not to gather it) applies to the whole opportunity, unless the user asks otherwise.
3. **Detect the mode** from the language of the request (see table below). No exact command needed.
4. **Execute the mode**, following the corresponding prompt's instructions to the letter (see "How to execute each mode").
5. **Offer to save the summary.** When the user reaches a result they're satisfied with for that box (typically after Generate+Select, or after incorporating Review feedback), draft a concise summary and show it to them before writing it to the file.
6. **Save with confirmation.** If the box already has content other than `_Pending_` in the file, show the old summary next to the new one and explicitly ask whether to confirm the replacement before overwriting. Never overwrite silently.
7. **Suggest the next step.** After saving, indicate which box is next pending, leaving it open for the user to choose a different one.

### Detecting the requested mode

| Signal in the user's request | Mode | Section of the prompts file to use |
|---|---|---|
| "help me fill in/think through/put together box N", "I don't know where to start with...", "give me options for..." | **Generate** | `## GENERATION PROMPT` |
| "I have these options, help me choose", "I generated several versions of box N", "which one should I pick?" | **Select** | `## SELECTION PROMPT` (if it exists for that box) |
| "review my box N", "how does this look?", "give me feedback on..." | **Review** | `## REVIEW PROMPT` |

If the request is ambiguous, ask which of the three modes they want before assuming one.

### How to execute each mode

In every case: read the corresponding `box{N}_*.md` file, locate the section for the detected mode, and **act it out yourself following those instructions** (don't just paste the raw prompt for the user to copy elsewhere — you are the AI that prompt describes).

- **Generate:** the prompt has placeholders in brackets (e.g. `[DESCRIBE YOUR SITUATION]`, `[PASTE YOUR BOX 1 PROBLEM STATEMENT]`). Before generating, resolve those placeholders:
  - If the data is already in the LPD file (e.g. a previous box's summary), use it directly without asking again.
  - If it isn't available, ask the user explicitly.
  - With placeholders resolved, generate content following exactly the format and number of options the prompt asks for (2-3, 5, etc.), including assumptions and validation evidence when the prompt calls for it — that's for the conversation, not for the file.
- **Select:** ask the user for the options if you didn't generate them yourself earlier in the same thread. Follow the prompt's question guide and decision framework exactly as written. Non-negotiable rule inherited from the prompt: **never choose for the user** — guide them with questions and trade-offs, and wait for their explicit decision.
- **Review:** ask for the box's current content if it isn't already in the LPD file or the conversation. Follow the prompt's review criteria (format adherence, clarity, risky assumptions, etc.). Non-negotiable rule inherited from the prompt: **don't rewrite the user's work** — give them specific guidance so they can improve it themselves.

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
