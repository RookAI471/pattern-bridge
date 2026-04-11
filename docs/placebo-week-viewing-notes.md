# Placebo Week Viewing Notes

## Current state

The placebo weeks in `placebo-week-pack-v0.md` are currently **narrative specs**, not full synthetic OHLC time series.

That means Edward cannot truly "view" them yet as market weeks, because there are no bar sequences to render.

## What is needed to view a placebo week

A placebo week needs to be converted into a synthetic bar dataset, at minimum:
- timestamp
- open
- high
- low
- close

For a first pass, we do **not** need perfect 30-minute realism.
We need a structurally faithful week sketch that preserves:
- higher-timeframe location
- Tuesday failure logic
- FOMC weekly-high logic
- post-FOMC range establishment
- Friday lower-value chop

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
- one or more synthetic placebo datasets in JSON
- enough viewing controls to compare:
  - the canonical real week
  - Positive Placebo A
  - Positive Placebo B
  - Negative Placebo A
  - Negative Placebo B
