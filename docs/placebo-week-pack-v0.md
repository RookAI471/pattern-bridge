# Placebo Week Pack, v0

## Purpose

This pack defines the first comparison weeks for the January 7, 2022 weekly meta-playbook.

Current direction:
- these should be implemented as **real historical ES weeks first**, not invented synthetic bar paths
- the point is to test whether a human and then an AI agree on what counts as:
  - the same important weekly meta
  - versus a superficially similar but structurally different week

The earlier synthetic-bar experiment was useful mainly as a negative lesson: preserving a narrative sketch is not enough if the resulting bar texture stops looking like a real market.

## Reference weekly meta

Reference week:
- `weekly-meta-playbook-2022-01-07.md`

Core meta:
- multi-week range-high context matters
- Tuesday failure at that important location matters most
- Tuesday signal quality is stronger when the high also reads like a **poor TPO high / weak auction high**
- failure creates a new liquidation / operating area
- FOMC confirms the new range and sets the weekly high
- post-FOMC regime is range-dominant
- Friday NFP is lower value for momentum because the market is more exhausted and informed by then

## Candidate selection rule, updated

When building placebos for this family, ignore FOMC and NFP as primary selection criteria.
They are acceptable as background catalysts, but they are **not** the core of the setup.

The minimum structural screen is:
1. attempt to break above or below a prior well-defined range from previous weeks
2. fail to break, better if there is a PTPOH or PTPO L
3. clean break of the other side of the range

If a candidate week does not do those three things, it is not the weekly setup we want.

A better match then adds:
- establishment of a **new range**, not just continued trend
- a latter portion of the week that becomes notably more range-bound

---

## Positive Placebo A, real week ending 2021-12-17

### Candidate reason
- archive note: `ES Sun Wick/Fail, M b, FOMC range sweep higher leave CINAH, Thu CINAH, Fri close weekly near low`
- structurally this looked closer than the earlier catalyst-led pick because it appears to include a more explicit early wick/fail and later range behavior

### Current status
This is the **replacement Positive A candidate** and still needs Edward's visual judgment.

### Why it belongs in the pack
- looks closer on structure-first screening than the previous May 6 candidate
- may preserve more of the fail-at-an-edge then later range-control feel
- still provisional until visual review confirms it

---

## Positive Placebo B, real week ending 2021-10-08

### Candidate reason
- archive note: `ES AnA Cont. Failure, bad TPOL, pre NFP`
- this looked like a better structure-first candidate because it suggests failure/absorption logic and weak-auction quality rather than just shared catalysts

### Current status
This is the **replacement Positive B candidate** and still needs Edward's visual judgment.

### Why it belongs in the pack
- screened in because of failure structure and weak-auction language, not because of event overlap
- may be closer to the Jan 7 family on profile logic even if the catalyst mix differs
- still provisional until visual review confirms it

---

## Negative Placebo A, real week ending 2022-03-18

### Candidate reason
- archive note: `ES 60m W broken, post FOMC grind higher, 5min flag 4420 Fri Trend Higher Quad Witching`
- event family overlaps through FOMC, but the post-event behavior appears materially different

### Human intention
This should probably be a **FAIL**.

### Why it belongs in the pack
- likely breaks the canonical post-FOMC regime
- continuation / grind-higher behavior is exactly the kind of false cousin we want the model to reject

---

## Negative Placebo B, real week ending 2021-09-24

### Candidate reason
- archive note: `ES Sun Break AnA, test 50EMA, Washback M, FOMC Grind through Sun Gap, close within prior week range`
- tagged `Auction & Absorption`, not `Range Sweep`

### Human intention
This should probably be a **FAIL** or at minimum a strong contrast case.

### Why it belongs in the pack
- still an FOMC week, so surface similarity exists
- but the controlling weekly logic appears to belong to a different archetype family
- useful for testing whether the model confuses "another FOMC week" with "the same weekly meta"

---

## Human grading template

For each placebo:
- `grade`: PASS / FAIL
- `analog_strength`: strong / medium / weak
- `why`: one short paragraph
- `what mattered most`: bullet list
- `what did not matter`: bullet list

## AI grading template

For each placebo, the AI must output:
- `grade`: PASS / FAIL
- `analog_strength`: strong / medium / weak
- `must-match features present?`
- `non-invalidating differences ignored correctly?`
- `major reason for pass or fail`

## Note

These are first-pass **real historical candidate** labels.

The first attempted positive slate already exposed a useful failure mode:
- shared catalysts and broad archive labels are too weak for candidate selection

Next version should:
- replace weak candidates using the stricter structural screen above
- add more precise event sequencing notes for each chosen real week
- keep using real historical weeks as the default placebo substrate unless a later synthetic lane earns its way in
