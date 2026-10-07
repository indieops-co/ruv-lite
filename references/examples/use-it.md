# Example: USE IT

**User:** We're a 3-person agency. Every Monday we run the same competitor-research crew for 8 clients. We
built it with Claude Code subagents and a skill, and it works, but: the agents can't see what each other or
last week's run found, so they re-research the same things; each of us runs it slightly differently; and our
token bill has doubled with no idea which step is eating it. It's internal, and we're fine with fast-moving
tools. Is this where Ruflo comes in?

---

**Goal.** Weekly competitor briefs for 8 clients: research only what's new, run the same way by all three of
you, and know where the spend goes.

**What you have.** Claude Code with built-in subagents and a shared skill, run by three people.

**The boring answer.** You're already on it, and it got you this far. The native fixes would be: write
findings to dated files per client and have each subagent read last week's first; put the skill in the repo
so everyone runs the same version; and add a usage log by hand. That covers some of it, but you'd be building
a memory index, a shared workflow and cost tracking yourselves, three separate projects.

**Where rUv could fit.**

- Ruflo — Strong now. You need three things native subagents don't do well, at once: memory several agents
  can search across weeks, one shared workflow, and per-step cost tracking. Ruflo ships each as a plugin.
- AgentDB — Medium, but only through Ruflo. Ruflo's memory runs on it, so you'd get it with the plugin rather
  than adopting it directly. It's an alpha; see the trial below.
- RuVector — Low. Your memory problem is "what did we find last week", not search at scale.

**The crew** (keep the one you have):

| Role | Why it exists | Model |
|---|---|---|
| Researcher × 2 per client batch | Fetch and summarise what changed | Mid-tier |
| Skeptic | Checks claims against the fetched pages | Strong |
| Synthesizer | Writes each client's brief | Strong |
| Change detector | Diffs against last week | Not an agent: a script |

Don't grow it in the trial. The point is to test memory, consistency and cost visibility, not more agents.

**What it would cost you.** Three plugins in this project only. `ruflo-core` registers Ruflo's MCP server and
ships hooks, which `claude plugin details` will show before you install. Ruflo releases almost daily, so pin
what works. Undo is three uninstall commands; your briefs stay ordinary files.

```
THE CALL
Recommendation:   USE IT — add three Ruflo plugins to the crew you already have
rUv technology:   Ruflo (plugins, not the full init; its memory runs on AgentDB, an alpha)
Keep using now:   Your Claude Code subagents and skill, with briefs in dated files
Why:              You need shared memory across agents and weeks, one workflow for three people, and per-step cost tracking all at once. Building those natively is three projects; Ruflo ships them as plugins.
Start with:       In project scope only: ruflo-core, ruflo-rag-memory and ruflo-cost-tracker. Run two Mondays for two clients. No full init, no daemon.
Measure:          Repeat research avoided (findings reused from last week), token spend per client against your current run, run-to-run consistency across the three of you, and whether memory recall is actually correct.
Not needed now:   RuVector (no search-at-scale problem), a full ruflo init (VERY HIGH, and it edits global config)
Difficulty:       Low
Migration risk:   Low: three plugin uninstalls, and your skill and briefs don't depend on Ruflo
Confidence:       Medium
Evidence:         Bundled snapshot 2026-10-07, verify before production use
```

*ruv lite is an unofficial guide, not affiliated with rUv or the rUv projects.*

Sources: [Ruflo README](https://github.com/ruvnet/ruflo) · [Ruflo plugin list](https://github.com/ruvnet/ruflo/blob/main/.claude-plugin/marketplace.json) · [AgentDB on npm](https://www.npmjs.com/package/agentdb)

---

Why this is a good answer: native Claude Code was the baseline, and Ruflo won only because three needs stacked
up that native features don't cover. The trial keeps the crew the same, tests the things Ruflo is supposed to
add, and checks the alpha memory layer instead of trusting it. Confidence is Medium because the plugin details
came from the snapshot; a live check would raise it.

The same question from a solo user who just wanted the 40 lookups to run in parallel gets CONSIDER LATER:
native subagents and a skill do that, with nothing to install.
