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

# BOX 5: Solutions/Features

## Purpose

Contain solution ideas, typically specified as headlines or simple brainstorm ideas.

---

## GENERATION PROMPT: Solutions/Features

**When to use:** Brainstorming feature ideas, evaluating solution concepts

```
Based on my Lean Product Canvas so far:
- Business Problem (Box 1): [BRIEF SUMMARY]
- Users (Box 3): [BRIEF PERSONA]  
- User Outcomes/JTBD (Box 4): [WHAT THEY'RE TRYING TO DO]

Generate 10 feature ideas that could address this need. For each:
1. Brief feature description
2. What user outcome it addresses
3. Key assumptions this feature makes
4. What could make this feature fail

Include both obvious and creative ideas.
```

**Validation Required:** Test feature concepts with customers before building. Don't build features just because AI suggested them.

---

## SELECTION PROMPT: Solutions/Features

**When to use:** After Generation Prompt gives you 10+ feature ideas

```
I've generated multiple feature ideas and need help selecting which one(s) to 
prototype/test first. Here are my options:

[PASTE YOUR 10+ FEATURE IDEAS]

Context from my Canvas:
- Users (Box 3): [BRIEF PERSONA]
- User Outcomes (Box 4): [KEY USER OUTCOMES]

I need to choose 1-3 features to focus on and organize the others as a backlog. 
Please help me think through this decision. Do NOT choose for me.

Guide me through this decision by:

1. USER OUTCOME ALIGNMENT
   For each feature, ask:
   - Which user outcome from Box 4 does this address?
   - How directly does it help users achieve their goal?
   - Are any features solving problems users don't have?

2. ASSUMPTION RISK
   For each feature, ask:
   - What's the riskiest assumption this feature makes?
   - What must be true about users for this to work?
   - What must be true about technology/business model?
   - Which features make the biggest leaps in assumptions?

3. TEST-ABILITY
   For each feature, ask:
   - How easily could we test this with an MVP/prototype?
   - What's the cheapest way to validate this idea?
   - Which features could we test in 1 week vs. 1 month?

4. VALUE VS. COMPLEXITY
   For each feature, estimate:
   - Potential value to users (High/Medium/Low)
   - Potential value to business (High/Medium/Low)
   - Complexity to build (High/Medium/Low)
   - Complexity to test (High/Medium/Low)

5. DECISION FRAMEWORK
   Present this as a 2x2 matrix:
   - X-axis: Risk/Uncertainty (Low to High)
   - Y-axis: Potential Value (Low to High)
   Plot each feature and identify which are in "High Value, High Risk" quadrant 
   (test these first)

Then ask ME: "Based on this analysis, which 1-3 features will you test first 
and why? Remember: test high-value, high-risk ideas first."

After I answer, help me organize the others as a backlog categorized by:
- High priority (test next)
- Medium priority (test later)
- Low priority / parking lot (maybe never)
```

---

## REVIEW PROMPT: Solutions/Features

**When to use:** After you've brainstormed solution ideas

```
I've completed Box 5 (Solutions/Features) of the Lean Product Canvas. Please 
review my work and provide constructive feedback.

Here are my solution ideas:
[PASTE YOUR FEATURE LIST]

Context: This box contains solution ideas, typically as headlines or simple 
brainstorm ideas.

Please provide feedback on:

1. FORMAT ADHERENCE
   - Are these expressed as simple headlines or ideas?
   - Are they at the right level of detail (not too specific, not too vague)?
   - Are they solutions/features, not problems or outcomes?

2. CLARITY
   - Can someone understand what each solution is from the headline?
   - Are they distinct from each other?
   - Do they connect to the user outcomes in Box 4?
   - Do they address the business problem in Box 1?
   - Is there sufficient variety in approaches?

3. RISKY ASSUMPTIONS
   - Identify 2-3 assumptions across these solutions
   - For each solution, what must be true for it to work?
   - Which solutions make the biggest leaps in assumptions?
   - What user behaviors are we assuming will happen?

Do NOT rewrite my solutions. Instead, provide specific guidance on how I can 
improve them myself.
```
