# Placebo Week Validation Framework

## Purpose

This framework tests whether the AI actually understands a weekly meta-playbook structure, rather than merely matching historical labels or memorizing the original week.

The core question is:

> If we create synthetic weeks that preserve or break the important weekly logic, can the AI correctly pass or fail them for the right reasons?

## Why placebo weeks matter

Historical analog testing alone is not enough.
A model can appear competent by:
- memorizing real weeks
- overfitting archive language
- anchoring to known event dates or famous price action

Placebo weeks force a harder test:
- the structure must be understood
- not just recognized from memory

## Reference week

Canonical reference:
- `weekly-meta-playbook-2022-01-07.md`

Core weekly meta to preserve or break:
- important higher-timeframe location at a multi-week range high
- Tuesday bikini failure at that important location
- failure creates a new liquidation / operating area
- FOMC confirms the new range and sets the weekly high
- post-FOMC regime becomes range-dominant
- Friday NFP is lower value for momentum, though potentially still useful for other expressions like 0DTE

## Test classes

### 1. Historical truth case
- the original real week
- used as the reference anchor

### 2. Positive placebo weeks
These should receive a **pass** from both a human and the AI.

A positive placebo preserves the important structure while allowing irrelevant details to vary.
Examples of acceptable variation:
- a different lower nearby range that is not controlling
- slightly different intraday path shape
- different exact price levels
- different surface clutter that does not change the real weekly thesis

### 3. Negative placebo weeks
These should receive a **fail** from both a human and the AI.

A negative placebo may look superficially similar but breaks the important logic.
Examples:
- failure occurs away from the controlling HTF location
- the event confirms continuation instead of new range establishment
- post-event regime is trend continuation instead of range dominance
- Friday still offers the best momentum opportunity, which conflicts with the reference week’s information economics

## Required evaluation order

### Step 1: Human grading first
Edward grades each placebo week before AI sees the result.

Each placebo should receive:
- `human_grade = pass / fail`
- short explanation why

### Step 2: AI grading second
The AI evaluates the same placebo and must provide:
- `ai_grade = pass / fail`
- explanation of:
  - what matched
  - what varied but did not matter
  - what broke the analogy, if failed

### Step 3: Compare
We then compare:
- human grade
- AI grade
- reasoning quality

## Pass/fail criteria

### A week should PASS if
It preserves the important weekly meta:
- controlling HTF range-high context
- early important failure at that context
- creation of a new operating / liquidation area
- event confirmation of the new range
- post-event range-bound regime
- information economics roughly consistent with the reference week

### A week should FAIL if
One or more of the important features is missing or reversed:
- wrong controlling location
- no meaningful early failure
- no new range established
- event confirms continuation rather than failed structure / new range
- post-event regime wrong
- opportunity ranking meaningfully different in a way that changes the weekly playbook

## What the AI must learn to ignore

The AI should not fail a valid analog just because of:
- unrelated lower structure
- different exact price levels
- slightly different event-day path noise
- cosmetic differences in secondary context

This is critical.
The test is partly about whether the AI knows what **not** to care about.

## What the AI must identify correctly

At minimum, it must identify:
- the controlling context
- the important early failure
- the structural consequence of that failure
- what FOMC confirmed
- the post-event operating regime
- the opportunity / information ranking of the week

## Scoring dimensions

Each placebo evaluation should be scored on:
1. `grade_correctness`
2. `controlling_context_correct`
3. `important_failure_correct`
4. `event_confirmation_correct`
5. `post_event_regime_correct`
6. `ignored_irrelevant_differences`
7. `opportunity_ranking_understood`

## Immediate next step

Create a small placebo pack:
- Positive Placebo A, close analog
- Positive Placebo B, same meta with different irrelevant clutter
- Negative Placebo A, similar early failure but wrong post-FOMC regime
- Negative Placebo B, failure not at the important HTF location

Edward grades first.
Then AI grades.
Only after that do we claim the weekly meta is machine-comparable.
