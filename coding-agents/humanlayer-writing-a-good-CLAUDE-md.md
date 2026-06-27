# Writing a good CLAUDE.md

> SOURCE: HumanLayer Blog, by Kyle — https://www.humanlayer.dev/blog/writing-a-good-claude-md (Nov 25, 2025). Saved 2026-06-26.
> Note: this also applies to `AGENTS.md`, the open-source equivalent for OpenCode, Zed, Cursor, Codex, etc.
> This is the single best essay on *why* most CLAUDE.md files fail and how to write one that actually changes the agent's behavior.

## Principle: LLMs are (mostly) stateless

LLMs are stateless functions. Their weights are frozen by the time they're used for inference, so they don't learn over time. The only thing the model knows about your codebase is the tokens you put into it.

Coding agent harnesses such as Claude Code usually require you to manage the agent's memory explicitly. `CLAUDE.md` (or `AGENTS.md`) is the only file that by default goes into *every single conversation* you have with the agent.

Three implications:

1. Coding agents know absolutely nothing about your codebase at the beginning of each session.
2. The agent must be told anything that's important to know about your codebase each time you start a session.
3. `CLAUDE.md` is the preferred way of doing this.

## CLAUDE.md onboards Claude to your codebase

Since Claude doesn't know anything about your codebase at the beginning of each session, use `CLAUDE.md` to onboard it. At a high level it should cover:

- **WHAT**: the tech, your stack, the project structure. Give Claude a map of the codebase. Especially important in monorepos — tell Claude what the apps are, what the shared packages are, and what everything is for so it knows where to look.
- **WHY**: the *purpose* of the project and what everything is doing in the repository.
- **HOW**: how it should work on the project. Do you use `bun` instead of `node`? How can Claude verify its changes? How does it run tests, typechecks, and compilation steps?

But the way you do this matters. Don't try to stuff every command Claude could possibly need into your `CLAUDE.md` — you'll get sub-optimal results.

## Claude often ignores CLAUDE.md

Claude Code injects this system reminder along with your `CLAUDE.md` content:

```
<system-reminder>
      IMPORTANT: this context may or may not be relevant to your tasks.
      You should not respond to this context unless it is highly relevant to your task.
</system-reminder>
```

As a result, Claude ignores the contents of `CLAUDE.md` if it decides they're not relevant to the current task. The more information in the file that's not **universally applicable**, the more likely Claude is to ignore your instructions. Most CLAUDE.md files include instructions that aren't broadly applicable — people treat the file as a place to add "hotfixes" for behavior they didn't like. The Claude Code team apparently found that telling Claude to ignore the bad instructions produced better results overall.

## Creating a good CLAUDE.md file

### Less (instructions) is more

It's tempting to stuff every command, code standard, and style guideline into `CLAUDE.md`. Don't. [Research](https://arxiv.org/pdf/2507.11538) indicates:

1. **Frontier thinking LLMs can follow ~150–200 instructions with reasonable consistency.** Smaller and non-thinking models attend to fewer.
2. **Smaller models degrade much faster** — exponential decay in instruction-following as instruction count rises, vs. linear for large thinking models. Avoid small models for multi-step tasks.
3. **LLMs bias toward instructions on the peripheries of the prompt** — the very beginning (system message and CLAUDE.md) and the very end (most recent user messages).
4. **As instruction count increases, instruction-following quality decreases *uniformly***. More instructions doesn't mean it ignores the newest ones — it begins to ignore *all of them* uniformly.

Claude Code's system prompt already contains ~50 individual instructions — nearly a third of what the agent can reliably follow, before your rules, plugins, skills, or user messages. So your `CLAUDE.md` should contain as few instructions as possible, ideally only ones universally applicable to your tasks.

### File length & applicability

An LLM performs better when its context window is full of focused, relevant context (examples, related files, tool calls, results) than when it has a lot of irrelevant context. Since `CLAUDE.md` goes into *every* session, keep its contents as universally applicable as possible. Avoid, e.g., instructions on how to structure a new database schema — they won't matter and will distract the model when you're working on something unrelated.

General consensus: **< 300 lines is best, shorter is better.** HumanLayer's root `CLAUDE.md` is *less than sixty lines*.

### Progressive disclosure

Instead of cramming build/test/convention instructions into `CLAUDE.md`, keep task-specific instructions in *separate markdown files* with self-descriptive names:

```
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- service_architecture.md
  |- database_schema.md
  |- service_communication_patterns.md
```

In `CLAUDE.md`, list these files with a brief description of each and instruct Claude to decide which (if any) are relevant and read them before working. Or ask Claude to present the files it wants to read for approval first.

**Prefer pointers to copies.** Don't include code snippets — they go out of date fast. Use `file:line` references to point Claude to the authoritative context. (Conceptually similar to how Claude Skills work.)

### Claude is (not) an expensive linter

One of the most common mistakes is putting code style guidelines in `CLAUDE.md`. **Never send an LLM to do a linter's job** — LLMs are expensive and slow compared to deterministic tools. Style guidelines add instructions and mostly-irrelevant snippets that degrade performance and eat context.

LLMs are in-context learners. If your code follows certain patterns, a few searches of your codebase (or a good research doc) will get the agent to follow existing conventions without being told. If you feel strongly, set up a [Stop hook](https://code.claude.com/docs/en/hooks#stop) that runs your formatter/linter and presents errors to Claude to fix. Use a linter that auto-fixes (e.g., Biome). Or create a slash command that includes your guidelines and points Claude at your `git status`.

### Don't use /init or auto-generate your CLAUDE.md

Because `CLAUDE.md` goes into *every* session, it's one of the highest-leverage points of the harness. A bad line of code is one bad line. A bad line in `CLAUDE.md` affects every phase of every workflow and every artifact it produces. Spend time thinking carefully about every single line. Don't auto-generate it.

## In conclusion

1. `CLAUDE.md` is for onboarding Claude into your codebase. Define your project's **WHY**, **WHAT**, and **HOW**.
2. **Less (instructions) is more.** Include as few instructions as reasonably possible.
3. Keep the contents **concise and universally applicable**.
4. Use **progressive disclosure** — tell Claude *how to find* important information rather than dumping it all in.
5. Claude is not a linter. Use linters, formatters, hooks, and slash commands instead.
6. `CLAUDE.md` is the highest-leverage point of the harness, so avoid auto-generating it. Craft it carefully.

## Related HumanLayer posts
- Context-Efficient Backpressure for Coding Agents — https://www.humanlayer.dev/blog/context-efficient-backpressure
- Advanced Context Engineering for Coding Agents — https://www.humanlayer.dev/blog/advanced-context-engineering
- 12-factor-agents — https://github.com/humanlayer/12-factor-agents
