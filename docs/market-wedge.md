# Market Wedge

## Purpose

This document evaluates how the product should sequence market coverage.

The key question is not just where the product can work.
It is where the product can prove its value fastest without collapsing into noise.

## The decision

Should Pattern Bridge begin with:
- futures only,
- stocks only,
- or a staged futures-to-stocks path?

## Recommendation

Recommended path:
**futures-first for framework design, then stocks for scale.**

Short version:
- futures are the better proving ground
- stocks are the better scaling wedge

## Why futures are a strong proving ground

### 1. Cleaner context relationships
Futures express macro, rates, commodity, FX, and event context more directly.

That makes them useful for building and testing:
- bridge ontology
- event prep workflows
- correlation logic
- participation concepts
- translation rules

### 2. Fewer instruments, deeper study
A small set of markets allows deeper pattern work.

Examples:
- ES / NQ
- CL
- GC
- ZN / UB
- 6E

This is good for establishing whether the framework itself is real.

### 3. Stronger event structure
Many of the archive's strongest examples depend on recurring event and session structure:
- FOMC
- NFP
- CPI
- ECB
- overnight inventory
- cash open interaction

Futures make this structure obvious.

### 4. Better environment for ontology development
If the product cannot define bridges well in futures, it will not survive the messier stock universe.

## Why futures are a weak scaling wedge

### 1. Limited market count
There are only so many liquid futures markets worth watching.

That constrains:
- candidate discovery volume
- user-perceived leverage
- breadth of bridge surfacing

### 2. Smaller audience
The addressable market is narrower than stocks.

### 3. Some bridges depend on session structure that may not generalize cleanly
This is useful for framework design but can limit mass-market growth.

## Why stocks are attractive for scale

### 1. Large opportunity set
Stocks allow the product to surface many more candidates.

That means the user benefit can become obvious quickly:
- less manual hunting
- better analog retrieval across many names
- more opportunities to apply known bridge families

### 2. Better product leverage
If the engine can evaluate thousands of names and bring the trader a ranked set of possible bridges, that is a clear workflow advantage.

### 3. More natural commercial wedge
It is easier to tell a product story around:
- watchlists
- daily candidate sets
- sector rotation
- earnings and catalyst context
- trader-specific bridge matching

## Why stocks are dangerous too early

### 1. Too much noise
If the ontology is weak, stocks will flood the product with junk candidates.

### 2. Easy to collapse into generic scanning
Without a strong bridge model, the product will become:
- RVOL scanners
- breakout scanners
- gap scanners
with fancier wording

That would be a strategic failure.

### 3. Session structure differs
Some futures-native bridges rely on:
- overnight inventory
- cash session transition
- cleaner macro transmission

Not every bridge will port cleanly to stocks.

### 4. More symbol-specific distortion
Single-name stocks introduce:
- earnings effects
- idiosyncratic news
- sector-relative behavior
- liquidity differences
- float and microstructure quirks

The bridge model must account for these differences.

## What transfers cleanly from futures to stocks

Likely transferable:
- context-first thinking
- regime classification
- participation assessment
- structural references
- analog retrieval
- confirmation vs invalidation logic
- debrief-to-playbook workflow
- correlation and leadership concepts

## What needs adaptation for stocks

Needs explicit adjustment:
- catalyst taxonomy
- sector and relative strength context
- earnings and guidance effects
- single-name liquidity patterns
- open-drive and intraday behavior by float / market cap / news intensity
- translation of profile concepts into stock-friendly structure language

## Suggested wedge sequence

### Phase 1: futures-based ontology and workflow
Goal:
Prove the framework and the bridge schema.

Deliverables:
- bridge object model
- analog retrieval logic
- debrief workflow
- event context engine
- candidate bridge review surface

### Phase 2: stock bridge families
Goal:
Translate the framework into stock-compatible bridge families.

Likely initial focus:
- large-cap liquid names
- sector leaders
- earnings and macro-sensitive names
- index-relative movers

Avoid in earliest stock phase:
- thin small caps
- meme-style names
- highly illiquid edge cases

### Phase 3: scaled stock discovery
Goal:
Use the engine to surface ranked candidate bridges across a broad stock universe.

This is where the product becomes obviously useful as a discovery machine.

## MVP recommendation

For an MVP, do not try to solve every market at once.

Best route:
- define the bridge framework using futures logic
- test workflow on a narrow futures set
- then deliberately design stock-compatible bridge families
- only then widen the scan universe

## What to avoid

Avoid these traps:
- jumping directly to broad stock scanning before ontology is mature
- assuming all futures bridges port directly to stocks
- trying to automate exact execution too early
- treating stocks as just more symbols rather than a different expression environment

## Closing view

Futures are the laboratory.
Stocks are the distribution channel.

That is the cleanest strategic framing for now.
