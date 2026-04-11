# Canonical Week Reconstruction Test

## Purpose

This document defines the first serious validation gate for Pattern Bridge.

Before trying to generalize weekly event archetypes, we need to answer a simpler and harsher question:

> Given near-exact but imperfect market data replicas, can the machine reconstruct the actual week well enough that a human discretionary trader would say: yes, that is basically what happened?

If the answer is no, then the current archetypes are still too human-shaped and not yet computer-usable.

## Why this comes first

The classic failure mode here is trying to teach the computer trader shorthand directly:
- `Bikini`
- `Poor TPO`
- `CINAH`
- `inv P`

That is usually not machine-usable as a starting point.

A computer should not be expected to understand those labels directly unless we can first show that it can recover the **underlying structure** from data.

So the first task is not:
- classify many weeks
- define lots of archetypes
- translate trader jargon into code

The first task is:
- reconstruct one canonical week from machine-available inputs
- compare that reconstruction to the real human weekly story
- decide whether the data and primitives are good enough to proceed

## First seed week

Start with:
- **Week ending January 7, 2022**

Archive reference:
- `ES T Bik Fail at Range High, Wed FOMC Min inv P liq, bad TPOL, Fri NFP Bik`
- Event: `FOMC, NFP`
- Higher Timeframe Event: `Range Sweep`

This is a good first test because:
- it is event-heavy
- it contains a clear weekly story
- it has a compressed human label already
- it is exactly the kind of week we are tempted to overstate before proving the machine can see it

## Core question

The question is **not**:
- can the machine say `Bikini`?

The question is:
- can the machine recover enough of the week’s structure that the human shorthand begins to make sense as a downstream summary?

## Allowed inputs

For v0, the machine may use only these kinds of inputs:

### Market data
- daily bars
- 60-minute bars
- optionally finer bars later if needed, but do not assume that yet

### Basic reference data
- prior week high / low / close
- current week evolving high / low / close
- event dates and timestamps
- session timestamps
- volume if available

### Derived machine-legal features
Allowed examples:
- range width
- distance from prior week high / low
- failed break attempts defined mechanically
- acceptance versus rejection defined mechanically
- close location within weekly range
- percentage of weekly range traversed
- time spent above / below prior range
- post-event continuation vs reversal

## Forbidden shortcuts

Do **not** let the machine cheat by using human shorthand as primitives.

Forbidden as primary inputs:
- `Bikini`
- `Poor TPO`
- `CINAH`
- `inv P`
- any discretionary profile label that has not yet been reduced to explicit measurable criteria

These may appear later only as:
- human comparison labels
- evaluation targets
- downstream explanatory overlays

## Success criteria

A successful reconstruction does **not** require matching the human language exactly.

It does require the machine to recover the major structural truths of the week.

### Minimum success looks like this
The machine can correctly identify things such as:
1. whether a prior controlling range existed
2. whether early-week action failed at or near one edge of that range
3. whether the FOMC move created stable acceptance or only excursion / liquidation
4. whether late-week trade re-engaged the opposite side of the range
5. where the week closed relative to the controlling structure
6. what the dominant weekly story was, in plain language

### Example of acceptable machine output
Something like:
- the week was controlled by a prior range
- an early attempt failed near the upper edge
- the midweek event produced an excursion without durable acceptance
- late-week trade moved back toward the opposite side of the range
- the weekly close confirmed two-sided auction rather than stable breakout

That would count as meaningful progress.

### Example of failure
- vague labels only
- generic summaries that could fit many weeks
- overfitting to the known answer
- using trader jargon without measurable support
- claiming a trend week when the core week was range control and sweep behavior

## Evaluation standard

The test should compare three layers:

### 1. Raw machine reconstruction
What the model infers from market data + event calendar only.

### 2. Archive label
The compressed historical label already in the archive.

### 3. Human judgment
Edward’s actual assessment of whether the reconstruction captured the real week.

The gate is not whether the machine matches the archive phrase exactly.
The gate is whether the machine’s structural account is close enough to earn trust.

## What we are actually testing

This test is meant to answer:
1. are our current archetypes too vague?
2. are our current data inputs sufficient?
3. are the right primitives geometric/temporal rather than profile-jargon based?
4. can one canonical week be reconstructed well enough to justify pursuing variants?

## Proposed workflow

### Step 1
Choose one canonical week:
- January 7, 2022

### Step 2
Gather the machine-visible data for that week:
- prior week data
- current week daily bars
- current week 60-minute bars
- event timestamps for FOMC and NFP

### Step 3
Define candidate measurable primitives for the week, such as:
- prior range boundaries
- distance from prior range edges
- number of failed break attempts
- event-day excursion beyond range and whether it held
- Friday close percentile within weekly range
- whether weekly travel traversed both sides of the prior box

### Step 4
Produce a machine reconstruction in plain English.

### Step 5
Compare it against:
- archive label
- human judgment

### Step 6
Only if reconstruction is convincing:
- define generalized archetype rules
- test neighboring weeks and imperfect variants

## Immediate output we need next

The next artifact should be a **single-week reconstruction spec** for January 7, 2022 that answers:
- what exact data do we have?
- what exact measurable primitives will we compute?
- what would count as enough fidelity to proceed?

## Blunt operating rule

Until the machine can reconstruct one canonical week from data in a way that survives human scrutiny, we should assume the archetypes are still story-shaped rather than computer-shaped.
