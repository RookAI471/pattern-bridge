# Weekly Meta-Playbook Schema

## Purpose

This schema captures the real value layer for Pattern Bridge.

The goal is not to reproduce every handwritten note or every TPO nuance.
The goal is to capture the **highest-value weekly intelligence**:
- controlling higher-timeframe context
- ranked key events
- structural consequences
- post-event regime
- what mattered vs what did not
- where the best opportunities actually were
- which strategy styles were advantaged or disadvantaged

This is the level the AI needs to understand to become useful.

## Core principle

The AI does **not** need to recreate the full playbook from scratch every time.
It needs to:
1. understand the event vocabulary and structural terms
2. identify the most important weekly events
3. infer the weekly meta
4. compare that meta to prior weeks

## Schema fields

### 1. Identity
- `week_end_date`
- `market`
- `title`
- `summary`

### 2. Controlling context
- `controlling_context`
  - the higher-timeframe structure that actually matters
- `decision_relevant_structure`
  - the specific range / channel / location / neckline / etc. that governs the week
- `non_invalidating_differences`
  - nearby differences that should **not** disqualify an analog

### 3. Ranked key events
A list ordered by importance.
Each item should include:
- `rank`
- `event`
- `term_meaning`
- `location`
- `structural_consequence`
- `why_it_matters`

### 4. Structural progression
- `early_week_state`
- `midweek_inflection`
- `late_week_state`
- `weekly_resolution`

### 5. Event interpretation
- `major_event`
- `what_was_unknown_before_event`
- `what_the_event_confirmed`
- `post_event_operating_assumption`

### 6. Weekly regime / strategy implication
- `post_event_regime`
  - examples: range-dominant, breakout continuation, failed break auction
- `dominant_strategy_implication`
- `what_to_deprioritize`

### 7. Opportunity ranking
- `best_trade_of_week`
- `second_best_trade`
- `lowest_value_trade_window`
- `hardest_trade_to_take`
- `why_the_best_trade_was_hard`

### 8. Strategy-style fit
- `best_for_momentum`
- `best_for_range_trading`
- `best_for_options`
- `worst_for_momentum`
- `style_specific_notes`

### 9. Information economics
- `when_information_was_lowest`
- `when_information_became_actionable`
- `when_the_market_became_too_informed_or_exhausted`
- `information_edge_note`

### 10. Comparison utility
- `what_must_match_for_analog`
- `what_can_vary_without_breaking_the_analog`
- `what_would_invalidate_comparison`

## Why this matters

This schema forces the machine to reason at the right level:
- not every visible detail matters
- not every similar nearby structure matters
- the best trade is not always where the most information exists
- the most obvious late-week move may be less valuable than the harder early-week pivot

That is the intelligence layer the product needs.
