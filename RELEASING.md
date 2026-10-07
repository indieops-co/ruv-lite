# Releasing ruv lite

Maintainer notes. This file never ships: `make-release.sh` leaves it out, along with `marketing/`, `guide.md`
and itself. The standard every release has to meet is "Skilllet release requirements" in
`../../indieops-brand/BRAND.md`.

| | |
|---|---|
| Catalogue ID | `2026-22` (permanent) |
| Slug, skill name, shipped folder | `ruv-lite` |
| Repo and local folder | `ruv-lite` (GitHub `indieops-co/ruv-lite`, public; renamed from `rUv-vs` on 2026-10-07) |
| License | IndieOps Free License v1.0 (catalogue `price` is 0) |
| Product brief | `../../Internal/ruv-lite/PRD.txt` (kept out of this public repo) |

The PRD asked for MIT. BRAND.md says Skilllets are never MIT, so this ships under the IndieOps Free License,
decided 2026-10-07.

## The one thing that goes stale: the snapshot

The capability cards are dated. rUv projects ship weekly (Ruflo near-daily), so re-check the cards whenever
the snapshot passes 90 days, and before every release. `validate.py` warns when a card is over 90 days old.

1. For each card, re-read the sources named in its "Verify live before relying on" section (`sources.json`
   has raw and registry URLs). Check the version and labels, the install path, what a full install writes,
   and the known problems.
2. Update the card's facts and its `Snapshot` date, and the matching `snapshot` in `capabilities/index.json`
   and `sources.json`. Update the snapshot date quoted in `README.md` and `references/examples/`.
3. Re-check `ecosystem-map.md` against rUv's `llms.txt` and `data/projects.json`.
4. If a card's maturity changed (an alpha went stable, a spec left draft), revisit the eval scenarios that
   cite it: their acceptable calls may change.

Facts that moved fastest in the first snapshot: Ruflo's plugin list and counts, AgentDB's release status,
RVF's open data bugs, SPARC v1.0's npm publication, and RuvNet Brain's hook list.

## Cutting a release

1. **Bump the version** in `SKILL.md` (`metadata.version`) and tag `v<version>`. The first public release is
   `1.0.0`.
2. **Check the skill:**
   ```bash
   python3 scripts/validate.py
   ```
   It checks the frontmatter (name matches the folder, description under 1024 characters, no angle brackets,
   the "Not for" clause), every card against the index and sources, the eval file, THE CALL template, the
   license and the no-prices rule.
3. **Run the evals** and record the result here:
   ```bash
   python3 scripts/run_evals.py            # snapshot only
   python3 scripts/run_evals.py --web      # with live checks
   ```
   Release gates: Unnecessary rUv Recommendation Rate **under 10%**, complete THE CALL card on every run.
   Target for later versions: under 5%. See `evals/README.md`.
4. **The rest of the release checklist** in BRAND.md:
   - **Guide:** edit `guide.md`, then rebuild so the chooser matches the catalogue:
     `node ../../indieops-brand/scripts/build-guide.mjs --skill ruv-lite --in guide.md --out guide.html`
   - **Cover:** `ruv-lite-cover.html`, made from LaunchSkeptic's layout with the one-icon theme toggle. Check it
     in light and dark, at desktop and 390px.
   - **Demo GIF:** `docs/demo.gif` and `docs/demo-dark.gif` (not made yet).
   - **Launch post:** `../../Internal/ruv-lite/launch-post.md`, because the repo is public.
5. **Build the zip:** `./make-release.sh` → `release/IndieOps-Skilllet-2026-22-ruvlite-v<version>.zip`,
   unzipping to `ruv-lite/`.
6. Set the catalogue entry's `status` to `shipped` once it's downloadable.

## Eval results

| Date | Version | Mode | URR | Missed fits | Passed | Card complete | Notes |
|---|---|---|---|---|---|---|---|
| 2026-10-07 | 0.1.0 | Sonnet, snapshot | 0% (0/31) | 1/8 | 38/40 | 40/40 | First full run. Too conservative: 2/8 positives got USE IT; it treated a do-it-yourself native build as free. |
| 2026-10-07 | 0.1.0 | Sonnet, snapshot | 0% (0/7) | 0/8 | 15/15 | 15/15 | After the honest-baseline rule and Ruflo plugin table: 6/8 positives USE IT. Re-ran the 15 calibration-sensitive scenarios only; run all 40 before release. |
| 2026-10-07 | 0.1.0 | Sonnet, snapshot | 0% (0/32) | 0/8 | 40/40 | 40/40 | Full run after calibration. USE IT on 6/8 positives (s03 and s08 got a defensible CONSIDER LATER). Cost about $6. |
