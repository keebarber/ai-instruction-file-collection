# Career context — keeping your "about me" in front of an agent

The problem: re-explaining who you are every time you ask an agent to draft something. The fix: one canonical file, `candidate-profile.md`, that you maintain and hand to the agent.

## Fill it in once
Open `candidate-profile.md` and replace the `[fill in]` / `[NEED: ...]` placeholders. You don't have to do it all at once — the agent-instructions at the top tell the agent to leave a marked placeholder when a fact is missing, so you can grow it over time. Keep skill tiers honest and accomplishments specific (numbers beat adjectives).

## Then present it to the agent — three ways, easiest first

1. **Reference it per session (no setup).** Keep the file in whatever folder you do job-search work in. Start a drafting chat with:
   > "Read `candidate-profile.md`, then draft a cover letter for the JD below: …"
   In Claude Code / Cursor you can use `@candidate-profile.md`. In a plain chatbot, paste the file contents.

2. **Put it where the agent auto-reads project context.** If you use a coding-style agent, drop the profile into the project as `CLAUDE.md` / `AGENTS.md`, or import it from one (`See @career-context/candidate-profile.md`). Then it loads every session in that folder without you asking.

3. **Make it a skill (auto-loads when relevant).** A skill named e.g. `job-search-context` would load whenever you ask for job-search drafting. You can't create a skill from inside this chat session — set one up via **Settings → Capabilities** (point its `SKILL.md` at this profile, or paste the content in). Best if you do this often and want zero friction.

For most people, option 1 is plenty. Move to 2 or 3 only if the repetition starts to annoy you.

## Keep it healthy
- Update the `Last updated` line and prune stale items.
- Don't let it bloat — the same rule from the rest of this repo applies: a long context file gets half-ignored. Keep entries tight; move rarely-needed detail to the bottom.
- The voice rules in the profile point at `../writing-and-voice/words-and-phrases-to-avoid.cheatsheet.md` so your drafts don't read as AI-generated.

## Optional companions you might add later
- `resume-master.md` — your full, untailored resume in plain text, for the agent to cut down per role.
- `outreach-snippets.md` — reusable intro lines, recruiter replies, thank-you notes.
- `applications-log.md` — a table of where you applied, status, and the tailoring notes you used.
