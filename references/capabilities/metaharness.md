# MetaHarness

| | |
|---|---|
| Formerly | agent-harness-generator (the old repo redirects) |
| Category | Agent harness generation: scaffolds a stand-alone agent package for a repo |
| Status | v0.4.17 (2026-09-26). **Pre-1.0.** Parts are labelled experimental; some of its own docs still say "v0.1.x beta". MIT. |
| Snapshot | 2026-10-07 |
| Sources | [src:metaharness-repo] [src:metaharness-userguide] [src:metaharness-studio] [src:metaharness-releases] |

## In plain words

A generator that reads a repository (or starts from a template) and produces a separate, publishable agent
package for it: agent prompts, skills, an MCP server stub with a locked-down policy, and the settings for
Claude Code, Codex or another agent host. [src:metaharness-repo]

## What it's for

Turning a generic agent setup into a repo-specific one that you own, can version, publish and sign, rather
than adopting a large all-in-one environment. Its README describes Ruflo as the all-in-one it "factors
apart": you generate only the parts you need. [src:metaharness-repo]

## Use when

- You need to **ship** an agent setup to other people: a client, a team, or the public, as a versioned,
  signed package.
- You maintain several repos that each need a consistent, repo-specific agent configuration.
- You want to leave a full Ruflo project for something smaller you own (`--from-existing`).
- You want a browser-based way to see what a harness for your repo would contain, without installing
  anything.

## Avoid when

- One developer, one repo, and no need to distribute the setup. A hand-written `CLAUDE.md`, a few skills,
  or Claude Code's `/init` is enough.
- You want a chatbot, a no-code platform, a hosted agent or fine-tuning. Its own guide lists these as "not
  the right tool". [src:metaharness-userguide]
- Stability matters more than features: it's pre-1.0, and its diagnostics warn about breakage across
  kernel versions.

## What people use instead

- A hand-written `CLAUDE.md`, `.claude/skills/` and `settings.json`, or Claude Code's `/init`.
- A small Claude Code plugin you write yourself.
- The Claude Agent SDK, for a branded command-line agent.

## Advantages it can buy

portability, deployment footprint, reusable learned patterns

## Lightest path

**LOW: the Studio in a browser, nothing installed.** Open the Studio, paste a repo URL, and download the
generated `.zip` to read through. The docs say it runs fully in the browser. [src:metaharness-studio]

**LOW: generate into a new folder.** `npx metaharness --wizard`, or `npx metaharness my-bot --template
vertical:coding --host claude-code`. It writes a **new** project folder (`my-bot/`) and doesn't run your
repository's code. [src:metaharness-repo] Delete the folder to undo.

A Claude Code plugin also exists in the repo (`metaharness`, 14 skills). The install commands below are
inferred from its marketplace file, not stated in the README; check them first:
`claude plugin marketplace add ruvnet/metaharness --scope project`, then
`claude plugin install metaharness@metaharness --scope project`.

## What a full install changes

The generator writes a new package folder, not your repo: `package.json`, `CLAUDE.md`, `src/agents/`,
`src/mcp/`, `.claude/settings.json` with hooks and MCP servers, and `.harness/manifest.json` with a
checksum. MCP tools are deny-by-default (no network, shell or file writes). [src:metaharness-repo]

- For the Codex host you copy a config into `~/.codex/config.toml` yourself, which is a **global** change.
- `npm run evolve` lets it rewrite its own harness config.
- `harness publish` needs a Pinata token.
- No hosted backend, no telemetry, no API key needed to scaffold. Needs Node.js 20+.

## Model routing and cost

`@metaharness/router` picks "the cheapest model predicted to clear your quality bar", learned from your own
eval logs, and a cost cascade escalates to a frontier model only when the cheap one fails.
[src:metaharness-repo] The headline numbers (SWE-bench and "about one-tenth the cost") are **claims**, and
the README itself notes one cost figure is an estimate.

## Maturity

- Pre-1.0, a few months old, active (hundreds of stars, commits most days). [src:metaharness-releases]
- Its own docs disagree on counts (templates, subcommands), and the status section lags the releases.
- Treat generated harnesses as a starting point to review, not a finished product.

## Verify live before relying on

- The plugin install commands, which are inferred: [src:metaharness-repo]
- Current version, and whether it has reached 1.0: [src:metaharness-releases]
- The supported hosts and templates: [src:metaharness-userguide]

## Related

- **Ruflo**: the all-in-one environment MetaHarness factors apart. Ruflo also has an optional
  `ruflo-metaharness` plugin, and its README uses "MetaHarness" for a separate readiness-grading feature.
  Don't mix the two up. [src:ruflo-metaharness-plugin]
