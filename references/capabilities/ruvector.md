# RuVector

| | |
|---|---|
| Category | Vector and graph memory: an embedded vector store, with Node, browser and Postgres options |
| Status | npm `ruvector` 0.3.3 (2026-09-23), **pre-1.0**. Rust crates are 2.x (`ruvector-core` 2.3.1), so there's no single project version. Its README labels several parts proof-of-concept or research. MIT. |
| Snapshot | 2026-10-07 |
| Sources | [src:ruvector-repo] [src:ruvector-npm] [src:ruvector-crates] [src:ruvector-postgres] [src:ruvector-changelog] |

## In plain words

A database that finds things by meaning, which runs inside your program (no separate server, no API key)
and saves to a local file. It's written in Rust, with packages for Node.js and the browser, an optional
Postgres extension, and many add-on modules for graphs, compression and learning. [src:ruvector-repo]

## What it's for

Giving an app or an agent local, persistent "remember and recall by meaning" without running a database
service. It also bundles a command line and an MCP server, so a coding agent can store and search memories
directly. [src:ruvector-repo]

## Use when

- Semantic search has to run **locally or offline**: on a laptop, in a desktop app, in the browser, at the
  edge, with no server.
- Data can't leave the machine (privacy), and an embedded store is simpler than running a database.
- A Node.js or Rust project wants agent memory with a ready-made command line and MCP server.
- The user wants vector and graph search in one embedded library, and accepts a pre-1.0 dependency.

## Avoid when

- They already have Postgres with pgvector and it works. Every managed Postgres service offers pgvector;
  RuVector's Postgres extension needs its own image or a source build, uses its own column and index types,
  and isn't drop-in despite its "100% compatible" wording. [src:ruvector-postgres]
- The stack is Python. There's no Python package. [src:ruvector-repo]
- They need stable versioning, working replication or incremental backups. Its README lists replication and
  incremental snapshots as incomplete. [src:ruvector-repo]
- The data is small (thousands of items). Any store, even a plain table with brute-force search, is fast
  enough.
- Search needs selective metadata filters. The core applies filters after the search, so filtered queries
  can return fewer results than asked for. [src:ruvector-repo]

## What people use instead

- **Postgres + pgvector**, the default when there's already a Postgres database.
- **Embedded**: SQLite + sqlite-vec, LanceDB, Chroma, hnswlib.
- **A server**: Qdrant, or a hosted vector database.

## Advantages it can buy

local execution, offline use, privacy, deployment footprint, persistent agent memory, specialized performance

## Lightest path

**LOW: try the command line in a scratch folder.** Needs Node.js 20+. The first semantic call downloads a
small embedding model. [src:ruvector-npm]

```
npx ruvector hooks remember --semantic --type decision "We chose pgvector for search"
npx ruvector hooks recall --semantic "what did we choose for search?"
```

**MEDIUM: a library behind an interface.** `npm install --save-exact ruvector` (pin the exact version), with
a `RetrievalProvider` interface in front, so the existing store keeps working beside it. Its read-only MCP
mode is `RUVECTOR_MCP_PROFILE=readonly npx ruvector mcp start`. [src:ruvector-repo]

Other entry points: `@ruvector/wasm` for the browser, `cargo add ruvector-core` for Rust (its docs disagree
on the minimum Rust version), and the `ruflo-ruvector` plugin for Ruflo users.

## What a full install changes

- **Library:** a local data file, and the embedding model cache on first use. Nothing global.
- **Postgres extension:** **HIGH**. Either a Docker image (`ruvnet/ruvector-postgres`, which lags the crate
  version) or a source build with `cargo pgrx` against PostgreSQL 14–17. You'd create parallel tables and
  convert types. [src:ruvector-postgres]
- **Whole repo:** a large Rust workspace (over a hundred crates); not a beginner path.

## Known limits it documents itself

[src:ruvector-repo]

- Reopening a saved index rebuilds it from the stored vectors, so cold starts grow with the data.
- The quantization option is stored but not applied; real compression needs separate crates.
- GNN reranking is a "research surface", not something search does automatically.
- Its learning features only update from recorded feedback; searching doesn't teach it anything.
- Recent releases fixed serious bugs (one router build returned 3.6% recall@10; a size setting was
  ignored), so pin versions and test recall on your own data. [src:ruvector-changelog]

## Maturity

Pre-1.0 on npm with frequent releases; active, thousands of stars, about a hundred open issues. The only
production claim is that it powers rUv's own Cognitum. Benchmark and latency figures in its docs are
**claims**, and some are explicitly workload-specific. [src:ruvector-repo]

## Verify live before relying on

- The current npm and crate versions, and whether 1.0 has shipped: [src:ruvector-npm] [src:ruvector-crates]
- The "Known boundaries" section of the README, which changes as limits are fixed: [src:ruvector-repo]
- Postgres extension compatibility with the user's Postgres version and host: [src:ruvector-postgres]

## Related

- **RVF**: RuVector's own file format, in the same repo; the core library saves differently, with redb.
- **AgentDB**: uses `@ruvector` packages, and RuVector as an optional backend.
- **Ruflo**: lists RuVector as optional, and offers a `ruflo-ruvector` plugin.
- Watch the names: the Rust type `AgenticDB` inside `ruvector-core` isn't the npm `agentdb` package.
