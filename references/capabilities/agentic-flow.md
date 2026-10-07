# agentic-flow

| | |
|---|---|
| Category | Agent workflows and model switching for Claude Code and the Claude Agent SDK |
| Status | npm 2.1.3 (2026-09-16); a 3.0.0 alpha is on its `alpha` tag. Maintained, with stale pull requests recently triaged. It pins AgentDB to an alpha. |
| Snapshot | 2026-10-07 |
| Sources | [src:agentic-flow-repo] [src:agentic-flow-npm] [src:ruflo-userguide] |

## In plain words

A toolkit for running agent workflows on top of Claude Code or the Claude Agent SDK, including switching
which model or provider handles each part. Ruflo's guide says Ruflo v3 is built on it, though Ruflo also
works without it. [src:ruflo-userguide]

## What it's for

Defining multi-step agent workflows and routing them across models and providers, below the level of a
full environment like Ruflo. [src:agentic-flow-repo]

## Use when

- A developer is building agent workflows in code (the Agent SDK) and wants model or provider switching
  without writing it themselves.
- They're digging into how Ruflo works underneath, or need a piece of it without the full environment.

## Avoid when

- A beginner wants multi-agent work inside Claude Code. Ruflo's plugins, or Claude Code's own subagents,
  are the gentler entry.
- One provider and one model are fine. Routing adds moving parts.
- They need a dependency tree without alphas. It pins AgentDB to an alpha release. [src:agentic-flow-npm]

## What people use instead

- The Claude Agent SDK directly, with its own subagents.
- LangGraph, CrewAI or the OpenAI Agents SDK, for workflow graphs.
- A small router in their own code that picks a model per task.

## Advantages it can buy

model routing, multi-agent coordination

## Lightest path

**LOW: read before installing.** The snapshot doesn't record a verified install or quickstart command.
Check the README live before giving one, and try it in a scratch folder. [src:agentic-flow-repo]

## What a full install changes

Unknown in this snapshot. Check the README before Apply. Expect an npm package with AgentDB in its
dependencies.

## Maturity

Maintained, post-1.0, with an alpha line in progress. Lower-level and less documented for beginners than
Ruflo.

## Verify live before relying on

- The install command and what it writes: [src:agentic-flow-repo]
- The current stable version and the 3.0 status: [src:agentic-flow-npm]

## Related

- **Ruflo**: built on it (optional dependency).
- **AgentDB**: pinned in its dependencies.
