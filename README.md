# ISO 27001 ISMS / GRC Portfolio (Audit-Grade) — CloudFin SaaS Scenario

This repository is an **audit-grade ISO/IEC 27001 ISMS portfolio** built for a fictional B2B SaaS (“CloudFin Analytics”). It is designed to demonstrate **US-market GRC / ISMS / internal audit capability** with **verifiable traceability** and evidence (EV-001..EV-015).

## What this proves (skills)
- Build an ISO 27001 ISMS set: scope, policy, risk method, objectives, documented information control
- Maintain **traceability**: Risk → SoA Control → Evidence → Internal Audit → CAPA → Verification
- Write audit-grade findings (Requirement → Evidence → Gap → Impact → Classification)
- Document operational controls and records: IR plan & tabletop, backup/restore testing, supplier assessment, vulnerability workflow, access review, awareness training

## 10-minute reviewer path (open in this order)
1) **RECRUITER-ONE-PAGER.md**
2) **CASE-STUDY.md** (baseline audit → findings → CAPA → follow-up verification)
3) **PORTFOLIO-MAP.md** (ISO clauses → exact artifacts + evidence)
4) **04_Evidence/EV-INDEX_Evidence_Index_v0.1_2026-02-07.csv** (master evidence list EV-001..EV-015)
5) **03_Audit_Pack/AUD-005_Audit_Report_Findings_v0.1_2026-02-07.md**
6) **03_Audit_Pack/AUD-008_Followup_Audit_Report_v0.1_2026-02-07.md**
7) **02_Registers/ISMS-005_SoA_v0.1_2026-02-07.csv**

## Validation (audit-grade checks)
Run:
```bash
python3 healthcheck.py
