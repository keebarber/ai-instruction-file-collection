# Words & phrases to avoid — quick reference

> A distilled cheat-sheet pulling together the most reliable AI "tells" from several sources, for pasting into a CLAUDE.md / AGENTS.md / style guide.
> Primary sources: conorbronsdon/avoid-ai-writing (https://github.com/conorbronsdon/avoid-ai-writing), Wikipedia "Signs of AI writing" (https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing), Pangram Labs detection research, brandonwise/humanizer.
> For the full, authoritative rule set with tiers, context profiles, and rewrite logic, see `avoid-ai-writing.SKILL.md` in this folder.

## The short list (drop into a style rule)

> Avoid these words and phrases. They are the strongest signals of machine-generated text.
> delve, leverage, utilize, harness, robust, seamless, streamline, empower, foster, elevate, unleash, bolster, facilitate, navigate (metaphor), embark, showcase, underscore, spearhead, revolutionize, transformative, game-changer, cutting-edge, state-of-the-art, best-in-class, paradigm, paradigm-shift, pivotal, cornerstone, landscape (metaphor), realm, tapestry, ecosystem (metaphor), synergy, interplay, holistic, actionable, impactful, comprehensive, meticulous, nuanced, multifaceted, myriad, plethora, vibrant, thriving, bustling, nestled, ever-evolving, testament to, watershed moment.

## Words by tier (from avoid-ai-writing)

**Tier 1 — always replace:** delve, landscape (metaphor), tapestry, realm, paradigm, embark, beacon, testament to, robust, comprehensive, cutting-edge, leverage, pivotal, underscores, meticulous, seamless, game-changer, utilize, watershed moment, nestled, vibrant, thriving, showcasing, deep dive / dive into, unpack, bustling, intricate / intricacies, complexities, ever-evolving, enduring, daunting, holistic, actionable, impactful, learnings, thought leader, best practices, at its core, synergy, interplay, in order to (→ to), due to the fact that (→ because), serves as (→ is), features/boasts/presents (→ has/is), commence, ascertain, endeavor, keen, symphony, embrace (metaphor).

**Tier 2 — flag when 2+ in a paragraph:** harness, navigate, foster, elevate, unleash, streamline, empower, bolster, spearhead, resonate, revolutionize, facilitate, underpin, nuanced, crucial, multifaceted, ecosystem, myriad, plethora, encompass, catalyze, reimagine, galvanize, augment, cultivate, illuminate, elucidate, juxtapose, paradigm-shifting, transformative, cornerstone, paramount, poised, burgeoning, nascent, quintessential, overarching, underpinning.

**Tier 3 — flag only at high density:** significant, innovative, effective, dynamic, scalable, compelling, unprecedented, exceptional, remarkable, sophisticated, instrumental, world-class / state-of-the-art / best-in-class.

## Sentence structures to ban
- **Negative parallelism:** "It's not just X — it's Y." / "This isn't about X, it's about Y." / "It wasn't X, it was Y." — rewrite as a direct positive claim.
- **"X is more than just Y; it's Z."**
- **"This is where X comes in."**
- **Rule of three everywhere:** "fast, reliable, and scalable" — vary your groupings.
- **Rhetorical-question openers:** "But what does this mean for you?" / "So why does this matter?" — just say it.
- **False concession:** "While X is impressive, Y remains a challenge." — make it specific or pick a side.
- **Hedge stacking:** "could potentially," "may eventually unlock."

## Opening/closing filler to cut
- Openers: "In today's fast-paced world…", "In an era where…", "As we navigate the complexities of…", "Let's dive in.", "In this article, we'll explore…"
- Closers: "In conclusion…", "The future looks bright.", "Only time will tell.", "One thing is certain.", "As we move forward."

## Transition / connective filler
Moreover, Furthermore, Additionally, Notably, Importantly, It's worth noting that, When it comes to, At the end of the day, That being said.

## Chatbot / assistant artifacts (in published writing)
"Certainly!", "Absolutely!", "Great question!", "I hope this helps!", "Feel free to reach out", "Let me know if you need anything else", "You're absolutely right!", "As an AI…", "As of my last update", "I don't have access to real-time data."

## Formatting tells
- Em dashes (— or --) used heavily. Target ~0; hard cap ~1 per 1,000 words.
- Bold sprinkled on phrases throughout.
- Emoji in headers (`## 🚀 Overview`).
- Bullet lists where prose would do; inline-header bullets ("**Speed:** Speed improved…").
- Title Case On Every Heading.
- 6+ hashtags stacked at the end of a social post.

## The deeper signal: structure, not vocabulary
Swapping flagged words is not enough. The #1 detection signal is **structural uniformity** — every sentence 15–25 words, every paragraph the same length, metronomic rhythm, relentless neutrality, no first-person voice. Fix rhythm and specificity, not just vocabulary. And don't over-polish: sanding away every irregularity pushes writing *toward* the AI statistical profile.
