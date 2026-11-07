# Sense & Respond — Product Discovery Kit

A set of Claude Code skills/commands for running Product Discovery using the [Sense & Respond](https://senseandrespond.com/) methodology (Jeff Gothelf & Josh Seiden).

## What's included

- **[market-research](market-research/)** — maps the competitive landscape of an opportunity across 4 tiers (direct competitors, indirect competitors, potential acquirers, adjacent players) using web search. Command only: `/market-research <opportunity>`.
- **[lean-product-canvas](lean-product-canvas/)** — fills in, selects between options for, and reviews the 8 boxes of the [Lean Product Canvas](https://jeffgothelf.com/blog/the-lean-product-canvas/), through guided conversation. Manages two related artifacts per product: a single main canvas and any number of per-problem canvases for experiments within it. Ships as an auto-triggered Skill — just talk to Claude about the Lean Product Canvas.
- **[founding-hypothesis](founding-hypothesis/)** — writes, selects between approaches for, and reviews a Founding Hypothesis (Jake Knapp & John Zeratsky, Foundation Sprint): "If we help [customer] solve [problem] with [approach], they will choose us over [competitors] because our solution is [differentiators]". Another way to describe an opportunity, strongest on competition and differentiation. Includes the Magic Lenses to compare approaches, an assumption scorecard, and a worked Spotify example. Ships as an auto-triggered Skill.
- **[friction-map-canvas](friction-map-canvas/)** — turns a saved Cognitive Friction Map (MFC, from `/afpm:map-frictions` or any map in the `cognitive-frictions` format) into an Obsidian canvas: the journey as a flow, grouped into phases, with each step's friction colored by severity, the ranked opportunities and a link back to the `.md`. Meant to run by itself as the last step of a friction mapping. Ships as an auto-triggered Skill with a small Python layout script (standard library only).

Each skill/command lives in its own self-contained folder and can be installed independently — see that folder's own README for install instructions.

## Quick install

With the [`skills`](https://github.com/vercel-labs/skills) CLI:

```bash
npx skills add fzuppa/sense-and-respond-discovery-kit/lean-product-canvas
npx skills add fzuppa/sense-and-respond-discovery-kit/founding-hypothesis
npx skills add fzuppa/sense-and-respond-discovery-kit/market-research
npx skills add fzuppa/sense-and-respond-discovery-kit/friction-map-canvas
```

`npx skills add` installs the skill content (`SKILL.md` + `references/`) but not slash commands — commands are a separate registry in Claude Code. `lean-product-canvas` and `founding-hypothesis` don't need one (they're auto-triggered). See the `market-research` README for the copy step needed if you want the `/market-research` command.

## Language

Every skill/command in this kit follows the same output-language rule:

1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language for generated notes.
2. Otherwise, use the language of the current conversation.
3. If still unclear, ask before writing.

The kit's own instructions (this README, `SKILL.md` files, prompt references, command files) are written in English — that's fixed. Only the **content each skill generates** (canvas boards, research notes) adapts to the target project/conversation language per the rule above.

## Typical flow

1. `/market-research <opportunity>` — understand the competitive landscape before committing to a problem framing.
2. Talk to Claude about the Lean Product Canvas (e.g. `help me fill in the main canvas for <product>`) — work through the 8 boxes for the product's main canvas, using the market research as input for Users and Solutions.
3. For each experiment you want to run inside that product, ask for a problem canvas (e.g. `help me fill in a canvas for problem <problem-name>`) — it reuses the main canvas's proto-personas and works through the same 8 boxes scoped to that specific problem.

Alternatively, or in addition, describe the opportunity with a Founding Hypothesis (`help me write the founding hypothesis for <product>`) when the key question is *why customers would choose you over the alternatives*. If Box 1 uses the Business Opportunity Statement, its competitive clause can be carried into the canvas.

Once you have a journey and want to see where AI could add value in it, map its cognitive frictions with `/afpm:map-frictions`; `friction-map-canvas` then draws the saved map as a canvas.

Nothing enforces this order — each skill can be used standalone.

## Roadmap

This kit currently covers the earliest stage of discovery (market context + framing the opportunity on a canvas). Natural next additions: JTBD interview synthesis, proto-persona builder from real interview data, opportunity solution tree, experiment/MVP design beyond Box 8.

## License

TBD before this repo is made public.
