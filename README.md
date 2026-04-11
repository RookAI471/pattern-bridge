# Pattern Bridge

Pattern Bridge is an AI-assisted research project for **ES weekly context and analog matching**.

Current focus:
- **ES only**
- **weekly event archetypes**
- especially **FOMC**, **FOMC + NFP**, and related event weeks
- proving whether AI can compare weeks based on the **important weekly meta**, not just labels or visual resemblance

## What this is

This repo is no longer centered on building a broad ontology of generic pattern bridges.

The current job is narrower and more honest:
- reconstruct known canonical ES weeks from machine-legal inputs
- represent the weekly meta that actually matters
- test whether similar weeks can be detected without cheating
- validate that with human-graded placebo weeks before claiming anything real

In plain English, the product direction is:
- help a trader remember the important higher-timeframe context
- compare the current week to prior event weeks that actually matter
- identify what is structurally important versus cosmetic noise
- support regime/context review, not fake-precision execution

## What we are trying to prove

The core research question is:

> Can AI distinguish a genuinely similar ES event week from a superficially similar one, using the right higher-timeframe context and weekly logic?

That means proving, in order:
1. a canonical real week can be reconstructed from actual intraday data
2. the important weekly meta can be represented explicitly
3. positive and negative placebo weeks can be human-graded honestly
4. AI can later pass or fail those weeks for the right reasons

## Current reference weeks

Primary canonical week:
- **Week ending 2022-01-07**

Secondary seed / contrast week:
- **Week ending 2022-02-11**

Locked ranked key events for the canonical Jan 7 week:
1. Tuesday bikini failure at the multi week range high
2. Wednesday FOMC Min inverse P liq
3. Friday NFP bikini chop at poor TPOL

## Key modeling rules

- **Daily bars are not enough** for honest validation.
- Use **ES intraday 30-minute data** as the primary substrate.
- Do not assume discretionary labels are automatically machine-definable.
- Start with **Market Profile / price structure first**, labels second.
- Preserve Edward's exact term meanings.
- Do not conflate:
  - `2022-01-04` = `bikini_failure`
  - `2022-01-07` = `true_bikini`
- The value is in **weekly meta and controlling context**, not recreating every handwritten chart note mechanically.

## Current repo structure

### Core docs
- `docs/es-weekly-event-archetypes.md`
- `docs/es-weekly-archetype-schema-v0.md`
- `docs/weekly-meta-playbook-schema.md`
- `docs/weekly-meta-playbook-2022-01-07.md`
- `docs/canonical-week-reconstruction-test.md`
- `docs/jan-7-2022-single-week-reconstruction-spec.md`
- `docs/jan-7-2022-raw-machine-reconstruction.md`
- `docs/jan-7-2022-label-precision-notes.md`
- `docs/minimal-market-profile-spec.md`
- `docs/placebo-week-validation-framework.md`
- `docs/placebo-week-pack-v0.md`
- `docs/placebo-week-viewing-notes.md`
- `docs/data-sources.md`

### Data and scripts
- `data/market-data/es_30m_continuous.csv`
- `data/placebos/`
- `scripts/build_price_profile.py`
- `scripts/evaluate_profile_features.py`

## Current status

Current status is no longer “broad product exploration.”

It is:
- **narrow ES weekly-context validation**
- **real-data reconstruction first**
- **placebo validation second**
- **AI grading only after human grading**

Recent progress:
- canonical Jan 7 week documented more precisely
- weekly meta object defined
- placebo validation framework written
- first placebo pack created
- multi-week context viewer served through the Track B lane for human review
- profile-feature detector started, but still crude and in need of tightening

## Immediate next steps

1. clean up the viewer UX so the evaluation week is obvious
2. human-grade the placebo pack
3. test AI pass/fail reasoning against those grades
4. tighten the profile / Market Profile detector logic
5. expand to the Feb 11, 2022 contrast week only after Jan 7 logic is grounded

## Anti-goals

Do not drift into:
- generic scanner product language
- auto-trading theater
- ladder-reading AI fantasies
- broad stock-market scope too early
- assuming archetypes are real before validation
- pretending weak labels are already machine-ready

## Repo principle

Be narrower and more empirical than feels exciting.

If a weekly archetype cannot survive:
- real-data reconstruction
- placebo testing
- human grading
- and honest comparison

then it is not real enough yet.
