# Complete AI Prompts by Canvas Box
## Product Discovery for Agile Teams

This document organizes all AI prompts (Generation, Selection, and Review) by Lean Product Canvas box for easy reference.

---

## 🎯 Core Principle

**AI outputs are assumptions that must be validated, not facts to be accepted.**

Use these prompts to accelerate your discovery work, but always treat AI-generated content as assumptions requiring validation with real evidence.

---

## How to Use This Document

**Three types of prompts for each Canvas box:**

1. **GENERATION PROMPTS** (Optional)
   - Use when: You need ideas, are stuck, or want alternatives
   - AI does: Generates multiple options
   - You do: Evaluate and treat as assumptions

2. **SELECTION PROMPTS** (After Generation)
   - Use when: AI gave you too many options
   - AI does: Asks you questions about options
   - You do: Choose ONE focus + organize backlog

3. **REVIEW PROMPTS** (Recommended)
   - Use when: After you've completed work manually
   - AI does: Critiques format, clarity, identifies assumptions
   - You do: Revise your own work

---

# BOX 6: Hypotheses

## Required Format

```
"We believe that [our business outcome] can be achieved if [these users] can 
achieve [this goal or outcome] with [this feature]."
```

**Note:** Each hypothesis should focus on ONE feature only.

---

## GENERATION PROMPT: Hypotheses

**When to use:** Writing testable hypotheses, identifying embedded assumptions

```
I'm writing hypotheses (Box 6) for the Lean Product Canvas using our specific format.

The hypothesis format is:
"We believe that [our business outcome] can be achieved if [these users] can 
achieve [this goal or outcome] with [this feature]."

Here's my draft hypothesis:
[PASTE YOUR DRAFT HYPOTHESIS]

Please:
1. Critique this hypothesis - does it follow the format? Is it testable? Is it 
   specific enough?
2. Identify ALL embedded assumptions (about users, value, feasibility, business model)
3. For each assumption, rate the risk if we're wrong (high/medium/low)
4. Suggest which assumption is riskiest to test first
5. Generate 2 alternative hypothesis statements using the same format but focusing 
   on different assumptions

Be critical and specific. Each hypothesis should focus on ONE feature only.
```

**Validation Required:** Design experiments to test your riskiest assumptions. Better hypothesis statements don't make them true.

---

## SELECTION PROMPT: Hypotheses

**When to use:** After writing multiple hypothesis statements

```
I've written multiple hypotheses and need help selecting which one to test first. 
Here are my options:

[PASTE YOUR HYPOTHESIS STATEMENTS]

I need to choose ONE hypothesis to test first and organize the others as a backlog. 
Please help me think through this decision. Do NOT choose for me.

Guide me through this decision by:

1. ASSUMPTION IDENTIFICATION
   For each hypothesis, ask:
   - What are the 3-4 biggest assumptions embedded in this hypothesis?
   - Which assumptions are about VALUE (will users want this)?
   - Which assumptions are about USABILITY (can users use this)?
   - Which assumptions are about FEASIBILITY (can we build this)?
   - Which assumptions are about VIABILITY (will this work for our business)?

2. RISK ASSESSMENT
   For each hypothesis, ask:
   - If this hypothesis is WRONG, what happens?
   - Which hypothesis, if wrong, would waste the most time/money?
   - Which assumptions, if wrong, would invalidate the entire approach?

3. TEST-ABILITY
   For each hypothesis, ask:
   - How easily can we test this hypothesis?
   - Can we test the riskiest assumptions without building the full feature?
   - What evidence would prove this wrong vs. right?
   - How long would it take to gather that evidence?

4. LEARNING VALUE
   For each hypothesis, ask:
   - What would we learn from testing this?
   - Does this hypothesis, if validated, unlock other hypotheses?
   - Is this hypothesis foundational or dependent on others?

5. DECISION FRAMEWORK
   Present this as a table comparing hypotheses across:
   - Riskiest assumption type (Value/Usability/Feasibility/Viability)
   - Impact if wrong (High/Medium/Low)
   - Ease of testing (Easy/Medium/Hard)
   - Learning value (High/Medium/Low)
   - Dependencies (Foundational/Dependent)

Then ask ME: "Based on this analysis, which hypothesis will you test first and 
why? Remember: test value and usability risks before feasibility risks."

After I answer, help me organize the others as a testing sequence:
- Test 1st (your choice)
- Test 2nd (next priority)
- Test 3rd (after that)
- Parking lot (deprioritized)
```

---

## REVIEW PROMPT: Hypotheses

**When to use:** After you've written your hypothesis statements

```
I've completed Box 6 (Hypotheses) of the Lean Product Canvas. Please review my 
work and provide constructive feedback.

Here are my hypotheses:
[PASTE YOUR HYPOTHESIS STATEMENTS]

The required format for each hypothesis is:
"We believe that [our business outcome] can be achieved if [these users] can 
achieve [this goal or outcome] with [this feature]."

Note: Each hypothesis should focus on ONE feature only.

Please provide feedback on:

1. FORMAT ADHERENCE
   - Does each hypothesis follow the required format?
   - Does each hypothesis focus on only ONE feature?
   - Are all four components present (business outcome, users, user goal, feature)?
   - Do the components map to specific boxes? (outcome from Box 2, users from Box 3, 
     user goal from Box 4, feature from Box 5)

2. CLARITY
   - Is the business outcome specific and measurable?
   - Are the users clearly identified?
   - Is the user goal/outcome clear?
   - Is the feature described concretely?
   - Is this hypothesis testable?
   - Would we know if this hypothesis is true or false?

3. RISKY ASSUMPTIONS
   - Identify 2-3 of the riskiest assumptions in these hypotheses
   - For each assumption, categorize: value, usability, feasibility, business viability
   - Which assumption, if wrong, would invalidate the entire hypothesis?
   - Rank assumptions by: risk level and ease of testing

Do NOT rewrite my hypotheses. Instead, provide specific guidance on how I can 
improve them myself.
```
