# January 7, 2022 Single-Week Reconstruction Spec

## Purpose

This document defines the next validation step after `canonical-week-reconstruction-test.md`.

The goal is not yet to classify a family of weeks.
The goal is to determine whether one canonical event week can be reconstructed from machine-legal inputs with enough fidelity to earn trust.

Target week:
- **Week ending January 7, 2022**

Archive label:
- `ES T Bik Fail at Range High, Wed FOMC Min inv P liq, bad TPOL, Fri NFP Bik`
- Event: `FOMC, NFP`
- Higher Timeframe Event: `Range Sweep`

## Current status

We now have:
- event calendar ingestion path for:
  - NFP
  - CPI
  - FOMC
- market-data ingestion path for:
  - SPY daily
  - SPY 60m

However, before we compute anything serious, we need to confirm the exact file locations and inspect whether the generated datasets are actually where we expect and usable for the January 2022 week.

So this spec distinguishes between:
- what we intend to measure
- what still needs to be verified in the local dataset

## Primary question

Given only market data plus event timing, can the machine reconstruct the major weekly structure of the January 7, 2022 week?

Not by using trader shorthand.
Not by backfilling human interpretation.
But by recovering the geometry and timing strongly enough that the shorthand becomes a downstream summary.

## Machine-legal inputs for this test

### Required
- prior week daily bars
- target week daily bars
- target week 60-minute bars
- FOMC timestamp/date
- NFP timestamp/date

### Optional but useful
- prior week high / low / close precomputed
- session labels
- volume
- overnight versus RTH segmentation

## Required data verification step

Before analysis, verify all of the following:

1. exact local paths for:
   - SPY daily CSV
   - SPY 60m CSV
   - `fomc_dates.csv`
   - `nfp_dates.csv`
2. whether the 60m file actually covers the week ending 2022-01-07
3. whether the timestamps are timezone-normalized and interpretable
4. whether the data is regular enough to segment event-day behavior around Wednesday FOMC and Friday NFP

If the 60m file does **not** cover January 2022, then the test must pause and either:
- use a different free source
- use daily-only reconstruction for an intentionally weaker first pass
- or accept that paid data is required to test the canonical week honestly

## Reconstruction targets

The machine should attempt to recover the following structural truths.

### 1. Was there a controlling prior range?
Questions:
- did the prior week create a range that still governed the target week?
- can the machine define plausible upper and lower reference boundaries without human shorthand?

Candidate measurable primitives:
- prior week high
- prior week low
- prior week midpoint
- width of prior week range
- number of target-week bars outside prior-week range
- total time spent outside prior-week range

### 2. Did early-week action fail near one edge?
Questions:
- was there an early failed move near the upper edge or lower edge?
- was the first major attempt accepted or rejected?

Candidate measurable primitives:
- Monday/Tuesday maximum excursion beyond prior-week high or low
- close-back-inside behavior after excursion
- consecutive bars outside prior range before re-entry
- rejection speed after excursion

### 3. What did Wednesday FOMC actually do?
Questions:
- did the FOMC move create stable acceptance outside the controlling structure?
- or did it produce excursion followed by liquidation/re-entry?

Candidate measurable primitives:
- event-day range expansion relative to trailing 5-day average
- max distance beyond prior range during FOMC day
- close location relative to prior range after FOMC day
- percentage of FOMC-day bars that remained outside the prior range after initial break
- whether post-event bars continued or reversed

### 4. What did Friday NFP actually do?
Questions:
- did Friday continue the FOMC direction?
- did Friday return the market toward the opposite edge of the structure?
- did Friday confirm a range-sweep week rather than trend continuation?

Candidate measurable primitives:
- Friday excursion relative to Wednesday close
- Friday close percentile inside the current weekly range
- Friday close position relative to prior-week range
- net weekly move versus total weekly traversal distance

### 5. What was the dominant weekly story?
Questions:
- was this primarily a trend week?
- was it a two-sided auction week controlled by a prior structure?
- did late-week behavior invalidate a breakout interpretation?

Candidate measurable primitives:
- weekly high-low traversal versus net close-to-close move
- fraction of weekly range revisited after event day
- whether both edges of the controlling box were meaningfully engaged
- weekly close location inside current-week and prior-week range

## First-pass plain-English reconstruction template

When the machine eventually runs, its output should look something like this structure:

1. `Controlling structure`
   - what structure governed the week?
2. `Early week`
   - what happened Monday/Tuesday relative to that structure?
3. `FOMC reaction`
   - acceptance, rejection, or temporary excursion?
4. `Late week / NFP`
   - continuation or reversal?
5. `Weekly close implication`
   - what did the close say about the whole week?

That keeps the model honest and forces it to explain the week geometrically, not with trader cosplay.

## What would count as success

This test passes if the machine can produce a reconstruction that Edward would judge as roughly structurally true, even if the language differs from the archive label.

Examples of passing qualities:
- identifies a controlling box or range that mattered all week
- identifies failed or weak acceptance near one edge early in the week
- identifies FOMC as a non-final impulse rather than a clean accepted breakout
- identifies late-week reversion / opposite-edge engagement
- identifies the weekly close as evidence of two-sided auction rather than clean trend continuation

## What would count as failure

Examples of failing qualities:
- relies on vague labels like `volatile week`
- says `range week` without demonstrating why
- says `trend continuation` despite late-week reversal behavior
- requires trader shorthand to sound intelligent
- cannot distinguish acceptance from excursion

## Immediate next tasks

1. Verify the actual local data files and paths
2. Check whether the SPY 60m history really includes January 2022
3. If yes, run a raw reconstruction attempt
4. If no, decide between:
   - alternate free intraday source
   - daily-only degraded test
   - paid data requirement

## Decision rule

Do not move on to broader archetype validation until this week is either:
- reconstructed convincingly
- or shown to be impossible with the current data/input set

Either result is useful.
