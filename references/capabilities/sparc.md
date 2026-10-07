# SPARC

| | |
|---|---|
| Category | Development method: a phase-gated way of building with AI agents |
| Status | The method is stable. The new TypeScript v1.0 tool is announced but **not yet published** on npm (`@ruvnet/sparc` returns 404); the older Python package `sparc` is at 0.88.0 (2026-05). |
| Snapshot | 2026-10-07 |
| Sources | [src:sparc-repo] [src:sparc-pypi] [src:ruflo-sparc-plugin] |

## In plain words

A five-step way of building software with an AI agent: **S**pecification, **P**seudocode,
**A**rchitecture, **R**efinement, **C**ompletion. Each step has to be done and checked before the next. It's
mainly a discipline; the tools around it just enforce the steps. [src:sparc-repo]

## What it's for

Stopping an agent from jumping straight to code. Writing the spec and the plan first, with a gate between
phases, catches misunderstandings while they're cheap. The repo now describes itself as an "evidence-gated
engineering metaharness". [src:sparc-repo]

## Use when

- Features are big enough that a written spec and a design step pay for themselves.
- The agent keeps building the wrong thing, and the user wants gates that force a plan first.
- The user already runs Ruflo and wants the method inside it (the `ruflo-sparc` plugin).

## Avoid when

- Small changes and bug fixes. Five phases for a one-line fix is ceremony.
- The team already has a planning habit that works: a PRD, plan mode, design docs, tests first.
- They'd adopt it *only* through a heavy tool. The method works with nothing installed.

## What people use instead

- Claude Code's plan mode, then implementation.
- A PRD or design doc, plus tests written first.
- Architecture decision records (ADRs) for the big choices.

## Advantages it can buy

reusable learned patterns

## Lightest path

**LOW: use the method by hand.** Ask the agent to produce the five phases in order and stop for review
after Specification and Architecture. Nothing to install.

**LOW: inside Ruflo**, if they already use it: `claude plugin install ruflo-sparc@ruflo --scope project`
adds an orchestrator agent and `/sparc-spec`, `/sparc-implement`, `/sparc-refine`. [src:ruflo-sparc-plugin]

## What a full install changes

The v1.0 command-line tool (`sparc init`, `start`, `gate`, `advance`…) and its MCP server aren't published
yet. Check before suggesting them. [src:sparc-repo]

## Maturity

The method is years old and simple. The tooling is mid-rewrite. One place to watch: Ruflo's older "SPARC
modes" file expands the letters differently (Specification, Planning, Architecture, Review, Code). Use the
canonical expansion above. [src:ruflo-sparc-plugin]

## Verify live before relying on

- Whether `@ruvnet/sparc` 1.0 has been published: [src:sparc-repo]

## Related

- **Ruflo**: ships the `ruflo-sparc` plugin.
- rUv's discovery plugin can return an "advisory SPARC/MetaHarness integration plan".
