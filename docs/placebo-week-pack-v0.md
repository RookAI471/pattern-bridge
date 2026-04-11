# Placebo Week Pack, v0

## Purpose

This pack defines the first synthetic comparison weeks for the January 7, 2022 weekly meta-playbook.

These are not intended to be perfect market simulations.
They are intended to test whether a human and then an AI agree on what counts as:
- the same important weekly meta
- versus a superficially similar but structurally different week

## Reference weekly meta

Reference week:
- `weekly-meta-playbook-2022-01-07.md`

Core meta:
- multi-week range-high context matters
- Tuesday failure at that important location matters most
- failure creates a new liquidation / operating area
- FOMC confirms the new range and sets the weekly high
- post-FOMC regime is range-dominant
- Friday NFP is lower value for momentum because the market is more exhausted and informed by then

---

## Positive Placebo A, Close Analog

### Human intention
This should probably be a **PASS** if the evaluator agrees the important weekly logic is preserved.

### Structure
- ES is trading at the upper edge of a meaningful multi-week rectangular range
- Tuesday tries to complete a clean two-sided profile at the upper boundary but fails and breaks back through the opposite side late in the session
- the failure creates a lower operating area that did not matter much before Tuesday
- Wednesday FOMC rallies back up but fails to reclaim the important upper structure and instead sets the weekly high
- after FOMC, the market spends Thursday and Friday trading inside the newly established lower range
- Friday is choppy and lower value for momentum, but still tradable for a range or options trader

### Intended grade
- `human_expected`: `PASS`

### Why
- same controlling location
- same early failure type
- same new range establishment
- same post-FOMC range regime
- same information economics

---

## Positive Placebo B, Same Meta With Irrelevant Lower Clutter

### Human intention
This should probably be a **PASS**.

### Structure
- ES is still at the top of the important multi-week range
- there is also a visible lower nearby range below the market, but it is not the controlling context
- Tuesday fails at the upper decision-relevant structure and rotates back down aggressively
- Wednesday FOMC sets the weekly high and confirms that the week will now trade in a lower balance / liquidation area
- Thursday and Friday continue to respect the new lower operating area
- Friday remains a poor momentum day and a better fit for range or options logic

### Intended grade
- `human_expected`: `PASS`

### Why
- the extra lower range is explicitly **non-invalidating clutter**
- the important controlling structure and the weekly meta are unchanged

---

## Negative Placebo A, Wrong Post-FOMC Regime

### Human intention
This should probably be a **FAIL**.

### Structure
- ES begins near a meaningful higher-timeframe range high
- Tuesday fails at the upper edge and initially rotates lower
- Wednesday FOMC then reclaims the upper structure and establishes strong accepted continuation above the old range
- Thursday and Friday continue trend behavior rather than balance inside a new lower operating area
- Friday remains one of the best momentum opportunities of the week

### Intended grade
- `human_expected`: `FAIL`

### Why
- this breaks the most important weekly consequence
- FOMC does not confirm a lower range-dominant regime
- instead it confirms continuation
- the opportunity ranking is materially different

---

## Negative Placebo B, Failure at the Wrong Location

### Human intention
This should probably be a **FAIL**.

### Structure
- ES is trading in the middle of a broader weekly structure, not at the meaningful multi-week range high
- Tuesday forms and fails a superficially similar profile shape, but the failure occurs at a secondary intraday location rather than the decision-relevant higher-timeframe structure
- Wednesday FOMC behaves broadly rotationally
- Thursday and Friday are range-bound, but the early failure did not happen at the important location that made the reference week special

### Intended grade
- `human_expected`: `FAIL`

### Why
- superficial shape similarity is not enough
- the most important contextual requirement is missing
- the week is missing the decisive failure at the controlling HTF location

---

## Human grading template

For each placebo:
- `grade`: PASS / FAIL
- `why`: one short paragraph
- `what mattered most`: bullet list
- `what did not matter`: bullet list

## AI grading template

For each placebo, the AI must output:
- `grade`: PASS / FAIL
- `must-match features present?`
- `non-invalidating differences ignored correctly?`
- `major reason for pass or fail`

## Note

These are intentionally simple first-pass placebo descriptions.
If Edward agrees the framing is directionally right, the next version can add:
- more precise event sequencing
- finer structural detail
- perhaps partial synthetic bar/profile sketches
