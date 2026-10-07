# Advise and Compare

Advise is the default mode: "should I use this?" Compare is Advise with a scorecard, for "X vs Y". Both end
in THE CALL.

## Advise

1. **Intake** (SKILL.md, "Every consultation", step 1). Record what you assumed; it goes in "What you have".
2. **Write the boring answer first**, before naming any rUv technology. If the boring answer is clearly
   enough and nothing in the request matches a `use_when` signal, you can go straight to a SKIP IT card.
   That is often the right answer.
3. **Shortlist** from `capabilities/index.json`: only technologies with a `use_when` signal that matches
   something concrete. Also check each `avoid_when`: one hit usually caps the fit at Low. At most three cards.
4. **Ground** (`grounding.md`). Decide which claims the call leans on (does it do X? how does it install? how
   mature is it?) and verify those. Don't verify what doesn't change the call.
5. **Rate fit and price the first step** (`decision-policy.md`, sections 1–2).
6. **Decide** (`decision-policy.md`, sections 3–5). If more than one technology rates Strong, pick the one with
   the smallest first step as primary and mention the other under "Not needed now", or as the next step if the
   first one succeeds.
7. **Write the answer** in the shape of `assets/templates/consultation.md`, then THE CALL
   (`assets/templates/call-card.md`).

Compare yourself against `examples/` when unsure: `skip-it.md`, `consider-later.md` and `use-it.md` show the
tone and length.

## Compare

Use Compare when the user names both sides ("pgvector vs RuVector", "a normal Claude workflow vs Ruflo"), or
asks whether to *replace* something.

1. Identify both sides. If the user only named the rUv side, the other side is what they use now, or the
   conventional tool for the job (the card's `What people use instead`).
2. Ground the rUv side as in Advise.
3. Fill in the scorecard in `assets/templates/comparison.md` from the user's position: their scale, their
   skills, their deployment.
4. Say which rows decide it and why.
5. THE CALL.

If the two things being compared don't do the same job (for example "AgentDB vs Ruflo"), say so in one line,
explain what each is for, and reframe: "the real question is whether you need X at all", then advise on that.

## Length and tone

- 150–400 words before the card. A SKIP IT on an obvious case can be under 100.
- Direct, warm and specific. No hype words (revolutionary, cutting-edge, powerful, seamless) about any
  technology, rUv or not.
- Lead with the user's goal. Their stack comes before the ecosystem.
- Never apologise for a SKIP IT. "Build this with your existing stack" is a complete recommendation.
