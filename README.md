# ruv lite

**Tell it what you're building. It tells you which rUv tools are worth it, and which aren't.**

*An IndieOps Skilllet — a copyable skill folder that does one job properly.* · [indieops.co](https://indieops.co)

**Runs on** macOS · Windows · Linux  
**Works with** Claude  
**Needs** Web search turned on in Claude, for live source checks (optional)

rUv's open-source ecosystem is huge: Ruflo for agent swarms, RuVector for vector and graph memory, AgentDB,
RVF, MetaHarness, and dozens more. Most of the time the first question isn't "how do I use it?" but "do I
need any of it?" ruv lite answers that one. It knows the ecosystem well, and it has explicit permission to
tell you **"don't use any of it."**

Give it an idea, a PRD, a repo or a client problem. It writes down the simplest conventional way to build
it first, then weighs the most relevant rUv option against that, and ends with one of three calls:
**USE IT**, **CONSIDER LATER** or **SKIP IT**. A skip is a successful answer.

*Unofficial.* ruv lite isn't made, endorsed or reviewed by rUv or any rUv project, and it isn't a "lite"
edition of Ruflo or anything else.

## What you get

| Mode | Ask like | You get |
|---|---|---|
| **Advise** (default) | "Should I use Ruflo for this?" · "I'm building…" | A short consultation and THE CALL |
| **Compare** | "pgvector vs RuVector for us?" | A nine-row scorecard from where you stand, and THE CALL |
| **Scout** | "Could anything in rUv help this repo?" | What fits now, later, or not at all |
| **Explain** | "What is RVF, in plain English?" | Seven short parts: what it is, what you'd use instead, when you don't need it, how to try it without committing |
| **Apply** | "OK, help me try it" | The smallest safe setup, one approved step at a time |

Every recommendation ends with the same card:

```
THE CALL
Recommendation:   CONSIDER LATER
rUv technology:   RuVector (pre-1.0)
Keep using now:   PostgreSQL + pgvector
Why:              Your retrieval works at your size, and RuVector's main advantage (search that runs locally or offline) isn't something you need today.
Reconsider when:  Search has to work offline or inside a desktop or browser app, or agents need their own local memory outside the database.
Difficulty:       Medium
Migration risk:   Low if retrieval sits behind a RetrievalProvider interface
Confidence:       High
Evidence:         Bundled snapshot 2026-10-07, verify before production use
```

## Install

**Claude Code** (personal, available in every project):
```bash
unzip IndieOps-Skilllet-2026-22-ruvlite-*.zip -d ~/.claude/skills/
```
For a single project, unzip into `.claude/skills/` inside that project instead. Restart Claude Code, then
ask "what skills do you have?" and check that `ruv-lite` is listed.

**claude.ai:** go to **Settings → Capabilities** and upload the zip under **Skills**. Turn on web search in
your chat so it can check current sources.

## Use it

Describe what you're building. You don't have to name the skill, but `/ruv-lite` works too:

> I'm making a SaaS that drafts replies to customer reviews for business owners to approve. Should I be using any of the rUv stuff?

> Every Monday I research 40 competitors and write briefs in Claude Code. Is this a Ruflo thing?

> Compare pgvector and RuVector. We have 2,000 articles and search works fine.

> Scout this repo for anything rUv could genuinely help with.

> Explain AgentDB like I'm not a database person.

**Better input, better call:** say what you're trying to achieve, what you already run, and any hard
constraints (offline, privacy, budget, deadline). Inside a project folder it reads your manifests itself.

## How it stays honest

- **The boring answer comes first.** Every consultation writes down the simplest conventional solution
  before any rUv technology is mentioned.
- **rUv needs a reason.** A recommendation names the specific advantage and the requirement that makes it
  matter here. "It's written in Rust" isn't one.
- **Complexity has a price.** Each call rates the first step Low, Medium, High or Very high, and beginners
  aren't sent past Medium unless the problem demands it.
- **Current claims need current evidence.** rUv projects ship weekly. Capability cards are dated, each claim
  cites its source, and when a call depends on a fact it checks the live repo, registry or release page. Without
  web access it says it's using the bundled snapshot, and how old it is.
- **Claims stay claims.** Benchmark and savings figures that projects publish are reported as claims to test,
  never as facts. Alpha and pre-1.0 releases are labelled every time.
- **Multi-agent isn't assumed cheaper.** Any crew it suggests lists each agent's job, which ones need a strong
  model, and what to measure against a single-agent run.
- **Native Claude Code comes first.** Built-in subagents already run work in parallel, so Ruflo has to add
  something they don't (shared memory, coordinated code changes, cost tracking) to get a USE IT.

## What it won't do

- Install anything, initialize Ruflo, register MCP servers or add hooks unless you've asked it to set
  something up, and even then only after showing you the exact command, what it changes and how to undo it.
- Touch your global configuration (`~/.claude/`, global packages, shell profiles) without a separate yes for
  that specific change. (Worth knowing: a full `ruflo init` appends to your global `~/.claude/CLAUDE.md`
  by default; ruv lite always passes `--no-global` unless you say otherwise.)
- Delete or overwrite your existing configuration to make room for rUv's.
- Ask for, print or move API keys.

## Without web search

It still works. The bundled capability cards (snapshot **2026-10-07**) cover Ruflo, RuVector, AgentDB, RVF,
MetaHarness, RuView, SPARC, agentic-flow and RuvNet Brain, plus a map of the rest of the ecosystem. The card
says `Bundled snapshot`, confidence is capped at Medium, and it tells you what to check before adopting
anything.

## Relationship to RuvNet Brain

[RuvNet Brain](https://github.com/stuinfla/ruvnet-brain) is an independent plugin by Stuart Kerr that gives
Claude deep, source-level search over the rUv ecosystem. Its stated purpose is proactive capability advocacy:
a "CTO on your shoulder" that volunteers what you could turn on. ruv lite asks the question before that one:
should rUv be involved here at all?

They're complementary. If RuvNet Brain is installed, ruv lite can use its search for facts while keeping its
own decision rules. It never installs it for you. Once you've decided to build on the rUv stack, graduating
to RuvNet Brain, or to Ruflo's own tooling, makes sense.

## Better with the rest

If you have the free **IndieOps Shared Profiles** installed (one folder of notes on your computer, your
profile and one per business, that every IndieOps Skilllet reads), ruv lite reads your usual stack and
comfort level from there instead of asking. When you consult for a client business, it writes back each call
and its "reconsider when" trigger, so the next time you ask about that client it can tell you whether a
trigger has been met. Without it everything stays in the chat and works the same. Never required.

## What's inside

```
ruv-lite-cover.html      start here
guide.html               the guide: the three calls, reading THE CALL, the ecosystem on one page
SKILL.md                 the decision policy Claude follows on every answer
references/
  advise.md scout.md explain.md apply.md     one file per mode, loaded only when needed
  decision-policy.md     the rubric, complexity budget and cost guardrails
  grounding.md           how claims get checked, and the snapshot rule
  capabilities/          one dated card per technology, and the index used to shortlist
  sources.json           every canonical source the cards cite
  ecosystem-map.md       the rest of the rUv ecosystem: what exists, what's quiet, what's been renamed
  glossary.md            plain-English meanings for every term it uses
  examples/              worked use-it, consider-later and skip-it consultations
assets/templates/        the shape of every answer, THE CALL first
evals/scenarios.json     40 scenarios, 32 of them cases where recommending rUv would be wrong
scripts/                 validate.py (consistency checks) and run_evals.py (scores the calls)
```

## Names and trademarks

rUv, Ruflo, RuVector, AgentDB, RVF, MetaHarness, RuView and related project names belong to their creators
and projects. RuvNet Brain belongs to its author. ruv lite is an independent advisory layer: it isn't
affiliated with rUv, Cognitum or any project it describes, and its recommendations are its own.

## License

Copyright © 2026 IndieOps. All rights reserved.  
Licensed under the [IndieOps Free License v1.0](LICENSE). Free to use, even commercially; don't redistribute it.

---

**More Skilllets and plugins:** [indieops.co/skills-and-plugins](https://indieops.co/skills-and-plugins) · **Questions?** [support@indieops.co](mailto:support@indieops.co)
