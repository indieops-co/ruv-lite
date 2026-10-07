# Glossary

Plain meanings for the words that come up. Use the meaning the first time a term appears in an answer; in
Explain mode, always. Keep the wording, or something just as plain. *In rUv* notes where a term shows up in
the ecosystem.

## Agents and orchestration

**Agent.** An AI model that can take actions (read files, run tools, call other services) in a loop until
a task is done, not just answer once.

**Subagent.** A helper agent that the main agent hands a piece of work to, with its own fresh context.
Claude Code has these built in.

**Multi-agent / swarm.** A coordinated group of specialized agents working on one job: some in parallel,
some checking others. *In rUv:* Ruflo's core idea. "Hive-mind" is Ruflo's name for one coordination style.

**Crew.** ruv lite's word for a small, fixed team of agents with named roles (researcher, fact-checker,
skeptic, writer). Smaller and more predictable than a swarm.

**Orchestration.** Deciding which agent does what, in what order, and how their results come back together.

**Workflow.** A fixed sequence of agent steps you can run again, like a recipe.

**Harness.** Everything wrapped around a model to make it a useful agent for a job: its instructions,
tools, permissions, memory and settings. *In rUv:* MetaHarness generates one per repository.

**Model routing.** Sending each task to the cheapest model that can do it well: small edits to a small model,
hard reasoning to a large one. *In rUv:* Ruflo's "three-tier routing" recommends a tier per task; savings
figures are claims to measure.

**Inference.** One run of a model producing an answer. It's what you pay for: more agents usually means more
inference.

**Tokens.** The units models read and write, roughly three-quarters of a word. Cost and context limits are
counted in tokens.

**Context window.** How much text a model can consider at once. When it fills up, older details drop out.

## Claude Code pieces

**Skill.** A folder of instructions (and sometimes scripts) that Claude loads when a task matches. ruv lite
is one.

**Plugin.** A bundle installed into Claude Code that can add skills, slash commands, agents, hooks and MCP
servers in one go. *In rUv:* Ruflo ships around forty-six of them.

**Marketplace.** A list of plugins you add to Claude Code, then install from. Usually a GitHub repo.

**Scope (user / project / local).** Where a plugin or setting applies. *User* means every project on your
computer; *project* means this project, shared through its repo; *local* means this project, on this
computer only. ruv lite prefers project.

**Hook.** A script Claude Code runs automatically at a set moment (before a tool runs, when a session
starts). Hooks can add text to the conversation or block actions.

**MCP (Model Context Protocol).** A standard way to plug tools and data sources into an AI assistant.

**MCP server.** A small program that offers tools to the assistant over MCP, such as "search memory" or
"store a vector".

**Daemon / background process.** A program that keeps running on your computer after you close the chat.
*In rUv:* Ruflo's daemon is off unless you start it.

**`CLAUDE.md`.** A file of standing instructions Claude Code reads at the start of every session in a project.
A global one in `~/.claude/` applies to every project.

## Memory and search

**Embedding.** A list of numbers that captures what a piece of text means, so similar meanings have similar
numbers.

**Vector.** In this context, the same as an embedding: a list of numbers representing meaning.

**Vector database.** A way to store information and retrieve it by meaning rather than by exact words.
*In rUv:* RuVector.

**Semantic search.** Searching by meaning: "cheap flights" finds "low-cost airfare".

**RAG (retrieval-augmented generation).** Looking up relevant documents first, then giving them to the
model so its answer is based on them.

**HNSW (Hierarchical Navigable Small World).** A fast way to find similar items in a large collection of
embeddings, by hopping through a layered map instead of checking everything.

**Nearest-neighbour search (ANN).** Finding the items most similar to a query. "Approximate" (the A in ANN)
trades a little accuracy for a lot of speed.

**Recall (recall@10).** Of the truly best matches, how many the search actually returned. recall@10 means
"in the top ten".

**Metadata filter.** Narrowing a search by ordinary fields (date, customer, type) as well as meaning.

**Quantization.** Compressing embeddings to use less memory, at a small cost in accuracy.

**pgvector.** An extension that adds vector search to PostgreSQL. Offered by almost every managed Postgres
host; the usual default.

**sqlite-vec.** The same idea for SQLite: vector search inside a single local database file.

**Knowledge graph / graph database.** Storing things and the relationships between them ("Alice manages
Bob"), so you can follow connections.

**GNN (graph neural network).** A model that learns from connections in a graph. *In rUv:* RuVector uses one
for optional re-ranking, which it calls a research feature.

**Persistent memory.** Information an agent can retrieve in a later session, after the chat that created it
has ended.

**Cross-session learning.** An agent doing better next time because outcomes from earlier sessions were
recorded and used. It needs a feedback signal, such as "this worked" or "this didn't".

**Reflexion.** A pattern where an agent writes down what it tried, how it went, and a critique, so later
attempts can use the lesson. *In rUv:* one of AgentDB's memory types.

**Skill library (agent memory).** Saved, reusable procedures an agent learned or was given. Not the same as
a Claude Code skill.

## rUv names

**Ruflo.** rUv's agent orchestration add-on for Claude Code and Codex. Formerly claude-flow.

**RuVector.** rUv's embedded vector and graph store, written in Rust.

**AgentDB.** rUv's agent memory library: past tasks, outcomes and skills in a local file.

**RVF (RuVector Format).** A single file that holds an agent's memory, its search index and a tamper-evident
history, so the memory can move between programs. Its docs call it a "cognitive container". The spec is a
research draft.

**RVForge.** Tools for building and checking RVF bundles.

**MetaHarness.** rUv's generator that makes a stand-alone agent package for a repository.

**RuView.** rUv's research project for sensing presence and movement from WiFi signals, without cameras.
Formerly WiFi-DensePose.

**SPARC.** Specification, Pseudocode, Architecture, Refinement, Completion: a five-phase way to build with
agents, with a check between phases.

**agentic-flow.** rUv's lower-level toolkit for agent workflows and model switching; Ruflo builds on it.

**SONA.** RuVector's learning component. It adjusts only from recorded feedback; searching alone teaches it nothing.

**Agent Booster.** Ruflo's local tool for simple code edits without calling a model. Its speed figures are
claims.

**Cognitum.** A company and hardware platform linked from rUv's projects (cognitum.one). RuVector's README says it powers Cognitum.

**RuvNet Brain.** A third-party plugin (not rUv's) that searches rUv source code and advocates rUv
capabilities inside Claude Code.

## Software basics

**Rust.** A fast, safe programming language. Many rUv projects are written in it; you usually don't need
it installed to use their npm packages.

**Crate.** A Rust package, published on crates.io.

**npm / npx.** Node.js's package manager. `npx` runs a package without installing it permanently.

**Node.js.** The program that runs JavaScript outside a browser. Most rUv tools need version 18 or 20+.

**WASM (WebAssembly).** A way to run compiled code (often Rust) inside a browser or Node at near-native speed.

**CLI.** A command-line tool: something you run by typing a command.

**Adapter / provider interface.** A thin layer in your code that hides which tool does a job, so you can swap
pgvector for RuVector (or back) by changing one place.

**Semver / pre-1.0.** Version numbers like 2.4.1. Before 1.0, a project is signalling that anything may
still change between releases.

**Alpha / beta.** Early releases: alpha means expect breakage; beta means mostly working, still changing.

**Benchmark.** A measured test of speed or quality. A project's own benchmark is a claim about its chosen
workload, not a promise about yours.
