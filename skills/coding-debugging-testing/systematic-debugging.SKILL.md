<!--
SOURCE: obra/superpowers (Jesse Vincent) — https://github.com/obra/superpowers/blob/main/skills/systematic-debugging/SKILL.md
Retrieved 2026-06-26, verbatim. Part of the "superpowers" agentic software-development skill library.
Note: the original references sibling files (root-cause-tracing.md, defense-in-depth.md, condition-based-waiting.md)
that are NOT included here — get them from the source repo if you want the full skill.
-->
---
name: systematic-debugging
description: Use when encountering any bug, test failure, or unexpected behavior, before proposing fixes
---

# Systematic Debugging

## Overview

Random fixes waste time and create new bugs. Quick patches mask underlying issues.

**Core principle:** ALWAYS find root cause before attempting fixes. Symptom fixes are failure.

**Violating the letter of this process is violating the spirit of debugging.**

## The Iron Law

```
NO FIXES WITHOUT ROOT CAUSE INVESTIGATION FIRST
```

If you haven't completed Phase 1, you cannot propose fixes.

## When to Use

Use for ANY technical issue: test failures, bugs in production, unexpected behavior, performance problems, build failures, integration issues.

**Use this ESPECIALLY when:** under time pressure; "just one quick fix" seems obvious; you've already tried multiple fixes; previous fix didn't work; you don't fully understand the issue.

**Don't skip when:** issue seems simple (simple bugs have root causes too); you're in a hurry (rushing guarantees rework); manager wants it fixed NOW (systematic is faster than thrashing).

## The Four Phases

You MUST complete each phase before proceeding to the next.

### Phase 1: Root Cause Investigation

**BEFORE attempting ANY fix:**

1. **Read Error Messages Carefully** — don't skip errors/warnings; they often contain the exact solution. Read stack traces completely. Note line numbers, file paths, error codes.
2. **Reproduce Consistently** — can you trigger it reliably? Exact steps? Every time? If not reproducible → gather more data, don't guess.
3. **Check Recent Changes** — what changed that could cause this? Git diff, recent commits, new dependencies, config changes, environmental differences.
4. **Gather Evidence in Multi-Component Systems** — when a system has multiple components (CI → build → signing, API → service → database), BEFORE proposing fixes add diagnostic instrumentation at each component boundary: log what data enters and exits each component, verify environment/config propagation, check state at each layer. Run once to gather evidence showing WHERE it breaks, then analyze to identify the failing component, then investigate that specific component.
5. **Trace Data Flow** — when the error is deep in the call stack, trace backward: where does the bad value originate? What called this with the bad value? Keep tracing up until you find the source. Fix at source, not at symptom.

### Phase 2: Pattern Analysis

1. **Find Working Examples** — locate similar working code in the same codebase.
2. **Compare Against References** — if implementing a pattern, read the reference implementation COMPLETELY (don't skim).
3. **Identify Differences** — list every difference between working and broken, however small. Don't assume "that can't matter."
4. **Understand Dependencies** — what other components, settings, config, environment, and assumptions does it need?

### Phase 3: Hypothesis and Testing

1. **Form Single Hypothesis** — state clearly: "I think X is the root cause because Y." Be specific.
2. **Test Minimally** — make the SMALLEST possible change to test it. One variable at a time. Don't fix multiple things at once.
3. **Verify Before Continuing** — worked? → Phase 4. Didn't? → form a NEW hypothesis. DON'T stack more fixes.
4. **When You Don't Know** — say "I don't understand X." Don't pretend. Ask for help. Research more.

### Phase 4: Implementation

1. **Create Failing Test Case** — simplest possible reproduction; automated if possible. MUST have before fixing. (Use the test-driven-development skill.)
2. **Implement Single Fix** — address the root cause. ONE change at a time. No "while I'm here" improvements or bundled refactoring.
3. **Verify Fix** — test passes now? No other tests broken? Issue actually resolved?
4. **If Fix Doesn't Work** — STOP. Count fixes tried. If < 3: return to Phase 1 with new information. **If ≥ 3: STOP and question the architecture.** Don't attempt fix #4 without architectural discussion.
5. **If 3+ Fixes Failed: Question Architecture** — pattern indicating an architectural problem: each fix reveals new shared state/coupling elsewhere; fixes require "massive refactoring"; each fix creates new symptoms. STOP and question fundamentals: is this pattern fundamentally sound? Are we sticking with it through inertia? Refactor vs. continue fixing symptoms? Discuss with your human partner before more fixes. This is NOT a failed hypothesis — it's a wrong architecture.

## Red Flags — STOP and Follow Process

If you catch yourself thinking: "Quick fix for now, investigate later" · "Just try changing X and see" · "Add multiple changes, run tests" · "Skip the test, I'll manually verify" · "It's probably X, let me fix that" · "I don't fully understand but this might work" · proposing solutions before tracing data flow · "One more fix attempt" (after 2+) · each fix reveals a new problem elsewhere — **ALL of these mean: STOP. Return to Phase 1.**

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Issue is simple, don't need process" | Simple issues have root causes too. Process is fast for simple bugs. |
| "Emergency, no time for process" | Systematic debugging is FASTER than guess-and-check thrashing. |
| "Just try this first, then investigate" | First fix sets the pattern. Do it right from the start. |
| "I'll write test after confirming fix works" | Untested fixes don't stick. Test first proves it. |
| "Multiple fixes at once saves time" | Can't isolate what worked. Causes new bugs. |
| "Reference too long, I'll adapt the pattern" | Partial understanding guarantees bugs. Read it completely. |
| "I see the problem, let me fix it" | Seeing symptoms ≠ understanding root cause. |
| "One more fix attempt" (after 2+ failures) | 3+ failures = architectural problem. Question the pattern. |

## Quick Reference

| Phase | Key Activities | Success Criteria |
|-------|---------------|------------------|
| 1. Root Cause | Read errors, reproduce, check changes, gather evidence | Understand WHAT and WHY |
| 2. Pattern | Find working examples, compare | Identify differences |
| 3. Hypothesis | Form theory, test minimally | Confirmed or new hypothesis |
| 4. Implementation | Create test, fix, verify | Bug resolved, tests pass |

## Real-World Impact (from the author's debugging sessions)
- Systematic approach: 15-30 minutes to fix vs. 2-3 hours of thrashing with random fixes.
- First-time fix rate: 95% vs 40%. New bugs introduced: near zero vs common.
