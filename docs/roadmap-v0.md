# Roadmap v0

## Purpose

This roadmap reflects the current, narrower Pattern Bridge direction.

The goal is not to build a broad bridge library first.
The goal is to prove that **ES weekly event analogs** can be represented and validated honestly.

## Current guiding rule

Do not assume a weekly archetype is real because the label feels intuitive.

Start by proving that the product can:
- reconstruct a known canonical week from actual intraday data
- represent the important weekly meta explicitly
- separate controlling context from cosmetic variation
- distinguish true analogs from false lookalikes

## v0 definition

Pattern Bridge v0 should prove this loop:
- real intraday data
- canonical week reconstruction
- explicit weekly-meta object
- placebo weeks
- human grading
- later AI grading against those human judgments

## Phase 0: scope reset and source grounding

### Goal
Lock the project to the real wedge and stop ontology drift.

### Deliverables
- rewritten README
- ES-only weekly-archetype framing
- data-sources doc
- canonical week spec for Jan 7, 2022
- weekly-meta schema
- placebo validation framework

### Exit condition
The repo clearly explains that the active project is ES weekly-context validation, not generic pattern-library expansion.

Status: complete enough to proceed.

---

## Phase 1: canonical week reconstruction

### Goal
Prove one real week can be reconstructed from machine-legal inputs before making bigger claims.

### Current anchor
- week ending `2022-01-07`

### Work
- normalize real ES 30-minute data
- reconstruct the canonical week in machine-readable form
- document the important weekly events and opportunity ranking
- separate profile geometry from subjective shorthand

### Exit condition
A grounded observer can inspect the real week and agree that the canonical object is anchored to actual data, not just language.

Status: materially underway.

---

## Phase 2: minimum market-profile / structure layer

### Goal
Create the smallest useful price-based structure layer needed for weekly comparison.

### Work
- build minimal profile representations from price data
- detect simple geometry and weakness/strength clues
- avoid pretending branded labels are already solved
- tighten detector logic for tails, center width, repetition, and sequence

### Exit condition
The system can represent enough structure to support honest comparison without overselling fuzzy labels.

Status: started, still crude.

---

## Phase 3: placebo validation

### Goal
Test whether the weekly meta is actually discriminative.

### Work
- create positive and negative placebo weeks
- ensure each placebo includes the proper prior multi-week context
- have Edward grade each placebo first
- only then test AI pass/fail reasoning

### Exit condition
Humans can consistently explain why each placebo passes or fails, and the AI can later be measured against that standard.

Status: framework and initial pack created, human grading still pending.

---

## Phase 4: analog detection test

### Goal
See whether the weekly-meta object is enough to find similar weeks without cheating.

### Work
- compare the canonical week against placebo and historical cases
- use importance-weighted similarity, not flat feature matching
- confirm the system ignores irrelevant differences
- reject false positives that only resemble the surface pattern

### Exit condition
The system can identify relevant analogs for the right reasons and reject bad ones for the right reasons.

---

## Phase 5: second seed week and contrast class

### Goal
Expand only after Jan 7 logic is honest.

### Candidate next week
- week ending `2022-02-11`

### Work
- reconstruct the second seed week using the same discipline
- compare where the meta overlaps and diverges
- refine the schema if the second week exposes missing structure

### Exit condition
The project can handle at least two distinct event-week classes without collapsing into label soup.

---

## Immediate next work

1. improve viewer UX for human placebo grading
2. human-grade the placebo pack
3. tighten `scripts/evaluate_profile_features.py`
4. test similarity logic against placebo and historical cases
5. expand to Feb 11 only after Jan 7 is truly grounded

## What not to do yet

Do not do these early:
- broad stock scanning
- generic bridge-library expansion
- UX polish detached from validation needs
- AI grading before human pass/fail exists
- exaggerated claims about machine-detectable labels

## One-sentence roadmap summary

Pattern Bridge v0 should prove that a real ES event week can be reconstructed, abstracted into weekly meta, and distinguished from false analogs through placebo validation.
