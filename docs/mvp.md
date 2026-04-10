# MVP Definition

## Purpose

This document defines the minimum viable product for Pattern Bridge.

The goal is to make the first version small enough to build and test, while still proving the core value proposition.

## Core question

What is the smallest product that can prove traders find value in:
- AI-suggested pattern bridge candidates
- analog retrieval
- structured review
- and playbook improvement over time?

## MVP thesis

The MVP should prove that the product helps a trader:
1. understand context better
2. find relevant analogs faster
3. evaluate candidate bridges more clearly
4. debrief more usefully
5. build sharper playbooks with less manual burden

If those five things are not improving, the MVP is not working.

## What the MVP is

A lightweight context, candidate, and debrief tool for discretionary traders.

It should allow a trader to:
- review today's context
- see AI-suggested bridge candidates
- inspect why they surfaced
- compare them to similar prior examples
- accept, reject, or watch candidates
- debrief outcomes and improve the bridge memory

## What the MVP is not

The MVP is not:
- an auto-trader
- a signal engine
- a full charting platform
- a full broker integration stack
- a giant analytics dashboard
- a perfect real-time execution assistant

## MVP user

Primary user:
- serious discretionary trader

Secondary user:
- developing trader building first playbooks

## MVP surface area

### Required screens
- Today
- Candidates
- Candidate Detail
- Bridges Library
- Bridge Detail
- Journal
- Review

## Required capabilities

### 1. Context entry and summary
The product must support a simple way to structure the day's context.

Examples:
- event type
- macro themes
- market regime
- key levels
- participation expectations
- watchlist

### 2. Pattern Bridge library
The product must store bridge objects using the defined schema.

Minimum functions:
- create bridge
- edit bridge
- archive bridge
- attach evidence
- link variants

### 3. Candidate surfacing
The product must be able to surface candidate bridges for trader review.

In MVP, this does not need to be fully automated or fully real-time.
It can be driven by a narrower universe and simpler matching logic.

### 4. Analog retrieval
This is core.

For any candidate or bridge, the product must be able to show:
- similar prior examples
- related variants
- failed lookalikes when available

### 5. Candidate review actions
The trader must be able to:
- accept
- reject
- watch
- relabel
- attach to an existing bridge
- spin into a new variant

### 6. Confirmation and invalidation tracking
The product must support simple checklist-style tracking for:
- identifier
- confirmation
- invalidation
- progression notes

### 7. Journal and debrief flow
The product must allow:
- premarket notes
- live notes
- end-of-day debrief
- bridge refinement suggestions

### 8. Memory update loop
The product must preserve accepted and rejected candidate outcomes in a way that improves future retrieval and review.

## What can be manual in MVP

To keep v0 honest, some things can be manual or semi-manual:
- candidate curation
- bridge creation
- evidence linking
- debrief summaries
- market universe selection
- event tagging

That is fine if the workflow itself proves useful.

## Suggested MVP scope by market

Recommended:
- start with a narrow futures-based bridge library and workflow
- optionally include a small stock watch universe later in MVP or just after MVP

Do not start with broad stock-market scanning.
That is too likely to produce junk before the ontology is mature.

## Suggested MVP data scope

Potential MVP inputs:
- manually entered context
- watchlist symbols
- bridge schema objects
- historical examples and notes
- event tags
- simple market metadata

Potential later additions:
- richer chart integrations
- broader scanning
- automated event ingestion
- deeper correlation data

## MVP success criteria

The MVP is working if users report:
- they found relevant analogs faster
- surfaced candidates were often worth evaluating
- debriefs became easier and more useful
- bridge definitions improved over time
- manual documentation pain decreased

## MVP failure signals

The MVP is failing if:
- candidates feel generic
- analogs are not actually useful
- review takes too long
- traders treat it like just another scanner
- bridge objects stay vague and unhelpful
- debrief does not improve later retrieval

## MVP build philosophy

### 1. Retrieval first
If the product cannot retrieve relevant analogs, the rest gets shaky.

### 2. Explanation over confidence theater
The product should explain why something surfaced rather than pretending certainty.

### 3. Low-friction review
If accepting, rejecting, and debriefing are too heavy, usage dies.

### 4. Memory compounding
The product must get more useful as more examples and decisions accumulate.

## Suggested MVP sequence

### Stage 1
- schema
- bridge library
- manual example ingestion
- journal and debrief scaffolding

### Stage 2
- candidate surfacing for a narrow universe
- analog retrieval
- acceptance and rejection workflow

### Stage 3
- bridge refinement loop
- failure lookalike memory
- basic ranking improvements

## One-sentence MVP definition

The Pattern Bridge MVP is a trader-facing tool that surfaces candidate bridges, retrieves relevant analogs, and turns review into a compounding playbook memory.
