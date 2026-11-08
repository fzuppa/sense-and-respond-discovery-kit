# Capturing a Problem — Interview Guide

Used by the **Capture** mode (see `SKILL.md` → "Capturing a problem"). The goal is to collect, through questions, everything needed to write one **Business Problem Statement** for a product that already exists, plus the evidence and assumptions behind it.

The statement format is the one in `box1_business_problem_statement.md` — translate it into the output language keeping its structure intact:

```
[Our service/product] was designed to achieve [these goals]. We have observed
[in this way] that the product/service isn't meeting these goals which is causing
[this adverse effect/problem] to our business. How might we improve service/product
so that our customers are more successful as determined by [these measurable changes
in their behavior]?
```

## Rules

- **One question at a time.** Wait for the answer before asking the next one. If the user already gave an answer in their first message (e.g. "Erin can't get a clean report of which providers to use on big orders"), don't ask it again — confirm it and move on.
- **Problem, not solution.** If an answer can be built ("they need a dashboard", "add an export"), ask what problem that would solve for the customer, and use that. Park the solution as a note for the user, don't put it in the statement.
- **Concrete over vague.** Push once for specifics when an answer is vague ("it's confusing", "it takes long"): what exactly happens, how often, how much?
- **Never invent evidence.** If the user doesn't know or didn't observe it directly, write it down as unknown or `unverified`. A record full of `unverified` signals is fine — it just has more assumptions.
- **Don't draft until every slot below has an answer** (an honest "unknown" counts for slots 2 and 5, not for slots 1, 3 and 4).

## Questions, by statement slot

Ask them in this order. Wording is a guide — adapt it to the conversation and the output language.

### 1. `[Our service/product] was designed to achieve [these goals]`
- Which product or service is this about? *(skip if already clear)*
- What is it supposed to achieve for its customers? What goal did it set out to meet?

### 2. `We have observed [in this way] that it isn't meeting these goals`
- How did you notice this? Who saw it, when, and where (a conversation, support tickets, usage data, a feedback session…)?
- Is that direct observation (`real`), survey results (`survey`), market research (`secondary`), a synthetic persona/interview (`synthetic`), or something someone told you (`unverified`)? Is there a file or link?

Each answer becomes a row in the **Evidence** table (signal, provenance, source).

### 3. `causing [this adverse effect/problem] to our business`
- What does this cost the business as a result? (lost conversions, churn, support load, slower adoption, revenue not realized…)
- Can it be measured today? With which number or proxy?

### 4. `measurable changes in their behavior`
- If this problem were solved, what would customers do differently that you could observe?
- What number would move, and roughly how much would count as success?

### Context (goes in "Who suffers it" and "Open assumptions", not in the statement)
- Who exactly suffers it — which persona or segment, and in what situation does it show up? Are there people who don't suffer it?
- What do they do today to get around it?
- What would have to be true for this to be the real problem rather than a symptom of something else? What would show it's not?

## After the interview

1. Draft the statement with the answers, in the exact format above.
2. Show it together with the **Evidence** table and the **Open assumptions** (2–3 items, each with the evidence that would test it).
3. Offer the Box 1 Review prompt; run it only if the user accepts.
4. Ask for the problem name (short, kebab-case), then save per `SKILL.md`.

Remember the canvas principle: the statement is an assumption to validate, not a fact.
