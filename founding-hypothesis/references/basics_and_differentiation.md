# Founding Hypothesis — The Basics and Differentiation (Day 1)

## Core Principle

**AI outputs are assumptions that must be validated, not facts to be accepted.** When the user doesn't know an answer, record it as an assumption to validate; don't invent it for them.

## Where this comes from

In the Foundation Sprint (Jake Knapp & John Zeratsky, *Click*), the first day covers "the basics" — customer, problem, your advantage, competition — followed by differentiation. Per [Lenny's Newsletter](https://www.lennysnewsletter.com/p/introducing-the-foundation-sprint), each basics step is timeboxed (roughly 15-20 minutes) and run with Note-and-Vote: silent writing, silent dot-voting, a short debate, and then the **Decider** (the person with final say) makes the call.

The questions below are the kit's own adaptation, to be run as a guided conversation instead of a workshop. If the user has a team, suggest running each step with Note-and-Vote and naming a Decider; if they're working alone, they are the Decider.

---

## GENERATION PROMPT: The basics

**When to use:** starting a Founding Hypothesis from scratch. Ask **one step at a time**, wait for the answer, reflect it back, then move on.

```
We're going to work through the basics of a Founding Hypothesis, one step at a time.
Context about the opportunity:
[DESCRIBE THE OPPORTUNITY / PRODUCT IDEA — or use what's already in the project]

Step 1 — TARGET CUSTOMER
Ask me: Who, specifically, are the people we want to help first? Describe them in plain
language, as real people in a real situation. Could I find ten of them this week?
Push back if I answer with a broad segment.

Step 2 — IMPORTANT PROBLEM
Ask me: What problem do these people have that is painful enough that they'd pay the
cost of trying something new (time, money, habit change, risk)? What do they do today
about it? Push back if the "problem" is really a missing feature or a solution in disguise.

Step 3 — OUR ADVANTAGE
Ask me: Why us? What capability, insight, access, or motivation do we have that
others don't? Be honest about whether it's a real advantage or just enthusiasm.

Step 4 — COMPETITORS
Ask me: What does the customer do today instead of using us? List direct competitors,
indirect ones, workarounds (spreadsheets, manual processes, asking a friend), and
"do nothing". Then ask: which one is the most challenging for us, and why?
```

After each step, reflect back a one-line summary and mark anything the user isn't sure about as **an assumption to validate**.

---

## GENERATION PROMPT: Differentiation

**When to use:** after the four basics are filled in.

```
Based on the basics we've agreed on:
- Target customer: [CUSTOMER]
- Important problem: [PROBLEM]
- Our advantage: [ADVANTAGE]
- Competitors, with the most challenging marked: [COMPETITORS]

Help me find our differentiators. Ask me, one at a time:

1. What does the most challenging competitor do well for this customer? (Be generous.)
2. Where does that competitor fall short for this customer's problem?
3. What could we do that this competitor can't or won't — because of its model,
   its history, or its incentives?
4. Of those things, which would this customer actually notice and care about?

Then propose 2-4 candidate differentiators and, for each:
- name the competitor it is relative to
- run the swap test: "Could that competitor say the same thing about itself?"
  If yes, discard or sharpen it
- flag whether it comes from a real advantage of ours or from wishful thinking

Finish by asking me to pick the strongest 1-2. Do NOT pick for me.
```

**Output of this block:** customer, problem, advantage, competitors (most challenging marked), and 1-2 differentiators. Then move to `approach_magic_lenses.md`.
