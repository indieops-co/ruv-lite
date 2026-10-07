#!/usr/bin/env python3
"""Check that ruv lite is internally consistent. No network, standard library only.

    python3 scripts/validate.py

Checks the SKILL.md frontmatter, every capability card against index.json and sources.json, the eval
scenarios, THE CALL template, the license, and how old the bundled snapshot is. Exits 1 on any ERROR.
"""
import datetime as dt
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLUG = "ruv-lite"
STALE_DAYS = 90
CARD_SECTIONS = ["## In plain words", "## What it's for", "## Use when", "## Avoid when",
                 "## What people use instead", "## Advantages it can buy", "## Lightest path",
                 "## What a full install changes", "## Maturity", "## Verify live before relying on"]
INDEX_FIELDS = ["id", "name", "aliases", "category", "one_line", "card", "status", "snapshot", "sources",
                "use_when", "avoid_when", "advantages", "lightest_path_level"]
ADVANTAGES = {"local execution", "lower latency", "persistent agent memory", "multi-agent coordination",
              "model routing", "portability", "privacy", "offline use", "scale", "reusable learned patterns",
              "cross-session intelligence", "deployment footprint", "specialized performance"}
LEVELS = {"LOW", "MEDIUM", "HIGH", "VERY HIGH"}
DECISIONS = {"USE IT", "CONSIDER LATER", "SKIP IT"}
CALL_LABELS = ["Recommendation:", "rUv technology:", "Keep using now:", "Why:", "Start with:", "Measure:",
               "Reconsider when:", "Not needed now:", "Difficulty:", "Migration risk:", "Complexity avoided:",
               "Confidence:", "Evidence:"]

errors, warnings = [], []
err = errors.append
warn = warnings.append


def load(rel):
    try:
        return json.loads((ROOT / rel).read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as e:
        err(f"{rel}: {e}")
        return None


def check_skill_md():
    text = (ROOT / "SKILL.md").read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    if not m:
        return err("SKILL.md: no frontmatter")
    fm = m.group(1)
    name = re.search(r"^name: (.*)$", fm, re.M)
    desc = re.search(r"^description: (.*)$", fm, re.M)
    if not name or name.group(1).strip() != SLUG:
        err(f"SKILL.md: name must be {SLUG}")
    if not desc:
        return err("SKILL.md: no description")
    d = desc.group(1)
    if len(d) > 1024:
        err(f"SKILL.md: description is {len(d)} characters (max 1024)")
    if set("<>") & set(d):
        err("SKILL.md: description contains angle brackets")
    if "Not for" not in d:
        err("SKILL.md: description needs its 'Not for' clause (BRAND.md)")
    for ref in re.findall(r"`((?:references|assets)/[^`\s]+)`", text):
        if not (ROOT / ref).exists():
            err(f"SKILL.md mentions {ref}, which doesn't exist")


def check_cards(sources):
    index = load("references/capabilities/index.json")
    if not index or sources is None:
        return set()
    source_ids = {s["id"] for s in sources["sources"]}
    for s in sources["sources"]:
        if not s.get("url", "").startswith("https://"):
            err(f"sources.json: {s['id']} has no https url")
    ids, used_sources = set(), set()
    today = dt.date.today()
    for t in index["technologies"]:
        missing = [f for f in INDEX_FIELDS if f not in t]
        if missing:
            err(f"index.json: {t.get('id', '?')} is missing {', '.join(missing)}")
            continue
        tid = t["id"]
        if tid in ids:
            err(f"index.json: duplicate id {tid}")
        ids.add(tid)
        for sid in t["sources"]:
            used_sources.add(sid)
            if sid not in source_ids:
                err(f"index.json: {tid} cites unknown source {sid}")
        bad_adv = set(t["advantages"]) - ADVANTAGES
        if bad_adv:
            err(f"index.json: {tid} has advantages not on the PRD list: {', '.join(sorted(bad_adv))}")
        if t["lightest_path_level"] not in LEVELS:
            err(f"index.json: {tid} lightest_path_level must be one of {sorted(LEVELS)}")
        if not t["use_when"] or not t["avoid_when"]:
            err(f"index.json: {tid} needs both use_when and avoid_when signals")
        try:
            age = (today - dt.date.fromisoformat(t["snapshot"])).days
            if age > STALE_DAYS:
                warn(f"{tid}: snapshot is {age} days old; re-check its sources")
        except ValueError:
            err(f"index.json: {tid} snapshot isn't YYYY-MM-DD")
        card = ROOT / "references" / "capabilities" / t["card"]
        if not card.exists():
            err(f"index.json: {tid} card {t['card']} doesn't exist")
            continue
        body = card.read_text(encoding="utf-8")
        for section in CARD_SECTIONS:
            if section not in body:
                err(f"{t['card']}: missing section '{section}'")
        if t["snapshot"] not in body:
            err(f"{t['card']}: snapshot date {t['snapshot']} isn't in the card")
        for sid in re.findall(r"\[src:([a-z0-9-]+)\]", body):
            if sid in source_ids:
                used_sources.add(sid)
            else:
                err(f"{t['card']}: cites [src:{sid}], which isn't in sources.json")
    # Index-level sources serve grounding.md and ecosystem-map.md, not any one card.
    index_level = {s["id"] for s in sources["sources"] if s.get("kind") == "index"}
    for orphan in sorted(source_ids - used_sources - index_level):
        warn(f"sources.json: {orphan} isn't cited by any card")
    return ids


def check_evals(tech):
    data = load("evals/scenarios.json")
    if not data:
        return
    seen, cats = set(), {}
    for s in data["scenarios"]:
        sid = s.get("id")
        if sid in seen:
            err(f"scenarios.json: duplicate id {sid}")
        seen.add(sid)
        exp = s.get("expected", {})
        if exp.get("decision") not in DECISIONS:
            err(f"scenarios.json: {sid} expected.decision must be one of {sorted(DECISIONS)}")
        if not set(exp.get("acceptable", [])) <= DECISIONS or exp.get("decision") not in exp.get("acceptable", []):
            err(f"scenarios.json: {sid} acceptable must contain the expected decision and only valid decisions")
        if exp.get("technology") not in tech | {"none", "any"}:
            err(f"scenarios.json: {sid} technology '{exp.get('technology')}' isn't in index.json")
        cats[s.get("category")] = cats.get(s.get("category"), 0) + 1
    neg = sum(1 for s in data["scenarios"] if "USE IT" not in s["expected"]["acceptable"])
    pos = sum(1 for s in data["scenarios"] if s["expected"]["decision"] == "USE IT")
    print(f"evals: {len(seen)} scenarios, {pos} positive, {neg} where USE IT would be wrong; "
          + ", ".join(f"{k} {v}" for k, v in sorted(cats.items())))
    if neg < pos:
        warn("evals: fewer negative than positive scenarios; the URR metric needs plenty of negatives")


def check_call_card():
    text = (ROOT / "assets" / "templates" / "call-card.md").read_text(encoding="utf-8")
    block = re.search(r"```\nTHE CALL\n(.*?)```", text, re.S)
    if not block:
        return err("call-card.md: no THE CALL block")
    pos = [block.group(1).find(label) for label in CALL_LABELS]
    if min(pos) < 0:
        err("call-card.md: missing labels " + ", ".join(l for l, p in zip(CALL_LABELS, pos) if p < 0))
    elif pos != sorted(pos):
        err("call-card.md: labels are out of order")
    if "unofficial" not in text:
        err("call-card.md: the unofficial line is missing")


def check_license_and_prices():
    lic = (ROOT / "LICENSE").read_text(encoding="utf-8")
    if re.search(r"\{\{[A-Z]+\}\}|\[[A-Z][A-Z ,/]+\]", lic):
        err("LICENSE has unfilled placeholders")
    for rel in ["README.md", "SKILL.md"]:
        p = ROOT / rel
        if p.exists() and re.search(r"(?<![\w$])\$\d", p.read_text(encoding="utf-8")):
            err(f"{rel}: contains a price; prices live only in the catalogue (BRAND.md)")


def main():
    check_skill_md()
    tech = check_cards(load("references/sources.json"))
    check_evals(tech)
    check_call_card()
    check_license_and_prices()
    for w in warnings:
        print("WARNING", w)
    for e in errors:
        print("ERROR  ", e)
    print(f"{len(errors)} errors, {len(warnings)} warnings")
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
