# Placebo Week Viewing Notes

## Current state

The placebo weeks in `placebo-week-pack-v0.md` began as narrative specs.

We also tested a synthetic-bar rendering path, and it was not good enough. The charts became dense but visually fake, which made the comparison less trustworthy, not more.

Current decision:
- the next viewing lane should use **real historical ES weeks first**
- the viewer should present those real weeks as the placebo candidates

## What is needed to view a placebo week

For the current phase, a placebo week should be shown as a **real historical 30-minute ES week** with the right multi-week context window.

That means the job is:
- choose the right real historical candidate weeks
- document why each is positive or negative
- load them into the viewer on the same footing as the canonical week
- let Edward visually inspect and grade them

Only later, if needed, should we revisit fully synthetic generation.

## Charting tool

TradingView Lightweight Charts is appropriate for this, but only as a **viewer**.
It does not generate market data.

So the workflow is:
1. define the placebo week structure
2. convert it into synthetic OHLC bars
3. load those bars into a lightweight-charts viewer
4. let Edward visually inspect whether the synthetic week deserves a human pass/fail

## Immediate next deliverable

Create:
- a simple browser viewer using Lightweight Charts
- one or more **real historical placebo week datasets** in JSON
- enough viewing controls to compare:
  - the canonical real week
  - Positive Placebo A candidate
  - Positive Placebo B candidate
  - Negative Placebo A candidate
  - Negative Placebo B candidate
