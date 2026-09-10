# Sense & Respond — Product Discovery Kit

A set of Claude Code skills/commands for running Product Discovery using the [Sense & Respond](https://senseandrespond.com/) methodology (Jeff Gothelf & Josh Seiden).

## What's included

- **[market-research](market-research/)** — maps the competitive landscape of an opportunity across 4 tiers (direct competitors, indirect competitors, potential acquirers, adjacent players) using web search. Command only: `/market-research <opportunity>`.
- **[lean-product-canvas](lean-product-canvas/)** — fills in, selects between options for, and reviews the 8 boxes of the [Lean Product Canvas](https://jeffgothelf.com/blog/the-lean-product-canvas/) for an opportunity, through guided conversation. Ships as an auto-triggered Skill, plus an optional `/lpd <opportunity>` command.

Each skill/command lives in its own self-contained folder and can be installed independently — see that folder's own README for install instructions.

## Quick install

With the [`skills`](https://github.com/vercel-labs/skills) CLI:

```bash
npx skills add fzuppa/sense-and-respond-discovery-kit/lean-product-canvas
npx skills add fzuppa/sense-and-respond-discovery-kit/market-research
```

`npx skills add` installs the skill content (`SKILL.md` + `references/`) but not slash commands — commands are a separate registry in Claude Code. See each skill's README for the one extra copy step needed if you also want the `/lpd` or `/market-research` commands.

## Language

Every skill/command in this kit follows the same output-language rule:

1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language for generated notes.
2. Otherwise, use the language of the current conversation.
3. If still unclear, ask before writing.

The kit's own instructions (this README, `SKILL.md` files, prompt references, command files) are written in English — that's fixed. Only the **content each skill generates** (LPD boards, research notes) adapts to the target project/conversation language per the rule above.

## Typical flow

1. `/market-research <opportunity>` — understand the competitive landscape before committing to a problem framing.
2. `/lpd <opportunity>` (or just talk to Claude about the Lean Product Canvas) — work through the 8 boxes, using the market research as input for Users and Solutions.

Nothing enforces this order — each skill can be used standalone.

## Roadmap

This kit currently covers the earliest stage of discovery (market context + framing the opportunity on a canvas). Natural next additions: JTBD interview synthesis, proto-persona builder from real interview data, opportunity solution tree, experiment/MVP design beyond Box 8.

## License

TBD before this repo is made public.
