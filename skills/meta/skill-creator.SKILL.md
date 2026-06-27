<!--
SOURCE: anthropics/skills (official) — https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md
Retrieved 2026-06-26. License: Apache 2.0 (example skills in anthropics/skills).
CONDENSED: this keeps the reusable "how to write a good skill" guidance. The full skill also includes an
eval/benchmark harness (scripts/, eval-viewer/, agents/) for measuring skill performance — clone the repo for those.
This is the skill to use when you want to turn any of your repeating workflows into a new skill.
-->
---
name: skill-creator
description: Create new skills, modify and improve existing skills, and measure skill performance. Use when users want to create a skill from scratch, edit, or optimize an existing skill, run evals to test a skill, benchmark skill performance with variance analysis, or optimize a skill's description for better triggering accuracy.
---

# Skill Creator

A skill for creating new skills and iteratively improving them.

The high-level process:
- Decide what you want the skill to do and roughly how.
- Write a draft of the skill.
- Create a few test prompts and run Claude-with-the-skill on them.
- Evaluate the results qualitatively and (optionally) quantitatively.
- Rewrite based on feedback. Repeat until satisfied. Then expand the test set and try at larger scale.

## Creating a skill

### Capture intent
Understand the user's intent first. If the conversation already contains the workflow ("turn this into a skill"), extract: tools used, sequence of steps, corrections the user made, input/output formats observed. Confirm before proceeding.

Key questions:
1. What should this skill enable Claude to do?
2. When should it trigger? (what user phrases/contexts)
3. What's the expected output format?
4. Should we set up test cases? (Objectively verifiable outputs — file transforms, data extraction, code generation — benefit from tests. Subjective outputs — writing style, art — often don't.)

### Write the SKILL.md
Fill in these components:
- **name**: skill identifier.
- **description**: the primary triggering mechanism — include BOTH what the skill does AND specific contexts for when to use it. All "when to use" info goes here, not in the body. Claude tends to *undertrigger* skills, so make descriptions a little "pushy." Instead of "How to build a dashboard for internal data," write "How to build a dashboard for internal data. Use this skill whenever the user mentions dashboards, data visualization, internal metrics, or wants to display any company data, even if they don't explicitly say 'dashboard.'"
- the rest of the skill.

### Anatomy of a skill
```
skill-name/
├── SKILL.md (required)
│   ├── YAML frontmatter (name, description required)
│   └── Markdown instructions
└── Bundled Resources (optional)
    ├── scripts/    - Executable code for deterministic/repetitive tasks
    ├── references/ - Docs loaded into context as needed
    └── assets/     - Files used in output (templates, icons, fonts)
```

### Progressive disclosure (three-level loading)
1. **Metadata** (name + description) — always in context (~100 words).
2. **SKILL.md body** — in context whenever the skill triggers (<500 lines ideal).
3. **Bundled resources** — loaded as needed (unlimited; scripts can execute without loading into context).

Key patterns: keep SKILL.md under 500 lines; if approaching the limit, add a layer of hierarchy with clear pointers to follow-up files. Reference files clearly with guidance on when to read them. For large reference files (>300 lines), include a table of contents. When a skill supports multiple domains/frameworks, organize by variant (e.g., references/aws.md, gcp.md, azure.md) so Claude reads only the relevant one.

### Principle of lack of surprise
Skills must not contain malware, exploit code, or anything that compromises security. A skill's contents should not surprise the user given its description. Don't create misleading skills or skills for unauthorized access/data exfiltration. (Roleplay-style skills are fine.)

### Writing patterns
Prefer the imperative form. Define output formats explicitly with templates. Include input/output examples.
```markdown
## Commit message format
Input: Added user authentication with JWT tokens
Output: feat(auth): implement JWT-based authentication
```

### Writing style
Explain *why* things matter rather than piling on heavy-handed MUSTs. Today's models have good theory of mind; given the reasoning, they go beyond rote instructions. If you find yourself writing ALWAYS or NEVER in all caps or using rigid structures, that's a yellow flag — reframe and explain the reasoning instead. Write a draft, then look at it with fresh eyes and improve it.

### Test cases
After a draft, write 2-3 realistic test prompts (the kind a real user would actually type). Share them with the user, then run them. Save to `evals/evals.json` (prompts first; assertions later). Good assertions are objectively verifiable with descriptive names. Subjective skills are better judged qualitatively — don't force assertions onto things that need human judgment.

## Improving the skill (the heart of the loop)
1. **Generalize from feedback.** You're iterating on a few examples, but the skill must work across millions of future prompts. Avoid fiddly, overfit changes and oppressive MUSTs. If an issue is stubborn, try different metaphors or working patterns — it's cheap to try.
2. **Keep the prompt lean.** Remove things that aren't pulling their weight. Read the transcripts, not just the outputs — cut parts that make the model waste time.
3. **Explain the why.** Even if user feedback is terse, understand the task and transmit that understanding into the instructions.
4. **Look for repeated work across test cases.** If every run independently writes a similar helper script, bundle that script in `scripts/` and have the skill use it.

## Description optimization
The description field determines whether Claude invokes the skill. After creating/improving a skill, optimize it: generate ~20 realistic trigger eval queries (8-10 should-trigger with varied phrasings, 8-10 should-not-trigger "near-misses" that share keywords but need something else — avoid obviously-irrelevant negatives). The full skill provides a `run_loop.py` that splits train/held-out test, evaluates each description (3 runs per query for a reliable trigger rate), and iterates up to 5 times, selecting `best_description` by test score to avoid overfitting.

### How skill triggering works
Skills appear in Claude's `available_skills` list with name + description; Claude decides whether to consult a skill based on that description. Claude only consults skills for tasks it can't easily handle on its own — simple one-step queries ("read this PDF") may not trigger a skill even with a perfect description, because Claude handles them directly. So make eval queries substantive enough that consulting a skill is genuinely beneficial.

## Core loop (for emphasis)
- Figure out what the skill is about → draft/edit → run Claude-with-the-skill on test prompts → evaluate outputs with the user (qualitatively, plus quantitative evals if appropriate) → repeat until satisfied → package and return the final skill.

> The full official skill includes scripts for packaging (`package_skill.py`), an eval viewer (`generate_review.py`), grader/comparator/analyzer subagent instructions, and schema references. Get them from https://github.com/anthropics/skills if you want the measurement harness. NOTE: Cowork already ships a `skill-creator` skill — you can invoke it directly rather than installing this copy.
