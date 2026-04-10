# Roadmap v0

## Purpose

This document sequences the early work for Pattern Bridge into a practical v0 roadmap.

The goal is not to over-plan.
The goal is to make sure the next work reduces ambiguity in the right order.

## Guiding rule

Do not start by building a broad scanner.
Start by proving that the product can:
- represent bridges well
- retrieve useful analogs
- support trader review
- improve through debrief

## v0 definition

Pattern Bridge v0 should prove the core loop:
- context
- candidate bridge
- analog retrieval
- trader judgment
- debrief
- memory improvement

## Phase 0: foundation

### Goal
Lock the product frame so implementation does not drift.

### Deliverables
- README
- product thesis
- schema
- workflow
- market wedge
- personas
- screen map
- MVP doc

### Exit condition
Repo clearly explains the product and early scope.

Status: largely complete.

---

## Phase 1: ontology and bridge memory

### Goal
Create the first usable bridge library and memory model.

### Work
- finalize minimum bridge schema
- define bridge family / variant relationships
- create a starter bridge set manually
- define evidence linking approach
- define failure-case representation

### Suggested outputs
- 5 to 10 canonical bridge objects
- 2 to 3 examples each where possible
- at least some failed lookalikes documented

### Why this phase matters
If the bridge objects are weak, the whole product becomes vague.

### Exit condition
A user can browse a small but coherent bridge library and understand what each bridge is, when it belongs, and what it should not be confused with.

---

## Phase 2: analog retrieval

### Goal
Prove that the product can surface useful related examples.

### Work
- define similarity dimensions
- implement simple retrieval logic
- connect examples to bridges
- expose closest matches and false lookalikes
- test retrieval quality on a narrow set of cases

### Why this phase matters
Analog retrieval is one of the core sources of value.
If retrieval is weak, candidate surfacing will feel generic.

### Exit condition
Given a bridge or candidate, the product can show examples that traders consistently judge as relevant enough to inspect.

---

## Phase 3: candidate discovery workflow

### Goal
Surface candidate bridges for trader evaluation.

### Work
- define candidate object
- define candidate states
- implement candidate review actions
- attach bridge explanations
- show what matches and what is missing

### Suggested scope
Keep the universe narrow at first.
Do not try to scan everything.

### Exit condition
A trader can see candidate bridges, understand why they surfaced, and accept/reject/watch them with minimal friction.

---

## Phase 4: journal and debrief loop

### Goal
Make the product compound over time.

### Work
- implement premarket notes
- implement live notes
- implement post-session debrief
- connect debrief outcomes back into bridge refinement
- capture rejection reasons and failure modes

### Why this phase matters
Without debrief, the product becomes a memory toy.
With debrief, it becomes a learning engine.

### Exit condition
Daily use improves the bridge library instead of just generating more clutter.

---

## Phase 5: narrow real-user validation

### Goal
Test whether real traders get actual leverage from the loop.

### Suggested users
- 1 to 3 serious discretionary traders
- potentially one coach / mentor profile

### Questions to validate
- are surfaced candidates worth evaluating?
- are analogs genuinely useful?
- does this reduce manual burden?
- does debrief quality improve?
- does the trader feel more organized or just busier?

### Exit condition
At least some users say the product improves context, recall, or review enough that they would keep using it.

---

## Phase 6: stock wedge exploration

### Goal
Test whether the framework scales into a broader stock workflow.

### Work
- define stock-compatible bridge families
- choose initial stock universe
- define catalyst taxonomy
- adapt structural references where necessary
- test discovery quality on stocks

### Exit condition
The product can surface stock candidates without collapsing into generic scanner sludge.

---

## Suggested immediate next work

### Highest priority now
1. define 5 to 10 starter bridge objects
2. define candidate object and candidate states
3. define similarity dimensions for analog retrieval
4. decide how evidence and examples are stored

### Nice to have later
- richer charts
- collaboration
- coach workflows
- broader scanning
- automation around event ingestion

## What not to do yet

Do not do these too early:
- broad stock scanning
- broker integration
- auto-execution ideas
- performance dashboards as the center of the product
- complex visual design before workflow clarity

## One-sentence roadmap summary

v0 should prove that structured bridge memory plus analog retrieval plus debrief creates a better discretionary trading workflow.
