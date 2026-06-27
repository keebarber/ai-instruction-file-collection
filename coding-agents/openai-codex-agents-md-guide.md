# Custom instructions with AGENTS.md — OpenAI Codex

> SOURCE: https://developers.openai.com/codex/guides/agents-md — OpenAI. Saved 2026-06-26 (condensed).
> Useful for the precedence/discovery model: how global + project + nested instruction files merge. Same mental model applies to most agents that read AGENTS.md.

Codex reads `AGENTS.md` files before doing any work. Layer global guidance with project-specific overrides so every task starts with consistent expectations.

## How Codex discovers guidance

Codex builds an instruction chain when it starts (once per run / TUI session). Precedence order:

1. **Global scope:** In your Codex home (`~/.codex` unless `CODEX_HOME` is set), Codex reads `AGENTS.override.md` if it exists, otherwise `AGENTS.md`. Only the first non-empty file at this level is used.
2. **Project scope:** From the project root (usually the Git root) down to your current working directory, each directory is checked for `AGENTS.override.md`, then `AGENTS.md`, then any `project_doc_fallback_filenames`. At most one file per directory.
3. **Merge order:** Files are concatenated root-down, joined with blank lines. Files closer to your current directory override earlier guidance (they appear later in the combined prompt).

Codex skips empty files and stops once the combined size reaches `project_doc_max_bytes` (32 KiB default). Raise the limit or split instructions across nested directories when you hit the cap.

## Global guidance

```markdown
# ~/.codex/AGENTS.md

## Working agreements
- Always run `npm test` after modifying JavaScript files.
- Prefer `pnpm` when installing dependencies.
- Ask for confirmation before adding new production dependencies.
```

Use `~/.codex/AGENTS.override.md` for a temporary global override without deleting the base file.

## Project + nested overrides

```markdown
# AGENTS.md (repo root)

## Repository expectations
- Run `npm run lint` before opening a pull request.
- Document public utilities in `docs/` when you change behavior.
```

```markdown
# services/payments/AGENTS.override.md

## Payments service rules
- Use `make test-payments` instead of `npm test`.
- Never rotate API keys without notifying the security channel.
```

Codex stops searching once it reaches your current directory, so place overrides as close to specialized work as possible.

## Custom fallback filenames

If your repo already uses a different filename, add it to the fallback list:

```toml
# ~/.codex/config.toml
project_doc_fallback_filenames = ["TEAM_GUIDE.md", ".agents.md"]
project_doc_max_bytes = 65536
```

Codex then checks each directory in order: `AGENTS.override.md`, `AGENTS.md`, `TEAM_GUIDE.md`, `.agents.md`.

## Verify / troubleshoot
- `codex --ask-for-approval never "Summarize the current instructions."` from a repo root — Codex should echo guidance in precedence order.
- `codex --cd subdir ... "Show which instruction files are active."` confirms nested overrides.
- Nothing loads → verify you're in the intended repo and files aren't empty.
- Wrong guidance → look for an `AGENTS.override.md` higher in the tree or in Codex home.
- Truncated → raise `project_doc_max_bytes` or split across nested dirs.
