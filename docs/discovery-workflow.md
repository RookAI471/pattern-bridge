# Discovery Workflow

## Purpose

This document defines the end-to-end workflow for AI-suggested pattern bridges.

The product should help a trader discover, evaluate, accept, reject, and refine candidate bridges without pretending to replace trader judgment.

## Design goal

The workflow should do two things at the same time:
- reduce the manual burden of hunting, recall, and organization
- preserve the trader's role as final evaluator and decision-maker

## Core principle

The product should suggest.
The trader should judge.
The debrief should improve the next suggestion cycle.

## Workflow overview

1. Premarket context ingest
2. Candidate bridge generation
3. Analog retrieval and similarity framing
4. Trader review and triage
5. Confirmation and invalidation tracking
6. Session logging
7. Post-session debrief
8. Memory and playbook update

---

## 1. Premarket context ingest

### Purpose
Build the outer frame for the day.

### Inputs
- event calendar
- macro themes
- higher-timeframe structure
- overnight session state
- sector and cross-market context
- trader-entered hypotheses
- existing playbooks and bridge library

### Product behavior
The system should help answer:
- what type of day may be developing?
- what events or catalysts matter?
- which markets or names deserve attention?
- what structural references matter most?
- what broad bridge families may be relevant today?

### Output
A structured context card, not a prediction.

Example contents:
- key events
- key levels
- regime notes
- participation expectations
- likely bridge families to monitor

---

## 2. Candidate bridge generation

### Purpose
Surface plausible bridges before or during the session.

### Sources of candidates
- rule-based context matching
- analog retrieval from prior examples
- market scan outputs
- event-specific templates
- trader watchlists
- sector / correlation filters

### Product behavior
The system should say things like:
- these names resemble bridge family X
- these products show the same preceding conditions as prior bridge Y
- these 3 cases are the best contextual matches right now

It should not say:
- buy this now
- this trade will work
- confidence 97 percent

### Output shape
Each candidate bridge should include:
- bridge name or provisional label
- why it surfaced
- top matching features
- missing features
- closest prior analogs
- what still needs confirmation

---

## 3. Analog retrieval and similarity framing

### Purpose
Give the trader memory, not just alerts.

### Product behavior
When a candidate bridge is surfaced, the system should retrieve:
- prior examples with similar context
- related variants
- examples that looked similar but failed
- examples from correlated markets if relevant

### Similarity dimensions
Potential retrieval dimensions:
- regime
- event type
- structure
- participation
- timing within session
- progression shape
- confirmation behavior

### Output
A ranked analog set with plain-English explanation.

Example:
- closest match because of low-participation overnight drift, reclaimed open, and volume surge through prior range
- weaker match because structure aligns but event context differs
- false friend because it lacked the required participation shift

---

## 4. Trader review and triage

### Purpose
Create a human decision point.

### Trader actions
The trader should be able to:
- accept candidate as relevant
- reject candidate
- mark as interesting but incomplete
- relabel it
- assign it to an existing bridge family
- split it into a new variant

### Review questions
The interface should encourage questions like:
- does this really fit the bridge, or just rhyme with it?
- what is missing?
- is the context right but execution not there yet?
- is this actually a different bridge?
- am I forcing recognition because I want a trade?

### Output
A triaged candidate state:
- accepted
- rejected
- watchlist
- variant under review

---

## 5. Confirmation and invalidation tracking

### Purpose
Help the trader monitor whether the bridge is actually becoming real.

### Product behavior
Once a candidate is in play, the system should track:
- identifier observed?
- confirmation observed?
- progression matching expectations?
- invalidation triggered?
- tempo deviating from prior analogs?

### Important constraint
This is not auto-execution logic.
It is structured monitoring.

### Output
A live checklist or state tracker.

Example sections:
- context present
- identifier present
- confirmation pending
- invalidation not triggered
- progression diverging from expected template

---

## 6. Session logging

### Purpose
Capture reality while it is happening.

### Product behavior
The system should make it easy to log:
- key timestamps
- observed identifiers
- confirmation points
- entry/exit notes
- progression changes
- emotional state
- reasons for acceptance or rejection

### Requirement
Logging must be lightweight enough to use during live trading.
If too heavy, it will die.

### Output
A compact chronological session log attached to the bridge candidate.

---

## 7. Post-session debrief

### Purpose
Convert experience into improved pattern quality.

### Debrief questions
- did the bridge actually fit?
- what preceded it clearly?
- what was misread?
- what confirmed it best?
- what progression was expected versus observed?
- what invalidation signal was missed or respected?
- does this strengthen, weaken, split, or retire the bridge?

### Product behavior
The system should help transform raw notes into:
- revised bridge summary
- refined identifier
- refined confirmation
- refined progression notes
- failure case capture
- variant creation if warranted

---

## 8. Memory and playbook update

### Purpose
Close the loop so future suggestions improve.

### Product behavior
Accepted or debriefed candidates should feed:
- bridge memory
- analog retrieval indexes
- playbook updates
- variant trees
- trader-specific context preferences

### Learning loop
The product should learn from:
- accepted candidates
- rejected candidates
- bridges that looked similar but failed
- recurring invalidation patterns
- what kinds of candidates the trader actually finds useful

---

# Roles: AI vs trader

## AI should own
- retrieval
- organization
- candidate surfacing
- similarity framing
- checklist generation
- debrief structuring
- memory updates

## Trader should own
- final interpretation
- trade selection
- risk commitment
- execution discretion
- deciding whether a bridge truly applies

## Shared zone
- hypothesis formation
- variant creation
- refining bridge definitions
- reviewing failures

---

# Acceptance and rejection are equally important

This is non-negotiable.

The product must treat rejection as useful data.
If every surfaced bridge only trains on accepted cases, the system will drift toward confirmation bias and false confidence.

Useful rejection reasons include:
- wrong regime
- wrong participation
- wrong tempo
- looked similar but lacked identifier
- event context overrode structure
- execution too mature
- false bridge, actually different family

---

# What success looks like

A good workflow should make a trader say:
- I found relevant situations faster
- I remembered prior analogs more clearly
- I had a better way to think about today's context
- I debriefed more consistently
- my playbooks got sharper over time

Not:
- the AI told me what to buy

---

# MVP workflow recommendation

For v0, keep it simple:

1. trader enters or confirms premarket context
2. system surfaces candidate bridges and prior analogs
3. trader accepts/rejects/watchlists candidates
4. system tracks confirmation/invalidation notes
5. trader debriefs after session
6. system updates bridge memory

That is enough to validate whether the core loop is real.
