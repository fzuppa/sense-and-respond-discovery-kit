# Founding Hypothesis — Template and Review

## Core Principle

**A Founding Hypothesis is a bet that can be wrong, not a plan. AI outputs are assumptions that must be validated, not facts to be accepted.**

Source: Jake Knapp & John Zeratsky, *Click* (Foundation Sprint). See also [Introducing the Foundation Sprint](https://www.lennysnewsletter.com/p/introducing-the-foundation-sprint) (Lenny's Newsletter).

---

## Required Format

```
If we help [target customer] solve [important problem] with [approach]
(backup: [backup approach]), we believe they will choose it over
[competitors / alternatives] because our solution is [differentiator 1]
and [differentiator 2].
```

The `(backup: …)` part is optional but recommended: it's the second-best approach from the lens evaluation, kept as the pivot option if the top bet fails.

> **Note on wording.** This is the "If we help…" version used by community adaptations of the Foundation Sprint. The authors describe the hypothesis as a fill-in-the-blank sentence combining customer, approach and differentiation; their exact wording is in the book. To use the book's wording, replace the block above and keep the rest.

## What each slot must contain

| Slot | Must be | Not this |
|---|---|---|
| **Target customer** | Real people described in plain language, specific enough to go and find and talk to this week | "Everyone", "users", "SMBs", a job title with no situation |
| **Important problem** | Painful enough that it justifies the cost of trying something new | A nice-to-have, a feature gap, a restated solution |
| **Approach** | The *how*, at strategy level: the angle you take to solve the problem | A feature list or a technology name on its own |
| **Competitors / alternatives** | Real alternatives the customer uses today, **including workarounds and "do nothing"** | Only look-alike products |
| **Differentiators** | 1-2 things that are true, specific, relative to the named competitor, and that the customer cares about | "Better UX", "easier to use", "AI-powered", anything every competitor also claims |

## Quality check: "Could a competitor say the same sentence?"

If a competitor could swap their name into the "because our solution is…" part and it would still read true, the differentiator is not a differentiator yet. Good differentiators are *contrasts*: "as instant as piracy, but legal" only works against a specific competitor and a specific customer.

---

## GENERATION PROMPT: Founding Hypothesis sentence

**When to use:** after the basics, differentiation and approach have been worked through (see the other reference files) and you need to assemble the sentence.

```
I'm writing a Founding Hypothesis. Here is what we've agreed on so far:
- Target customer: [CUSTOMER]
- Important problem: [PROBLEM]
- Our advantage: [WHY WE, SPECIFICALLY]
- Competitors / alternatives (most challenging marked): [COMPETITORS]
- Differentiators: [DIFFERENTIATORS]
- Approach (top bet) and backup: [APPROACH] / [BACKUP]

Assemble 1-2 candidate sentences using this EXACT format:

"If we help [target customer] solve [important problem] with [approach]
(backup: [backup approach]), we believe they will choose it over
[competitors / alternatives] because our solution is [differentiator 1]
and [differentiator 2]."

Then:
1. Flag any slot that is vague, generic, or that a competitor could claim as well
2. List the assumptions each sentence is making
3. Do NOT add features, and do NOT invent facts that I haven't given you — if a slot is empty, leave it marked as an assumption to validate
```

**Validation Required:** the sentence is a hypothesis. It earns credibility only through the scorecard (see `scorecard.md`) and real evidence.

---

## REVIEW PROMPT: Founding Hypothesis

**When to use:** after the user has written their hypothesis.

```
I've written a Founding Hypothesis. Please review my work and give constructive feedback.

Here is my hypothesis:
[PASTE THE COMPLETE HYPOTHESIS]

The required format is:
"If we help [target customer] solve [important problem] with [approach]
(backup: [backup approach]), we believe they will choose it over
[competitors / alternatives] because our solution is [differentiator 1]
and [differentiator 2]."

Please provide feedback on:

1. FORMAT ADHERENCE
   - Does it follow the required format?
   - Which slots are missing or incomplete?

2. SPECIFICITY OF EACH SLOT
   - Customer: could I go and find these people this week? Or is it a broad segment?
   - Problem: is it painful enough to justify trying something new, or is it a nice-to-have?
   - Approach: is it a strategic "how", or a feature list / a technology?
   - Competitors: does the list include workarounds and "do nothing", or only look-alike products?
   - Differentiators: are they specific and relative to a named competitor? Would the customer care?

3. THE COMPETITOR SWAP TEST
   - Could the most challenging competitor say the same "because our solution is…"?
     If yes, point out which differentiator fails and why.

4. COHERENCE
   - Do the differentiators actually address the stated problem for that customer?
   - Does the approach plausibly deliver the differentiators?
   - Is it a falsifiable bet (could it turn out to be wrong), or a statement of intent
     in disguise ("we will succeed")?

5. RISKY ASSUMPTIONS
   - Identify the 2-3 beliefs that, if wrong, would sink this hypothesis
   - For each, say why it's risky and what evidence would test it
     (see the scorecard format in scorecard.md)

Do NOT rewrite my hypothesis. Instead, give me specific guidance on how I can
improve it myself.
```
