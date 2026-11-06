# Founding Hypothesis — Approach and Magic Lenses (Day 2)

## Core Principle

**AI outputs are assumptions that must be validated, not facts to be accepted.** The point of this step is to avoid committing to the first idea that comes to mind: generate genuinely different approaches, compare them honestly, and keep a backup.

## Where this comes from

In the Foundation Sprint (Jake Knapp & John Zeratsky, *Click*), the second day is about the **approach**: look for alternatives to the first idea, then evaluate them with the **Magic Lenses** to pick a top bet and a backup.

Sources describe the lenses as four classic ones (customer, pragmatic, growth, money) plus at least one custom lens specific to the team's situation. Those descriptions come from secondary sources (podcast notes and community adaptations), not from the book's text, so treat the lens wording below as the kit's adaptation.

| Lens | Question it answers |
|---|---|
| **Customer experience** | Will the customer love using this? Does it solve their problem in a way they'll notice? |
| **Feasibility** (pragmatic) | Can we actually build and ship this, with our team, skills and constraints, soon enough to learn? |
| **Growth potential** | If it works, can it grow without us pushing every user in by hand? |
| **Financial viability** | Is there a believable way for this to pay for itself? |
| **Custom lens** *(optional)* | One lens specific to this situation, e.g. "Legal / licensing", "Founder conviction", "Regulatory". Ask the user if one applies. |

---

## GENERATION PROMPT: Approaches and lens evaluation

**When to use:** after the basics and differentiation are done.

```
We have these basics:
- Target customer: [CUSTOMER]
- Important problem: [PROBLEM]
- Our advantage: [ADVANTAGE]
- Most challenging competitor: [COMPETITOR]
- Differentiators: [DIFFERENTIATORS]

Help me explore the approach (the strategic "how") for solving this problem.

1. FIRST IDEA
   Ask me what approach I already have in mind and write it down as option A.

2. ALTERNATIVES
   Generate 2-3 other approaches that are GENUINELY DIFFERENT from option A —
   a different mechanism or a different angle, not the same idea with different
   features or a different brand name. Keep each at strategy level (no feature lists).

3. LENS EVALUATION
   Present a table with every approach as a row and these columns:
   Customer experience | Feasibility | Growth potential | Financial viability
   Rate each cell High / Medium / Low, with a one-line reason.
   Ask me whether a custom lens applies to our situation, and add it if so.

4. ASSUMPTIONS
   For each approach, name the single biggest assumption it depends on.

5. TOP BET AND BACKUP
   Do NOT choose for me. Ask me which approach I'd bet on and which I'd keep as
   the backup, and why. Then write both down.
```

**Output of this block:** a top bet and a backup approach, each with a one-line lens summary. These go into the sentence's `with [approach] (backup: [backup approach])`.

**Validation Required:** lens ratings are judgments, not measurements. The customer-experience cell, in particular, can only be settled by talking to customers.

---

## SELECTION PROMPT: Choosing between approaches

**When to use:** the user already has 2+ approaches (generated here or elsewhere) and needs help deciding.

```
I have several approaches for the same problem and need help deciding which to bet on.
Here they are:

[PASTE THE APPROACH OPTIONS]

Context:
- Target customer: [CUSTOMER]
- Problem: [PROBLEM]
- Most challenging competitor: [COMPETITOR]

Please help me think through this by asking me questions and showing trade-offs.
Do NOT choose for me.

1. DIFFERENCE CHECK
   - Are these genuinely different approaches, or the same idea in different clothes?
   - If two are really the same, say so and suggest merging them.

2. LENS BY LENS
   For each lens (customer experience, feasibility, growth, financial viability,
   plus any custom one), ask me the question that would reveal which option is
   strongest, and what evidence I have today.

3. COMPETITOR CHECK
   - Which approach makes our differentiators most real against the most
     challenging competitor?
   - Which approach would be easiest for that competitor to copy?

4. LEARNING SPEED
   - Which approach lets us find out we're wrong the fastest and the cheapest?

5. DECISION TABLE
   Present a table comparing the options across:
   - Customer experience (High/Medium/Low)
   - Feasibility (High/Medium/Low)
   - Growth potential (High/Medium/Low)
   - Financial viability (High/Medium/Low)
   - Speed of learning (High/Medium/Low)
   - Evidence we have today (High/Medium/Low)

Then ask ME: "Which approach will you bet on, which will you keep as the backup,
and why?"

After I answer, record the top bet, the backup, and the conditions under which I'd
switch to the backup.
```
