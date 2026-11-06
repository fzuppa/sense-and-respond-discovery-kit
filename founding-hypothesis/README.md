# Founding Hypothesis (Claude Code skill)

Skill for writing, choosing between approaches for, and reviewing a **Founding Hypothesis** — the one-sentence output of the Foundation Sprint by Jake Knapp and John Zeratsky (book *Click*):

> If we help **[customer]** solve **[problem]** with **[approach]**, we believe they will choose it over **[competitors]** because our solution is **[differentiators]**.

It's one more way to describe an opportunity. Where the Business Opportunity Statement is strongest on the state of the market and the success behaviors, the Founding Hypothesis is strongest on **competition and differentiation**: *why would customers choose you and not the alternative?* The two combine well.

Part of the **[Sense & Respond Product Discovery kit](../README.md)**.

Self-contained: all the logic and prompts live inside this folder. Output language follows the kit-wide rule — see [Language](#language) below.

## Installation

### Option 1: with `npx skills` (recommended)

```bash
npx skills add fzuppa/sense-and-respond-discovery-kit/founding-hypothesis
```

To install it at the user level (available in all your projects):

```bash
npx skills add fzuppa/sense-and-respond-discovery-kit/founding-hypothesis -g
```

It's auto-triggered by Claude recognizing Founding Hypothesis requests in conversation, so there's no slash command to register.

### Option 2: manual

Copy this whole folder (`SKILL.md`, `README.md`, and `references/`) into:
- **A single project:** `.claude/skills/founding-hypothesis/` at the project's root.
- **All your projects:** `~/.claude/skills/founding-hypothesis/`.

No additional configuration or build step needed.

## Usage

Just ask Claude, in natural language:

- "Help me write the Founding Hypothesis for X"
- "Why would customers choose us over Y?"
- "I have three approaches for this problem, help me choose" *(uses the Magic Lenses)*
- "Review my founding hypothesis"
- "What are the riskiest assumptions of this hypothesis?"
- "Show me an example of a founding hypothesis"

## The three modes

| Mode | What it does |
|---|---|
| **Generate** | Guides you through the basics (customer, problem, your advantage, competitors including workarounds and "do nothing", most challenging competitor), then differentiation, then the approach (2-3 genuinely different options evaluated with the Magic Lenses, ending in a top bet and a backup). Finally assembles the sentence. |
| **Select** | Helps you choose between approaches with questions and a decision table. It never chooses for you. |
| **Review** | Checks format, specificity of each slot, the *competitor swap test* (could the strongest competitor say the same "because…"?), coherence and risky assumptions. It doesn't rewrite your sentence. |

It also builds the **assumption scorecard**: the five beliefs behind the sentence (right customer, right problem, right approach, they'll choose us, they care about our differentiators), each with what would prove it wrong and the cheapest next test.

## What gets saved

A `founding-hypothesis-<name>.md` file with five sections: the sentence, the basics, differentiation, approach, and the scorecard. The first time it's used in a project it asks which folder to save in (suggesting `Founding Hypotheses/`); afterwards it finds the folder by looking for existing `founding-hypothesis-*.md` files. It always shows a section before saving it, and never overwrites existing content without asking.

## Worked example

[`references/examples.md`](references/examples.md) includes a full worked example: **Spotify at its start (2006-2008)**, from the basics to the scorecard, with each fact tied to a source. It's a **retrospective reconstruction**, not a statement Spotify ever published. It also includes the Gmail example from the authors, and a weak-vs-strong comparison.

## A note on sources

The method comes from *Click* (Knapp & Zeratsky) and the Foundation Sprint article on [Lenny's Newsletter](https://www.lennysnewsletter.com/p/introducing-the-foundation-sprint). Some details could only be checked in secondary sources: the exact "If we help…" wording is the community version of the sentence, and the Magic Lenses and scorecard formats here are the kit's adaptation. If you have the book, you can swap the wording in `references/template.md`. The `SKILL.md` and each reference file say what is verified and what is adapted.

## Language

Output language follows this rule, in order:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the current conversation.
3. If still unclear, ask before writing.

Same rule as the rest of the kit. The kit's own instructions (this README, `SKILL.md`, reference files) are in English; only the content the skill generates adapts to the project's language.
