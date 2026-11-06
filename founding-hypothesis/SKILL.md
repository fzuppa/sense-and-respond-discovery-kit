---
name: founding-hypothesis
description: "Use when writing, choosing between approaches for, or reviewing a Founding Hypothesis (Jake Knapp & John Zeratsky, Foundation Sprint, from the book Click): the one-sentence 'If we help [customer] solve [problem] with [approach], they will choose us over [competitors] because our solution is [differentiators]'. Another way to describe an opportunity, focused on why customers would choose you over the alternatives. Triggers: 'founding hypothesis', 'Foundation Sprint', 'Knapp', 'Zeratsky', 'Click book', 'if we help', 'magic lenses', 'why would they choose us', 'differentiation vs competitors', 'strongest competitor', 'help me write the hypothesis', 'review my founding hypothesis', 'compare approaches', 'hypothesis scorecard'."
---

# Founding Hypothesis

Guide for writing, selecting between approaches for, and reviewing a **Founding Hypothesis**, the output of the Foundation Sprint by Jake Knapp and John Zeratsky (book *Click*). It's a single falsifiable sentence that combines customer, problem, approach, competition and differentiation, plus a scorecard of the beliefs that have to be true for it to hold.

This skill is part of the **Sense & Respond Product Discovery kit**. It's one more way to describe an opportunity, and it covers what the Business Opportunity Statement is weakest at: *why would customers choose you over the alternatives?* It's self-contained — it doesn't depend on any other skill, only on the project where it's invoked, to save its results.

## Output language

Follow these rules, in order:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the current conversation.
3. If still unclear, ask before writing.

The templates and prompts in `references/` are written in English — treat them as the canonical version and translate them naturally into the detected output language, both when talking to the user and when writing to the file. Keep the sentence's structure intact when translating (the "If we help… with… they will choose it over… because…" shape and its bracketed slots).

**Core principle (repeat it when relevant):** a Founding Hypothesis is a *bet that can be wrong*, not a plan. AI-generated content is an assumption to validate, not a fact to accept.

## About the template and its sources

The sentence shape used here is:

```
If we help [target customer] solve [important problem] with [approach]
(backup: [backup approach]), we believe they will choose it over
[competitors / alternatives] because our solution is [differentiator 1]
and [differentiator 2].
```

Knapp and Zeratsky describe the Founding Hypothesis as a fill-in-the-blank ("Mad Libs") sentence that combines customer, approach and differentiation. The exact wording above is the "If we help…" version popularized by community adaptations of the method; the authors' own wording lives in the book. If the user has the book and wants to use its exact wording, swap the template in `references/template.md` and keep everything else. The questions, scorecard format and examples in this skill are the kit's own adaptation of the method, not a transcription of the book.

## The three modes

| Signal in the user's request | Mode | File to read |
|---|---|---|
| "help me write the founding hypothesis", "I don't know where to start", "why would they choose us?" | **Generate** | `references/basics_and_differentiation.md` (Day 1 part), then `references/approach_magic_lenses.md` (Day 2 part), then `references/template.md` |
| "I have several approaches, help me choose", "which approach should we bet on?", "compare these options" | **Select** | `references/approach_magic_lenses.md` — `## SELECTION PROMPT` |
| "review my founding hypothesis", "how does this look?", "give me feedback on this sentence" | **Review** | `references/template.md` — `## REVIEW PROMPT`, then `references/scorecard.md` |
| "what are the riskiest assumptions?", "scorecard", "how do I test this?" | **Scorecard** | `references/scorecard.md` |

If the request is ambiguous, ask which mode they want before assuming one. `references/examples.md` has a fully worked example (Spotify at its start) — use it to show the user what a finished hypothesis looks like, or when they ask for an example.

### How to execute each mode

In every case, read the relevant reference file and **act it out yourself** following its instructions (don't paste the raw prompt for the user to copy elsewhere — you are the AI that prompt describes).

- **Generate:** work through the sprint's logic in two blocks, one question group at a time (don't dump all questions at once):
  1. **Basics + differentiation** (`basics_and_differentiation.md`): customer, problem, our advantage, competitors (including workarounds and "do nothing"), the most challenging competitor, then differentiators.
  2. **Approach** (`approach_magic_lenses.md`): generate 2-3 genuinely different approaches, evaluate them through the lenses, and name a top bet and a backup.
  3. **Sentence** (`template.md`): assemble the hypothesis from what was agreed. Show 1-2 candidate sentences.
  Use what's already in the conversation or in the project (an existing canvas, `market-research` output, interview notes) instead of asking again. When the user doesn't know an answer, say so and mark it as an assumption to validate.
- **Select:** follow the selection prompt's questions and decision table exactly. Non-negotiable rule: **never choose for the user** — guide with questions and trade-offs, and wait for their explicit decision.
- **Review:** follow the review prompt's criteria (format, specificity, differentiators, falsifiability, assumptions). Non-negotiable rule: **don't rewrite the user's work** — give specific guidance so they can improve it themselves.

## Saving the result

### File name and folder

- File: `founding-hypothesis-<name>.md` where `<name>` is short, kebab-case, in the output language (e.g. `founding-hypothesis-spotify.md`).
- **Look for a folder already in use.** Search the project for existing `founding-hypothesis-*.md` files (e.g. `find . -iname "founding-hypothesis-*.md"`); if found, use that folder without asking.
- **If none is found,** ask which folder to save in (suggest `Founding Hypotheses/` as a default) and create it if needed.

### The file scaffold

Create the file with this structure the first time (section names shown in English — translate per the output-language rule), all sections as `_Pending_`:

```markdown
# Founding Hypothesis — <Name>

## Founding Hypothesis
_Pending_

## The basics
_Pending_

## Differentiation
_Pending_

## Approach
_Pending_

## Assumption scorecard
_Pending_
```

Section content (concise — the long discussion stays in the conversation, not the file):

- **Founding Hypothesis:** the final sentence, in the template's shape.
- **The basics:** customer, problem, our advantage, competitors (marking the most challenging one), each in 1-2 lines.
- **Differentiation:** the 1-2 differentiators, each with the competitor it's relative to.
- **Approach:** the top bet and the backup, with a one-line lens verdict for each (customer experience, feasibility, growth, financial viability, plus any custom lens).
- **Assumption scorecard:** the table described in `references/scorecard.md`.

### Saving flow

1. Draft the concise content for the section and **show it before writing**.
2. If the section already has content other than `_Pending_`, show old and new side by side and ask explicitly whether to replace it. Never overwrite silently.
3. After saving, say which section is still `_Pending_` and suggest the next step. Once the scorecard is filled, the next step is testing the riskiest belief (interviews, a concierge test, a prototype) — suggest it, don't run it.

## Connection to the rest of the kit (optional, never forced)

- If a Lean Product Canvas exists for the same product, offer to carry the competitive clause into **Box 1** when it uses the Business Opportunity Statement format ("…and customers will choose us over [X] because we are [Y]"). Only offer it; don't edit the canvas without the user's go-ahead.
- If `market-research` has been run for the opportunity, use its competitor tiers as raw material for the competitors question instead of asking from scratch.
