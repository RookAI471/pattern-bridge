# ES Weekly Event Archetypes, v0

## Purpose

This document defines the first prototype set of **ES weekly event archetypes** for Pattern Bridge.

These are not tactical intraday playbooks.
They are **weekly context objects** meant to help a trader:
- recognize recurring event-week environments
- compare the current week to prior similar weeks
- maintain regime memory
- notice when the background begins to rhyme with a known week type

## Prototype scope

Start narrow:
- market: **ES only**
- unit of analysis: **weekly event profile**
- initial emphasis: **FOMC weeks**, especially **FOMC + NFP overlap**
- output style: **early context warning**, not hard prediction

## Source base

Primary source for this pass:
- `/home/lordtedders/.openclaw/workspace/tasks/notion_trading/unpacked/Weekly Profile Patterns dda93b295b2e44fb8012c82c8b131e4c.csv`

Important note:
- the weekly profile CSV is the best compressed source of branded weekly pattern language
- weekly markdown review pages should be used as richer narrative/evidence layers after archetypes are selected

## Archetype 1, Event-Week Range Sweep

### Summary
A major-event week that stays defined by an existing range, but repeatedly sweeps one side and then the other before resolving back toward an edge by Friday.

### Why it matters
This looks like one of the strongest prototype candidates because it is common, highly memorable once named, and exactly the kind of weekly context traders forget in real time.

### Typical shape
- the week starts with a known prior range or visible weekly box
- one early directional attempt fails at a boundary
- FOMC or another major catalyst produces an emotional move that does **not** create stable acceptance
- NFP or late-week trade re-tests the opposite side of the range
- the weekly close often matters more than any one intraday move

### Likely signals
- overlapping major events, especially FOMC + NFP
- prior multi-day range still controls
- failed breakout / failed breakdown behavior around range edges
- repeated liquidation and re-entry into the range

### Seed examples
1. `January 7, 2022`
   - `ES T Bik Fail at Range High, Wed FOMC Min inv P liq, bad TPOL, Fri NFP Bik`
   - Event: `FOMC, NFP`
   - Higher Timeframe Event: `Range Sweep`
2. `May 6, 2022`
   - corrupted CSV row, but still clearly an ES `FOMC, NFP` week ending with `Fri NFP close bot range`
   - Higher Timeframe Event: `Range Sweep`
3. `May 13, 2022`
   - `ES range box to Wed CPI, Thu false break lower, Friday P liquidation back into range`
   - Event: `Range Sweep, US CPI`
   - Higher Timeframe Event: `Range Sweep`

### Prototype use
This should probably be the **first archetype** the system tries to detect.

## Archetype 2, FOMC Grind Through Prior Structure

### Summary
An FOMC week where price does move, but the more important feature is a persistent grind through prior structure rather than a clean event-day trend resolution.

### Why it matters
This is useful because not every FOMC week is a dramatic reversal or sweep. Some are absorption-heavy, structural, and frustratingly gradual.

### Typical shape
- prior week structure remains important
- FOMC produces continuation through a prior gap, prior auction, or prior acceptance area
- the move looks directional but not fully clean
- close location relative to prior week range is a key readout

### Likely signals
- prior gap / prior week range still active
- repeated re-acceptance instead of one-time breakout
- event-day move is grindy rather than explosive
- close winds up back inside an older reference zone

### Seed examples
1. `September 24, 2021`
   - `ES Sun Break AnA, test 50EMA, Washback M, FOMC Grind through Sun Gap, close within prior week range`
   - Event: `FOMC`
   - Higher Timeframe Event: `Auction & Absorption`
2. `March 18, 2022`
   - `ES 60m W broken, post FOMC grind higher, 5min flag 4420 Fri Trend Higher Quad Witching`
   - Event: `FOMC, Quad Witching`
   - Higher Timeframe Event: `W break`

### Prototype use
This should likely be the **second FOMC archetype**, because it gives the model a non-sweep FOMC week type.

## Archetype 3, Event-Week Reversal Off Shock

### Summary
A news-heavy week where the market first extends the shock, then violently reverses and spends the back half of the week re-pricing the initial move.

### Why it matters
This is a good contrast class. It prevents the system from overfitting everything into range logic.

### Typical shape
- major geopolitical or macro shock creates directional emotional extension
- one or two sessions later the market reverses hard
- the reversal itself becomes the defining weekly feature
- late-week trade often liquidates from the reversal rather than from the original news impulse

### Likely signals
- outsized overnight move or holiday gap
- one-sided midweek emotional trade
- V-bottom / V-reversal language
- strong distinction between first-half narrative and second-half narrative

### Seed examples
1. `February 25, 2022`
   - `ES M Holiday Gap Fill, W Russia inv and ON b, Thu V-bot trend up, Fri P liq`
   - Event: `Russian Invasion`
   - Higher Timeframe Event: `V Reversal`

### Prototype use
Not day-one, but very useful as an early contrast archetype once FOMC weeks are seeded.

## Archetype 4, Event-Week Structural Failure

### Summary
A week where an important higher-timeframe structure was already vulnerable before the event, and the event simply forces the failure or failed retest.

### Why it matters
This is high value because it ties event interpretation back to pre-existing structure, which is exactly where AI can help traders keep their memory straight.

### Typical shape
- the week begins with a visible vulnerable structure, for example pennant, neckline, channel, or double top / head-and-shoulders context
- the event acts as an accelerant, not the whole story
- attempts to retest the broken structure are weak
- the late-week close confirms failure more than the event headline does

### Likely signals
- weekly profile language includes `retest`, `failed`, `break`, `neckline`, `channel`, `pennant`
- the event is important but nested inside prior technical weakness
- close location confirms failure of prior structure

### Seed examples
1. `February 11, 2022`
   - `ES M Trend brk of 60m pen, W att at D neckline, Thur CPI and Hawk mrkt lower, Fri fail prior wk pen DD on Russian inv`
   - Event: `Fed Comments, Russian Invasion, US CPI`
   - Higher Timeframe Event: `Break out Retest`
2. `July 29, 2022`
   - `ES top of Daily Channel broken after prior week H&S failure. Wed DD to top of channel on FOMC neutral rate. Thur weak GDP trend day break above channel.`
   - Event: `FOMC, GDP`
   - Higher Timeframe Event: `Channel Breakout`

### Prototype use
This should be in the first wave because it teaches the system to prioritize **pre-event structure**.

## Archetype 5, Event-Week Weak Structure Then Reversal

### Summary
A week where weak auction/profile quality is visible early, the event presses that weakness, and the week ends with a reversal or liquidation that only makes sense if the earlier poor structure was remembered.

### Why it matters
This is a strong AI use case because humans often remember the headline event but forget the structural weakness that made the event reaction behave the way it did.

### Typical shape
- weak TPO / poor profile / fragile balance early in the week
- event-day move intensifies the weakness
- late-week reversal or liquidation becomes the defining outcome
- poor structure is the hidden explanatory variable

### Likely signals
- profile language includes `weak TPOH`, `bad TPOL`, `poor TPO structure`, `cave sweep`
- event does not stand alone, it activates weak structure
- Friday action looks obvious only in hindsight

### Seed examples
1. `November 12, 2021`
   - `ES Post NFP weak TPOH, Tues b, CPI DD lower, Friday P reversal`
   - Event: `US CPI`
   - Higher Timeframe Event: `Cave Sweep, Poor TPO Structure`
2. `January 14, 2022`
   - `ES M Wash Rev, T CINAH, W Bik, Thu Wash down, Fri CINAH`
   - Event: `Range Sweep, US CPI`
   - Higher Timeframe Event: `Poor TPO Structure`

### Prototype use
This is a good early archetype because it connects event behavior to profile weakness instead of treating the week as pure news.

## Recommended first seed set

If we want the smallest useful prototype set, start with these three:

1. **Event-Week Range Sweep**
   - primary seed: `January 7, 2022`
2. **FOMC Grind Through Prior Structure**
   - primary seed: `September 24, 2021`
3. **Event-Week Structural Failure**
   - primary seed: `February 11, 2022`

Why these three:
- they are distinct
- they cover both range-bound and structural weeks
- they include clean FOMC and FOMC-adjacent logic
- they force the system to track both event labels and prior structure

## What to build next

Before building UI or workflow, define detection inputs for each archetype.

Minimum fields likely needed:
- event calendar labels for the week
- prior week range position
- presence of vulnerable higher-timeframe structure
- early week failed breakout / breakdown behavior
- event-day acceptance vs rejection
- Friday close location relative to weekly range
- whether the week resolved in range, through range, or back into range

## Open questions

1. Should one archetype be allowed to inherit from another, for example `Event-Week Range Sweep` with a `weak structure` modifier?
2. Should the first prototype use only the compressed weekly profile row, or also summarize the underlying weekly review notes?
3. Do we want a canonical branded naming scheme, or should the prototype preserve Edward’s original compressed language first?
4. Should CPI weeks be treated as first-class alongside FOMC in v0, or remain secondary until the FOMC lane is cleaner?
