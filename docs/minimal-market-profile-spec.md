# Minimal Market Profile Spec

## Purpose

This document defines the first machine-usable **price-based Market Profile layer** for Pattern Bridge.

The goal is not to reproduce every discretionary nuance.
The goal is to construct a profile representation from 30-minute ES bars that is good enough to test whether profile-derived ideas like:
- Bikini
- poor tails
- balance vs elongation
- double distribution
- edge failure

can be grounded in measurable structure.

## Input assumptions

Source data:
- ES 30-minute bars
- fields:
  - datetime
  - open
  - high
  - low
  - close
  - volume (optional for later, not primary here)

For v0, this profile is **price-based / TPO-style**, not volume-profile based.

## Core concept

Each 30-minute bar contributes **time-at-price** to every price level it traded through.

That means the machine should build a profile by:
1. choosing a price increment
2. mapping each 30-minute bar onto the traded price ladder
3. counting how many 30-minute segments touched each price level

This produces a simple TPO-style distribution.

## First-pass simplifications

To avoid fake precision, start simple.

### Price increment
Use one of these:
- **0.25 points** if performance is fine and structure is readable
- otherwise **1.00 point** for simpler first-pass geometry

Recommendation:
- start with **0.25** because ES trades in quarter points and the structure should stay faithful

### Session unit
Start with:
- one regular session / one trading day profile at a time

Then later:
- combine days into weekly composite views if needed

### Contribution rule
For each 30-minute bar:
- add one TPO count to every price step from bar low to bar high

This is intentionally simple.
We are not yet trying to infer exact within-bar path.

## Output representation

For one target session, output:
- `price_level`
- `tpo_count`
- `first_seen_period`
- `last_seen_period`
- `is_single_print`
- `relative_density`

Also keep the ordered 30-minute periods, for example:
- `A`, `B`, `C`, ...

Or if we want to avoid letters at first:
- period index `0,1,2,...`

## Minimum derived features

From the profile, compute at least:

### 1. Profile high and low
- highest traded price level
- lowest traded price level

### 2. Point of control candidate
- price level with highest TPO count
- if tie, use a deterministic tie-break rule

### 3. Value area candidate
Simple first pass:
- center on POC
- expand outward until ~70% of TPOs are included

### 4. Single prints
- price levels with TPO count == 1
- grouped into contiguous single-print zones

### 5. Tail quality
First pass idea:
- a tail is `clean` if the extreme end contains a short contiguous run of low-TPO levels and does not look repeatedly revisited
- a tail is `poor` if the extreme looks flat, repeatedly revisited, or lacks clear excess

This needs more refinement before hard labeling.

### 6. Distribution shape hints
First pass only, not final:
- balanced: center-heavy, roughly symmetric density
- elongated: directional extension with thin opposite side
- double distribution candidate: two dense zones separated by a thinner area

## Machine-legal questions this profile should help answer

The profile layer exists to answer questions like:
- did the session leave a clean tail or a poor tail?
- did price auction cleanly away from an extreme?
- was the profile balanced or elongated?
- is there a plausible double-distribution structure?
- did a move leave thin areas that were not revisited?
- did a prior edge fail because the profile kept accepting there rather than rejecting?

## User-defined working definitions to preserve

These definitions came directly from Edward and should be treated as the current source meaning unless revised.

### Bikini
A `Bikini` is:
- a profile with a **long upper tail**
- a **long lower tail**
- and a **fatter middle**

In other words, the machine should look for a session/day profile where:
- both extremes taper out
- the center has materially higher TPO density than the tails
- the silhouette is tail-heavy on both ends with a thicker center body

### Poor TPOL
`Poor TPOL` means:
- **no single-print tail** at the relevant lower extreme
- practically, this can show up as a double or triple print at the low rather than a clean single-print taper

That means the machine test for a poor lower tail should begin with:
- no clean single-print run at the lower extreme
- repeated TPO presence at the low end instead of immediate excess and rejection

## What this layer is not yet

It is **not yet**:
- a perfect replica of discretionary Market Profile reading
- a volume profile model
- a full playbook engine
- a finished classifier for Bikini / TPOL

It is the minimum honest middle layer between:
- raw OHLC bars
- human profile language

## First implementation target

Build one target-day profile first, using the Jan 2022 seed week.

Suggested order:
1. choose one day, likely **2022-01-04** or **2022-01-05**
2. generate the session profile from 30-minute bars
3. inspect whether the resulting structure is recognizable and readable
4. only then define measurable criteria for:
   - poor tail
   - thin zone
   - possible double distribution

## Success criteria

This first Market Profile layer is useful if:
- the output is inspectable and understandable
- the session shape is visually / structurally recognizable
- it gives us objective hooks for profile language
- it reduces the gap between raw bars and discretionary labels

## Immediate next artifact

The next step should be a small script that:
- reads `es_30m_continuous.csv`
- filters one target session
- builds the TPO-style price distribution
- writes a machine-readable CSV and/or JSON profile output
- optionally prints a simple ASCII profile summary for inspection
