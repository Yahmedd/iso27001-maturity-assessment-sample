"""Score an ISO 27001 maturity assessment and generate Markdown + HTML reports.

Input : assessment.csv (one row per control area, scores 0-5)
Output: report/maturity_report.md and report/maturity_report.html

Standard library only. Usage: python score.py [assessment.csv]
"""
import csv
import html
import sys
from collections import OrderedDict
from pathlib import Path

LEVELS = {0: "Non-existent", 1: "Initial", 2: "Repeatable", 3: "Defined", 4: "Managed", 5: "Optimised"}
PRIORITY_ORDER = {"High": 0, "Medium": 1, "Low": 2}


def load(path):
    with open(path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    for r in rows:
        r["current_score"] = int(r["current_score"])
        r["target_score"] = int(r["target_score"])
        r["gap"] = r["target_score"] - r["current_score"]
    return rows


def by_domain(rows):
    domains = OrderedDict()
    for r in rows:
        domains.setdefault(r["domain"], []).append(r)
    summary = []
    for name, items in domains.items():
        cur = sum(i["current_score"] for i in items) / len(items)
        tgt = sum(i["target_score"] for i in items) / len(items)
        summary.append({"domain": name, "current": cur, "target": tgt, "gap": tgt - cur, "count": len(items)})
    return summary


def roadmap(rows):
    open_items = [r for r in rows if r["gap"] > 0]
    return sorted(open_items, key=lambda r: (PRIORITY_ORDER.get(r["priority"], 9), -r["gap"]))


def write_markdown(rows, domains, overall, path, company):
    lines = [
        f"# ISO/IEC 27001:2022 maturity assessment — {company}",
        "",
        "> Fictional company and data, created for portfolio purposes only.",
        "",
        f"**Overall maturity:** {overall:.1f} / 5 ({LEVELS[round(overall)]})  ",
        f"**Control areas assessed:** {len(rows)}  ",
        f"**High-priority actions:** {sum(1 for r in rows if r['priority'] == 'High' and r['gap'] > 0)}",
        "",
        "## Maturity by domain",
        "",
        "| Domain | Current | Target | Gap |",
        "|---|---|---|---|",
    ]
    for d in sorted(domains, key=lambda d: -d["gap"]):
        lines.append(f"| {d['domain']} | {d['current']:.1f} | {d['target']:.1f} | {d['gap']:.1f} |")
    lines += ["", "## Prioritised roadmap", "", "| # | Priority | Area | ISO 27001 | Regulation | Action |", "|---|---|---|---|---|---|"]
    for n, r in enumerate(roadmap(rows), 1):
        lines.append(f"| {n} | {r['priority']} | {r['control_area']} | {r['iso27001_ref']} | {r['regulation_ref']} | {r['recommendation']} |")
    lines += ["", "## Detailed findings", ""]
    for r in rows:
        lines += [
            f"### {r['id']} — {r['control_area']} ({r['current_score']}/5 → {r['target_score']}/5)",
            f"- **Evidence reviewed:** {r['evidence_reviewed']}",
            f"- **Finding:** {r['finding']}",
            f"- **Recommendation:** {r['recommendation']}",
            "",
        ]
    lines += ["## Scale", ""] + [f"- **{k}** — {v}" for k, v in LEVELS.items()]
    path.write_text("\n".join(lines) + "\n", encoding="utf-8")


def write_html(rows, domains, overall, path, company):
    e = html.escape
    bars = "".join(
        f"<tr><td>{e(d['domain'])}</td><td><div class='bar'><span class='cur' style='width:{d['current'] * 20:.0f}%'></span>"
        f"<span class='tgt' style='left:{d['target'] * 20:.0f}%'></span></div></td><td>{d['current']:.1f} / {d['target']:.1f}</td></tr>"
        for d in domains
    )
    road = "".join(
        f"<tr><td>{n}</td><td class='p{e(r['priority'])}'>{e(r['priority'])}</td><td>{e(r['control_area'])}</td>"
        f"<td>{e(r['iso27001_ref'])}</td><td>{e(r['recommendation'])}</td></tr>"
        for n, r in enumerate(roadmap(rows), 1)
    )
    page = f"""<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<title>Maturity Assessment</title><style>
body{{font-family:Arial,sans-serif;max-width:960px;margin:24px auto;padding:0 16px;color:#1f1f1f}}
h1{{color:#07536F}} table{{border-collapse:collapse;width:100%;margin:12px 0}} td,th{{border-bottom:1px solid #dde7eb;padding:6px;text-align:left;vertical-align:top}}
.bar{{position:relative;height:14px;background:#eef5f8;border-radius:7px;min-width:160px}} .cur{{position:absolute;left:0;top:0;bottom:0;background:#07536F;border-radius:7px}}
.tgt{{position:absolute;top:-3px;bottom:-3px;width:3px;background:#e0a100}} .pHigh{{color:#b42318;font-weight:bold}} .pMedium{{color:#b54708}} .pLow{{color:#067647}}
.kpi{{font-size:28px;font-weight:bold;color:#07536F}} .note{{color:#666;font-size:13px}}</style></head><body>
<h1>ISO/IEC 27001:2022 maturity assessment — {e(company)}</h1>
<p class="note">Fictional company and data, created for portfolio purposes only.</p>
<p>Overall maturity: <span class="kpi">{overall:.1f} / 5</span> ({LEVELS[round(overall)]})</p>
<h2>Maturity by domain</h2><p class="note">Blue bar = current score, orange line = target.</p><table>{bars}</table>
<h2>Prioritised roadmap</h2><table><tr><th>#</th><th>Priority</th><th>Area</th><th>ISO 27001</th><th>Action</th></tr>{road}</table>
</body></html>"""
    path.write_text(page, encoding="utf-8")


def main():
    src = Path(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("assessment.csv"))
    company = "Velmora Payments (fictional)"
    rows = load(src)
    domains = by_domain(rows)
    overall = sum(r["current_score"] for r in rows) / len(rows)
    out = src.parent / "report"
    out.mkdir(exist_ok=True)
    write_markdown(rows, domains, overall, out / "maturity_report.md", company)
    write_html(rows, domains, overall, out / "maturity_report.html", company)
    print(f"Overall maturity {overall:.2f}/5 across {len(rows)} areas -> {out}")


if __name__ == "__main__":
    main()
