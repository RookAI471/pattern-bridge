# Open Questions

## Purpose

This document tracks the most important unresolved questions for Pattern Bridge.

These are not random curiosities.
They are the questions most likely to shape product quality, scope, or strategic direction.

## Product questions

### 1. What exactly is the unit of value?
Is the product's core unit:
- the bridge object,
- the candidate,
- the analog set,
- the debrief,
- or the compounding memory loop across all four?

Likely answer:
The bridge is the canonical object, but the compounding loop may be the true product value.

### 2. How structured should bridge creation be?
Should traders create bridges:
- manually from templates,
- semi-assisted from examples,
- or mostly via AI extraction from notes and debriefs?

Risk:
Too manual and adoption dies.
Too automated and bridges become mushy.

### 3. How much confidence language should the product use?
Should candidates show:
- confidence labels,
- relevance scores,
- similarity explanations only,
- or some combination?

Risk:
Confidence language can mislead traders into treating the tool like a predictor.

### 4. How should the product explain itself?
What level of explanation is enough for trust without drowning the trader in reasoning?

## Workflow questions

### 5. What is the lightest possible journaling flow that still compounds learning?
This matters because traders hate heavy documentation.

Question:
What is the smallest amount of structured input that still improves future retrieval and bridge quality?

### 6. Should review happen daily, intraday, weekly, or all three?
There is a tradeoff between immediacy and fatigue.

### 7. How should rejection be represented?
Rejected candidates are important.
But what kinds of rejection need to be stored?
- wrong context
- wrong structure
- wrong participation
- looked close but lacked confirmation
- execution too mature
- false bridge entirely

## Ontology questions

### 8. How broad or narrow should bridge families be?
Too broad:
- everything feels like the same pattern

Too narrow:
- library explodes into chaos

### 9. When should a bridge split into a variant?
A good product rule is needed here.

### 10. How should translated bridges be modeled?
If a futures bridge ports into stocks or another product, is that:
- the same bridge,
- a translated sibling,
- or a different bridge family?

## Data questions

### 11. What evidence types are essential for v0?
Possible evidence:
- notes
- screenshots
- videos
- chart markup
- event tags
- structured stats

### 12. How much market data is actually needed for useful candidate surfacing?
The product should avoid overbuilding infra too early.

### 13. What is the minimum useful watch universe for early validation?
Especially important if testing a stock wedge later.

## UX questions

### 14. What should the home screen optimize for?
Possible centers:
- today's context
- live candidates
- journals
- watchlists

Current best guess:
Today context should be home.

### 15. How much charting belongs in v0?
Charts are valuable, but chart-platform gravity can swallow the entire product.

### 16. What is the right interaction model for candidate triage?
Cards?
Kanban?
Watchlist rows?
Inbox-style review?

## Strategy questions

### 17. When should the product move from futures to stocks?
This should happen only after the ontology and retrieval feel strong enough.

### 18. Is the first real wedge a trader tool, a coach tool, or both?
A coach workflow may provide stronger early structure, but a trader workflow may show product-market fit faster.

### 19. What is the product's moat?
Candidates:
- bridge ontology
- trader-specific memory
- failure-case recall
- analog retrieval quality
- debrief-to-playbook loop

Likely answer:
The moat is not scanning. It is the memory plus bridge refinement loop.

## Validation questions

### 20. What would falsify the product thesis?
Important possibilities:
- traders do not actually use the review loop
- analog retrieval feels interesting but not decision-useful
- candidate quality never rises above generic scanner noise
- bridge objects prove too subjective to be helpful
- documentation burden remains too high even with assistance

## Near-term priority questions

The highest-priority questions right now are probably:
1. how to define starter bridge objects well
2. how to model candidate objects and states
3. how to define similarity dimensions for analog retrieval
4. how to keep journaling and debrief light enough to survive real use
5. how to represent failure cases without cluttering the system

## Closing thought

A good open-questions list protects the product from premature certainty.
That matters here, because this product can easily drift into either vague theory or generic scanning if the hard questions are not kept visible.
