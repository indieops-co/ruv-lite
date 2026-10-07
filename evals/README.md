# ruv lite evals

40 Advise-mode scenarios that check whether ruv lite recommends rUv technology only when it should.

| Category | Count | What a pass looks like |
|---|---|---|
| `ruflo-fit` | 4 | USE IT Ruflo: needs native Claude Code doesn't cover (shared memory, coordinated code changes, cost tracking), or already on Ruflo, or learning in a sandbox |
| `native-first` | 3 | CONSIDER LATER or SKIP IT: parallel, repeating work that built-in subagents and a skill already handle |
| `memory-fit` | 4 | USE IT or CONSIDER LATER for RuVector, AgentDB, MetaHarness or RuView, where a real requirement exists |
| `future-fit` | 7 | CONSIDER LATER with a concrete trigger (SKIP IT also passes) |
| `no-fit` | 10 | SKIP IT |
| `trap` | 8 | SKIP IT despite the pull of a benchmark, a buzzword or FOMO |
| `ambiguous` | 4 | Either of two defensible calls |

## The metric that matters

**Unnecessary rUv Recommendation Rate (URR):** of the scenarios where USE IT is wrong (32 of the 40), how
often the skill said USE IT anyway. Target **under 10%**, eventually under 5%. It matters more than how often
rUv gets recommended.

Also reported: missed fits (expected USE IT, got SKIP IT), overall pass rate, and card hygiene (a complete
THE CALL card in label order, a well-formed Evidence line, the unofficial line).

## Running

```bash
python3 scripts/run_evals.py                      # all 40, snapshot only
python3 scripts/run_evals.py --only s01,s29       # a few
python3 scripts/run_evals.py --category trap      # one category
python3 scripts/run_evals.py --web                # allow live source checks
python3 scripts/run_evals.py --natural            # don't prefix /ruv-lite: tests triggering too
python3 scripts/run_evals.py --score evals/runs/<run>   # re-score without calling Claude
```

Each scenario runs in a throwaway project with the skill copied into `.claude/skills/ruv-lite/`, through
`claude -p` with read-only tools (no Bash, Edit or Write). Set `CLAUDE_BIN` if `claude` isn't on your PATH.
Each scenario is capped at $3 by default (`--budget`); `--model sonnet` runs at roughly $0.30 a scenario. Answers and the report land in `evals/runs/<timestamp>/`,
which git ignores.

## Writing a scenario

Write it the way a real user would ask, with the details that should decide the call (scale, stack,
constraints). Set `expected.decision` to the best call, `acceptable` to every call you'd accept, and
`technology` to the card id, or `any` / `none`. A scenario with no USE IT in `acceptable` counts toward URR, so
keep the negatives plentiful. When a card's maturity changes, revisit the scenarios that cite it.
