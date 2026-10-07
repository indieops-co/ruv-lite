# Ruflo

| | |
|---|---|
| Formerly | claude-flow (the old repo and npm name still redirect or work) |
| Category | Agent orchestration for Claude Code and Codex |
| Status | v3.54.1 (2026-10-07). Post-1.0, but its npm `alpha` tag points at the same build and several dependencies are alphas. Releases roughly daily. MIT. |
| Snapshot | 2026-10-07 |
| Sources | [src:ruflo-repo] [src:ruflo-userguide] [src:ruflo-marketplace] [src:ruflo-init-source] [src:ruflo-skill] |

## In plain words

An add-on for Claude Code (and Codex) that gives it shared memory, task routing and tools for running
several agents together on one job. You can take one piece at a time as Claude Code plugins, or initialize
the whole environment in a project. [src:ruflo-repo]

## What it's for

Claude Code on its own runs one agent per context and keeps little between sessions. Ruflo adds coordinated
multi-agent runs ("swarms"), a local memory store the agents share, reusable workflows, and hooks that
suggest which model or tool fits each task. [src:ruflo-repo]

## Use when

The baseline is native Claude Code: built-in subagents already run independent work in parallel, skills make
a routine repeatable, and scripts handle the deterministic steps. Ruflo fits when the user needs what those
don't do well (`decision-policy.md`, section 5):

- Several agents should **share memory** they can search, across runs and weeks, and the user accepts
  Ruflo-managed state (it runs on AgentDB, an alpha).
- **Many agents change code at once** and keep colliding: Ruflo's swarm plugin isolates them in worktrees
  and keeps a shared record of decisions.
- **Per-step model routing or cost tracking at volume** matters, and the user would otherwise build it.
- **Two or more of those at once**, so assembling them from native pieces is the more complex option.
- The user **already runs Ruflo** and one more plugin (cost tracking, workflows, testing) fixes a current pain.
- The user explicitly wants to **learn agent orchestration**, in a sandbox.

## Avoid when

- Parallelism or repetition is the only need. Native subagents plus a skill cover it with nothing to
  install.
- One agent can do it in one sitting. Ruflo's own skill file says not to suggest it "for one-shot edits,
  simple bug fixes, or tasks a single agent can complete in one turn". [src:ruflo-skill]
- Each step depends on the one before. Hand-offs lose context, and one strong model usually does better.
- The team needs a predictable, audited `settings.json` and `CLAUDE.md`. A full init edits both, sets the
  model, and by default appends to the global `~/.claude/CLAUDE.md`. [src:ruflo-init-source]
- Nobody on the team will keep up with near-daily releases. Breaking changes land inside 3.x. [src:ruflo-releases]
- The product's runtime is a web app, not a developer workflow. Ruflo orchestrates agents in a coding
  assistant; it isn't an app backend.

## What people use instead

- Plain Claude Code: subagents, agent teams, skills, hooks, a hand-written `CLAUDE.md`, and auto-memory.
- One focused MCP server per need (a database, a search API) instead of a bundle.
- For agents inside a product: the Claude Agent SDK, LangGraph, CrewAI or the OpenAI Agents SDK.

## Advantages it can buy

multi-agent coordination, persistent agent memory, model routing, reusable learned patterns,
cross-session intelligence

## Lightest path

**LOW: one or two Claude Code plugins, in project scope.** The marketplace lists about 46 plugins
(`ruflo-core`, `ruflo-swarm`, `ruflo-workflows`, `ruflo-rag-memory`, `ruflo-agentdb`, `ruflo-ruvector`,
`ruflo-intelligence`, `ruflo-sparc`, `ruflo-cost-tracker` and many more). [src:ruflo-marketplace]

```
claude plugin marketplace add ruvnet/ruflo --scope project
claude plugin details ruflo-core@ruflo        # see what it adds and its token cost first
claude plugin install ruflo-core@ruflo --scope project
claude plugin install ruflo-swarm@ruflo --scope project
```

Inside Claude Code the same is `/plugin marketplace add ruvnet/ruflo` and `/plugin install
ruflo-core@ruflo`. Those default to **user** scope, so use the CLI form with `--scope project` (or pick
project in the `/plugin` menu) to keep it in one project. Undo with `claude plugin uninstall
ruflo-core@ruflo --scope project`.

- The README describes the plugin path as adding no files to the workspace. [src:ruflo-repo]
- `ruflo-core` registers Ruflo's MCP server, and it does ship hooks (PreToolUse, PostToolUse, PreCompact,
  Stop), even though the README's summary says the plugin path adds none. Tell the user. [src:ruflo-core-plugin]
- The console and mods plugins need Claude Code 2.1.287+, are marked early access, and the README warns
  that mods run with the account's permissions, unsandboxed. [src:ruflo-repo]

**The plugins most people ask about**, as the marketplace describes them (descriptions, not verified
behaviour; `claude plugin details <plugin>@ruflo` shows what each one actually installs): [src:ruflo-marketplace]

| Plugin | Marketplace description |
|---|---|
| `ruflo-core` | Core MCP tools, commands and orchestration patterns |
| `ruflo-swarm` | Agent teams, swarm coordination, Monitor streams, worktree isolation |
| `ruflo-workflows` | Workflow templates, orchestration and lifecycle management |
| `ruflo-loop-workers` | `/loop` workers and scheduled background automation |
| `ruflo-rag-memory` | Semantic retrieval memory (RuVector and AgentDB) |
| `ruflo-agentdb` | AgentDB memory with vector search and causal graphs |
| `ruflo-cost-tracker` | Token usage tracking, cost attribution per agent, budget alerts, optimization suggestions |
| `ruflo-observability` | Structured logging, tracing and metrics for swarm activity |
| `ruflo-intelligence` | Pattern learning and model routing |
| `ruflo-testgen` | Test-gap detection and test generation |
| `ruflo-security-audit` | Security review, dependency scanning, CVE monitoring |
| `ruflo-docs` / `ruflo-adr` | Documentation drift detection; architecture decision records |
| `ruflo-sparc` | The SPARC method with phase gates |

The rest are domain-specific (trading, music, IoT, federation) or early access (`ruflo-console`,
`ruflo-mods`).

**MEDIUM: the MCP server alone.** `claude mcp add claude-flow --scope project -- npx ruflo@latest mcp
start`. The server name is still `claude-flow`. [src:ruflo-repo]

## What a full install changes

`npx ruflo@latest init` (or `init --wizard`) is **VERY HIGH** on the complexity budget. From the init
source: [src:ruflo-init-source]

- **Creates** `.claude/` (skills, commands, agents, helpers), `.claude-flow/` (config, data, logs, sessions,
  hooks, workflows, metrics) and `.swarm/memory.db` (SQLite), plus `.agents/skills/ruflo/SKILL.md`.
- **Writes `.mcp.json`**, registering a `claude-flow` server that runs `npx -y ruflo@latest mcp start`.
- **Edits `.claude/settings.json`**: about a dozen hook events, a status line, permission rules, an
  experimental agent-teams environment flag, and a `model` setting. If the file exists it merges env and
  permissions, and adds hooks only when there are none. [src:ruflo-settings-generator]
- **Writes `CLAUDE.md`** if there isn't one. An existing one is skipped unless `--force`, which backs it up
  to `CLAUDE.md.pre-ruflo`.
- **Global:** appends a "Ruflo Integration" block to `~/.claude/CLAUDE.md` **by default**. `--no-global`
  prevents it. Always pass `--no-global` unless the user explicitly wants the global change.
- **Agents:** about 24 by default, 98 with `--all-agents`. The background daemon is off unless started.
- Needs Node.js 20+ and Claude Code. Install size is about 45 MB core-only, about 340 MB with the default
  ML extras. [src:ruflo-userguide]

## Model routing and cost

Ruflo describes "3-tier model routing": simple code transforms through a local tool (Agent Booster), then
Haiku or Sonnet, then Opus. In practice, hooks *recommend* a model or tool to Claude rather than force it.
[src:ruflo-userguide] The project's savings figures (for example "75% lower costs", "30–50% token
reduction") are **claims**. Treat them as a hypothesis to measure on the user's own workload.

## Maturity

- Very active (tens of thousands of stars, hundreds of open issues, releases most days). [src:ruflo-repo]
- Counts in its own docs disagree (MCP tools 313–323, agents "60+" to "100+", plugins 32–46), and some
  docs are months behind the code. Quote counts as "about" and from the snapshot, or check live.
- Breaking changes have shipped in minor releases. Pin a version for anything that matters.
  [src:ruflo-releases]

## Verify live before relying on

- The current plugin list and what `ruflo-core` installs (hooks, MCP server): [src:ruflo-marketplace]
- The plugin install commands and minimum Claude Code version: [src:ruflo-repo]
- What `init` writes, especially the global `CLAUDE.md` default: [src:ruflo-init-source]
- The latest version and recent breaking changes: [src:ruflo-releases] [src:ruflo-npm]

## Related

- **agentic-flow**: Ruflo's user guide says Ruflo v3 is built on it, and it's an optional dependency.
- **AgentDB** and **RuVector**: memory and vector stores Ruflo can use, also offered as Ruflo plugins.
- **MetaHarness**: generates a stand-alone agent package; it describes Ruflo as the all-in-one it "factors
  apart".
- **ruv-swarm** and **Flow Nexus**: optional extra MCP servers, off by default, quiet since 2025.
