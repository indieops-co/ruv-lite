# The rUv ecosystem, mapped

Snapshot 2026-10-07. For Scout and Explain: what exists, what it's for, and how alive it is. Only the
technologies in `capabilities/index.json` have full cards. For everything here, say what the map says, give
the link, and check live before saying more.

## rUv's own "Start here"

From the profile README at github.com/ruvnet/ruvnet. Machine-readable copies: `llms.txt` and
`data/projects.json` in the same repo. rUv calls it "a conceptual map, not a claim that every system is
already integrated".

| Goal | Project |
|---|---|
| Orchestrate agents and swarms | **Ruflo** (card) |
| Generate and evolve a portable harness | **MetaHarness** (card) |
| Add adaptive vector and graph memory | **RuVector** (card) |
| Package an agent into a portable RVF container | **RVF** (card) |
| Stage deterministic target bundles from RVF | **RVForge** |
| Explore camera-free WiFi spatial intelligence | **RuView** (card) |

## The layers, as rUv describes them

| Layer | Projects |
|---|---|
| Spatial perception | RuView, rvCSI, RuField |
| Sensing governance | WiFi Veil, RuCelium |
| Agent control plane | Ruflo, MetaHarness |
| Learning memory | RuVector, AgentDB, AgenticOW |
| Portable execution and transfer | RVF, RVForge, rvQR (alpha), RVM |
| Governed adaptation | Autogenous, Dream Machine, rGi (experimental) |
| Useful-work measurement | APx |
| World and research systems | WorldGraph, RuPixel, PhotonLayer, Helix |

ruv.io/projects lists over two hundred projects in five groups. Most builders will only ever need the first
four rows of "Start here".

## Other projects people ask about

| Project | What it is | Status (2026-10-07) |
|---|---|---|
| **agentic-flow** (card) | Agent workflows and model switching; under Ruflo | Maintained, 2.1.3 |
| **SPARC** (card) | Spec → Pseudocode → Architecture → Refinement → Completion method and tools | Method stable; v1.0 tool unpublished |
| **RVM** | A capability-controlled virtual machine, in Rust | Maintained, v1.7.0 (2026-08). The crates.io crate `rvm` is someone else's. |
| **RVForge** | Tools to author, validate and stage RVF bundles | 0.2.0 (2026-08) |
| **QuDAG** | Post-quantum messaging network for agent swarms | Active preview: "not production qualified" |
| **ruv-FANN** | Rust port of the FANN neural-network library; also home of ruv-swarm | Maintenance |
| **ruv-swarm** | Rust/WASM swarm orchestration, an optional extra MCP server for Ruflo | Dormant since 2025-09 |
| **Flow Nexus** | Hosted, gamified MCP cloud sandboxes | Dormant repo since 2025-09 |
| **SAFLA** | Python "self-aware feedback loop" memory | Maintenance; PyPI 0.1.3 (2025) |
| **DAA** | Rust SDK for decentralized autonomous agents | Maintenance |
| **Synaptic Mesh** | Peer-to-peer neural mesh research on QuDAG, DAA and ruv-FANN | Maintenance; its README contradicts itself on readiness |
| **sublinear-time-solver** | Fast solver for a class of linear systems, also as MCP | Maintained; research math |
| **Autogenous, Dream Machine, APx, rGi, ruOS, RuLake** | 2026 projects in the index | New; check live |

"Maintenance" here means mostly security fixes. A bulk security sweep on 2026-05-23 touched many older
repos at once, so that commit date isn't evidence of feature work.

## Renames

| Old name | Now |
|---|---|
| claude-flow | **Ruflo** (repo redirects; npm `claude-flow` still publishes; the MCP server is still named `claude-flow`) |
| agent-harness-generator | **MetaHarness** |
| WiFi-DensePose | **RuView** |
| SPARC (Python CLI) | SPARC v1.0 in TypeScript (announced, not yet on npm) |

## Not rUv projects

People often assume these are rUv's own. They aren't.

- **RuvNet Brain** (card): by Stuart Kerr (Isovision.ai), github.com/stuinfla/ruvnet-brain.
- **agentic-qe**: QA agents by Dragan Spiridonov, github.com/proffesor-for-testing/agentic-qe.
- **ruv lite** itself: an independent IndieOps Skilllet. Unofficial.

## rUv's own discovery plugin

rUv publishes a Claude Code plugin for exploring the ecosystem: `ruvnet@ruvnet` (marketplace
`ruvnet/ruvnet`). It ships four skills and connects to a hosted server at x.ruv.io (OAuth). A separate local
companion, `ruvnet-guide`, adds offline tools over a static catalogue: `ruvnet_discover`, `ruvnet_project`,
`ruvnet_changes`, `ruvnet_search_changes`, `ruvnet_plan`, `ruvnet_connect`. ruv lite can use them for facts
if they're installed (`grounding.md`).

## Name collisions

- PyPI `agentDB` is an unrelated project.
- crates.io `rvf` and `rvm` are unrelated projects.
- The Rust type `AgenticDB` inside `ruvector-core` isn't the npm `agentdb` package.
- Ruflo's README uses "MetaHarness" for its own readiness-grading feature, separate from the MetaHarness repo.
