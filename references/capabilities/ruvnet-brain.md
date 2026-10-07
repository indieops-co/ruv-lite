# RuvNet Brain

| | |
|---|---|
| Category | Ecosystem knowledge for Claude Code: a searchable index of rUv source code, plus hooks that push it into every session |
| Status | **Third-party**: by Stuart Kerr (Isovision.ai), not by rUv, and not in rUv's own index. npm `ruvnet-brain` 4.5.17 (2026-10-07), releases labelled "staged candidate". Its docs disagree with its code in places. |
| Snapshot | 2026-10-07 |
| Sources | [src:ruvnet-brain-repo] [src:ruvnet-brain-npm] [src:ruvnet-brain-hooks] |

## In plain words

A Claude Code plugin with a local search tool, `search_ruvnet`, over a downloaded index of rUv projects'
source code and docs, so Claude builds with the real stack instead of guessing. Its stated purpose goes
further: "Proactive capability advocacy is the product", meaning it is designed to volunteer rUv
capabilities. [src:ruvnet-brain-repo]

## What it's for

Developers already building on the rUv stack, who want Claude to check the actual source before using a
rUv feature, and to be told about capabilities they have but haven't turned on.

## Use when

- The user has decided to build on the rUv stack (Ruflo, RuVector, AgentDB) in Claude Code, and wants
  grounded answers about it all day.
- They want Claude to be *stopped* from asserting rUv capabilities without checking: it ships gates that
  enforce this.
- They've graduated past ruv lite: they want an advocate for the stack, not a skeptic about it.

## Avoid when

- They're still deciding whether to use rUv at all. Its design is to advocate; that's ruv lite's question.
- They don't want hooks in every session. It registers SessionStart and UserPromptSubmit hooks that inject
  text, a PreToolUse gate that can refuse Write and Edit until `search_ruvnet` has been consulted, and a
  Stop gate. [src:ruvnet-brain-hooks]
- They need a predictable, minimal Claude Code setup for a team.

## What people use instead

- rUv's own discovery plugin (`ruvnet@ruvnet`), which has offline discovery tools over rUv's catalogue
  (see `../ecosystem-map.md`). [src:ruvnet-discovery-plugin]
- Reading the project's README and releases directly, or ruv lite's grounding step.

## Advantages it can buy

cross-session intelligence

## Lightest path

**MEDIUM, and user scope by default.** The one-line installer `npx ruvnet-brain` downloads the knowledge
bundle to `~/.cache/ruvnet-brain`, wires the plugin at **user** scope (and Codex via
`~/.codex/config.toml`), and can offer to edit `CLAUDE.md`, schedule nightly updates, install Ruflo and
RuVector, and turn on telemetry. Opt-outs: `--no-enhance`, `--no-stack`, `--no-nightly-prompt`,
`--no-telemetry`. Preview first with `--plan` (or `--dry-run`); reverse with `--uninstall`.
[src:ruvnet-brain-repo]

The manual route is two commands: `claude plugin marketplace add stuinfla/ruvnet-brain`, then
`claude plugin install ruvnet-brain@ruvnet-brain`, where `--scope project` keeps it to one project.

## What a full install changes

- A knowledge bundle in `~/.cache/ruvnet-brain`, and a local MCP server (no cloud calls, per its docs).
- Four MCP tools: `search_ruvnet`, `ruvnet_registry_latest` and `ruvnet_cli_help` (read-only), and
  `ruvnet_cli_run`, marked destructive, which runs rUv command-line tools.
- Hooks in every session, as above. There's no documented search-only mode.

## Maturity

Active and frequently released, by one independent author. Its own README, security notes and hook file
currently disagree about which hooks exist; trust the hook file. [src:ruvnet-brain-hooks]

## Verify live before relying on

- The current hook list: [src:ruvnet-brain-hooks]
- Installer flags and defaults: [src:ruvnet-brain-repo]

## Related

- ruv lite can **use** `search_ruvnet` for facts if it's installed (`../grounding.md`). It never adopts
  Brain's advocacy, and never installs it unless the user asks.
- Ruflo cites `search_ruvnet` as a grounding source in its own design notes.
