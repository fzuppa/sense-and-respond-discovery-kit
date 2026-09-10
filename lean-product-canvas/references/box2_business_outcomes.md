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

# BOX 2: Business Outcomes

## Key Definition

**An outcome is "a measurable change in human behavior that creates value"**

## Required Format

```
[Who] [Does What] [By How Much]

Where:
- Who = the person doing the behavior
- Does What = the specific behavior
- By How Much = the measurable change in amount/number
```

---

## GENERATION PROMPT: Business Outcomes

**When to use:** Brainstorming measurable outcomes, defining success metrics

```
Our business problem is: [INSERT YOUR PROBLEM STATEMENT FROM BOX 1]

Help me define business outcomes (Box 2) using the Lean Product Canvas format.

Remember: An outcome is "a measurable change in human behavior that creates value."

Generate 5 potential business outcomes using this EXACT format:
[Who] [Does What] [By How Much]

Where:
- Who = the person doing the behavior
- Does What = the specific behavior
- By How Much = the measurable change in amount/number

For each outcome:
1. Write it in the format above
2. Identify what assumptions it makes
3. Note what data we'd need to measure this
4. Indicate if it's a leading or lagging indicator

Example: "New users complete onboarding 40% more often" 
(Who: new users | Does What: complete onboarding | By How Much: 40% more often)
```

**Validation Required:** Confirm you can actually measure these metrics and document current baselines.

---

## SELECTION PROMPT: Business Outcomes

**When to use:** After Generation Prompt gives you 5+ outcome options

```
I've generated multiple business outcome options and need help selecting which 
one(s) to focus on first. Here are my options:

[PASTE YOUR 5+ OUTCOME OPTIONS]

I need to choose 1-3 outcomes to focus on and organize the others as a backlog. 
Please help me think through this decision by asking me questions. Do NOT choose for me.

Guide me through this decision by:

1. MEASURABILITY CHECK
   For each outcome, ask:
   - Can we measure this today?
   - If not, how hard would it be to start measuring?
   - Do we have baseline data?
   - Which outcomes are easiest to track?

2. LEADING VS. LAGGING
   For each outcome, ask:
   - Is this a leading indicator (predicts future success) or lagging indicator 
     (shows past results)?
   - How quickly would we see movement in this metric?
   - Which outcomes give us the fastest feedback?

3. CONNECTION TO PROBLEM
   For each outcome, ask:
   - How directly does this outcome indicate we've solved our business problem (Box 1)?
   - Which outcomes are most relevant to our specific problem?
   - Are any outcomes too far downstream from the problem?

4. BEHAVIOR FOCUS
   For each outcome, check:
   - Is this truly a behavior change or just a metric?
   - Whose behavior needs to change?
   - Is the behavior change within our influence?

5. DECISION FRAMEWORK
   Present this as a table comparing outcomes across:
   - Currently measurable (Yes/No)
   - Leading or Lagging indicator
   - Direct link to problem (High/Medium/Low)
   - True behavior change (Yes/No)
   - Speed of feedback (Fast/Medium/Slow)

Then ask ME: "Based on this analysis, which 1-3 outcomes will you focus on and why? 
Consider: you need at least one leading indicator."

After I answer, help me organize the others as a backlog.
```

---

## REVIEW PROMPT: Business Outcomes

**When to use:** After you've written your business outcomes

```
I've completed Box 2 (Business Outcomes) of the Lean Product Canvas. Please review 
my work and provide constructive feedback.

Here are my business outcomes:
[PASTE YOUR OUTCOMES LIST]

The required format for each outcome is:
[Who] [Does What] [By How Much]

Where:
- Who = the person doing the behavior
- Does What = the specific behavior
- By How Much = the measurable change in amount/number

Remember: An outcome is "a measurable change in human behavior that creates value"

Please provide feedback on:

1. FORMAT ADHERENCE
   - Does each outcome follow the [Who] [Does What] [By How Much] format?
   - Which outcomes are missing components?
   - Are the components clearly separated?

2. CLARITY
   - Is "Who" specific enough? (not just "users" but which users?)
   - Is "Does What" a clear, observable behavior?
   - Is "By How Much" measurable and realistic?
   - Does each outcome represent a behavior change (not just a feature)?
   - Are these leading or lagging indicators?

3. RISKY ASSUMPTIONS
   - Identify 2-3 assumptions across all these outcomes
   - For each assumption, note why it's risky if wrong
   - Suggest what data or evidence would test each assumption

Do NOT rewrite my outcomes. Instead, provide specific guidance on how I can 
improve them myself.
```
