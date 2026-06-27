# Real system prompts — where to read the actual files

> The richest source of "how a top lab tells a model to write, code, and ask questions" is the system prompts of shipping products. These collections host the actual files. They're large and change often, so this folder links to them rather than vendoring megabytes of prompts. Clone any repo below to get the raw `.md`/`.txt` files.
>
> Caveat: these are community-extracted/"leaked" prompts. Treat them as approximate and possibly out of date, not as official ground truth. Anthropic, OpenAI, etc. do not publish most of these. Use them to study patterns, not as authoritative documentation.

## Best collections (clone these)

- **jujumilk3/leaked-system-prompts** — https://github.com/jujumilk3/leaked-system-prompts
  Long-running, well-organized archive of leaked system prompts (Claude, ChatGPT, Gemini, Grok, Cursor, v0, Devin, and more). Good first stop. One file per product/version.

- **elder-plinius/CL4R1T4S** — https://github.com/elder-plinius/CL4R1T4S
  Very large, frequently updated. Full system prompts + tool definitions from OpenAI, Google, Anthropic, xAI, Perplexity, Cursor, Windsurf, Devin, Manus, Replit, Lovable, and more.

- **asgeirtj/system_prompts_leaks** — https://github.com/asgeirtj/system_prompts_leaks
  Focus on the frontier chat assistants (Anthropic Claude, OpenAI ChatGPT/Codex, Google Gemini, xAI Grok). Updated regularly.

- **x1xhlol / system-prompts-and-models-of-ai-tools** — https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools
  The 100k+ star collection of coding-tool prompts: Cursor, Windsurf, Devin, v0, Augment, Lovable, Bolt, Replit, plus their tool JSON. The best source for "how coding agents are instructed."

- **EliFuzz/awesome-system-prompts** — https://github.com/EliFuzz/awesome-system-prompts
  Curated set of system prompts + tool definitions from coding agents (Augment, Claude Code, Cursor, Devin, Kiro, Perplexity, VS Code agent, Gemini, Codex).

- **Piebald-AI/claude-code-system-prompts** — https://github.com/Piebald-AI/claude-code-system-prompts
  Specifically Claude Code: the system prompt, 27 built-in tool descriptions, sub-agent prompts (Plan/Explore/Task), and utility prompts (CLAUDE.md handling, compaction, WebFetch, security review, agent creation). Versioned per Claude Code release. The single best resource if you want to see exactly how an agent harness is wired.

## What to look for when you read them
- **Style/voice rules**: how the model is told to format, when to use lists vs. prose, tone constraints, "don't be sycophantic", emoji rules.
- **Code rules**: verify-before-done instructions, "don't invent APIs", root-cause-not-symptom, test/lint gating, diff discipline.
- **Question-asking**: when the harness tells the model to ask vs. proceed, and how (e.g. an AskUserQuestion tool).
- **Tool-use discipline**: how tools are described, parallelism rules, and refusal/safety framing.
- **Refusals & safety**: how labs phrase boundaries — a useful template for your own guardrails.

## Official prompt-engineering references (not leaks)
- Anthropic prompting best practices — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- Anthropic interactive prompt-engineering tutorial — https://github.com/anthropics/prompt-eng-interactive-tutorial
- Anthropic, "Effective context engineering for AI agents" — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
- OpenAI Codex prompting guide — https://developers.openai.com/codex/prompting
- Anthropic system-prompts release notes (official, for Claude.ai) — https://docs.claude.com/en/release-notes/system-prompts
