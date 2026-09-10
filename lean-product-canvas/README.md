# Lean Product Canvas (Claude Code skill)

Skill for filling in, selecting between options for, and reviewing the 8 boxes of the [Lean Product Canvas](https://jeffgothelf.com/blog/the-lean-product-canvas/) by talking to Claude — no copy-pasting prompts by hand. Results are saved to an `LPD <Opportunity>.md` file inside the project.

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

`npx skills add` installs the skill (`SKILL.md` + `references/`) — that's all this skill needs, since it's auto-triggered by Claude recognizing Lean Product Canvas requests in conversation. No slash command to register.

### Option 2: manual

1. Copy this whole folder (`SKILL.md`, `README.md`, and `references/`) into Claude Code's skills folder:
   - **For a single project:** paste it into `.claude/skills/lean-product-canvas/` at that project's root.
   - **For all your projects:** paste it into `~/.claude/skills/lean-product-canvas/` (user-level skills).
2. No additional configuration or build step needed.

## Usage

Just ask Claude, in natural language, something like:

- "Help me fill in a Lean Product Canvas for opportunity X"
- "Generate options for box 1"
- "I have several options for box 5, help me choose"
- "Review my box 3"

The skill guides you box by box, asking for the information it needs, showing you the generated results, and asking for your confirmation before saving each summary to the `LPD <Opportunity>.md` file.

The first time it's used in a new project, it'll ask which folder to save LPD files in. Subsequent uses reuse that same folder automatically (it finds it by looking for existing `LPD *.md` files).

## Language

Output language follows this rule, in order:
1. If the target project has its own `CLAUDE.md` specifying a language convention, use that language.
2. Otherwise, use the language of the current conversation.
3. If still unclear, ask before writing.

The skill's own instructions (`SKILL.md`, this README, the prompts in `references/`) are written in English — that doesn't change; only the **content it generates** (the LPD file, the conversation) adapts to the detected language.

## Structure

```
lean-product-canvas/
├── SKILL.md              # instructions Claude follows
├── README.md              # this file
└── references/
    ├── box1_business_problem_statement.md
    ├── box2_business_outcomes.md
    ├── box3_users_proto_personas.md
    ├── box4_user_outcomes_benefits.md
    ├── box5_solutions_features.md
    ├── box6_hypotheses.md
    ├── box7_most_important_thing_to_learn.md
    └── box8_least_amount_of_work_to_learn_it.md
```

Each file in `references/` contains the Generation, Selection (when applicable), and Review prompts for that canvas box.
