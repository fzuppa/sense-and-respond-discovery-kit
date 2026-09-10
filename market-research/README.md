# Market Research (Claude Code command)

Command that maps the competitive landscape of an opportunity across 4 tiers — direct competitors, indirect competitors, potential acquirers, and adjacent players who could move into the space — using web search, and saves the result as a note in the project.

Part of the **[Sense & Respond Product Discovery kit](../README.md)**.

Unlike `lean-product-canvas`, this is a Command only (no `SKILL.md`): it's a single self-contained flow with an explicit required argument (the opportunity name), so it doesn't need auto-triggering or bundled reference files.

## Installation

Commands are a plain markdown file with YAML frontmatter — no CLI needed. Copy `commands/market-research.md` into Claude Code's commands folder:

- **For a single project:** `.claude/commands/market-research.md` at that project's root.
- **For all your projects:** `~/.claude/commands/market-research.md`.

## Usage

```
/market-research <opportunity-or-project-name>
```

Claude will look for existing context on the opportunity in the project (a Lean Product Canvas file, prior research notes), confirm the value proposition/customer/geography it understood, research the four tiers with web search, and save a note with a summary table and strategic implications.

## Language

Output language follows this rule, in order:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the current conversation.
3. If still unclear, ask before writing.

This is the same rule used by the `lean-product-canvas` skill, so both parts of the kit behave consistently across projects.
