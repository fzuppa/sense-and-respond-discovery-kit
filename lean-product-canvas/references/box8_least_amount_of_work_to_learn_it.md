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

# BOX 8: Least Amount of Work to Learn It

> **Main canvas vs. problem canvas:** in the product's main canvas, the experiment identified here is typically the product's first MVP — its name/focus commonly becomes the seed for the first problem canvas (`lean-product-canvas-<problem-name>.md`). In a problem canvas, this box is the concrete experiment for that specific problem.

## Purpose

Specify the experiment to de-risk your hypothesis. Focus on what you could learn in 1 day / 1 week / 1 month.

---

## GENERATION PROMPT: Experiments (MVPs)

**When to use:** Designing experiments, planning MVPs

```
I need to test this assumption: [STATE YOUR ASSUMPTION FROM BOX 7]

Context:
- My hypothesis (Box 6): [STATE HYPOTHESIS]
- What I need to learn (Box 7): [STATE LEARNING GOAL]

Help me design an experiment by:
1. Suggesting 3 different experiment approaches (cheap/fast/different methods)
2. For each approach:
   - What exactly would I do?
   - Who would I do it with (what users)?
   - What would I measure/observe?
   - What would validate the assumption?
   - What would invalidate the assumption?
   - Timeline (1 day / 1 week / 1 month)
3. For each approach, identify potential biases or validity threats
4. Rank approaches by: speed to insight, cost, and quality of learning

Focus on the LEAST amount of work needed to learn. What's the minimum viable test?
```

**Validation Required:** RUN THE EXPERIMENT. Collect real data from real users. Don't rationalize results after the fact.

---

## SELECTION PROMPT: Experiments

**When to use:** After Generation Prompt suggests multiple experiment approaches

```
I need to test this assumption: [STATE YOUR ASSUMPTION FROM BOX 7]

AI has suggested multiple experiment approaches:
[PASTE EXPERIMENT OPTIONS]

I need to choose ONE experiment approach to run first. Please help me think through 
this decision. Do NOT choose for me.

Guide me through this decision by:

1. VALIDITY CHECK
   For each experiment, ask:
   - Does this actually test the assumption from Box 7?
   - What could we learn from this experiment?
   - What WON'T we learn?
   - Could this give us false positive or false negative results?

2. RESOURCE REQUIREMENTS
   For each experiment, ask:
   - How much time will this take?
   - What access to users/customers do we need?
   - What tools or materials do we need?
   - Do we have these resources available now?

3. SPEED TO INSIGHT
   For each experiment, ask:
   - How quickly will we get results?
   - Can we run this in 1 day / 1 week / 1 month?
   - How many participants do we need?
   - How long to recruit participants?

4. BIAS POTENTIAL
   For each experiment, ask:
   - What biases could affect results?
   - Are we at risk of confirmation bias?
   - Could participants tell us what they think we want to hear?
   - How can we design for honest feedback?

5. DECISION FRAMEWORK
   Present this as a table comparing experiments across:
   - Directly tests assumption (Yes/Partial/No)
   - Time to complete (Days/Weeks/Months)
   - Resource requirements (Low/Medium/High)
   - Risk of bias (Low/Medium/High)
   - Quality of insight (High/Medium/Low)

Then ask ME: "Based on this analysis, which experiment will you run first and why? 
Consider: the best experiment is the fastest one that gives you valid results."

After I answer, suggest how to refine the chosen experiment to reduce bias and 
increase speed.
```

---

## REVIEW PROMPT: Experiments (Box 8)

**When to use:** After you've designed your experiment

```
I've completed Box 8 (Least Amount of Work to Learn It) of the Lean Product Canvas. 
Please review my work and provide constructive feedback.

Here is my experiment design:
[PASTE YOUR EXPERIMENT DESCRIPTION]

Context from Box 7 - What I need to learn:
[PASTE YOUR BOX 7 CONTENT]

Remember: Box 8 should specify the experiment to de-risk the hypothesis. Focus on 
the LEAST amount of work needed to learn. Think: what could you learn in 1 day / 
1 week / 1 month?

Please provide feedback on:

1. FORMAT ADHERENCE
   - Is this an experiment (not a full feature build)?
   - Is it clearly described with concrete steps?
   - Does it include what you'll measure/observe?
   - Is there a timeline (1 day/week/month)?

2. CLARITY
   - Does this experiment actually test the assumption from Box 7?
   - What exactly will you do?
   - Who will you do it with (what users)?
   - What will you observe/measure?
   - What result would validate the assumption?
   - What result would invalidate the assumption?
   - Is this truly the MINIMUM needed to learn, or could it be simpler?

3. RISKY ASSUMPTIONS
   - Identify 2-3 assumptions embedded in the experiment design itself
   - What are we assuming about user willingness to participate?
   - What biases might affect results?
   - What could give us false positive or false negative results?
   - Are we at risk of confirming what we want to believe?

Do NOT rewrite my experiment. Instead, provide specific guidance on how I can 
improve it myself.
```
