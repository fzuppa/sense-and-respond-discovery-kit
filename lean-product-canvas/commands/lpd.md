---
description: Creates (or resumes) the Lean Product Canvas for an opportunity and starts by completing Box 1
argument-hint: <opportunity-name>
---

I want to work on the Lean Product Canvas for the opportunity "$ARGUMENTS" using the `lean-product-canvas` skill.

- If the skill appears in your list of invokable skills, use it with `Skill({skill: "lean-product-canvas", args: "$ARGUMENTS"})`, explicitly requesting: create or resume the LPD file for this opportunity and start with Box 1.
- If it doesn't appear as invokable but is installed as a folder, find it (`find . -iname "SKILL.md" -path "*lean-product-canvas*"`, both at the project level and in `~/.claude/skills` or `~/.agents/skills`), read that `SKILL.md`, and follow its instructions yourself to the letter.

In either case, the flow to execute is the one the skill describes:

1. **Locate the boards folder** of the current project: look for existing `LPD *.md` files and use that folder. If none is found, ask where to save this project's LPD files (suggest `Lean Product Canvas Boards/` as a default).
2. **Create the file if it doesn't exist.** If `LPD $ARGUMENTS.md` doesn't exist in that folder, create it with the full scaffold of the 8 boxes as `_Pending_` (exact format from `SKILL.md`, in the output language determined by the skill's language rule).
3. **If it already exists:**
   - If Box 1 already has content (not `_Pending_`), show it and ask whether to review it (Review mode) or move straight to the next pending box — don't silently regenerate it.
   - If Box 1 is still `_Pending_`, continue to step 4.
4. **Start Box 1.** Before generating content, ask about research scope (use related project information vs. go straight to Box 1), as the skill's general flow requires. With that resolved, execute the **GENERATION PROMPT** from `box1_business_problem_statement.md`, resolving its placeholders with what the user tells you.

Follow the rest of the skill's non-negotiable rules: never overwrite silently, offer the concise summary before saving, and ask for explicit confirmation to replace existing content.
