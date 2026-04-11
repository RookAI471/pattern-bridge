# Placebo Week Validation Framework

## Purpose

This framework tests whether the AI actually understands a weekly meta-playbook structure, rather than merely matching historical labels or memorizing the original week.

The core question is:

> If we compare the canonical week against other carefully chosen weeks that preserve or break the important weekly logic, can the AI correctly pass or fail them for the right reasons?

## Why placebo weeks matter

Historical analog testing alone is not enough.
A model can appear competent by:
- memorizing real weeks
- overfitting archive language
- anchoring to known event dates or famous price action

Placebo weeks force a harder test:
- the structure must be understood
- not just recognized from memory

## Source policy, current decision

Use **real historical ES weeks first**.

Why:
- they preserve real auction texture automatically
- they avoid fake-looking interpolated or filler bars
- they make the validation more honest
- we already have the historical data needed for this lane

Synthetic/generated weeks are now demoted to a possible later research lane, not the primary validation method.
Only revisit synthetic generation if we later need controlled perturbation after the real-week baseline is already working.

## Reference week

Canonical reference:
- `weekly-meta-playbook-2022-01-07.md`

Core weekly meta to preserve or break:
- important higher-timeframe location at a multi-week range high
- Tuesday PTPOH-driven bikini failure at that important location
- Tuesday is the best trade of the week, despite occurring before the marquee catalysts
- failure creates a new liquidation / operating area
- FOMC confirms the new range and sets the weekly high
- post-FOMC regime becomes range-dominant
- Friday NFP is lower value for momentum, though potentially still useful for other expressions like 0DTE

## Critical reminder

FOMC and NFP are **catalysts**, not the essence of the analog.

When screening candidates for this Jan 7 family, it is fine if one of those catalysts is present, but they should be treated as **unimportant unless the structure already matches**.

A week does **not** qualify as a strong positive analog just because it shares the same news labels.
The real comparison target is:
- weekly profile logic
- controlling higher-timeframe structure
- signal quality at the important location
- opportunity ranking across the week

## Minimum structural screen

If a candidate week does **not** do these three things, it is **not** the weekly setup we want:

1. **Attempt to break above or below a prior well-defined range from previous weeks**
2. **Fail to break**, preferably with a **poor TPO high or poor TPO low** signal at the failure point
3. **Cleanly break the other side of the range**

This is the minimum definition.

After that, a **better** match is one where:
- the market begins to establish a **new range**, not just continue trending
- the latter portion of the week becomes more range-bound rather than extension-driven

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

Non-criteria by themselves:
- shared catalyst labels like `FOMC` or `NFP`
- superficial event-family overlap without the same weekly profile logic

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
- attempt to break a well-defined prior multi-week range
- meaningful failure at that location
- preferably weak-auction quality at the failure point, for example a poor TPO high rather than a clean rejection wick
- clean break of the opposite side of the range
- creation of a new operating / liquidation area
- better still, a new range begins to establish rather than the market simply continuing to trend
- post-event or later-week regime becomes range-bound enough that the latter portion of the week is clearly lower-information than Tuesday
- information economics roughly consistent with the reference week

### A week should FAIL if
One or more of the important features is missing or reversed:
- wrong controlling location
- no attempt to break a well-defined prior range
- no meaningful failure at that range edge
- no clean break of the opposite side of the range
- no new range established, or the week simply trends instead
- later-week regime wrong
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

Create a small placebo pack using **real historical ES weeks**:
- Positive Placebo A, close analog
- Positive Placebo B, same meta with different irrelevant clutter
- Negative Placebo A, similar early failure but wrong post-FOMC regime
- Negative Placebo B, failure not at the important HTF location

Edward grades first.
Then AI grades.
Only after that do we claim the weekly meta is machine-comparable.
