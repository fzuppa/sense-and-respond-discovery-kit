# Impact-to-Outcome mapping — method

Reference for `SKILL.md`. Read it before the first interview question.

## Sources and what is certain

- **Jeff Gothelf, [Why you should map outcomes to impact metrics](https://jeffgothelf.com/blog/why-you-should-map-outcomes-to-impact-metrics/)** (the post and its diagram). The post says: *an outcome is a measure of human behavior*; *impact metrics are the high-level measures of the health of the business*. The words **lagging** and **leading** appear only in the diagram's legend, not in the text.
- **Josh Seiden, *Outcomes Over Output*.** An outcome is a change in human behavior that drives business results. The `[Who] [does what]` shape comes from here; the Lean Product Canvas's Box 2 extends it to `[Who] [Does What] [To What Extent]`.
- Gothelf & Seiden, *Sense & Respond* and *Lean UX* are the wider frame (outcome-driven teams, hypotheses over requirements). The exact wording of the diagram's legend is in `SKILL.md`.
- The distinction between *what the post defines* and *what the diagram shows* matters: when the user asks "where does lagging/leading come from", answer with this.

## Definitions

| Term | Meaning here | Looks like | Is not |
|---|---|---|---|
| **Impact metric** | A high-level measure of the health of the business. How we know the strategy worked. | Revenue, Profit Margin, Churn, Customer Lifetime Value | A behavior, a feature, a project |
| **Outcome (lagging)** | A customer behavior we can observe and measure that indicates we are going to reach the impact metric. Closer to the impact, slower to move. | Customer renews annual membership | A business metric, a feature |
| **Outcome (leading)** | A customer behavior that leads to the behavior above it. Earlier, more frequent, closer to what the team can influence. | Customer clicks renewal email link | A feature ("renewal email"), an activity of the team |
| **Output** | What the team builds or ships. Not on this map. | The renewal email, the new widget | An outcome |

"Lagging" and "leading" are **relative**, not absolute: a behavior is leading *with respect to the node above it*. The same behavior can be lagging for the one below.

## Quality checks

Run them silently on every node the user proposes. If one fails, say which one and why in a single line, and ask how to reword it. Never rewrite silently, and never block: the user decides.

### Impact metrics
1. **Business health.** Is it a measure of the business (money, retention, cost, margin) rather than a customer behavior? If it is a behavior ("users log in more"), it belongs one level down.
2. **Measurable.** Could someone read its value today or after the next period?
3. **Few.** Two or three. More than four loses focus.
4. **Not a project.** "Launch the new app" is an output.

### Outcomes (lagging and leading)
1. **Who + does what.** Is there an actor (usually the customer, sometimes an internal user) and an observable verb? "Better personalization" has neither.
2. **Behavior, not feature.** If it names a screen, button, campaign or release, it is an output. Ask: *what would the person do differently because of it?* and use that.
3. **Observable.** Could we see it in data, a session recording or an interview? "Customer feels valued" is a feeling; "Customer replies to the survey" is a behavior.
4. **Causal link to the parent.** Would more of this behavior plausibly produce more of the one above? State it as a hypothesis, e.g. *"if more customers click the renewal email link, more of them will renew"*.
5. **Right level.** Leading outcomes should come earlier, happen more often, and be closer to what the team can influence than their parent. If a node is as far from the team as its parent, it is probably the same level.
6. **One behavior per node.** "Customer views and clicks" is two nodes.
7. **No numbers in the text.** "Users receive ads in realtime 20% more" is a behavior plus a target: the behavior goes in the text and the number goes in baseline/target.

### Structure
- Every lagging outcome should end up with at least one leading outcome (report the ones that don't).
- An outcome with several parents is fine (it is visible in the diagram), but check it is really one behavior and not two.
- Keep the map about **behavior**, not features and launches (Gothelf). Features come later, as the ideas to move an outcome.

## Suggestions (levels 2 and 3, and metric names)

Only when the user says yes, and ask before brainstorming alone.

- Give **3 to 5** options, in `[Who] [does what]` format, in the output language. Different from each other (different stages of the journey, different actors), not variations of one idea.
- Under each option, one line: **why it would move the parent** and **what it rests on**: *the user's words* / *project material (cite the file)* / *general reasoning*. Say so when it is general reasoning.
- Present them as **hypotheses**. The canvas principle of the kit: AI-generated content is an assumption to validate, not a fact.
- The user picks, edits or discards. Nothing goes into the map until they say so. Don't number-crunch: no invented baselines, targets, conversion rates or benchmarks, even as "typical" ones.
- If the user's context is thin (no product description, no journey), ask one question about the journey first instead of generating generic options.
- For leading outcomes, look at the steps **just before** the parent behavior in the customer's journey. For lagging outcomes, look at the behaviors that are visible in the data and that precede the business metric.

## Review (when the user asks for feedback on a finished or hand-drawn map)

Don't rewrite the map. Go through, in this order, and give specific guidance:
1. Impact metrics: business health, measurable, few.
2. Each outcome against the outcome checks, quoting the node.
3. Structure: lagging outcomes with no leading outcomes, nodes with no metric, a chain deeper than the team can act on, outcomes that look like features.
4. Which outcomes look like the best candidates to prioritize: the ones the team can influence directly and that sit under the strategy's impact metrics. Give the reasoning; the choice is the user's.
5. The riskiest hypothesis on the map (the causal link you believe least) and the cheapest way to check it with data or a quick experiment.

## Example (from Gothelf's diagram)

```
Revenue
├─ Customer adds item to cart                  (lagging)
│  ├─ Customer views product page              (leading) ⇄ Customer clicks related item link
│  │  ├─ Customer logs in                      (leading, earlier)
│  │  └─ Customer clicks referral link         (leading, earlier)
│  └─ Customer clicks related item link        (leading)
└─ Customer renews annual membership           (lagging)
   └─ Customer views renewal offers            (leading)
      └─ Customer clicks renewal email link    (leading, earlier)

Profit Margin
├─ Referred customer creates account           (lagging) ◄─┐ both fed by the
└─ Referred customer puts item in cart         (lagging) ◄─┤ same leading outcome:
                                                           │ Customer arrives via referral link   (leading)
                                                           └─ Customer shares referral link       (leading, earlier)
```

`example-gothelf.json` is the input that draws this map.
