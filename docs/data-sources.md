# Data Sources and Reference Tools

## Purpose

This document captures important implementation references, market-data candidates, and economic-calendar sources for Pattern Bridge.

The rule is simple:
- important source links do **not** stay only in chat
- if a link materially affects product design, data ingestion, or implementation, it belongs here

## Confirmed reference links from Edward

### Charting / UI
- **TradingView Lightweight Charts**
  - `https://github.com/tradingview/lightweight-charts`
  - Why it matters:
    - strong candidate for browser-based historical chart display
    - likely useful for replaying weekly archetype comparisons
    - could support later surfaces for analog comparison and context review

### Economic data ingestion
- **fredapi**
  - `https://github.com/mortada/fredapi`
  - Why it matters:
    - Python client for pulling FRED data
    - likely useful for historical macro series and release-adjacent data workflows
    - can serve as part of the historical event-data ingestion layer

## Market data requirements

For validating ES weekly event archetypes, the minimum useful market dataset is:
- **ES intraday data**, at least **60-minute bars or better**
- ideally **3 to 5 years** of history
- fields:
  - timestamp
  - open
  - high
  - low
  - close
  - volume
- preferred additions:
  - session boundary information
  - overnight vs RTH segmentation
  - continuous front-month handling or clear contract-roll policy

## Economic calendar requirements

For v0 weekly archetype work, the minimum useful event calendar is:
- FOMC decision dates
- NFP release dates
- CPI release dates

Preferred later additions:
- Fed Minutes
- Powell speeches
- GDP
- PPI
- ECB
- BOE
- Jackson Hole

## Historical economic calendar sources

### FOMC
- **Federal Reserve official FOMC calendars**
  - `https://www.federalreserve.gov/monetarypolicy/fomccalendars.htm`
  - Notes:
    - official source
    - best canonical source for historical FOMC meeting dates

### NFP / Employment Situation
- **FRED Employment Situation release page**
  - `https://fred.stlouisfed.org/release?rid=50`
  - Notes:
    - useful historical anchor for Employment Situation / NFP-related release context
    - likely good as a validation/reference source
    - not by itself the final normalized event table

- **BLS release calendar**
  - use as canonical release-date source for Employment Situation when building normalized event tables

### CPI
- **BLS CPI release schedule/history**
  - use as canonical release-date source for CPI event normalization
- **FRED CPI-related series/pages**
  - useful secondary validation layer, not necessarily the canonical calendar source

## ES intraday data candidates to verify

These are candidates, not yet blessed as the canonical source.

### Yahoo Finance / `ES=F`
- Pros:
  - easy access
  - fast for early experiments
- Cons:
  - intraday history windows may be too short
  - may not support durable multi-year hourly retrieval cleanly
- Status:
  - useful to test
  - not yet trusted as the main archive

### Barchart
- Example reference:
  - `https://www.barchart.com/futures/quotes/ESM26/interactive-chart`
- Pros:
  - clearly supports futures chart history views
- Cons:
  - export/API access and historical depth need validation
  - may be delayed/gated for systematic use
- Status:
  - worth testing

### Stooq
- `https://stooq.com/`
- Pros:
  - free market-data site
- Cons:
  - unclear whether it can provide clean multi-year hourly ES futures history in a reproducible format
- Status:
  - worth probing, not yet trusted

### Other unofficial scraping paths
- Examples:
  - Investing.com-style pages
  - TradingView-adjacent unofficial extraction flows
- Pros:
  - sometimes enough for exploratory work
- Cons:
  - brittle, unofficial, poor substrate for a durable system
- Status:
  - fallback only

## Current recommendation

### Event calendar
Build our own normalized event files from official sources:
- Fed for FOMC
- BLS for NFP / Employment Situation
- BLS for CPI
- FRED as a cross-check and supporting ingestion layer

### ES intraday
Run a focused source validation pass to determine:
- which free source, if any, gives usable **multi-year 60m ES**
- whether the data is continuous futures or contract-specific
- whether session boundaries are good enough
- whether the coverage is clean enough for archetype validation

If no free source is good enough, acknowledge that quickly and choose a small paid source instead of building on bad substrate.

## Immediate next files we may want
- `data/economic-calendar/fomc.csv`
- `data/economic-calendar/nfp.csv`
- `data/economic-calendar/cpi.csv`
- `data/market-data/README.md`
- `scripts/ingest/fred/`
- `scripts/ingest/events/`

## Operational rule

When Edward provides a project-relevant implementation link, ingestion tool, or data source:
- capture it here or in a directly relevant project doc the same day
- do not leave it only in chat history
