# When and how an AI should ask questions

> A compact, paste-ready rule set for "when to ask clarifying questions vs. proceed, and how to do it well." Synthesized from Anthropic's Claude Code best practices (the "let Claude interview you" pattern), OpenAI Codex prompting guidance, and common agent-harness system prompts.

## The core decision: ask vs. proceed

Asking has a cost (it interrupts the user) and a benefit (it avoids solving the wrong problem). The rule of thumb most good harnesses use:

- **Proceed without asking** when the request has an obvious default, the answer is discoverable from the code/files/context, or the task is small and reversible. State the assumption you're making and move on.
- **Ask** only when the answer would *change what you build*, you cannot resolve it from the request or sensible defaults, and getting it wrong would waste real work.
- **Don't gate research on a question.** For information-gathering tasks, start searching first — initial results usually make the clarifying question sharper and more concrete. Ask alongside or after first results, not before.

## Paste-ready rule block

```
# Asking questions
- Before multi-step work, surface genuine ambiguity (audience, scope, format, constraints) in ONE batched round of questions, then proceed.
- Only ask when the answer changes what you do. If a sensible default exists, take it, state it, and continue.
- Don't ask what you can find. Check the code, files, docs, and conversation history first.
- One round, not a drip. Group related questions together rather than asking one at a time across many turns.
- Prefer concrete multiple-choice options over open-ended questions; offer a recommended default.
- For factual lookups and small reversible edits, don't ask — just do it and report what you assumed.
- After finishing something ambiguous, note the assumptions you made so the user can correct course.
```

## The "interview me" pattern (Anthropic, for larger features)

For a non-trivial feature, have the agent interview the user *before* writing code:

```
I want to build [brief description]. Interview me in detail using a multiple-choice
question tool. Ask about technical implementation, UI/UX, edge cases, concerns, and
tradeoffs. Don't ask obvious questions — dig into the hard parts I might not have
considered. Keep interviewing until we've covered everything, then write a complete
spec to SPEC.md.
```

Why it works: the agent raises things the user hasn't thought about (edge cases, tradeoffs), and the output is a self-contained spec — naming the files/interfaces involved, stating what's out of scope, and ending with an end-to-end verification step. Then a fresh session executes the spec with clean context. Time spent making the spec precise pays off more than time spent watching the implementation.

## How to ask well
- **Batch and bound.** One screen of questions, each with a clear default, beats a long back-and-forth.
- **Make options mutually exclusive and concrete.** "Postgres vs. SQLite vs. in-memory" beats "what database do you want?"
- **Recommend.** Put your recommended option first and label it. Users often just want a sensible default confirmed.
- **Explain the stakes briefly.** A one-line "this changes X" tells the user why you're asking.
- **Don't ask to ask.** Never send "Is my plan ready?" or "Should I proceed?" — either proceed, or ask a substantive question.

## Signs you're asking too much (or too little)
- **Too much:** asking things answered in the project files or the user's own message; asking one question per turn; asking when any reasonable default would do.
- **Too little:** building for an hour on an assumption you could have confirmed in one question; producing a deliverable in the wrong format/scope; "fixing" the symptom because you didn't confirm the actual goal.

## Source patterns worth reading
- Anthropic, "Best practices for Claude Code" → the "Let Claude interview you" section: https://code.claude.com/docs/en/best-practices
- OpenAI Codex prompting: https://developers.openai.com/codex/prompting
- Anthropic prompt engineering ("if unsure, say so; ask 1 clarifying question"): https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
