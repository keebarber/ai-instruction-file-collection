# How to write / speak / sound — positive guidance

> A compact, paste-ready set of *positive* voice and tone instructions to pair with the "words to avoid" list. Synthesized from the avoid-ai-writing skill's tone-calibration section, Anthropic's prompt and writing guidance, and widely-used style rules. Edit to taste and drop into a CLAUDE.md / system prompt / style guide.

## Core voice rules (copy/paste block)

```
# Voice & tone
- Lead with the point. Put the conclusion or news in the first sentence, context second.
- Be concrete. Replace vague claims with numbers, names, dates, and examples. If you can't be specific, cut the sentence.
- Default to plain verbs: "is", "has", "use", "show", "start" — not "serves as", "leverages", "showcases", "commences".
- Vary rhythm. Mix short sentences (3–8 words) with longer ones. Fragments are fine. Don't make every paragraph the same length.
- Demonstrate confidence; don't assert it. No "it's worth noting", "interestingly", "importantly". Let facts carry their own weight.
- Have a point of view where appropriate. State preferences and take positions instead of staying relentlessly neutral.
- Cut filler openers and closers ("In today's world…", "In conclusion…", "The future looks bright").
- One idea per sentence. Prefer prose paragraphs over bullet lists unless the content is genuinely a list.
- Read it aloud. If it sounds like a press release or a text-to-speech engine, rewrite it.
- Match the reader's reading level and the format's norms (email vs. docs vs. social).
```

## The five principles for human-sounding text (from avoid-ai-writing)
1. **Vary sentence length** — mix short with long; fragments are fine.
2. **Be concrete** — numbers, names, dates, examples instead of vague claims.
3. **Have a voice** — use first person where appropriate, state preferences, show reactions.
4. **Cut the neutrality** — humans have opinions; if the piece should take a position, take it.
5. **Earn your emphasis** — don't *tell* the reader something is interesting; make it interesting.

## Formatting discipline
- Em dashes: avoid; use commas, periods, or parentheses.
- Bold: at most one bolded phrase per section, or none. If it matters, restructure the sentence to lead with it.
- Headings: sentence case, and only when they tell the reader something specific. Don't put 5 headers in 300 words.
- Lists: only for genuinely list-like content (steps, parameters, comparisons). Convert bullet-heavy sections to prose.

## A note on over-correction
Applying every rule at maximum strictness produces *new* uniformity — the very thing you're trying to avoid. Keep natural disfluency, idiosyncratic word choices, and uneven pacing. The goal is writing that sounds like a specific person wrote it, not writing that has been scrubbed clean.

## Anthropic's own framing (for prompting Claude to write well)
- Be explicit and specific about audience, length, tone, and format up front — vague instructions produce generic output.
- Give positive and negative examples of the style you want.
- Add an uncertainty rule ("if unsure, say so") and ask for citations on factual claims; Claude responds well to explicit "don't guess" instructions.
- For long-document tasks, ask the model to quote the relevant parts first, then write — it cuts through noise.
  (See https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices and Anthropic's interactive tutorial: https://github.com/anthropics/prompt-eng-interactive-tutorial)
