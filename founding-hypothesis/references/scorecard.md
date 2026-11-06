# Founding Hypothesis — Assumption Scorecard

## Core Principle

**A hypothesis nobody tries to refute is just an opinion.** The scorecard turns the sentence into the list of beliefs that must be true, and says how each could be proven wrong.

## What the scorecard asks

The Founding Hypothesis bundles five beliefs. The scorecard asks, for each one, whether it's true:

1. **Right customer** — are these the right people to start with?
2. **Right problem** — is the problem real and painful for them?
3. **Right approach** — does this approach actually solve that problem?
4. **They'll choose us** — will they pick us over the competition (including workarounds and "do nothing")?
5. **They care about our differentiators** — do the differences we claim matter to their choice?

> **Note on provenance.** The authors' own scorecard format wasn't available in sources I could verify. The five questions above follow the structure of the Foundation Sprint hypothesis; the table columns below are the kit's own adaptation, in line with community adaptations that pair each belief with reasons to believe it, what could prove it wrong, and a next validation step. Check against *Click* if the exact format matters.

## Format (what gets saved in the file)

```markdown
| # | Belief | Why we believe it | What would prove us wrong | Risk | Next step |
|---|---|---|---|---|---|
| 1 | Right customer: … | Evidence we have today, or "assumption" | An observable result that would refute it | High / Med / Low | The cheapest test that could refute it |
| 2 | Right problem: … | … | … | … | … |
| 3 | Right approach: … | … | … | … | … |
| 4 | They'll choose us over …: … | … | … | … | … |
| 5 | They care about [differentiators]: … | … | … | … | … |
```

Rules for filling it in:

- **Why we believe it** must separate *evidence* (something observed: an interview, data, a market fact) from *assumption* (something we hope). If it's an assumption, write "assumption".
- **What would prove us wrong** must be observable. "If customers don't like it" is not observable; "if fewer than 3 of 10 interviewees currently work around this problem weekly" is.
- **Risk** = how badly the hypothesis breaks if the belief is wrong × how little evidence we have. Rank honestly: the riskiest belief is usually one of the last two.
- **Next step** is the *cheapest* test that could refute the belief, not the most thorough one. Name the test type (customer interviews, concierge test, prototype shown, fake door, technical spike, buyer conversation), but don't run it unless asked.
- Mark the single **riskiest belief** with a ⚠️ — that's the one to test first.

---

## GENERATION PROMPT: Build the scorecard

**When to use:** the sentence is written and the user wants to know what to test.

```
Here is my Founding Hypothesis:
[PASTE THE HYPOTHESIS]

Basics and context:
[CUSTOMER / PROBLEM / COMPETITORS / DIFFERENTIATORS / APPROACH — or use what's in the file]

Build an assumption scorecard with exactly these five beliefs: right customer,
right problem, right approach, they'll choose us over the competition, they care
about our differentiators.

For each belief, fill in:
1. Why we believe it — separating EVIDENCE from ASSUMPTION. If I haven't given you
   evidence, write "assumption" — do not invent evidence
2. What would prove us wrong — an observable result, not a feeling
3. Risk (High/Medium/Low) — consider both impact if wrong and how little evidence we have
4. Next step — the cheapest test that could refute it

Then:
- Mark the single riskiest belief and explain in one line why it's the riskiest
- Do NOT claim any belief is validated. Everything here is a hypothesis until real
  evidence says otherwise
```

**Validation Required:** the scorecard's value comes from running the test on the riskiest belief and updating the table with what happened, including when the result says "we were wrong".
