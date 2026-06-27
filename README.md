# AI Instruction File Collection

A curated, opinionated collection of the best instruction files and references for steering LLMs and AI coding agents — the real files, plus distilled cheat-sheets and an annotated link directory.

Covers the five things you asked for:
1. Words / practices / patterns to **avoid**
2. How to **write / speak / sound**
3. How to **write code** — what to avoid, check for, and do
4. How to **respond to questions**
5. **When** to ask questions, and **how**

Compiled 2026-06-26. Everything is attributed to its source; cheat-sheets are marked as distilled.

---

## What's in this repo

```
coding-agents/        How agents should write code + how to write CLAUDE.md / AGENTS.md
writing-and-voice/    Words/patterns to avoid + how to sound human (the anti-slop material)
asking-questions/     When to ask vs. proceed, and how to ask well
system-prompts/       Where to read the actual shipping system prompts (links)
```

### Files
- **`coding-agents/humanlayer-writing-a-good-CLAUDE-md.md`** — the best essay on why instruction files fail and how to fix them (less-is-more, progressive disclosure, "Claude is not a linter"). *Verbatim, condensed.*
- **`coding-agents/anthropic-claude-code-best-practices.md`** — Anthropic's official guide: verify-your-work, explore→plan→code, what to put in (and keep out of) a CLAUDE.md. *Verbatim, condensed.*
- **`coding-agents/agents-md-spec-and-examples.md`** — the cross-tool AGENTS.md open standard with copy-paste examples. *Verbatim.*
- **`coding-agents/openai-codex-agents-md-guide.md`** — how global + project + nested instruction files merge and override. *Verbatim, condensed.*
- **`coding-agents/shanraisshan-CLAUDE.md`** — a real, working CLAUDE.md to use as a structural template. *Verbatim.*
- **`coding-agents/how-to-write-code-rules.cheatsheet.md`** — paste-ready coding rules (verify, avoid, do). *Distilled.*
- **`writing-and-voice/avoid-ai-writing.SKILL.md`** — the standout file: a 42-pattern, 3-tier word/phrase audit you can install as a skill. *Verbatim, MIT.*
- **`writing-and-voice/words-and-phrases-to-avoid.cheatsheet.md`** — the short list + structures to ban. *Distilled.*
- **`writing-and-voice/how-to-write-and-sound.md`** — positive voice/tone rules to pair with the avoid-list. *Distilled.*
- **`asking-questions/when-and-how-to-ask-questions.md`** — ask-vs-proceed rules + the "interview me" pattern. *Distilled.*
- **`system-prompts/README.md`** — annotated links to the big leaked-system-prompt archives. *Links.*

---

## Annotated link directory

### 1. Words / practices / patterns to avoid
- **conorbronsdon/avoid-ai-writing** — https://github.com/conorbronsdon/avoid-ai-writing — the best single resource. SKILL.md with 42 detected patterns, a tiered 109-entry word table, context profiles, and a detect-only mode. Saved here as `writing-and-voice/avoid-ai-writing.SKILL.md`. (1.5k★, MIT)
- **Wikipedia: Signs of AI writing** — https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing — the canonical, editor-maintained catalogue of AI tells.
- **brandonwise/humanizer** — https://github.com/brandonwise/humanizer — the tiered-vocabulary research the avoid-ai-writing word tables are adapted from (burstiness, sentence-length variation, trigram repetition).
- **Pangram Labs** — https://www.pangram.com/ — AI-detection research; the source for "structure beats vocabulary as a detection signal."
- "The prompt we use to prevent AI slop" (Towards AI) — https://learnaitogethernewsletter.substack.com/p/the-prompt-we-use-to-prevent-ai-slop

### 2. How to write / speak / sound
- See `writing-and-voice/how-to-write-and-sound.md` (positive rules) and the tone-calibration section of the avoid-ai-writing skill.
- **Anthropic prompting best practices** — https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- **Anthropic interactive prompt-engineering tutorial** — https://github.com/anthropics/prompt-eng-interactive-tutorial
- **Effective context engineering for AI agents** (Anthropic) — https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents

### 3. How to write code (avoid / check / do)
- **Anthropic, Best practices for Claude Code** — https://code.claude.com/docs/en/best-practices (saved here)
- **HumanLayer, Writing a good CLAUDE.md** — https://www.humanlayer.dev/blog/writing-a-good-claude-md (saved here)
- **PatrickJS/awesome-cursorrules** — https://github.com/PatrickJS/awesome-cursorrules — the largest collection of real `.cursorrules` / `.cursor/rules/*.mdc` files, organized by language/framework. Best place to grab a ready-made coding rules file.
- **tonynguyennvt/cursor-rules-awesome** — https://github.com/tonynguyennvt/cursor-rules-awesome — 4,800+ lines of comprehensive coding standards (OWASP, SRE, multiple languages, compliance frameworks).
- **agents.md** — https://agents.md/ — the cross-tool standard (saved here).
- **FlorianBruniaux/claude-code-ultimate-guide** — https://github.com/FlorianBruniaux/claude-code-ultimate-guide — large guide to agentic workflows, hooks, skills, MCP, templates.
- **hesreallyhim/awesome-claude-code** — https://github.com/hesreallyhim/awesome-claude-code — curated skills, hooks, slash-commands, agents, plugins.
- **shanraisshan/claude-code-best-practice** — https://github.com/shanraisshan/claude-code-best-practice — patterns for skills/subagents/hooks (its CLAUDE.md saved here).
- **kirill-markin, Claude Code rules** — https://kirill-markin.com/articles/claude-code-rules-for-ai/ — a worked global-instructions setup.

### 4. How to respond to questions
- The shipping **system prompts** are the best teachers here — see `system-prompts/README.md`. Look at how Claude / ChatGPT / Cursor are told to format answers, when to use prose vs. lists, and how to avoid sycophancy.
- **Piebald-AI/claude-code-system-prompts** — https://github.com/Piebald-AI/claude-code-system-prompts — Claude Code's full prompt + tool descriptions + sub-agent prompts.
- **x1xhlol/system-prompts-and-models-of-ai-tools** — https://github.com/x1xhlol/system-prompts-and-models-of-ai-tools — 100k★ coding-tool prompts.

### 5. When + how to ask questions
- See `asking-questions/when-and-how-to-ask-questions.md`.
- The **"let Claude interview you"** pattern in Anthropic's best-practices guide is the standout technique.
- **OpenAI Codex prompting** — https://developers.openai.com/codex/prompting

---

## How to use this

- **Building a CLAUDE.md / AGENTS.md?** Start with `coding-agents/humanlayer-writing-a-good-CLAUDE-md.md` and the Anthropic include/exclude table, then pull lines from `how-to-write-code-rules.cheatsheet.md`. Keep it under ~150 lines and only include what would actually change behavior.
- **Want cleaner writing out of any model?** Install `writing-and-voice/avoid-ai-writing.SKILL.md` as a skill (drop it in `~/.claude/skills/avoid-ai-writing/`), or paste `words-and-phrases-to-avoid.cheatsheet.md` + `how-to-write-and-sound.md` into your system prompt.
- **Setting agent question-asking behavior?** Use the paste-ready block in `asking-questions/`.
- **Studying how the pros do it?** Clone a repo from `system-prompts/README.md`.

## A meta-warning (from the sources themselves)
More rules ≠ better behavior. Research cited by HumanLayer shows instruction-following degrades *uniformly* as instruction count rises — past a point, the model starts ignoring *all* your rules, not just the newest. Keep instruction files short, specific, and observable. Prune ruthlessly. Use deterministic tools (linters, hooks, tests) for anything a tool can enforce, and save the instruction file for what only it can convey.
