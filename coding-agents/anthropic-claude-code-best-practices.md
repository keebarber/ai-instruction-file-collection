# Best practices for Claude Code (Anthropic, official)

> SOURCE: https://code.claude.com/docs/en/best-practices — Anthropic. Saved 2026-06-26 (lightly condensed; nav/links trimmed).
> The authoritative guidance from Anthropic on how to drive an agentic coding tool well. Most of it generalizes to any coding agent.

Most best practices follow from one constraint: **Claude's context window fills up fast, and performance degrades as it fills.** The context window holds the entire conversation — every message, every file read, every command output. LLM performance degrades as it fills; Claude may "forget" earlier instructions or make more mistakes. Context is the most important resource to manage.

## Give Claude a way to verify its work

Claude stops when the work *looks* done. Without a check it can run, "looks done" is the only signal, and you become the verification loop. Give Claude something that produces a pass/fail and the loop closes on its own: a test suite, a build exit code, a linter, a script that diffs output against a fixture, or a browser screenshot compared against a design.

| Strategy | Before | After |
|---|---|---|
| Provide verification criteria | "implement a function that validates email addresses" | "write a validateEmail function. example test cases: user@example.com is true, invalid is false, user@.com is false. run the tests after implementing" |
| Verify UI changes visually | "make the dashboard look better" | "[paste screenshot] implement this design. take a screenshot of the result and compare it to the original. list differences and fix them" |
| Address root causes, not symptoms | "the build is failing" | "the build fails with this error: [paste error]. fix it and verify the build succeeds. address the root cause, don't suppress the error" |

How hard the check gates the stop: in one prompt (ask Claude to run it and iterate), across a session (a `/goal` condition re-checked every turn), as a deterministic gate (a Stop hook that blocks the turn until it passes), or by a second opinion (a verification subagent / fresh model that tries to refute the result, so the agent doing the work isn't grading itself).

Have Claude show **evidence** rather than asserting success: the test output, the command it ran and what it returned, or a screenshot. Reviewing evidence is faster than re-running the verification yourself.

## Explore first, then plan, then code

Letting Claude jump straight to coding can produce code that solves the wrong problem. Four phases:

1. **Explore** — plan mode; Claude reads files and answers questions without making changes.
2. **Plan** — ask for a detailed implementation plan; edit it before proceeding.
3. **Implement** — code, verifying against the plan.
4. **Commit** — descriptive message and a PR.

Plan mode adds overhead. For small, clear-scope fixes (typo, log line, rename), skip it. Planning is most useful when the approach is uncertain, the change touches multiple files, or you're unfamiliar with the code. If you could describe the diff in one sentence, skip the plan.

## Provide specific context in your prompts

The more precise the instructions, the fewer corrections you'll need.

| Strategy | Before | After |
|---|---|---|
| Scope the task | "add tests for foo.py" | "write a test for foo.py covering the edge case where the user is logged out. avoid mocks." |
| Point to sources | "why does ExecutionFactory have such a weird api?" | "look through ExecutionFactory's git history and summarize how its api came to be" |
| Reference existing patterns | "add a calendar widget" | "look at how existing widgets are implemented on the home page... HotDogWidget.php is a good example. follow the pattern... build from scratch without libraries other than the ones already used" |
| Describe the symptom | "fix the login bug" | "users report that login fails after session timeout. check the auth flow in src/auth/, especially token refresh. write a failing test that reproduces the issue, then fix it" |

Provide rich content: reference files with `@`, paste images/screenshots, give URLs for docs, pipe data (`cat error.log | claude`), or tell Claude to fetch context itself.

## Write an effective CLAUDE.md

CLAUDE.md is read at the start of every conversation. Keep it short and human-readable. Run `/init` for a starter, then refine. Only include things that apply broadly; use skills for sometimes-relevant knowledge.

For each line, ask: *"Would removing this cause Claude to make mistakes?"* If not, cut it. **Bloated CLAUDE.md files cause Claude to ignore your actual instructions.**

| ✅ Include | ❌ Exclude |
|---|---|
| Bash commands Claude can't guess | Anything Claude can figure out by reading code |
| Code style rules that differ from defaults | Standard language conventions Claude already knows |
| Testing instructions and preferred test runners | Detailed API documentation (link to docs instead) |
| Repository etiquette (branch naming, PR conventions) | Information that changes frequently |
| Architectural decisions specific to your project | Long explanations or tutorials |
| Developer environment quirks (required env vars) | File-by-file descriptions of the codebase |
| Common gotchas or non-obvious behaviors | Self-evident practices like "write clean code" |

If Claude keeps doing something you don't want despite a rule against it, the file is probably too long and the rule is getting lost. You can add emphasis ("IMPORTANT", "YOU MUST") to improve adherence. Check CLAUDE.md into git. It can import files with `@path/to/import` syntax. Locations: `~/.claude/CLAUDE.md` (all sessions), `./CLAUDE.md` (shared, checked into git), `./CLAUDE.local.md` (personal, gitignored), plus parent/child directories in monorepos.

Example:

```markdown
# Code style
- Use ES modules (import/export) syntax, not CommonJS (require)
- Destructure imports when possible (eg. import { foo } from 'bar')

# Workflow
- Be sure to typecheck when you're done making a series of code changes
- Prefer running single tests, and not the whole test suite, for performance
```

## Configure your environment
- **Permissions**: reduce interruptions with auto mode (a classifier blocks risky commands), permission allowlists (`npm run lint`, `git commit`), or sandboxing (OS-level isolation).
- **CLI tools**: tell Claude to use `gh`, `aws`, `gcloud`, `sentry-cli`. CLI tools are the most context-efficient way to hit external services.
- **MCP servers**: connect Notion, Figma, databases, issue trackers.
- **Hooks**: for actions that must happen every time with zero exceptions (deterministic, unlike advisory CLAUDE.md).
- **Skills**: `SKILL.md` files in `.claude/skills/` give domain knowledge and reusable workflows, loaded on demand.
- **Subagents**: specialized assistants in `.claude/agents/` with their own context and tool allowlist.
- **Plugins**: bundle skills, hooks, subagents, MCP servers into one installable unit.

## Communicate effectively
- **Ask codebase questions** the way you'd ask a senior engineer ("How does logging work?", "What edge cases does X handle?"). No special prompting needed.
- **Let Claude interview you** for larger features. Start minimal and ask Claude to interview you using the AskUserQuestion tool, covering implementation, UI/UX, edge cases, and tradeoffs, then write a complete spec to `SPEC.md`. Start a fresh session to execute it. The most useful specs name the files and interfaces involved, state what's out of scope, and end with an end-to-end verification step.

## Manage your session
- **Course-correct early and often.** `Esc` to stop mid-action (context preserved), `Esc+Esc` / `/rewind` to restore earlier state, "undo that," `/clear` to reset between unrelated tasks. If you've corrected Claude more than twice on the same issue, the context is polluted — `/clear` and restart with a better prompt.
- **Manage context aggressively.** `/clear` between unrelated tasks; `/compact <instructions>` for partial summarization.
- **Use subagents for investigation.** They explore in a separate context and report back summaries, keeping your main conversation clean.
- **Rewind with checkpoints.** Every prompt creates a checkpoint (tracks Claude's changes only — not a git replacement).

## Avoid common failure patterns
- **The kitchen sink session.** Mixing unrelated tasks fills context with irrelevant info. → `/clear` between tasks.
- **Correcting over and over.** Context pollutes with failed approaches. → After two failed corrections, `/clear` and write a better prompt.
- **The over-specified CLAUDE.md.** Too long → Claude ignores half of it. → Ruthlessly prune; convert rules to hooks.
- **The trust-then-verify gap.** Plausible-looking code that misses edge cases. → Always provide verification. If you can't verify it, don't ship it.
- **The infinite exploration.** Unscoped "investigate" reads hundreds of files. → Scope narrowly or use subagents.

## Develop your intuition

These patterns are starting points, not rules. Sometimes you should let context accumulate, skip planning, or use a vague prompt on purpose. Pay attention to what works: when Claude produces great output, notice the prompt structure, context, and mode you used; when it struggles, ask whether the context was too noisy, the prompt too vague, or the task too big for one pass.
