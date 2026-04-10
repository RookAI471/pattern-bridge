# Screen Map

## Purpose

This document turns the Pattern Bridge concept into a concrete product surface.

The goal is not final UI polish.
The goal is to define the minimum set of screens required to make the product real.

## Product principle

The product should feel like a thinking tool for discretionary traders.

It should help the trader:
- understand today's context
- see likely bridge candidates
- inspect why they surfaced
- compare them to prior analogs
- decide whether they matter
- log what happened
- debrief and improve the bridge library

## Core navigation

Suggested top-level navigation:
- Today
- Candidates
- Bridges
- Journal
- Review
- Settings

A future version may also split out:
- Events
- Watchlists
- Analytics

But those should not be necessary for v0.

---

## 1. Today screen

### Purpose
Give the trader the context for the session in one place.

### Main sections
- macro and event context
- regime summary
- key structural references
- participation expectations
- bridge families likely relevant today
- watchlist focus

### Questions this screen should answer
- what kind of day might this be?
- what matters most today?
- what should I be prepared for?
- what bridge families are worth watching?

### Suggested components
- event card
- context summary card
- key levels panel
- participation panel
- likely bridge families panel
- notes / hypothesis area

### MVP note
This can start as a mostly text-and-cards screen.
No fancy charting required for the first version.

---

## 2. Candidates screen

### Purpose
Show AI-suggested pattern bridge candidates for trader review.

### Main sections
- active candidates list
- candidate details panel
- analog preview
- state tags

### Candidate card should show
- candidate label
- instrument / symbol
- bridge family
- why it surfaced
- confidence as a soft heuristic, not promise
- what's missing
- candidate state

### Candidate states
- new
- watching
- accepted
- rejected
- variant under review
- expired

### Trader actions
- accept
- reject
- watch
- relabel
- attach to existing bridge
- create new bridge variant

### Questions this screen should answer
- what looks interesting right now?
- why is the system surfacing this?
- does this actually fit a known bridge?
- what still needs to happen?

---

## 3. Candidate detail screen

### Purpose
Let the trader inspect one candidate deeply before acting on it.

### Main sections
- context fit
- structural fit
- identifier / confirmation checklist
- analog cases
- failure lookalikes
- notes and logs

### Must-have panels

#### A. Why this surfaced
Plain-English explanation of the match.

#### B. Match dimensions
- regime
- event type
- structure
- participation
- session structure
- correlation

#### C. Missing pieces
What still needs confirmation.

#### D. Analog cases
- closest historical matches
- closest failed lookalikes
- translated examples if relevant

#### E. Confirmation / invalidation tracker
Live checklist for:
- identifier seen
- confirmation seen
- invalidation hit
- progression aligned or diverging

#### F. Trader notes
Fast notes during the session.

### Questions this screen should answer
- is this real or just rhyming?
- what would make this actionable?
- what would kill it?
- what prior examples should shape my expectations?

---

## 4. Bridges library screen

### Purpose
Provide a searchable home for existing pattern bridges.

### Main sections
- bridge list
- filters and tags
- bridge family tree / variants
- summary panel

### Useful filters
- market
- event type
- regime
- active vs draft vs archived
- bridge family
- confidence
- recent usage

### Bridge card should show
- name
- summary
- status
- markets
- event tags
- last reviewed date
- example count

### Questions this screen should answer
- what bridges do I already have?
- what families are most developed?
- where are my thin spots?

---

## 5. Bridge detail screen

### Purpose
Show the full bridge object.

### Main sections
- summary
- context definition
- pattern definition
- execution notes
- failure modes
- translation / variants
- evidence gallery
- debrief history

### Must-have sections
- preceding context
- identifier
- confirmation
- expected progression
- invalidation
- failure modes
- related variants
- examples

### Trader actions
- edit bridge
- split variant
- archive bridge
- link candidate to bridge
- add evidence

### Questions this screen should answer
- what is this bridge really?
- when does it belong?
- what should not be confused for it?
- how has understanding changed over time?

---

## 6. Journal screen

### Purpose
Support premarket prep, live notes, and post-session reflection in one workflow.

### Suggested sections
- preparation
- event prep
- hypotheses
- watchlist
- live observations
- trade observations
- learning notes
- end-of-day debrief

### MVP goal
The journal should be lighter than a giant Notion ritual but more structured than freeform notes.

### Questions this screen should answer
- what was I thinking before the session?
- what actually happened?
- what did I notice that matters later?

---

## 7. Review screen

### Purpose
Convert daily outcomes into improved bridges and better memory.

### Main sections
- accepted candidates
- rejected candidates
- bridge changes suggested by AI
- recurring failure patterns
- analogs worth adding to playbook

### Review actions
- strengthen bridge
- split bridge
- retire bridge
- mark false lookalike
- attach notes to existing bridge
- create debrief summary

### Questions this screen should answer
- what got sharper today?
- what fooled me today?
- what should change in the library?

---

## 8. Settings / profile screen

### Purpose
Configure product behavior and trader-specific preferences.

### Include
- markets followed
- event preferences
- watchlist sources
- bridge ranking preferences
- journaling defaults
- note taxonomy / tagging preferences
- risk language / tone preferences

### Future use
This area can later personalize retrieval and ranking behavior.

---

# MVP screen set

For v0, the minimum viable set is:

1. Today
2. Candidates
3. Candidate Detail
4. Bridges Library
5. Bridge Detail
6. Journal
7. Review

That is enough to validate the core loop.

# Suggested first-click experience

When a trader opens the product, they should land on **Today**.

From there the main loop should be:
- review context
- inspect candidates
- drill into one candidate
- watch or accept it
- log notes
- review and debrief later

That sequence should feel obvious.

# What to avoid

Avoid early UI mistakes like:
- overbuilding analytics dashboards
- making chart annotation the center of the product too early
- flooding the trader with low-quality candidates
- turning the home screen into a generic stock scanner

The product should feel like context first, candidates second, memory always.
