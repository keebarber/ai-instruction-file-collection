<!--
SOURCE: obra/superpowers (Jesse Vincent) — https://github.com/obra/superpowers/blob/main/skills/test-driven-development/SKILL.md
Retrieved 2026-06-26, verbatim. References a sibling testing-anti-patterns.md not included here.
-->
---
name: test-driven-development
description: Use when implementing any feature or bugfix, before writing implementation code
---

# Test-Driven Development (TDD)

## Overview

Write the test first. Watch it fail. Write minimal code to pass.

**Core principle:** If you didn't watch the test fail, you don't know if it tests the right thing.

**Violating the letter of the rules is violating the spirit of the rules.**

## When to Use

**Always:** new features, bug fixes, refactoring, behavior changes.
**Exceptions (ask your human partner):** throwaway prototypes, generated code, configuration files.

Thinking "skip TDD just this once"? Stop. That's rationalization.

## The Iron Law

```
NO PRODUCTION CODE WITHOUT A FAILING TEST FIRST
```

Write code before the test? Delete it. Start over. No exceptions — don't keep it as "reference," don't "adapt" it while writing tests, don't look at it. Delete means delete. Implement fresh from tests.

## Red-Green-Refactor

### RED — Write Failing Test
Write one minimal test showing what should happen.

GOOD — clear name, tests real behavior, one thing:
```typescript
test('retries failed operations 3 times', async () => {
  let attempts = 0;
  const operation = () => {
    attempts++;
    if (attempts < 3) throw new Error('fail');
    return 'success';
  };
  const result = await retryOperation(operation);
  expect(result).toBe('success');
  expect(attempts).toBe(3);
});
```
BAD — vague name, tests the mock not the code:
```typescript
test('retry works', async () => {
  const mock = jest.fn()
    .mockRejectedValueOnce(new Error())
    .mockRejectedValueOnce(new Error())
    .mockResolvedValueOnce('success');
  await retryOperation(mock);
  expect(mock).toHaveBeenCalledTimes(3);
});
```
Requirements: one behavior, clear name, real code (no mocks unless unavoidable).

### Verify RED — Watch It Fail (MANDATORY. Never skip.)
Run the test. Confirm: it fails (not errors), the failure message is expected, it fails because the feature is missing (not typos). Test passes? You're testing existing behavior — fix the test. Test errors? Fix the error, re-run until it fails correctly.

### GREEN — Minimal Code
Write the simplest code to pass the test. Don't add features, refactor other code, or "improve" beyond the test. (YAGNI — no speculative options objects.)

### Verify GREEN — Watch It Pass (MANDATORY)
Run it. Confirm: test passes, other tests still pass, output pristine (no errors/warnings). Test fails? Fix the code, not the test. Other tests fail? Fix now.

### REFACTOR — Clean Up
After green only: remove duplication, improve names, extract helpers. Keep tests green. Don't add behavior.

### Repeat
Next failing test for the next feature.

## Why Order Matters
- **"I'll write tests after to verify it works"** — tests written after code pass immediately, which proves nothing (might test the wrong thing, test implementation not behavior, miss edge cases). Test-first forces you to see the test fail, proving it actually tests something.
- **"I already manually tested the edge cases"** — manual testing is ad-hoc; no record, can't re-run, easy to forget under pressure. Automated tests are systematic.
- **"Deleting X hours of work is wasteful"** — sunk cost fallacy. The waste is keeping code you can't trust. Working code without real tests is technical debt.
- **"TDD is dogmatic; pragmatic means adapting"** — TDD IS pragmatic: finds bugs before commit, prevents regressions, documents behavior, enables refactoring.
- **"Tests after achieve the same goals"** — no. Tests-after answer "What does this do?" Tests-first answer "What should this do?" Tests-after are biased by your implementation.

## Common Rationalizations

| Excuse | Reality |
|--------|---------|
| "Too simple to test" | Simple code breaks. Test takes 30 seconds. |
| "I'll test after" | Tests passing immediately prove nothing. |
| "Already manually tested" | Ad-hoc ≠ systematic. No record, can't re-run. |
| "Deleting X hours is wasteful" | Sunk cost fallacy. Keeping unverified code is technical debt. |
| "Keep as reference, write tests first" | You'll adapt it. That's testing after. Delete means delete. |
| "Test hard = design unclear" | Listen to the test. Hard to test = hard to use. |
| "TDD will slow me down" | TDD is faster than debugging. |

## Red Flags — STOP and Start Over
Code before test · test after implementation · test passes immediately · can't explain why the test failed · tests added "later" · "just this once" · "I already manually tested it" · "it's about spirit not ritual" · "keep as reference" · "already spent X hours, deleting is wasteful." **All mean: Delete code. Start over with TDD.**

## Verification Checklist (before marking work complete)
- [ ] Every new function/method has a test
- [ ] Watched each test fail before implementing
- [ ] Each test failed for the expected reason (feature missing, not typo)
- [ ] Wrote minimal code to pass each test
- [ ] All tests pass
- [ ] Output pristine (no errors, warnings)
- [ ] Tests use real code (mocks only if unavoidable)
- [ ] Edge cases and errors covered

Can't check all boxes? You skipped TDD. Start over.

## When Stuck

| Problem | Solution |
|---------|----------|
| Don't know how to test | Write the wished-for API. Write the assertion first. Ask your human partner. |
| Test too complicated | Design too complicated. Simplify the interface. |
| Must mock everything | Code too coupled. Use dependency injection. |
| Test setup huge | Extract helpers. Still complex? Simplify the design. |

## Final Rule
```
Production code → test exists and failed first
Otherwise → not TDD
```
No exceptions without your human partner's permission.
