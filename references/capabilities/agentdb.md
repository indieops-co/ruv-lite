# AgentDB

| | |
|---|---|
| Category | Agent memory: a local store for an agent's past tasks, outcomes and skills |
| Status | npm `latest` is **3.0.0-alpha.20** (2026-07-30): an **alpha**. The last non-alpha release was 1.6.1 (2025-10). No commits since 2026-07-30, with bug reports filed since. MIT. |
| Snapshot | 2026-10-07 |
| Sources | [src:agentdb-repo] [src:agentdb-npm] [src:agentdb-full-docs] [src:agentdb-issues] [src:claude-flow-memory-npm] |

## In plain words

A TypeScript library, command line and MCP server that keeps an agent's memory in a local file: what it was
asked, what it did, whether it worked, and reusable "skills". It can search those memories by meaning, and
is meant to rank memories better as you report which ones helped. [src:agentdb-repo]

## What it's for

Letting an agent remember past tasks and their outcomes across sessions, without running a database server.
It ships ready-made structures for that: Reflexion episodes (task, result, self-critique), a skill library,
and a cause-and-effect graph. [src:agentdb-full-docs]

## Use when

- The product genuinely needs **cross-session agent learning**: the agent should do better next time because
  of recorded outcomes, and there's a real feedback signal (a user approval, a test result).
- The user already runs Ruflo or agentic-flow. Ruflo's memory runs on AgentDB, so it's already in their
  stack. [src:claude-flow-memory-npm]
- A JavaScript/TypeScript prototype wants episode and skill memory as MCP tools, today, and can accept
  alpha software.

## Avoid when

- "Memory" just means storing data the app needs. That's a normal database table.
- There's no feedback signal or not enough repetition. Nothing can be learned, whatever the database.
- Production or client work that needs stable releases. The current release is an alpha, and the project
  has gone quiet since July 2026 with open bugs. [src:agentdb-issues]
- They already keep this data in Postgres or SQLite. A table of episodes plus pgvector or sqlite-vec covers
  most needs.
- The stack isn't JavaScript or TypeScript. (A PyPI package called `agentDB` is an unrelated project.)

## What people use instead

- A few plain tables (episodes, outcomes, skills) in the database they already have, plus pgvector or
  sqlite-vec for search by meaning.
- An embedded vector store (LanceDB, Chroma) for a prototype.
- Claude Code's own memory files and `CLAUDE.md`, for a coding assistant's memory.

## Advantages it can buy

persistent agent memory, cross-session intelligence, reusable learned patterns, local execution

## Lightest path

**LOW: a throwaway memory file.** Needs Node.js 18+. [src:agentdb-npm]

```
mkdir agentdb-trial && cd agentdb-trial
npx agentdb@3.0.0-alpha.20 init my-memory.rvf
```

Pin the version: `@latest` currently installs an alpha too. Delete the folder to undo.

**MEDIUM: as an MCP server in one project.**
`claude mcp add agentdb --scope project -- npx agentdb@3.0.0-alpha.20 mcp start`. Undo with
`claude mcp remove agentdb --scope project`. [src:agentdb-repo]

## What a full install changes

- `npm i agentdb` adds a small package with many optional native dependencies (embedding models, SQLite,
  HNSW and `@ruvector` packages). It defaults to a pure-WASM SQLite, so no build tools are needed.
- Memory is saved as `.rvf` files by default (RVF, RuVector's format). [src:agentdb-full-docs]
- An open bug reports files being created in the working directory instead of next to the database path. [src:agentdb-issues]
- The Docker setup in the repo is reported broken. [src:agentdb-issues]

## Known problems

[src:agentdb-issues]

- The documented feedback call does nothing when given a document id, so "self-learning" silently doesn't
  happen unless you pass an undocumented `feedbackId`. That's the main feature; check it in any trial.
- Command-line write commands exit with an error code after saving, and one ignores `--db`.
- Batch insert has a reported schema mismatch.

## Maturity

Small project (under a hundred stars) and alpha releases since February 2026. Its own docs call v2 "latest
stable", which doesn't match npm. The large speed figures ("150× faster than SQLite", "800× faster than
Pinecone") are **claims**; Ruflo's own audit measured a more modest 2–5× over brute force, and a tie or loss
at small sizes. [src:agentdb-full-docs] [src:ruflo-repo]

## Verify live before relying on

- Whether a stable (non-alpha) release has shipped, and the commit activity since 2026-07: [src:agentdb-npm] [src:agentdb-repo]
- Whether the feedback-learning bug is fixed: [src:agentdb-issues]

## Related

- **Ruflo**: its memory layer depends on AgentDB, and the `ruflo-agentdb` plugin calls itself the substrate
  for Ruflo memory. Using Ruflo memory means using AgentDB.
- **RuVector** and **RVF**: optional backend and default file format. AgentDB's optional dependency ranges
  don't include RuVector's current 0.3.x line.
