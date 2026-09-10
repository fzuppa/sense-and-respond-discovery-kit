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

# BOX 1 (ALTERNATE FORMAT): Business Opportunity Statement

## When to Use This Instead of the Business Problem Statement

Use the Business Opportunity Statement instead of the Business Problem Statement when there's no existing product/service to improve — you're building something genuinely new from scratch, with no baseline to observe. This is rarer than it seems: most situations, even ones that feel "new," turn out to be improving something that already exists. Try the Business Problem Statement first; only switch to this format if it genuinely doesn't fit.

Source: [Business Problem Statements vs Opportunity Statements](https://jeffgothelf.com/blog/business-problem-statement-opportunity-statement/) — Jeff Gothelf.

## Required Format

```
The current state of [domain] has focused mainly on [segments, pain points, etc.].
What existing products/services fail to address is [this gap]. Our product/service
will address this gap by [vision/strategy]. Our initial focus will be [this segment].
We'll know we are successful when we see [these behaviors].
```

---

## GENERATION PROMPT: Business Opportunity Statement

**When to use:** Framing a genuinely new product/initiative that has no existing baseline to improve

```
I'm working on defining a business opportunity using the Lean Product Canvas, for
something we're building from scratch (no existing product/service to improve).
Here's my situation:
[DESCRIBE YOUR SITUATION - e.g., "We want to enter the corporate wellness market.
There's no existing product of ours here — we'd be starting from zero."]

Help me create Business Opportunity Statements using this EXACT format:

"The current state of [domain] has focused mainly on [segments, pain points, etc.].
What existing products/services fail to address is [this gap]. Our product/service
will address this gap by [vision/strategy]. Our initial focus will be [this segment].
We'll know we are successful when we see [these behaviors]."

Please:
1. Generate 2-3 different opportunity statements using this exact format
2. For each statement, identify what assumptions are being made about the gap and the segment
3. Note what evidence would validate that this gap is real and unaddressed
4. Keep the strategy at the level of vision/approach — avoid prescribing specific features

Use the exact format above. I need opportunity statements, not a feature list.
```

**Validation Required:** Gather evidence (market research, customer conversations, competitive analysis) that the gap is real and that your initial segment actually experiences it.

---

## SELECTION PROMPT: Business Opportunity Statement

**When to use:** After the Generation Prompt gives you 2-3 opportunity statement options

```
I've generated multiple business opportunity statement options and need help selecting
which one to focus on first. Here are my options:

[PASTE YOUR 2-3 OPPORTUNITY STATEMENT OPTIONS]

I need to choose ONE to focus on and organize the others as a backlog. Please help
me think through this decision by asking me questions and showing trade-offs.
Do NOT choose for me.

Guide me through this decision by:

1. EVIDENCE CHECK
   For each option, ask:
   - What evidence do I currently have that this gap really exists?
   - What would I need to validate to confirm this gap and segment?
   - Which option has the most existing evidence?

2. IMPACT ANALYSIS
   For each option, ask:
   - If we capture this opportunity, what business impact would we see?
   - Which opportunity, if captured, creates the most value?
   - Which opportunity is most urgent vs. most strategic?

3. FEASIBILITY CHECK
   For each option, ask:
   - Do we have the capability/right to compete in this space?
   - What's in our control vs. outside our control?
   - Which opportunity can we realistically pursue with our current resources?

4. FOCUS TEST
   Help me consider:
   - Which opportunity, if we focus on it exclusively for the next few months, would matter most?
   - Which opportunities might actually be facets of the same underlying opportunity?
   - Which opportunity is most foundational for future ones?

5. DECISION FRAMEWORK
   Present this as a table comparing options across:
   - Existing evidence (High/Medium/Low)
   - Potential business impact (High/Medium/Low)
   - Our ability to pursue it (High/Medium/Low)
   - Strategic importance (High/Medium/Low)

Then ask ME: "Based on this analysis, which opportunity statement will you focus on
first and why?"

After I answer, help me organize the others as a backlog with notes on when to
revisit each.
```

---

## REVIEW PROMPT: Business Opportunity Statement

**When to use:** After you've written your business opportunity statement

```
I've completed Box 1 (Business Opportunity Statement) of the Lean Product Canvas.
Please review my work and provide constructive feedback.

Here is my business opportunity statement:
[PASTE YOUR COMPLETE OPPORTUNITY STATEMENT]

The required format is:
"The current state of [domain] has focused mainly on [segments, pain points, etc.].
What existing products/services fail to address is [this gap]. Our product/service
will address this gap by [vision/strategy]. Our initial focus will be [this segment].
We'll know we are successful when we see [these behaviors]."

Please provide feedback on:

1. FORMAT ADHERENCE
   - Does my statement follow the required format?
   - Which sections are missing or incomplete?
   - Are all the template elements present?

2. CLARITY
   - Is the current state of the domain clearly described?
   - Is the gap specific and credible, or vague?
   - Is the strategy described at the vision level, without prescribing specific features?
   - Is the initial segment concrete enough to go find and talk to?
   - Are the success behaviors specific and observable?

3. RISKY ASSUMPTIONS
   - Identify 2-3 assumptions embedded in this opportunity statement
   - For each assumption, note why it's risky if wrong
   - Suggest what evidence would test each assumption

4. FIT CHECK
   - Is this genuinely a new-from-scratch situation, or is there an existing product/baseline hiding in here that would make the Business Problem Statement format a better fit?

Do NOT rewrite my opportunity statement. Instead, provide specific guidance on how
I can improve it myself.
```
