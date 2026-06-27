# How an AI should write code — rules cheat-sheet

> A distilled, paste-ready set of coding rules for a CLAUDE.md / AGENTS.md / .cursorrules. Synthesized from Anthropic's Claude Code best practices, the AGENTS.md ecosystem conventions, and recurring rules across the most-starred .cursorrules collections (PatrickJS/awesome-cursorrules) and "rules for AI" guides.
> Use these as a menu — keep only the lines that would actually change the agent's behavior on YOUR codebase, and delete the rest. A bloated rules file gets ignored (see `humanlayer-writing-a-good-CLAUDE-md.md`).

## Verify-your-work (the highest-value rule)
```
- After a series of changes, run the build, typecheck, linter, and tests. Don't report done until they pass.
- Show evidence, not assertions: the command you ran and its output, or a screenshot of the result.
- Fix the root cause, not the symptom. Never suppress or silence an error to make a check pass.
- Add or update tests for the code you change, even if nobody asked.
- Prefer running the single relevant test over the whole suite while iterating.
```

## Before writing code
```
- For anything non-trivial, explore and plan before editing. Read the relevant files first.
- Match existing patterns. Find a similar feature in the codebase and follow its structure, naming, and libraries.
- Don't add a new dependency without checking what's already used. Ask before adding production dependencies.
- If the approach is unclear or touches many files, write a short plan (or SPEC.md) and confirm before implementing.
```

## While writing code
```
- Make the smallest change that solves the problem. Don't refactor unrelated code in the same pass.
- Don't reformat files you aren't changing. Keep diffs focused and reviewable.
- Preserve existing public APIs and behavior unless the task is to change them.
- No placeholder/stub code, no TODOs left behind, no commented-out blocks. Finish the change.
- Handle errors and edge cases explicitly; don't swallow exceptions.
- Don't hardcode secrets. Read config/env the way the rest of the codebase does.
- Comment the "why", not the "what". Don't narrate obvious code.
- Prefer clarity over cleverness. Readable beats short.
```

## Things to avoid (common AI coding failure modes)
```
- Don't invent APIs, file paths, env vars, or library functions. If unsure, check the source or say so.
- Don't delete or weaken tests to make them pass.
- Don't introduce a new framework/library/pattern when the codebase already has one for the job.
- Don't leave the build broken. If you can't finish, say what's incomplete and why.
- Don't claim something works without running it.
- Avoid over-engineering: no speculative abstraction, defensive code for impossible cases, or tests for cases that can't happen.
```

## After writing code
```
- Run the project's checks (build, lint, typecheck, test) and report results.
- Summarize what changed and why, list the files touched, and call out anything risky or out of scope.
- Use conventional commit messages / the repo's PR etiquette (branch naming, title format).
```

## Project facts the agent can't guess (fill these in)
```
- Package manager + exact commands: install / dev / build / test / lint / typecheck
- Language/runtime versions and any required env vars
- Where things live: apps, shared packages, entry points (a map of the repo)
- Test framework and how to run a single test
- Non-obvious gotchas, required setup steps, and "do not touch" areas
```

## Anthropic's include/exclude guide for a coding rules file

| Include | Exclude |
|---|---|
| Bash commands the agent can't guess | Anything it can figure out by reading the code |
| Code style rules that differ from language defaults | Standard conventions the model already knows |
| Test instructions and the preferred runner | Detailed API docs (link instead) |
| Repo etiquette (branches, PR format) | Info that changes frequently |
| Architecture decisions specific to your project | File-by-file descriptions of the codebase |
| Env quirks (required env vars) | Self-evident advice like "write clean code" |

## An adversarial review step (for autonomous runs)
```
- Before treating work as done, have a fresh-context reviewer (subagent) check the diff against the plan:
  every requirement implemented, listed edge cases tested, nothing out of scope changed.
- Tell the reviewer to flag only gaps that affect correctness or stated requirements — not style preferences —
  to avoid over-engineering.
```

Sources: https://code.claude.com/docs/en/best-practices · https://agents.md/ · https://github.com/PatrickJS/awesome-cursorrules
