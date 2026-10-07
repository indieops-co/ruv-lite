# Example: CONSIDER LATER (a Compare)

**User:** compare pgvector and ruvector for our knowledge base. It's about 2,000 support articles in Postgres
with pgvector, and the search works fine. Should we switch?

---

**What you're choosing between.** pgvector adds search-by-meaning to the Postgres you already run.
RuVector is an embedded vector store, written in Rust, that runs inside your program or browser and saves to a
local file; it also has its own Postgres extension.

| Dimension | pgvector | | RuVector |
|---|---|:-:|---|
| Complexity | Already running | ◀ | New dependency or a new Postgres image |
| Maturity | Widely used, stable | ◀ | npm 0.3.x, pre-1.0 |
| Performance | Instant at 2,000 rows | = | Claimed fast; irrelevant at this size |
| Cost | Included in your host | ◀ | Free software; extra ops time |
| Local / privacy | Server-side | ▶ | Can run on-device or offline |
| Scale | Comfortable far past your size | = | Built for large local indexes |
| Learning burden | None | ◀ | New API, Rust-backed builds |
| Reversibility | n/a | ◀ | Its Postgres extension uses its own types; not drop-in |
| Strategic upside | — | ▶ | Offline and in-browser search, agent memory tools |

**What decides it.** Complexity, maturity and reversibility. At 2,000 articles pgvector answers instantly,
and nothing you described needs search to run on a device. RuVector's real edge, local and offline search,
isn't a requirement yet.

```
THE CALL
Recommendation:   CONSIDER LATER
rUv technology:   RuVector (pre-1.0)
Keep using now:   PostgreSQL + pgvector
Why:              Your retrieval works at your size, and RuVector's main advantage (search that runs locally or offline) isn't something you need today.
Reconsider when:  Search has to work offline or inside a desktop or browser app, or agents need their own local memory outside the database.
Difficulty:       Medium
Migration risk:   Low if retrieval sits behind a RetrievalProvider interface
Confidence:       High
Evidence:         Bundled snapshot 2026-10-07, verify before production use
```

*ruv lite is an unofficial guide, not affiliated with rUv or the rUv projects.*

Sources: [RuVector README](https://github.com/ruvnet/RuVector) · [RuVector Postgres extension](https://github.com/ruvnet/RuVector/blob/main/crates/ruvector-postgres/README.md)

---

Why this is a good answer: the scorecard was filled in from where the user stands, a vendor benchmark didn't
sway it, and the trigger is concrete. Cheap next step if they want one: put retrieval behind an interface
now, which costs little and keeps the door open.
