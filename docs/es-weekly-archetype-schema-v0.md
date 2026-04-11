# ES Weekly Archetype Schema, v0

## Purpose

This document turns the first three ES weekly event archetypes into a buildable detection schema.

The goal is not to predict the week.
The goal is to let an AI system say:
- this week is beginning to resemble a known historical weekly archetype
- here is why
- here is what still needs to happen before confidence should increase
- here is what would invalidate the comparison

## Scope

Initial archetypes:
1. Event-Week Range Sweep
2. FOMC Grind Through Prior Structure
3. Event-Week Structural Failure

Initial market:
- ES only

Initial time horizon:
- weekly context

Initial product behavior:
- context recognition
- analog comparison
- early warning
- no trade signals

---

## Shared schema

Each weekly archetype should be represented with the following fields.

### 1. Identity
- `archetype_id`
- `name`
- `summary`
- `why_it_matters`

### 2. Event context
- `primary_events`
  - examples: `FOMC`, `NFP`, `US CPI`, `Fed Minutes`
- `secondary_events`
- `event_overlap_required`
  - boolean
- `event_timing_importance`
  - examples: `midweek catalyst critical`, `Friday catalyst critical`, `overlap important`

### 3. Prior context
- `prior_week_structure`
  - examples: `range`, `channel`, `vulnerable neckline`, `failed breakout`, `multi-week balance`
- `higher_timeframe_vulnerability`
  - examples: `high`, `medium`, `low`
- `key_reference_behavior`
  - examples: `range edge respected`, `breakout level vulnerable`, `gap still unresolved`

### 4. Early-week behavior
- `monday_tuesday_shape`
- `early_attempt_type`
  - examples: `failed breakout`, `failed breakdown`, `grind continuation`, `range hold`
- `early_signal_features`
  - short list of observable conditions

### 5. Event-day behavior
- `event_day_shape`
- `event_day_acceptance_test`
  - did the event create stable acceptance or only an emotional excursion?
- `event_day_interpretation`

### 6. Late-week behavior
- `thursday_friday_shape`
- `friday_close_meaning`
- `resolution_type`
  - examples: `back in range`, `through range`, `failed continuation`, `confirmed failure`

### 7. Detection logic
- `required_features`
- `supporting_features`
- `invalidators`
- `confidence_ladder`
  - `early_watch`
  - `developing_match`
  - `strong_match`

### 8. Output behavior
- `what_to_tell_user`
- `what_not_to_do`
- `comparison_targets`
  - historical weeks to compare against

---

## Archetype 1, Event-Week Range Sweep

### Identity
- `archetype_id`: `es_event_week_range_sweep`
- `name`: `Event-Week Range Sweep`
- `summary`: Major event week remains governed by an established range and repeatedly sweeps both sides before closing back near an edge.
- `why_it_matters`: Traders often over-read one event move and forget that the real weekly story is two-sided auction around a controlling range.

### Event context
- `primary_events`: `FOMC`
- `secondary_events`: `NFP`, `US CPI`
- `event_overlap_required`: `false`, but overlap increases confidence
- `event_timing_importance`: midweek catalyst plus late-week catalyst is highly informative

### Prior context
- `prior_week_structure`: established range or visible weekly box
- `higher_timeframe_vulnerability`: medium
- `key_reference_behavior`: range high / low matter more than intraday event spikes

### Early-week behavior
- `monday_tuesday_shape`: one side of the range is tested and rejected, or the market washes through a boundary but cannot hold beyond it
- `early_attempt_type`: failed breakout or failed breakdown
- `early_signal_features`:
  - prior range still visually controls
  - rejection near one range edge
  - inability to establish clean acceptance outside range

### Event-day behavior
- `event_day_shape`: emotional move, liquidation, or sharp impulse that still does not produce durable acceptance beyond the range
- `event_day_acceptance_test`: fail preferred
- `event_day_interpretation`: FOMC move is important, but mostly as a range sweep amplifier

### Late-week behavior
- `thursday_friday_shape`: opposite-side test, reversal, or liquidation back through the box
- `friday_close_meaning`: closing near an edge tells the real weekly story
- `resolution_type`: back in range or edge close after two-sided sweep

### Required features
- identifiable prior range
- at least one failed directional attempt at a range edge
- major event move that does not create stable acceptance outside the range
- late-week trade challenges the opposite side or re-anchors the weekly read at an edge

### Supporting features
- FOMC + NFP overlap
- weak TPO structure during one of the sweeps
- repeated liquidation language in the archive notes
- Friday close near weekly low or high after both sides traded

### Invalidators
- clean breakout with sustained acceptance and orderly continuation
- no meaningful prior range context
- week stays one-sided after event without meaningful reversal or re-entry

### Confidence ladder
- `early_watch`:
  - known event week
  - prior range still controlling
  - Monday or Tuesday failed break at an edge
- `developing_match`:
  - FOMC or main catalyst produces excursion without lasting acceptance
- `strong_match`:
  - late-week trade sweeps or liquidates toward opposite edge and Friday close confirms range dominance

### Comparison targets
- `January 7, 2022`
  - `ES T Bik Fail at Range High, Wed FOMC Min inv P liq, bad TPOL, Fri NFP Bik`
  - Event: `FOMC, NFP`
  - HTF: `Range Sweep`
- `May 6, 2022`
  - corrupted row but clearly FOMC + NFP and `Fri NFP close bot range`
  - HTF: `Range Sweep`
- `May 13, 2022`
  - `ES range box to Wed CPI, Thu false break lower, Friday P liquidation back into range`
  - HTF: `Range Sweep`

### Output behavior
- `what_to_tell_user`:
  - this week is starting to look like a two-sided event-week range sweep
  - the event move matters less than whether ES can accept outside the weekly box
  - watch whether Friday confirms edge control instead of continuation
- `what_not_to_do`:
  - do not describe this as a trend week too early
  - do not treat one catalyst move as decisive without acceptance

---

## Archetype 2, FOMC Grind Through Prior Structure

### Identity
- `archetype_id`: `es_fomc_grind_through_prior_structure`
- `name`: `FOMC Grind Through Prior Structure`
- `summary`: FOMC week where price grinds through prior structural references instead of resolving in one obvious impulse.
- `why_it_matters`: This prevents misclassifying a structural, absorption-heavy week as either pure range chop or pure breakout.

### Event context
- `primary_events`: `FOMC`
- `secondary_events`: `Quad Witching`, other context events
- `event_overlap_required`: `false`
- `event_timing_importance`: FOMC day is central, but the close relative to prior structure matters most

### Prior context
- `prior_week_structure`: prior gap, prior range, prior acceptance zone, prior auction reference
- `higher_timeframe_vulnerability`: low to medium
- `key_reference_behavior`: prior structure remains sticky even while price grinds through it

### Early-week behavior
- `monday_tuesday_shape`: washback, test of prior references, gradual directional pressure
- `early_attempt_type`: grind continuation or controlled retrace
- `early_signal_features`:
  - repeated interaction with prior structural references
  - no dramatic failure yet
  - directional pressure without decisive release

### Event-day behavior
- `event_day_shape`: grind, absorption, or continuation through prior structural reference
- `event_day_acceptance_test`: mixed
- `event_day_interpretation`: the key question is not spike magnitude but whether the market is being re-auctioned through prior structure

### Late-week behavior
- `thursday_friday_shape`: continuation, measured extension, or close back inside older structure
- `friday_close_meaning`: tells whether the grind truly re-priced the week or merely traversed prior structure temporarily
- `resolution_type`: through range, partial re-acceptance, or contained continuation

### Required features
- FOMC week
- prior structural reference remains central all week
- directional progress happens by grind/absorption, not only by one explosive move
- closing location relative to prior week range or prior gap matters to final interpretation

### Supporting features
- prior gap mention
- 50 EMA / prior auction / washback language
- close inside prior week range after seeming continuation

### Invalidators
- sharp two-sided sweep week that clearly fits Range Sweep better
- obvious structural failure of prior HTF pattern
- no meaningful prior structural reference in play

### Confidence ladder
- `early_watch`:
  - prior structural reference keeps getting tested
  - week is FOMC-tagged
- `developing_match`:
  - FOMC move advances through prior structure without clean trend resolution
- `strong_match`:
  - weekly close confirms the key story is how ES re-auctioned through prior structure

### Comparison targets
- `September 24, 2021`
  - `ES Sun Break AnA, test 50EMA, Washback M, FOMC Grind through Sun Gap, close within prior week range`
  - Event: `FOMC`
  - HTF: `Auction & Absorption`
- `March 18, 2022`
  - `ES 60m W broken, post FOMC grind higher, 5min flag 4420 Fri Trend Higher Quad Witching`
  - Event: `FOMC, Quad Witching`
  - HTF: `W break`

### Output behavior
- `what_to_tell_user`:
  - this is beginning to resemble an FOMC grind-through week, not a pure impulse week
  - prior structure still matters more than the headline move
  - focus on where the week closes relative to older references
- `what_not_to_do`:
  - do not force this into a simple breakout/reversal label too early

---

## Archetype 3, Event-Week Structural Failure

### Identity
- `archetype_id`: `es_event_week_structural_failure`
- `name`: `Event-Week Structural Failure`
- `summary`: A vulnerable higher-timeframe structure was already in place before the event, and the event week ends up confirming its failure or failed retest.
- `why_it_matters`: This is exactly where AI can help preserve memory, because traders often misattribute the whole week to the event rather than to the pre-existing structural weakness.

### Event context
- `primary_events`: `FOMC`, `US CPI`, `Fed Comments`
- `secondary_events`: geopolitical shock, additional macro stressors
- `event_overlap_required`: `false`
- `event_timing_importance`: catalyst timing matters, but pre-event vulnerability matters more

### Prior context
- `prior_week_structure`: pennant, neckline, channel, double top, head-and-shoulders, breakout retest, vulnerable balance
- `higher_timeframe_vulnerability`: high
- `key_reference_behavior`: the event forces decision at already fragile references

### Early-week behavior
- `monday_tuesday_shape`: attempted retest, weak rally, or failed repair into a vulnerable structure
- `early_attempt_type`: failed retest or weak continuation into resistance
- `early_signal_features`:
  - clear pre-existing higher-timeframe pattern vulnerability
  - inability to reclaim or repair structure cleanly
  - weak retest behavior before or around catalyst

### Event-day behavior
- `event_day_shape`: breakdown acceleration, failed retest, or brief reaction that cannot restore the damaged structure
- `event_day_acceptance_test`: acceptance away from the broken structure preferred
- `event_day_interpretation`: event confirms the structural problem rather than inventing a new story

### Late-week behavior
- `thursday_friday_shape`: continuation away from failed structure, or failed attempt to recover before renewed weakness
- `friday_close_meaning`: confirms whether the structure truly failed or was only stressed temporarily
- `resolution_type`: confirmed failure or failed retest

### Required features
- visible higher-timeframe structural vulnerability before the main event
- weak retest, failed reclaim, or failed repair behavior
- catalyst accelerates or confirms failure
- closing behavior supports the structural-failure read

### Supporting features
- words like `neckline`, `pennant`, `channel`, `failed`, `retest`, `head and shoulders`
- multiple events stacking on top of weak structure
- late-week inability to regain the broken area

### Invalidators
- no meaningful pre-existing structure to fail
- week is better explained by a two-sided range sweep with no durable structural consequence
- event creates fresh accepted breakout instead of confirming weakness

### Confidence ladder
- `early_watch`:
  - visible vulnerable structure exists before the main catalyst
  - early retest behavior is weak
- `developing_match`:
  - event pushes price away from the weak structure without convincing repair
- `strong_match`:
  - late-week close confirms failed retest / confirmed structural break

### Comparison targets
- `February 11, 2022`
  - `ES M Trend brk of 60m pen, W att at D neckline, Thur CPI and Hawk mrkt lower, Fri fail prior wk pen DD on Russian inv`
  - Event: `Fed Comments, Russian Invasion, US CPI`
  - HTF: `Break out Retest`
- `July 29, 2022`
  - `ES top of Daily Channel broken after prior week H&S failure. Wed DD to top of channel on FOMC neutral rate. Thur weak GDP trend day break above channel.`
  - Event: `FOMC, GDP`
  - HTF: `Channel Breakout`

### Output behavior
- `what_to_tell_user`:
  - this week is beginning to resemble an event-driven confirmation of pre-existing structural weakness
  - the key story is the vulnerable higher-timeframe structure, not just the headline event
  - watch whether rallies are repairing structure or merely retesting failure
- `what_not_to_do`:
  - do not treat every sharp event reaction as new information if the structure was already fragile

---

## Minimum v0 detection inputs

If we want to classify the week early, the system likely needs these inputs:
- weekly event calendar tags
- prior week high, low, close, and rough range location
- whether ES is in multi-day balance, channel, or obvious vulnerable structure
- whether Monday/Tuesday attempted and failed to break or reclaim a key area
- event-day acceptance vs rejection
- Friday close location relative to weekly range and prior structure
- human-readable notes layer for qualitative language like:
  - `bad TPOL`
  - `weak TPOH`
  - `CINAH`
  - `range sweep`
  - `retest`
  - `failed`

## Suggested next step

Before designing UI, map another 5 to 10 ES weeks into this schema and check:
- are these archetypes actually separable?
- which fields are easy to observe early in the week?
- which fields only become clear in hindsight?
- where do mixed weeks force nested or hybrid labels?
