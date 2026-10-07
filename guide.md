# ruv lite

## Start here

Unzip the `ruv-lite` folder into `~/.claude/skills/` (or upload the zip on claude.ai under **Settings → Capabilities → Skills**), turn web search on if you can, and describe what you're building the way you'd describe it to a friend:

```
I'm making a SaaS that takes customer reviews, drafts replies and lets
business owners approve them. Should I be using any of the rUv stuff?
```

You don't have to name the skill. "Do I need Ruflo for this?", "pgvector or RuVector?" and "what is RVF, in plain English?" all start it, and `/ruv-lite` works too. A minute later you get a short consultation that ends in one of three calls, with the reason, the cost in complexity, and what would change its mind.

---

## The three calls

| | |
|---|---|
| **USE IT** | A requirement you have *today* maps to what the rUv tool is for, your current setup handles it badly, and there's a small first step you can undo. It always comes with the smallest way to start and what to measure. |
| **CONSIDER LATER** | It could matter, but something isn't true yet. You get a trigger you'd actually notice ("search has to work offline", "agents need to share memory across runs"), never "as you grow". |
| **SKIP IT** | What you have, or the simplest established option, does the job. This is the most common answer, and it's a successful one. |

People often arrive hoping for permission to use the exciting thing. ruv lite starts from your goal instead, and has explicit permission to say "don't use any of it".

---

## Reading THE CALL

Every recommendation ends with the same card:

```
THE CALL
Recommendation:   CONSIDER LATER
rUv technology:   RuVector (pre-1.0)
Keep using now:   PostgreSQL + pgvector
Why:              Your retrieval works at your size, and RuVector's main
                  advantage (search that runs locally or offline) isn't
                  something you need today.
Reconsider when:  Search has to work offline or inside a desktop or browser
                  app, or agents need their own local memory.
Difficulty:       Medium
Migration risk:   Low if retrieval sits behind a RetrievalProvider interface
Confidence:       High
Evidence:         Bundled snapshot 2026-10-07, verify before production use
```

- **Keep using now** is the plain option it compared against. It's always named, even on a USE IT.
- **Difficulty** rates the *first step*, not the whole adoption: **Low** means you can try it without changing your architecture, **Medium** means a new package or a small adapter in your code, **High** changes how your app runs or stores data, and **Very high** brings in several new systems at once.
- **Migration risk** is how hard it would be to back out, and what keeps it low.
- **Evidence** says whether the facts were checked live today or came from the bundled snapshot, and how old that is.

---

## Why it says no so often

ruv lite works to five rules, in this order:

1. **Goals before tools.** It starts from what you're trying to do, never from "how could Ruflo do this?"
2. **Boring is allowed to win.** If the plain option is good enough with much less complexity, it wins, even when the rUv tool is technically better. "Boring" means what already works, or one small established step, not a do-it-yourself build of several pieces.
3. **rUv needs a reason.** A recommendation names the specific advantage (running offline, keeping data on your machine, agents sharing memory, coordinating many agents) and the requirement of yours that makes it matter. "It's written in Rust" isn't a reason.
4. **Complexity has a price.** Installing, learning, running, debugging and backing out all count.
5. **Current claims need current evidence.** The rUv projects change month to month, so nothing about them comes from memory alone.

Two more habits follow from those. **Claude Code comes first:** its built-in subagents already run work in parallel, so Ruflo has to add something they don't, such as shared memory across runs, coordinated code changes, or cost tracking, to get a USE IT. And **more agents aren't assumed cheaper:** any crew it suggests lists each agent's job, which ones need a strong model, and what to measure against a single-agent run.

---

## Five ways to ask

| Mode | Ask like | You get |
|---|---|---|
| **Advise** | "Should I use Ruflo for this?" · "I'm building…" | A short consultation and THE CALL |
| **Compare** | "pgvector vs RuVector for us?" | A nine-row scorecard from where you stand, and THE CALL |
| **Scout** | "Could anything in rUv help this repo?" | What fits now, later, or not at all |
| **Explain** | "What is AgentDB, simply?" | Seven short parts, ending with how to try it without committing |
| **Apply** | "OK, help me try it" | The smallest safe setup, one approved step at a time |

**Better input, better call:** say what you're trying to achieve, what you already run, and any hard limits (offline, privacy, budget, deadline). Inside a project folder it reads your manifests itself, so you don't have to describe your stack.

---

## The rUv ecosystem on one page

rUv publishes a large family of open-source projects. Most people only ever need to know these six, which head rUv's own "start here" list:

| Project | In plain words |
|---|---|
| **Ruflo** | An add-on for Claude Code that runs several agents together on one job, with shared memory and reusable workflows. Formerly claude-flow. You can take it one plugin at a time. |
| **RuVector** | A database that finds things by meaning, which runs inside your program with no server, written in Rust with Node.js and browser versions. |
| **AgentDB** | A local memory store for an agent's past tasks, outcomes and skills. Ruflo's memory runs on it. |
| **RVF** | A single file that carries an agent's memory and its history between programs. The format is still a research draft. |
| **MetaHarness** | A generator that turns a repository into a stand-alone, publishable agent package. |
| **RuView** | Research software that senses presence and movement from WiFi signals, without cameras. |

Many of these are young: alpha releases, pre-1.0 versions, specs marked as drafts. ruv lite says so every time it recommends one, and treats speed and savings figures that projects publish as claims to test, not facts.

Two things people often assume are rUv projects aren't: **RuvNet Brain** is an independent plugin by Stuart Kerr, and **ruv lite** itself is an unofficial IndieOps Skilllet.

---

## How it stays current

The skill carries a dated **capability card** for each major project: what it is, when it helps, when it doesn't, what people use instead, the lightest way to try it, what a full install changes, and its known problems. Every fact on a card cites its source.

When a call depends on something that changes fast (does it do this yet, how does it install, is the latest release still an alpha), ruv lite checks the project's own repository, release page or package registry, and the card says **Checked live**. Without web access it uses the cards, says **Bundled snapshot** with the date, caps its confidence, and tells you what to check before you adopt anything.

If you have RuvNet Brain or rUv's own discovery plugin installed, ruv lite can use their search for facts. It keeps its own rules for the decision.

---

## Trying something safely

Apply mode only starts when you ask for it. A USE IT isn't permission to install anything. When you do ask:

- **You see every step first:** the exact command, what it creates or changes, and how to undo it. Nothing runs without a yes.
- **Project scope by default.** Claude Code installs plugins for every project unless told otherwise, so ruv lite passes the project-scope flag explicitly.
- **Global changes are separate.** Anything outside your project gets its own step and its own yes. One example worth knowing: a full Ruflo initialization adds a block to your global Claude Code instructions by default. ruv lite always turns that off unless you ask for it.
- **The smallest path first.** A plugin or a library behind an interface in your code, never "initialize everything".
- **Your existing setup wins.** It won't delete or overwrite your configuration to make room, and it never asks for API keys in the chat.

---

## What it won't do

- **Recommend something because it exists.** Every rUv recommendation has to name its reason.
- **Pretend experimental is proven.** Alpha, pre-1.0 and research-draft labels are stated every time.
- **Install anything you didn't ask for**, or change anything outside your project without a separate yes.
- **Speak for rUv.** It's an independent guide: not made, endorsed or reviewed by rUv or any rUv project, and not a "lite" edition of any of them.

rUv, Ruflo, RuVector, AgentDB, RVF, MetaHarness, RuView and related names belong to their creators. RuvNet Brain belongs to its author.
