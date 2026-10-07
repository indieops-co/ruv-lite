# THE CALL

The last thing in every Advise or Compare answer, and in any answer that recommends something. Render it as
a plain fenced block (no language tag) so it reads as one card in a terminal and in chat. Keep the labels and
their order exactly as below. Leave out a line marked *(only …)* when it doesn't apply, and never leave a
`<…>` placeholder in the output.

```
THE CALL
Recommendation:   <SKIP IT | CONSIDER LATER | USE IT>
rUv technology:   <Name, plus "(experimental)", "(alpha)" or "(pre-1.0)" when it is, or "none needed">
Keep using now:   <the baseline: what they have or the simplest established option>
Why:              <one or two sentences tied to a requirement the user stated>
Start with:       <the smallest reversible first step>                  (only USE IT)
Measure:          <what the trial must show before going further>       (only USE IT)
Reconsider when:  <an observable trigger, never "as you grow">          (only CONSIDER LATER and SKIP IT)
Not needed now:   <other technologies considered, a few words each>     (only when others were considered)
Difficulty:       <Low | Medium | High | Very high>, from the complexity budget
Migration risk:   <Low | Medium | High>, plus the condition that keeps it low
Complexity avoided: <Low | Medium | High | Very high>                   (only SKIP IT)
Confidence:       <High | Medium | Low>
Evidence:         <Checked live YYYY-MM-DD | Bundled snapshot YYYY-MM-DD, verify before production use>
```

Directly under the card, one line in italics:

*ruv lite is an unofficial guide, not affiliated with rUv or the rUv projects.*

Then the sources the call relied on, as links, one line each. Two to four is normal; zero is fine for a
SKIP IT that rests only on the user's own requirements.

## Filling it in

- **Recommendation.** Exactly one of the three phrases, in capitals. USE IT may carry a short qualifier
  after an em dash, e.g. `USE IT — start with a small Ruflo crew`.
- **rUv technology.** One technology, the one the call is about. For SKIP IT with nothing worth naming, write
  `none needed`.
- **Why.** Name the requirement and the advantage (or the missing one). "Your 2,000 records already search
  fast in pgvector; RuVector would add a service without solving a current problem", not "Simpler is better".
- **Start with.** One concrete action that can be undone: a plugin install in project scope, a spike branch,
  an adapter with one alternative implementation behind it. Never "initialize the full environment".
- **Reconsider when.** Something the user could notice: a number, an event, a new requirement. Two triggers
  at most.
- **Difficulty.** The budget level of the *first step* (`references/decision-policy.md`).
- **Migration risk.** How hard it would be to back out, and the condition that keeps it there ("Low if
  retrieval stays behind a provider interface").
- **Confidence.** High only when the capability claims were checked live or the call rests on the user's own
  requirements. Medium when you relied on a snapshot under 90 days old. Low when the snapshot is older, or a
  key fact is unknown.
