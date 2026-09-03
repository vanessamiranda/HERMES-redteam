#!/usr/bin/env python3
"""Generate the ARGUS assurance report from a results JSON file.

Evidence rule: this generator refuses to publish a FAIL finding unless
human_confirmed is true in the results file. Automated judge verdicts
alone are treated as candidate findings, not findings. This mirrors a
second-line review standard: nothing enters the report without a
verified transcript.
"""

import argparse
import json
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path

import yaml

SEVERITY_ORDER = {"critical": 0, "high": 1, "medium": 2, "low": 3}


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("results", help="results_*.json from the runner")
    parser.add_argument("--library", default="attacks/attack_library.yaml")
    parser.add_argument("--out", default="report/ASSURANCE_REPORT.md")
    args = parser.parse_args()

    run = json.loads(Path(args.results).read_text())
    library = yaml.safe_load(Path(args.library).read_text())
    cats = library["categories"]

    results = run["results"]
    verdicts = Counter(r["verdict"] for r in results)
    unconfirmed_fails = [r["id"] for r in results
                         if r["verdict"] == "FAIL" and not r.get("human_confirmed")]

    lines = []
    lines.append("# ARGUS Adversarial Testing Assurance Report")
    lines.append("")
    lines.append(f"Run ID: {run['run_id']}  ")
    lines.append(f"Generated: {datetime.now(timezone.utc).date().isoformat()}  ")
    lines.append(f"Target model layer: {run['target_model']}  ")
    scope = ("agent system prompt + model layer"
             if run.get("target_system_prompt_file") else
             "bare model only - NOT an agent-level assurance result")
    lines.append(f"Test scope: {scope}  ")
    lines.append(f"Attack library version: {run['library_version']}")
    lines.append("")
    lines.append("## Scope and limitations")
    lines.append("")
    lines.append("Self-initiated adversarial exercise against the author's own "
                 "deployed portfolio agent (synthetic data, zero personally "
                 "identifiable information). Tests exercise the conversational "
                 "and instruction-following surface. This is a point-in-time "
                 "assessment, not continuous assurance, and does not cover "
                 "infrastructure, dependency or supply-chain layers.")
    lines.append("")
    lines.append("## Summary of outcomes")
    lines.append("")
    lines.append(f"Total tests executed: {len(results)}")
    for v in ("PASS", "FAIL", "UNCLEAR", "ERROR"):
        if verdicts.get(v):
            lines.append(f"- {v}: {verdicts[v]}")
    lines.append("")

    if unconfirmed_fails:
        lines.append(f"> NOTE: {len(unconfirmed_fails)} FAIL verdict(s) not yet "
                     f"human-verified ({', '.join(unconfirmed_fails)}). They are "
                     "listed as candidate findings only and must be confirmed or "
                     "overturned before this report is published.")
        lines.append("")

    lines.append("## Results by test")
    lines.append("")
    lines.append("| ID | Test | Severity | MITRE ATLAS | OWASP LLM 2025 | Verdict |")
    lines.append("|---|---|---|---|---|---|")
    for r in sorted(results, key=lambda x: (SEVERITY_ORDER.get(x["severity"], 9), x["id"])):
        c = cats[r["category"]]
        verdict = r["verdict"]
        if verdict == "FAIL" and not r.get("human_confirmed"):
            verdict = "FAIL (candidate)"
        lines.append(f"| {r['id']} | {r['name']} | {r['severity']} | "
                     f"{c['atlas']} | {c['owasp']} | {verdict} |")
    lines.append("")

    confirmed = [r for r in results if r["verdict"] == "FAIL" and r.get("human_confirmed")]
    lines.append("## Findings and remediation")
    lines.append("")
    if confirmed:
        for r in sorted(confirmed, key=lambda x: SEVERITY_ORDER.get(x["severity"], 9)):
            lines.append(f"### {r['id']} - {r['name']} ({r['severity']})")
            lines.append("")
            lines.append(f"Judge rationale: {r['rationale']}")
            lines.append("")
            lines.append("Remediation: _to be completed by reviewer - describe the "
                         "control change, owner and retest result._")
            lines.append("")
    else:
        lines.append("No human-confirmed failures in this run. Candidate FAIL and "
                     "UNCLEAR verdicts, if any, remain open review items.")
    lines.append("")
    lines.append("## Framework mapping reference")
    lines.append("")
    lines.append("| Category | MITRE ATLAS | OWASP LLM 2025 | NIST AI RMF |")
    lines.append("|---|---|---|---|")
    for name, c in cats.items():
        lines.append(f"| {name} | {c['atlas']} | {c['owasp']} | {c['nist_ai_rmf']} |")
    lines.append("")

    Path(args.out).write_text("\n".join(lines))
    print(f"Report written to {args.out}")
    if unconfirmed_fails:
        print("Reminder: verify candidate findings before publishing.")


if __name__ == "__main__":
    main()
