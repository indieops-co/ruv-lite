# Decision policy

How a candidate becomes USE IT, CONSIDER LATER or SKIP IT. Read this before deciding any Advise or Compare
call.

## 1. Rate the fit

For each shortlisted technology, rate how well it fits **today**, then separately **later**:

| Fit | Means |
|---|---|
| **Strong** | A requirement the user has *now* maps directly to the technology's core purpose, and the baseline handles it badly. "The baseline" is what they run today plus at most one small step; a bespoke build of several pieces doesn't count as handling it. |
| **Medium** | A present requirement maps to it, but the baseline handles it acceptably, or the fit is partial. |
| **Low** | Some overlap, but nothing the baseline can't do. |
| **None** | No requirement it addresses. |

"Later" is the fit once a specific, observable condition becomes true. If you can't name the condition,
"later" is the same as today.

## 2. Price the first step: the complexity budget

Rate the **smallest step that would show the benefit**, not the full adoption:

| Level | Means | Typical rUv examples |
|---|---|---|
| **LOW** | Testable without meaningfully changing the architecture. Undo by deleting a folder or uninstalling one thing. | A project-scope Claude Code plugin; a sandbox folder; reading the docs quickstart |
| **MEDIUM** | A new package or service, or an adapter in the user's code. | Adding a library behind a provider interface; running a local server for a spike |
| **HIGH** | Changes the runtime architecture, the persistence model, the orchestration model or deployment. | Moving production retrieval or agent memory onto a new store; making a multi-agent workflow the product's core path |
| **VERY HIGH** | Several new subsystems at once, or the whole agent environment. | A full Ruflo initialization (agents, commands, MCP tools, hooks, background processes, generated config) |

**Beginner rule.** Unless the user shows they already run this kind of infrastructure, don't recommend a
HIGH or VERY HIGH first step unless their stated problem clearly needs it. Look for a smaller first step
first; there usually is one.

## 3. Decide

| Situation | Call |
|---|---|
| Fit Strong now, documented advantage, first step LOW or MEDIUM and reversible | **USE IT** |
| Fit Strong now, but the first step is HIGH+ for a beginner, or the component is experimental and the work is production or client-facing | **CONSIDER LATER**: name what would make it safe (a smaller path, a stable release, a sandbox result) |
| Fit Medium now, with a named trigger that would make it Strong | **CONSIDER LATER** |
| Fit Medium now and no credible trigger | **SKIP IT** |
| Fit Low or None | **SKIP IT** |
| The advantage is only inferred, never documented | At most **CONSIDER LATER**, and say what to verify |

Things that never lift a call on their own:

- **Strategic upside.** "You'll want this eventually" is a CONSIDER LATER trigger, not a USE IT reason.
- **Benchmarks.** A vendor's performance figure is a claim. Unless the user's bottleneck *is* that operation,
  it doesn't matter how fast it is.
- **Breadth.** Winning more scorecard rows doesn't win the call. The rows tied to the user's requirement do.

## 4. Special cases

- **The goal is learning.** "I want to learn Ruflo" or "I'm curious about RuVector" is a real goal. The call
  can be USE IT for a **sandbox** (a separate folder or branch), while the product itself stays SKIP IT or
  CONSIDER LATER. Say which is which.
- **Client or production work.** Raise the bar on maturity. An experimental or pre-1.0 component in a client
  deliverable is CONSIDER LATER unless it sits behind an adapter with a proven fallback.
- **Already installed.** If the project already uses a rUv component, judge whether it earns its keep, and
  flag overlap (pgvector and AgentDB both holding the same embeddings, two memory systems). Removing
  something that works is also a change with a cost; say so.
- **They asked for a specific tool.** "Set up RuVector for me" is still a question you may answer with "here's
  why you might not want to, and here's how if you still do". Give the call, then respect their decision.
  Apply mode is theirs to enter.

## 5. The baseline for multi-agent work is Claude Code itself

Claude Code already runs work in parallel (built-in subagents), repeats a routine (skills), and keeps
deterministic steps out of the model (scripts). So when the question is "do I need Ruflo?", the boring answer
is **native Claude Code**, not a single plain session. Parallel, independent, repeating work is not by itself
a reason for Ruflo.

Ruflo earns USE IT when it adds something native features don't do well, for example:

- **Shared memory** that several agents search, across runs and weeks.
- **Many agents changing code at once** without colliding (worktree isolation), with a shared record of
  decisions.
- **Model routing or cost tracking at volume**, where knowing and steering per-step spend matters.
- **The user already runs Ruflo**, and one more Ruflo plugin fixes a pain they have now.
- **The goal is learning orchestration**, in a sandbox.

**Price the native version honestly.** "Boring" means what already works, or one small established step.
It doesn't mean anything that could in principle be built. If matching what the user asked for natively
means building and maintaining several pieces yourself (a run script, per-step token logging, a findings
index, conventions three people must follow), that build *is* the baseline's complexity: rate it on the same
budget as the rUv option, and count the maintenance.

When two or more of these stack up, assembling them natively becomes the complex option, and Ruflo's
plugins can be the simpler path. Say that explicitly when it's the reason. When only parallelism or
repetition is in play, recommend native subagents and a skill, and make Ruflo CONSIDER LATER with the
trigger that would change it.

## 6. Cost guardrails for multi-agent work

Never imply that several agents are cheaper or better by default. Each agent re-reads context and spends
its own inference. For any call that involves more than one agent, show:

- **How many agents**, and why each one exists. Start a first trial at five or fewer.
- **Which need a strong model** and which can run on a cheap, local or deterministic tool (fetching pages,
  diffing text, counting, formatting).
- **Where one strong model would do better**: tightly coupled reasoning, short tasks, anything where
  hand-offs lose context.
- **What to measure** in the trial: wall-clock time, tokens and total cost, source quality, missed findings,
  and final quality against a single-agent run of the same task.

Model routing and savings figures that rUv projects publish are hypotheses to measure in the user's own
workload, never a promised percentage.

## 7. Prefer adapters

When a rUv component is recommended for something fast-moving or experimental, put it behind an interface
so it can be swapped out:

```
RetrievalProvider   →  PgVectorProvider  | RuVectorProvider
MemoryProvider      →  PostgresMemory    | AgentDBMemory
AgentOrchestrator   →  SingleAgentRunner | RufloCrew
EmbeddingProvider   →  ApiEmbeddings     | LocalEmbeddings
```

That keeps Migration risk at Low, and it's often the whole of the first step.

## 8. Label maturity every time

When you name a component in a recommendation, say how mature it is, from its card or a live check:

- **Version**: pre-1.0 is noted.
- **Labels the project itself uses**: alpha, beta, experimental, preview.
- **Activity**: the date of the last release, if it has been quiet for six months or more.

Don't present a capability as production-proven just because it exists in a README.

## 9. Common traps

| The pull | What to check instead |
|---|---|
| "It's written in Rust, so it's faster" | Is the operation it speeds up actually the bottleneck? In most small apps the network and the model call dominate. |
| "A swarm will be smarter" | Does the work actually split into independent parts? If every step needs the previous one, one strong agent is usually better. |
| "It's parallel, so it's a Ruflo job" | Claude Code's built-in subagents already run independent work in parallel. What would Ruflo add that they don't? |
| "Persistent memory makes agents learn" | Is there a feedback signal, and enough repetitions, for anything to be learned? |
| "Replace pgvector" | Is pgvector failing at something today: speed, scale, offline use? If not, keep it. |
| "Let Ruflo run the whole workspace" | Which single workflow needs orchestration? Start there, in project scope. |
| "It's self-learning / neural" | What does it learn from, and where is that documented? |
