# Advise: the consultation shape

Short sections with bold labels, no headings bigger than bold text. Aim for 150–400 words before the card.
Leave out a section that has nothing to say.

**Goal.** One line: the outcome, in the user's terms. `Receive review → draft reply → owner approves → publish.`

**What you have.** The current or planned stack, as you read it from the message or the project. Mark
anything you assumed: `Next.js + Supabase + a model API (assumed from package.json)`.

**The boring answer.** The simplest established way to get the outcome, and whether it's enough. This comes
*before* any rUv technology is mentioned.

**Where rUv could fit.** One line per candidate you shortlisted, strongest first:

`<Name> — <None | Low | Medium | Strong> now<, <level> later>. <The concrete reason, tied to the request.>`

Only technologies with a matching `use_when` signal appear here. If none matched, say so in one sentence and
skip to the card.

**The crew** *(only when the call involves several agents)*. A small table: role, why it exists, whether it
needs a strong model or can use a cheap, local or deterministic one. Then one sentence on where a single
strong model would do better. See "Cost guardrails" in `references/decision-policy.md`.

**What it would cost you** *(only for USE IT or a close CONSIDER LATER)*. Two to four bullets: what gets
installed, what it creates in the project, what you'd have to learn, how you'd back out.

Then THE CALL (`call-card.md`).
