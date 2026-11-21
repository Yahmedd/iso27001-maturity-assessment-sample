# ISO 27001 maturity assessment — sample (fictional company)

A complete example of an ISO/IEC 27001:2022 maturity assessment, the kind a security consultant delivers before an ISMS project or a NIS2/DORA readiness review.

**Velmora Payments is a fictional company.** All evidence, findings and scores are invented for this portfolio and do not describe any real organisation.

## Scenario

Velmora Payments is a fictional 120-person payment fintech: cloud-hosted platform, SaaS office tools, an in-house development team. It wants ISO 27001 certification within 12 months and must prepare for DORA as a financial entity.

## What's inside

| File | Content |
|---|---|
| [`assessment.csv`](assessment.csv) | 20 control areas across 11 domains: ISO 27001 reference, NIS2/DORA reference, current and target score (0–5), evidence reviewed, finding, recommendation, priority |
| [`score.py`](score.py) | Python script (standard library only) that scores the assessment and generates the reports |
| [`report/maturity_report.md`](report/maturity_report.md) | Generated report: overall maturity, maturity by domain, prioritised roadmap, detailed findings |
| [`report/maturity_report.html`](report/maturity_report.html) | Same report as a one-page HTML dashboard |
| [`ebios-rm/`](ebios-rm/README.md) | Full EBIOS Risk Manager analysis (5 workshops, in French) building on the assessment's findings |

## Method

1. **Scope and evidence:** for each control area, review documents, configurations and records, and interview owners.
2. **Score** on a 0–5 maturity scale: 0 Non-existent · 1 Initial · 2 Repeatable · 3 Defined · 4 Managed · 5 Optimised.
3. **Set a target** per area, based on risk and the certification/regulatory goal.
4. **Prioritise** the gaps (High / Medium / Low) and turn them into a roadmap.
5. **Map** every area to ISO 27001:2022 and to NIS2/DORA, so one roadmap serves certification and compliance. See the companion project `nis2-dora-iso27001-mapping`.

## Run it

```bash
python score.py
```

Edit `assessment.csv` with your own data and rerun to regenerate the reports.

Author: Ahmed Mejbri, Security Engineer (ISO 27001 GRC + infrastructure security).
