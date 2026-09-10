---
description: Maps the competitive landscape of an opportunity across 4 tiers (direct, indirect, potential acquirers, adjacent) using web search — initial market research for the Product Discovery kit (Sense & Respond)
argument-hint: <opportunity-or-project-name>
---

I want to map the competitive landscape for the opportunity "$ARGUMENTS".

This command is self-contained: do not invoke any external skill, do not search for or read any `SKILL.md` or additional prompt file. Everything needed is in the instructions below.

This command is part of the **Sense & Respond Product Discovery kit**. It serves as market research — a typical input before or during the Lean Product Canvas (see the `lean-product-canvas` skill), especially for the Users and Solutions boxes.

## Flow

1. **Opportunity name.** If `$ARGUMENTS` is empty, ask what it is before continuing.

2. **Gather context on the opportunity** — with a scoped glob/grep, without exploring the whole filesystem:
   - An `LPD $ARGUMENTS.md` file (Lean Product Canvas), if it exists, to pull the value proposition, users, and business problem.
   - Any prior research inside a folder named after the opportunity (e.g. `Projects/$ARGUMENTS/`), such as a testable-hypothesis note or other prior research.
   - If nothing is found, ask the person to describe in 2-3 lines: what the product/service does, for whom (customer/market type), and what geography it operates in.

3. **Detect the output language.** Follow these rules, in order:
   - If the project folder has its own `CLAUDE.md` specifying a language convention, use that language.
   - Otherwise, use the language of the current conversation (the language the user is writing in right now) — do not default to any broader/root-level convention that isn't part of this rule.
   - If still unclear, ask before writing.

4. **Confirm scope** before going out to research: show, in 2-3 lines, the value proposition, target customer, and geography as you understood them, and ask for explicit confirmation or correction.

5. **Research with web search** and map the landscape across 4 tiers. For every player, in any tier, include: name, one-line description, size/funding/owner if known, geographic focus, business model, and the specific reason it belongs in that tier.

   - **Tier 1 — Direct competitors**: same problem, same customer, same core solution mechanism. Include both large and small/regional players, not just the best-known ones.

   - **Tier 2 — Indirect competitors**: same underlying problem, different solution mechanism (manual services/consulting, structurally different alternatives, substitutes competing for the same budget or decision).

   - **Tier 3 — Potential acquirers**: who would benefit strategically from acquiring this opportunity (or a similar player) and why — explain the strategic logic for each one, not just list names. Look for recent M&A/consolidation signals in the industry that support it.

   - **Tier 4 — Adjacent players**: companies not competing today but with the assets (data, distribution, customer relationship) to pivot or bolt on a competing feature quickly. Flag which ones seem most likely to move, and why.

6. **Close with:**
   - A summary table: tier | company | key risk | timeframe.
   - 3-5 strategic implications for the opportunity (where the white space is, what watch-list to prioritize, moat or data/distribution-dependency risks).
   - Sources used, as markdown links.

7. **Save the result** as a new note in the project's folder (same location as prior research, e.g. a testable-hypothesis note, if one exists; if there's no clear folder, ask where). File name in the language detected in step 3 (e.g. `Competitive Landscape.md` in English). If a competitive landscape note already exists for this opportunity, do not silently overwrite it — ask whether to update it or version it.

8. Show a brief summary of the result in the chat (do not paste the full note) along with a link to the note created.
