# RVF (RuVector Format)

| | |
|---|---|
| Category | A portable file format for agent memory and "cognitive containers" |
| Status | Spec is "0.1.0-draft, Status: Research" (2026-02). All packages 0.x: `@ruvector/rvf` 0.3.4, `rvf-runtime` 0.3.2 (2026-07). Open bugs that drop or mangle data. MIT OR Apache-2.0. |
| Snapshot | 2026-10-07 |
| Sources | [src:rvf-readme] [src:rvf-spec] [src:rvf-npm] [src:ruvector-issues] [src:ruvnet-profile] |

## In plain words

A single file that holds an agent's memory together with its history: the vectors (meaning-based search
data), a search index, metadata, and a tamper-evident log of every change. Copy the file and the memory
goes with it, to another machine or another program. Optional sections can also carry code or even a small
bootable system image, which is why its docs call it a "cognitive container". [src:rvf-readme]

## What it's for

Moving memory, and the proof of where it came from, between programs as one file: across Rust, Node.js and
the browser, with cheap copy-on-write branches and signed history. [src:rvf-readme] The rUv profile is
careful to say that carrying a capability in a file doesn't grant permission to run it. [src:ruvnet-profile]

## Use when

- Agent memory has to **move**: between machines, between tools, or shipped to a customer, as one file.
- A signed, tamper-evident history of what an agent knew and when is a real requirement (audit, provenance).
- They already use AgentDB or Ruflo memory, which use `.rvf` files, and want to understand or move those
  files.
- Research or experimentation with the format itself, in a sandbox.

## Avoid when

- Anything production-critical today. The spec is a research draft and there are open bugs where metadata
  is silently dropped, IDs collapse, wrong-sized rows are accepted, and the browser docs show APIs that
  haven't shipped. [src:ruvector-issues]
- Other tools need to read the data. Only rUv tools read `.rvf`.
- "Portable" just means "exportable". JSON Lines, Parquet, a SQLite file, or a database dump already do that.
- The user wants encryption. The log is tamper-evident, not encrypted.

## What people use instead

- **Portable data**: a SQLite file (with sqlite-vec), Lance, Parquet or Arrow files, or JSON Lines with the
  embeddings included.
- **Provenance**: signed releases and attestations (Sigstore, in-toto).
- **Shipping a runnable service**: a container image.

## Advantages it can buy

portability, deployment footprint, offline use, local execution

## Lightest path

**LOW: generate the sample files and look at them**, in a scratch clone of the RuVector repo (needs Rust
1.87+): `cd examples/rvf && cargo run --example generate_all`. [src:rvf-readme]

**LOW: from Node.js in a scratch folder.** `npm install @ruvector/rvf` (Node 18+, prebuilt binaries). Treat
any `.rvf` file as a copy derived from a source of truth you keep elsewhere. [src:rvf-npm]

## What a full install changes

Nothing global for the SDKs: a package and the files you write. Building the bootable-image sections needs
Docker, and running them needs QEMU or Firecracker, which is **HIGH** and far beyond a first trial.
[src:rvf-readme]

## Maturity

Research-status spec, months old, all 0.x. The npm page labels its native backends "Stable", which doesn't
square with the open data-fidelity bugs. Its performance figures (sub-millisecond queries, microsecond cold
boot) are **claims** from its own benchmarks. [src:rvf-spec] [src:rvf-npm]

## Verify live before relying on

- Whether the spec has left draft status: [src:rvf-spec]
- The status of the metadata and ID bugs (#704, #1104–#1107): [src:ruvector-issues]
- Current package versions: [src:rvf-npm]

## Related

- **RuVector**: RVF lives in the RuVector repo (`crates/rvf`).
- **AgentDB**: stores memory as `.rvf` by default.
- **Ruflo**: the `ruflo-rvf` plugin offers "portable agent memory", but saves sessions as JSON and doesn't
  encrypt exported files by default.
- Watch the name: the crates.io crate `rvf` is an unrelated project.
