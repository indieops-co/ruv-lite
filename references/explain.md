# Explain

"What is RVF?", "explain AgentDB like I'm not a database person", "what does Ruflo actually do?" A
plain-English translation, not a sales pitch and not a recommendation.

## Steps

1. Find the technology in `capabilities/index.json` (match on `name`, `aliases` and `id`). If it has no
   card, check `ecosystem-map.md` for what the map says about it, its status and any rename. Beyond that,
   if you can browse, look it up from the sources in `sources.json` (start with the project index); if you
   can't, say you'd only be guessing and stop.
2. Read its card. Use `In plain words`, `Status`, `Use when`, `Avoid when`, `What people use instead` and
   `Lightest path`.
3. If the user's question touches anything time-sensitive (installation, versions, whether a feature exists
   yet), check it live (`grounding.md`).
4. Write it in the shape of `assets/templates/explain.md`: seven parts, one to three sentences each.

## Beginner rules

Explain mode always runs in beginner mode:

- No acronym or jargon word without its meaning beside it the first time. Take meanings from
  `glossary.md`, and if a term isn't there, define it in under fifteen words.
- One idea per sentence. Prefer everyday comparisons ("like a library catalogue that sorts by topic instead
  of title") when they're accurate.
- Name the thing they probably already use (Postgres, a single Claude chat, a folder of notes) before the
  rUv thing.
- Don't invent or round up capabilities to make the explanation tidier. If the project's own docs are vague,
  say "the docs describe it as…" and quote briefly.

## Glossary requests

"What's a swarm?", "what's HNSW?" Answer from `glossary.md` in two or three sentences, and add one line on
where it shows up in the rUv ecosystem, if it does. No seven-part structure for a single term.
