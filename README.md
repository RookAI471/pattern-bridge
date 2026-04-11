# Pattern Bridge

Pattern Bridge is an AI-assisted research project for **rare weekly structural analogs** in futures markets.

## Current conclusion

We are no longer just looking for whether a Jan 7-style family might exist.

Current evidence says it **does** exist as a **rare, high-specificity structural family**.

What has changed:
- this is **not** being treated as a broad weekly label taxonomy anymore
- this is **not** being selected by shared catalysts like FOMC or NFP anymore
- this **is** being treated as a structure-first analog problem anchored to real 30-minute price history

The working family definition is now:
1. attempt to break above or below a prior well-defined multi-week range
2. fail at that edge, ideally with weak-auction quality such as PTPOH / PTPOL
3. cleanly break the other side of the range
4. stronger match if the market then begins to establish a **new range** instead of simply continuing to trend

In plain English, the product direction is:
- help a trader remember rare but important weekly structural families
- compare the current week to prior real weeks that actually match the structure
- identify what is structurally important versus cosmetic noise
- support regime/context review, not fake-precision execution

## What this repo is now

This repo is no longer centered on a broad ontology of generic pattern bridges.

The current job is narrower and more grounded:
- reconstruct canonical weeks from machine-legal intraday data
- represent the weekly meta that actually matters
- search full price history for structurally similar weeks
- separate real analogs from false cousins
- validate those findings with human review before making stronger claims

## What we have actually shown so far

The current claim is no longer just:
- "maybe there is a pattern here"

It is:
- there appears to be a **real but rare structural family**
- the hard part is not finding reversals
- the hard part is finding the subset that then **settles into a new range**

That is the intelligence layer Pattern Bridge is trying to model.

## Current reference weeks

Primary canonical week:
- **Week ending 2022-01-07**

Secondary seed / contrast week:
- **Week ending 2022-02-11**

Locked ranked key events for the canonical Jan 7 week:
1. Tuesday PTPOH-driven bikini failure at the multi week range high
2. Wednesday FOMC Min inverse P liq
3. Friday NFP bikini chop at poor TPOL

## Markets explored so far

### Primary anchor market
- **ES** remains the canonical anchor market and the main validation lane.

### Cross-market exploratory scan completed
The current structural family has already been explored across:
- **ES**
- **CL**
- **BP**
- **FV**
- **JY**
- **NQ**
- **EU**
- **GC**
- **US**
- **TY**

### Current takeaways by market
- **ES**: rare but real under the current scan. Strongest current range-establishing hit is **2016-11-11**.
- **CL**: strongest non-ES market so far. Strongest current range-establishing hit is **2011-05-06**.
- **BP** and **FV**: exploratory hits justify later inspection.
- **JY, NQ, EU, GC, US, TY**: explored at first-pass structural-scan level, but not yet priority follow-up lanes.

## Key modeling rules

- **Daily bars are not enough** for honest validation.
- Use **30-minute futures data** as the working substrate.
- **ES** remains the canonical anchor, but the structural family can be explored cross-market.
- Do not assume discretionary labels are automatically machine-definable.
- Start with **Market Profile / price structure first**, labels second.
- Preserve Edward's exact term meanings.
- Do not conflate:
  - `2022-01-04` = `bikini_failure`
  - `2022-01-07` = `true_bikini`
- Treat **FOMC** and **NFP** as catalysts, not as the core selection logic for analogs.
- The value is in **weekly meta, controlling context, and later range-establishment**, not recreating every handwritten chart note mechanically.

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
- **rare weekly structural-family validation**
- **ES anchor, cross-market exploratory follow-through**
- **real-data reconstruction first**
- **mechanical screening plus human review**
- **AI grading only after human grading**

Recent progress:
- canonical Jan 7 week documented more precisely
- weekly meta object defined and tightened around PTPOH / weak-high nuance
- placebo validation framework rewritten around structure-first rules
- catalyst-led candidate picking explicitly rejected
- synthetic filler-bar placebo generation explicitly rejected
- full-history sequence-aware price scan run on ES and across 9 additional markets
- ES and CL both produced a stronger range-establishing hit under the current scan
- multi-week context viewer served through the Track B lane for human review
- profile-feature detector started, but still crude and in need of tightening

## Immediate next steps

1. inspect success vs near-miss weeks side by side
   - ES: `2016-11-11` vs `2022-12-16`
   - CL: `2011-05-06` vs `2012-05-04` and `2025-04-04`
2. improve the sequence-aware scan with better tempo and range-establishment logic
3. build stronger PTPOH / PTPOL and weak-auction proxies
4. revisit BP and FV after ES/CL discriminators are clearer
5. only then expand the family map further or revisit Feb 11 as a contrast class

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
