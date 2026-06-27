# Skills

Real, downloaded `SKILL.md` files for the things you do most: job searching/applying, coding, debugging, testing, and building your own skills. Each file keeps its source attribution in a comment at the top. Full provenance is in `../SOURCES.md`.

## What a skill is (and how to use these)
A skill is a folder with a `SKILL.md` (YAML frontmatter + Markdown instructions), optionally bundled with scripts/references/assets. An agent loads the name + description always, the body when the skill triggers, and bundled files only as needed. To use one of these:

- **Claude Code / Cursor / Codex / most agents:** put the file in a folder named after the skill (e.g. `~/.claude/skills/systematic-debugging/SKILL.md`) and the agent auto-discovers it.
- **Cowork (this app):** several of these already ship built in (skill-creator, learn, docx/pdf/pptx/xlsx). For the others, install via Settings → Capabilities, or just paste the file's content into a chat when you want that behavior.
- **Quick use anywhere:** paste the file contents into the chat and say "follow this."

> Note: most of these are single `SKILL.md` files. A few reference sibling files (bundled scripts or `references/*.md`) that are NOT included here — the header comment says when, and points you to the source repo to get the rest.

## Job search & applying  (`job-search/`)
These four chain together: analyze a posting → tailor docs → prep the interview → negotiate. They pair with your `../career-context/candidate-profile.md` — feed that in as the candidate background.

- **`job-description-analyzer.SKILL.md`** — paste a JD, get a match score, gap analysis, red-flag detection, and a tailoring strategy. Run this *first* to decide if a role is worth the effort. (Paramchoudhary/ResumeSkills, MIT)
- **`resume-cover-letter.SKILL.md`** — tailored resume/CV and cover letters with ATS rules, achievement bullets (CAR format), regional formats, and handling for gaps/career-changes/overqualified. (jezweb/claude-skills)
- **`interview-prep-generator.SKILL.md`** — turns your experience into STAR stories, predicts questions from the JD, and scripts the hard ones ("greatest weakness," "why leaving"). Uses the STAR bank in your profile. (Paramchoudhary/ResumeSkills, MIT)
- **`salary-negotiation-prep.SKILL.md`** — market-rate research, total-comp math, and ready counter-offer email/call scripts. (Paramchoudhary/ResumeSkills, MIT)

> The Paramchoudhary repo has 16 more job-search skills (ATS optimizer, bullet writer, resume quantifier, LinkedIn optimizer, tech-resume-optimizer, offer-comparison, etc.). Browse: https://github.com/Paramchoudhary/ResumeSkills

## Coding, debugging & testing  (`coding-debugging-testing/`)
From the `superpowers` library — the most disciplined, battle-tested agentic engineering skills out there. They enforce the loop you described wanting in your CLAUDE.md work: don't guess, test first, verify before claiming done.

- **`systematic-debugging.SKILL.md`** — a four-phase root-cause method with one iron law: no fixes without investigation first. Includes the "stop after 3 failed fixes and question the architecture" rule. (obra/superpowers)
- **`test-driven-development.SKILL.md`** — strict RED/GREEN/REFACTOR: no production code without a failing test first. (obra/superpowers)
- **`verification-before-completion.SKILL.md`** — never claim "done/passing/fixed" without running the command and reading the output. Evidence before assertions. (obra/superpowers)

> The full superpowers library adds writing-plans, executing-plans, brainstorming, code-review (requesting/receiving), subagent-driven-development, git-worktrees, and more: https://github.com/obra/superpowers

## Build your own  (`meta/`)
- **`skill-creator.SKILL.md`** — how to write, test, and optimize a skill, including the description-writing rules that control whether a skill triggers. Use this to turn any repeating workflow of yours into a skill. (anthropics/skills, official, Apache 2.0)

## Learning
No standalone file vendored here, but two strong options:
- Cowork ships a built-in **`learn`** skill (teaching, ELI5, quizzes, learning paths) — just ask it to teach you something.
- For self-study collections, browse the curated lists below (filter by "learning"/"education").

## Where to find more skills (curated lists)
- karanb192/awesome-claude-skills — https://github.com/karanb192/awesome-claude-skills (50+ verified, TDD/debugging/git/docs)
- VoltAgent/awesome-agent-skills — https://github.com/VoltAgent/awesome-agent-skills (1000+, official + community)
- travisvn/awesome-claude-skills — https://github.com/travisvn/awesome-claude-skills
- ComposioHQ/awesome-claude-skills — https://github.com/ComposioHQ/awesome-claude-skills
- anthropics/skills — https://github.com/anthropics/skills (official examples)
- obra/superpowers — https://github.com/obra/superpowers (full software-dev workflow)
- Paramchoudhary/ResumeSkills — https://github.com/Paramchoudhary/ResumeSkills (20 job-search skills, MIT)

## A note on licenses
The Paramchoudhary job-search skills are MIT. The anthropics/skills example skills (incl. skill-creator) are Apache 2.0. The superpowers and jezweb skills retain their repo licenses — check each repo before redistributing. Attribution headers are preserved in every file.
