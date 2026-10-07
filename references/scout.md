# Scout

"Could anything in the rUv ecosystem materially help this project?" Scout reads, ranks and stops. It never
installs or edits anything, and it doesn't issue a call.

## Inputs

An idea, a PRD, an architecture description, a repository, a problem or a client requirement.

- **A document or pasted PRD:** read it fully. Note the workloads (what runs, how often, how much data),
  the constraints (privacy, offline, latency, budget) and the stack.
- **A repository:** read-only. Start with the README, the manifests (`package.json`, `pyproject.toml`,
  `Cargo.toml`, `requirements.txt`), `docker-compose.yml`, `.env.example` (names only, never values),
  `.mcp.json`, `.claude/` and `CLAUDE.md`. Search for existing retrieval, memory and agent code (`pgvector`,
  `embedding`, `vector`, `agent`, `crew`, `swarm`, `ruflo`, `claude-flow`, `agentdb`, `ruvector`). Don't
  read the whole codebase; the aim is the shape, not the details.
- **Already-installed rUv components:** list them. Scout notes possible overlap (two systems holding the
  same memory) as a finding.

## Steps

1. Summarise what you looked at in one line.
2. Walk `capabilities/index.json`. For each technology, test its `use_when` signals against what you found,
   and its `avoid_when` signals against the constraints. If the project already mentions a rUv project
   without a card, place it using `ecosystem-map.md`.
3. Rate each match now and later (`decision-policy.md`, section 1). For a LATER rating, write the trigger.
4. Check freshness (`grounding.md`) only for anything you put in NOW. Scout's ratings are cheap; the live
   checks belong to Advise.
5. Write it in the shape of `assets/templates/scout.md`.

## Rules

- An empty NOW row is a normal, correct result.
- Ratings are about the project's needs, not the technology's quality.
- Don't explain every project in the ecosystem. NOT NEEDED is a list of names, not a tour.
- End by offering Advise on the top candidate, or Explain. Not Apply.
