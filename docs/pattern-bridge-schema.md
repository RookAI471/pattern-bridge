# Pattern Bridge Schema

## Purpose

This document defines the minimum viable schema for a Pattern Bridge.

The goal is to create a structure strong enough to support:
- storage
- retrieval
- analog matching
- trader review
- debrief refinement
- variant and translation handling

A Pattern Bridge should be richer than a setup note and more actionable than a loose trade journal entry.

## Core principle

A pattern bridge is not just a setup.
It is a structured relationship between:
- preceding context
- structural conditions
- participation conditions
- executable identifiers
- expected progression
- failure modes
- review outcomes

## Minimum viable object

```yaml
id: string
slug: string
name: string
status: draft | active | archived
summary: string
created_at: datetime
updated_at: datetime
owner: string
confidence: low | medium | high

context:
  regime:
    - panic
    - trend
    - balance
    - event_day
    - squeeze
    - liquidation
    - other
  event_types:
    - FOMC
    - NFP
    - CPI
    - ECB
    - earnings
    - none
    - other
  session_structure:
    overnight_required: boolean
    cash_open_required: boolean
    intraday_only: boolean
  market_scope:
    instruments: []
    sectors: []
    market_types: []
  higher_timeframe_conditions: []
  structural_references: []
  participation_conditions: []
  correlation_conditions: []

pattern:
  brand: string
  narrative: string
  preceding_conditions: []
  mechanics: []
  identifier: []
  confirmation: []
  expected_progression: []
  target_logic: []
  invalidation: []
  failure_modes: []
  execution_notes: []
  risk_notes: []

translation:
  source_market: string
  transferable_to: []
  constraints: []
  known_variants: []

evidence:
  examples: []
  charts: []
  notes: []
  linked_events: []
  linked_playbooks: []

review:
  debrief_summary: string
  lessons: []
  do_not_confuse_with: []
  tags: []
  quality_score: integer
```

## Field definitions

### id / slug / name
Basic identity.

- `id`: internal unique identifier
- `slug`: stable URL-safe key
- `name`: human-readable bridge name

### status
Lifecycle state.

Suggested values:
- `draft`: still forming
- `active`: usable bridge with enough evidence
- `archived`: retired, stale, or superseded

### summary
One-paragraph plain-English explanation of the bridge.

This should answer:
- what kind of opportunity this is
- when it tends to appear
- why it matters

### confidence
High-level confidence in the bridge as a reusable object.

This is confidence in the bridge definition, not confidence in any single trade.

## Context block

The context block describes the environment in which the bridge becomes plausible.

### regime
Broad environment labels.

Examples:
- panic
- trend
- balance
- liquidation
- event-driven
- squeeze

This is one of the most important blocks because it keeps the system from treating all patterns as universal.

### event_types
Which event classes commonly host the bridge.

Examples:
- FOMC
- CPI
- NFP
- earnings
- none

### session_structure
Important session assumptions.

Examples:
- requires overnight inventory
- requires cash open interaction
- only relevant intraday

### market_scope
Where this bridge can logically appear.

Examples:
- ES, NQ, CL, GC, 6E
- large-cap equities
- sector ETFs
- single-name stocks

### higher_timeframe_conditions
The big-picture setup.

Examples:
- multi-day balance
- failed breakdown below weekly support
- trend day extension into obvious prior level
- gap below value but reclaiming open

### structural_references
Specific map features the trader uses.

Examples:
- HVN / LVN
- single prints
- ledge
- cave
- ONH / ONL
- prior day high / low
- VWAP bands
- gap fills
- range extremes

### participation_conditions
Who is involved and how much energy is in the move.

Examples:
- RVOL elevated
- low participation drift
- high-volatility event day
- trapped shorts / trapped longs

### correlation_conditions
Cross-market or cross-name relationships.

Examples:
- bonds leading equities
- oil confirming inflation trade
- sector strength leading individual setup

## Pattern block

This is the heart of the bridge.

### brand
A memorable internal label.

This can be emotional, visual, or descriptive.
The point is recall.

### narrative
A short explanation of the story the pattern is expressing.

Examples:
- trapped overnight shorts forced to unwind into a thin structure
- event shock rejected, then trend resumes through second-wave confirmation

### preceding_conditions
What typically happens before the bridge appears.

This is distinct from the setup itself.

### mechanics
The chronological stages of the bridge.

This should answer:
- what happens first
- what happens second
- where the shape changes

### identifier
The early clue that the bridge may be forming.

This is where real-time usefulness starts.

### confirmation
What upgrades the bridge from possibility to executable opportunity.

Examples:
- volume surge
- reclaim of prior range
- failure to sustain at lows
- shift in pace

### expected_progression
How the bridge should move if valid.

Examples:
- slow grind to first resistance
- fast initial pop then pause
- second-wave acceleration later in session

### target_logic
How the move is expected to resolve.

Not a single price target necessarily.
Could include:
- first resistance
- prior high/low
- fill target
- measured move
- liquidation objective

### invalidation
What must not happen if the bridge is right.

Examples:
- cannot stay below reclaimed range
- cannot lose the volume surge zone cleanly
- cannot fail to attract participation after confirmation

### failure_modes
Ways the bridge often fools traders.

This field is essential.
The system must not only remember what works.
It must remember near-matches and misreads.

### execution_notes
Practical notes on access.

Examples:
- aggressive early access possible at absorption
- safer entry on second surge
- poor R if entered after first target extension

### risk_notes
How risk behaves in this bridge.

Examples:
- wide stop but asymmetric path
- low-risk early punt, but only partial size
- must carry core beyond pre-cash range

## Translation block

This captures how the bridge ports across products.

### source_market
Where the bridge was originally identified or best understood.

### transferable_to
Other markets where the bridge may appear.

### constraints
Why translation may fail.

Examples:
- requires overnight plus cash session
- depends on certain liquidity profile
- only reliable in correlated environments

### known_variants
Named variants or sibling bridges.

This allows one bridge family to branch without collapsing into chaos.

## Evidence block

This is the memory substrate.

### examples
Canonical examples of the bridge.

### charts
Annotated screenshots, videos, replays.

### notes
Research notes, debriefs, linked markdown pages.

### linked_events
Relevant event hubs or event classes.

### linked_playbooks
Related playbooks or sister patterns.

## Review block

This is where learning compounds.

### debrief_summary
Current best understanding after accumulated review.

### lessons
What has been learned so far.

### do_not_confuse_with
Common false matches.

This field matters a lot.
It helps prevent observational selection bias and lazy analog matching.

### tags
Loose retrieval labels.

### quality_score
A rough score for internal use.

Not for traders as a promise metric.
Mostly useful for ranking candidate bridges and prioritizing review.

## Non-negotiable design rules

### 1. Context and execution must stay separate
A bridge without context becomes a generic setup.
A bridge without execution logic becomes theory sludge.

### 2. Failure cases must be first-class
The schema must store near-matches, misreads, and broken expectations.
Otherwise the system will overfit to winners.

### 3. Variant support is required
The same bridge can express differently by market, tempo, session structure, or event environment.

### 4. Translation support is required
A useful bridge engine must support structural transfer, not just single-market memorization.

### 5. The schema must support trader disagreement
The product should allow a trader to reject, relabel, or split a bridge.
The ontology should be living.

## MVP implementation note

For v0, this schema does not need to be perfect.
It only needs to be strong enough to support:
- manual bridge creation
- analog retrieval
- candidate bridge review
- structured debrief
- iterative refinement

If those five things work, the schema is doing its job.
