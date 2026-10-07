#!/usr/bin/env python3
"""Run the ruv lite eval scenarios through Claude Code and score the calls.

    python3 scripts/run_evals.py                       # every scenario, bundled snapshot only
    python3 scripts/run_evals.py --only s01,s07        # a few
    python3 scripts/run_evals.py --category trap       # one category
    python3 scripts/run_evals.py --web                 # allow live web checks (slower, costs more)
    python3 scripts/run_evals.py --model sonnet        # cheaper: about $0.30 a scenario
    python3 scripts/run_evals.py --score evals/runs/X  # re-score a finished run, no API calls

Each scenario runs in a throwaway project with the skill copied into .claude/skills/ruv-lite/, through
`claude -p` with read-only tools. Set CLAUDE_BIN if `claude` isn't on your PATH.

The headline metric is the Unnecessary rUv Recommendation Rate (URR): of the scenarios where USE IT is
wrong, how often the skill said USE IT anyway. Target under 10%.

Standard library only.
"""
import argparse
import concurrent.futures as cf
import datetime as dt
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SLUG = "ruv-lite"
DECISIONS = ("USE IT", "CONSIDER LATER", "SKIP IT")
# What make-release.sh leaves out, plus maintainer-only folders: the eval copy is what a user installs.
NOT_SHIPPED = re.compile(r"^(marketing/|guide\.md$|REPO\.md$|PUSH\.md$|RELEASING\.md$|make-release\.sh$|"
                         r"\.gitignore$|\.github/|release/|PLAN[^/]*\.md$|evals/|scripts/)")
CARD_LABELS = ["Recommendation:", "rUv technology:", "Keep using now:", "Why:", "Difficulty:",
               "Migration risk:", "Confidence:", "Evidence:"]


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def shipped_files():
    try:
        out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True).stdout
        files = [f for f in out.splitlines() if f]
    except (subprocess.CalledProcessError, FileNotFoundError):
        files = []
    # Untracked work in progress counts too, so evals can run before the first commit.
    for p in ROOT.rglob("*"):
        rel = p.relative_to(ROOT).as_posix()
        if p.is_file() and not rel.startswith((".git/", ".kilo/")) and rel not in files:
            files.append(rel)
    return [f for f in files if not NOT_SHIPPED.match(f) and "__pycache__" not in f and not f.endswith(".DS_Store")]


def make_project(tmp):
    skill_dir = Path(tmp) / ".claude" / "skills" / SLUG
    for rel in shipped_files():
        dest = skill_dir / rel
        dest.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(ROOT / rel, dest)
    return Path(tmp)


def run_one(sc, args, run_dir):
    claude = args.claude or os.environ.get("CLAUDE_BIN") or shutil.which("claude")
    if not claude:
        sys.exit("Can't find the claude CLI. Put it on PATH or set CLAUDE_BIN.")
    tools = ["Read", "Glob", "Grep", "Skill"] + (["WebSearch", "WebFetch"] if args.web else [])
    prompt = f"/{SLUG} {sc['prompt']}" if not args.natural else sc["prompt"]
    with tempfile.TemporaryDirectory(prefix="ruv-lite-eval-") as tmp:
        project = make_project(tmp)
        cmd = [claude, "-p", prompt, "--output-format", "json", "--no-session-persistence",
               "--setting-sources", "project", "--allowedTools", ",".join(tools),
               "--disallowedTools", "Bash,Edit,Write,NotebookEdit", "--max-budget-usd", str(args.budget)]
        if args.model:
            cmd += ["--model", args.model]
        try:
            proc = subprocess.run(cmd, cwd=project, capture_output=True, text=True, timeout=args.timeout,
                                  stdin=subprocess.DEVNULL)  # claude -p appends piped stdin to the prompt
            raw = proc.stdout
        except subprocess.TimeoutExpired:
            raw, proc = "", None
    text, cost, status = "", None, "no output"
    try:
        data = json.loads(raw)
        text, cost = data.get("result", "") or "", data.get("total_cost_usd")
        status = data.get("subtype", "unknown")  # "success", or why it stopped (e.g. the budget cap)
    except json.JSONDecodeError:
        text = raw or (proc.stderr if proc else "")
        status = "timeout" if proc is None else "unparseable output"
    (run_dir / f"{sc['id']}.json").write_text(raw or "", encoding="utf-8")
    (run_dir / f"{sc['id']}.md").write_text(
        f"<!-- prompt: {sc['prompt']} -->\n<!-- status: {status} -->\n\n{text}\n", encoding="utf-8")
    return {"id": sc["id"], "cost_usd": cost, "status": status}


def tech_ids():
    index = load_json(ROOT / "references" / "capabilities" / "index.json")
    pairs = []
    for t in index["technologies"]:
        for name in [t["id"], t["name"], *t.get("aliases", [])]:
            pairs.append((name.lower(), t["id"]))
    return pairs


def parse_card(text, names):
    rec = re.search(r"Recommendation:\s*(USE IT|CONSIDER LATER|SKIP IT)", text)
    tech = re.search(r"rUv technology:\s*(.+)", text)
    found = {"decision": rec.group(1) if rec else None, "technology": None, "technology_raw": None}
    if tech:
        raw = tech.group(1).strip()
        found["technology_raw"] = raw
        low = raw.lower()
        if low.startswith("none"):
            found["technology"] = "none"
        else:
            # The technology named first wins ("Ruflo (its memory runs on AgentDB)" is about Ruflo);
            # among names starting at the same spot, the longest wins ("ruflo core" over "ruflo").
            hits = []
            for name, tid in names:
                m = re.search(r"(?<![a-z])" + re.escape(name) + r"(?![a-z])", low)
                if m:
                    hits.append((m.start(), -len(name), tid))
            if hits:
                found["technology"] = min(hits)[2]
    # Card hygiene: labels present and in order, the unofficial line, the mode-specific lines.
    positions = [text.find(label) for label in CARD_LABELS]
    found["card_complete"] = all(p >= 0 for p in positions) and positions == sorted(positions)
    found["unofficial_line"] = "unofficial" in text.lower()
    found["evidence_ok"] = bool(re.search(r"Evidence:\s*(Checked live|Bundled snapshot) \d{4}-\d{2}-\d{2}", text))
    if found["decision"] == "USE IT":
        found["mode_lines_ok"] = "Start with:" in text and "Measure:" in text
    elif found["decision"]:
        found["mode_lines_ok"] = "Reconsider when:" in text
    else:
        found["mode_lines_ok"] = False
    return found


def score(run_dir, scenarios):
    names = tech_ids()
    rows = []
    for sc in scenarios:
        path = run_dir / f"{sc['id']}.md"
        if not path.exists():
            continue
        body = path.read_text(encoding="utf-8")
        got = parse_card(body, names)
        m = re.search(r"<!-- status: (.*?) -->", body)
        got["status"] = m.group(1) if m else "unknown"
        exp = sc["expected"]
        ok_decision = got["decision"] in exp["acceptable"]
        # A SKIP IT is about the whole ecosystem, so which technology it names doesn't matter.
        ok_tech = exp["technology"] in ("any", got["technology"]) or (
            got["decision"] == "SKIP IT" and "SKIP IT" in exp["acceptable"])
        rows.append({**sc, "got": got, "pass": ok_decision and ok_tech,
                     "unnecessary": "USE IT" not in exp["acceptable"] and got["decision"] == "USE IT",
                     "missed": exp["decision"] == "USE IT" and got["decision"] == "SKIP IT"})
    return rows


def report(rows, run_dir, costs):
    neg = [r for r in rows if "USE IT" not in r["expected"]["acceptable"]]
    pos = [r for r in rows if r["expected"]["decision"] == "USE IT"]
    pct = lambda a, b: f"{100 * a / b:.0f}%" if b else "n/a"
    urr = sum(r["unnecessary"] for r in neg)
    missed = sum(r["missed"] for r in pos)
    passed = sum(r["pass"] for r in rows)
    cards = sum(r["got"]["card_complete"] for r in rows)
    lines = [
        f"# ruv lite eval: {run_dir.name}", "",
        f"| Metric | Result | Target |", "|---|---|---|",
        f"| **Unnecessary rUv Recommendation Rate** | **{pct(urr, len(neg))}** ({urr}/{len(neg)}) | under 10% |",
        f"| Missed-fit rate (expected USE IT, got SKIP IT) | {pct(missed, len(pos))} ({missed}/{len(pos)}) | under 15% |",
        f"| Scenarios passed | {pct(passed, len(rows))} ({passed}/{len(rows)}) | |",
        f"| Complete THE CALL card | {pct(cards, len(rows))} ({cards}/{len(rows)}) | 100% |",
        f"| Evidence line well-formed | {pct(sum(r['got']['evidence_ok'] for r in rows), len(rows))} | 100% |",
        f"| Unofficial line present | {pct(sum(r['got']['unofficial_line'] for r in rows), len(rows))} | 100% |",
    ]
    errors = [r for r in rows if r["got"]["status"] not in ("success", "unknown")]
    if errors:
        lines.append(f"| Runs that didn't finish | {len(errors)} (see the Got column; raise --budget or --timeout) | 0 |")
    total = sum(c for c in costs.values() if c)
    if total:
        lines.append(f"| Cost | ${total:.2f} | |")
    lines += ["", "| Scenario | Category | Expected | Got | Technology (got) | |", "|---|---|---|---|---|---|"]
    for r in rows:
        mark = "pass" if r["pass"] else ("**UNNECESSARY**" if r["unnecessary"] else "fail")
        if r["got"]["status"] not in ("success", "unknown"):
            mark += f" ({r['got']['status']})"
        lines.append(f"| {r['id']} | {r['category']} | {' / '.join(r['expected']['acceptable'])} "
                     f"({r['expected']['technology']}) | {r['got']['decision']} | {r['got']['technology_raw']} | {mark} |")
    out = "\n".join(lines) + "\n"
    (run_dir / "REPORT.md").write_text(out, encoding="utf-8")
    (run_dir / "results.json").write_text(json.dumps(rows, indent=1), encoding="utf-8")
    print(out)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--only", help="comma-separated scenario ids")
    ap.add_argument("--category", help="run one category")
    ap.add_argument("--web", action="store_true", help="allow WebSearch and WebFetch")
    ap.add_argument("--natural", action="store_true", help="don't prefix /ruv-lite: tests triggering too")
    ap.add_argument("--model", help="model alias or id, e.g. sonnet")
    ap.add_argument("--claude", help="path to the claude CLI")
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--budget", type=float, default=3.0, help="max USD per scenario")
    ap.add_argument("--timeout", type=int, default=600, help="seconds per scenario")
    ap.add_argument("--score", metavar="RUN_DIR", help="re-score an existing run without calling Claude")
    args = ap.parse_args()

    scenarios = load_json(ROOT / "evals" / "scenarios.json")["scenarios"]
    if args.only:
        wanted = set(args.only.split(","))
        scenarios = [s for s in scenarios if s["id"] in wanted]
    if args.category:
        scenarios = [s for s in scenarios if s["category"] == args.category]
    if not scenarios:
        sys.exit("No scenarios matched.")

    costs = {}
    if args.score:
        run_dir = Path(args.score)
    else:
        stamp = dt.datetime.now().strftime("%Y%m%d-%H%M%S") + ("-web" if args.web else "")
        run_dir = ROOT / "evals" / "runs" / stamp
        run_dir.mkdir(parents=True, exist_ok=True)
        print(f"Running {len(scenarios)} scenarios → {run_dir.relative_to(ROOT)}", file=sys.stderr)
        with cf.ThreadPoolExecutor(max_workers=args.jobs) as pool:
            for res in pool.map(lambda s: run_one(s, args, run_dir), scenarios):
                costs[res["id"]] = res["cost_usd"]
                print(f"  {res['id']} done", file=sys.stderr)
    report(score(run_dir, scenarios), run_dir, costs)


if __name__ == "__main__":
    main()
