# Full-History Structural Scan Notes — 2026-04-11

## Purpose

This note records what we learned after abandoning catalyst-led placebo selection and synthetic filler-bar generation.

The question became:

> If we search the full futures price history directly, using the structural logic of the Jan 7, 2022 week, do we find a rare but real family, or just story-shaped noise?

## Core correction

Do **not** select candidates by shared catalysts like FOMC or NFP.

Those are acceptable background events, but they are **not** the essence of the setup.

Edward's minimum structural definition for the Jan 7 family is now:
1. attempt to break above or below a prior well-defined range from previous weeks
2. fail to break, ideally with a PTPOH or PTPOL style weak-auction signal
3. clean break of the other side of the range

A stronger match then adds:
- establishment of a **new range**, not just continuation
- a later portion of the week that becomes more **range-bound**

## Why the earlier placebo lane changed

Two earlier shortcuts were explicitly rejected by the work:

### 1. Catalyst-led candidate picking
This produced bad positive candidates.
Shared `FOMC` / `NFP` labels were too shallow and did not preserve the actual weekly profile logic.

### 2. Synthetic filler-bar generation
This produced charts that were dense enough to render but did **not** look like real markets.
That made the comparison less honest, not more.

Current source policy:
- use **real historical weeks first**
- use price-only structural screening first
- only revisit synthetic generation later, if it is ever needed for controlled perturbation work

## Scan method, current version

The current scan is still an early mechanical pass, not a finished detector.
But it is better than the first rough distance-based attempt.

### Current scanner characteristics
- uses full **30-minute** price history
- uses a rolling **prior 4-week range** as the reference box
- searches for an **ordered sequence**, not just week-end distances:
  - break attempt
  - failure
  - opposite-side break
- then adds weak proxies for:
  - later-week balance
  - residency on the new side
  - avoidance of reclaiming the old edge

### Important limitation
This scanner does **not** yet model:
- PTPOH / PTPOL directly
- true Market Profile/TPO shape
- tape quality
- the difference between a reversal that keeps extending and one that actually settles into a new range, except through crude range/balance proxies

So the counts below are useful, but still preliminary.

## ES, current tiered results

Using the current sequence-aware scan on ES:

- total weeks scanned: **864**
- skeleton hits: **3**
  - ordered attempt -> fail -> opposite-break sequence present
- tier-2 better-structure hits: **2**
- tier-3 plus range-bound aftermath: **1**

### ES weeks currently identified
- tier-2: `2016-11-11`, `2022-12-16`
- tier-3: `2016-11-11`

### ES interpretation
This suggests the family is **rare** in ES under the current structural rule set.
It also suggests that the real separator is not the reversal skeleton alone, but whether the week then **settles into a new range**.

## CL, current tiered results

Using the same sequence-aware scan on CL:

- total weeks scanned: **864**
- skeleton hits: **3**
- tier-2 better-structure hits: **3**
- tier-3 plus range-bound aftermath: **1**

### CL weeks currently identified
- tier-2: `2025-04-04`, `2012-05-04`, `2011-05-06`
- tier-3: `2011-05-06`

### CL interpretation
CL currently looks like the strongest non-ES market for this family.
That does **not** prove the same family exists identically in CL, but it does suggest the structural logic may recur across markets.

## Cross-market exploratory pass

An earlier broad cross-market pass suggested that the current structural family may not be ES-only.
The most interesting exploratory markets so far were:
- **CL**
- **BP**
- **FV**
- **ES**

CL looked strongest on the first normalized scan.
BP and FV produced enough mechanical hits to justify future inspection.

## Human review result already obtained

Edward reviewed the first two CL candidates and judged them as:
- **solid enough examples**

That is important because it means the scanner is not merely generating obvious nonsense once moved off catalyst-led picking.

## What seems to separate stronger hits from near misses

So far, the most useful difference is **not** simply:
- did it fail
- did it break the other side
- did it avoid reclaiming the old edge

Those are often true for both stronger hits and near misses.

The more important separator appears to be:
- **tempo** of the sequence
- whether the opposite-side break happens early enough to leave time for balance
- whether the latter part of the week actually **compresses and rotates**
- whether the market behaves like it is **establishing a new operating range** rather than just continuing directional energy

This fits Edward's intuition that the ultimate separator may lie in:
- tape
- auction quality
- and other finer structural clues not yet modeled directly

## Current conclusion

This work does appear to have **legs**, but only in a narrow form.

More specifically:
- this does **not** look like a broad, easy weekly classifier
- it does look like a **rare, high-specificity weekly family**
- the useful product direction is likely:
  - rare structural analog search
  - mechanical screening first
  - human judgment second
  - increasingly better tape/profile proxies over time

## Next recommended steps

1. inspect the current success vs near-miss weeks side by side
   - ES: `2016-11-11` vs `2022-12-16`
   - CL: `2011-05-06` vs `2012-05-04` and `2025-04-04`
2. extract additional distinguishing features from 30-minute bars
   - speed of failure
   - speed of opposite-side break
   - later-week compression
   - reclaim attempts
3. build better weak-auction proxies
   - PTPOH
   - PTPOL
   - crude TPO quality metrics
4. only after that, revisit broader cross-market expansion

## Bottom line

The current evidence supports this statement:

> The Jan 7 family may be a real but rare structural pattern. The hard part is not finding reversal weeks, but identifying the subset that truly transitions into a new range rather than simply extending the move.
