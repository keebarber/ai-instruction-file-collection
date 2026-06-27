# AGENTS.md — the open standard, spec + examples

> SOURCE: https://agents.md/ — stewarded by the Agentic AI Foundation (Linux Foundation). Repo: https://github.com/agentsmd/agents.md. Saved 2026-06-26.
> AGENTS.md is "a README for agents" — used by 60k+ open-source projects and supported by Codex, Cursor, Jules, Factory, Aider, goose, opencode, Zed, Warp, Gemini CLI, Copilot coding agent, Devin, Windsurf, Junie, and more. One file works across all of them.

## Why AGENTS.md (and not just README)

README files are for humans: quick starts, project descriptions, contribution guidelines. AGENTS.md holds the extra, sometimes detailed context coding agents need — build steps, tests, conventions — that would clutter a README or isn't relevant to human contributors. Keeping it separate gives agents a predictable place for instructions and keeps READMEs focused on people.

## Minimal example

```markdown
# AGENTS.md

## Setup commands
- Install deps: `pnpm install`
- Start dev server: `pnpm dev`
- Run tests: `pnpm test`

## Code style
- TypeScript strict mode
- Single quotes, no semicolons
- Use functional patterns where possible
```

## Fuller example

```markdown
# Sample AGENTS.md file

## Dev environment tips
- Use `pnpm dlx turbo run where <project_name>` to jump to a package instead of scanning with `ls`.
- Run `pnpm install --filter <project_name>` to add the package to your workspace so Vite, ESLint, and TypeScript can see it.
- Use `pnpm create vite@latest <project_name> -- --template react-ts` to spin up a new React + Vite package with TypeScript checks ready.
- Check the name field inside each package's package.json to confirm the right name—skip the top-level one.

## Testing instructions
- Find the CI plan in the .github/workflows folder.
- Run `pnpm turbo run test --filter <project_name>` to run every check defined for that package.
- From the package root you can just call `pnpm test`. The commit should pass all tests before you merge.
- To focus on one step, add the Vitest pattern: `pnpm vitest run -t "<test name>"`.
- Fix any test or type errors until the whole suite is green.
- After moving files or changing imports, run `pnpm lint --filter <project_name>` to be sure ESLint and TypeScript rules still pass.
- Add or update tests for the code you change, even if nobody asked.

## PR instructions
- Title format: [<project_name>] <Title>
- Always run `pnpm lint` and `pnpm test` before committing.
```

## How to use it

1. **Add AGENTS.md** at the repo root. Most agents can scaffold one if you ask.
2. **Cover what matters.** Popular sections: project overview, build/test commands, code style guidelines, testing instructions, security considerations.
3. **Add extra instructions.** Commit message / PR guidelines, security gotchas, large datasets, deployment steps — anything you'd tell a new teammate.
4. **Large monorepo? Use nested AGENTS.md files.** Agents read the *nearest* file in the directory tree, so the closest one takes precedence and each subproject ships tailored instructions. (The main OpenAI repo has 88 AGENTS.md files.)

## FAQ (from agents.md)
- **Required fields?** No. It's plain Markdown; use any headings you like.
- **Conflicting instructions?** The closest AGENTS.md to the edited file wins; explicit user chat prompts override everything.
- **Will the agent run testing commands found in it?** Yes — if you list them. The agent attempts relevant checks and fixes failures before finishing.
- **Update later?** Treat it as living documentation.
- **Migrating from another filename?** `mv AGENT.md AGENTS.md && ln -s AGENTS.md AGENT.md`
- **Aider:** add `read: AGENTS.md` to `.aider.conf.yml`.
- **Gemini CLI:** set `{ "context": { "fileName": "AGENTS.md" } }` in `.gemini/settings.json`.

## Real-world AGENTS.md to study
- openai/codex — https://github.com/openai/codex/blob/main/AGENTS.md
- apache/airflow — https://github.com/apache/airflow/blob/main/AGENTS.md
- temporalio/sdk-java — https://github.com/temporalio/sdk-java/blob/main/AGENTS.md
- Browse 60k+ live examples: https://github.com/search?q=path%3AAGENTS.md+NOT+is%3Afork+NOT+is%3Aarchived&type=code
