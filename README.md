# CloudFin ISMS Portfolio (ISO/IEC 27001) — GRC / ISMS Demonstration

This repository is a **hands-on ISMS portfolio** for a fictional B2B SaaS (“CloudFin Analytics”). It demonstrates practical capability in:
- **ISO 27001 ISMS documentation** (scope, policy, risk method, objectives)
- **Risk management + SoA + traceable evidence**
- **Internal audit program + findings + CAPA closure + management review**
- Real operational controls documented with records:
  **Incident Response**, **Backup/Restore testing**, **Supplier assessment**, **Vulnerability management**, **Repo access review**, **Security awareness training**

## 10-minute review path (what a hiring manager should open)
1) **RECRUITER-ONE-PAGER.md** — fast summary of what I built  
2) **CASE-STUDY.md** — story: baseline audit → findings → CAPA → follow-up verification  
3) **PORTFOLIO-MAP.md** — ISO clauses → exact files + evidence  
4) **04_Evidence/EV-INDEX...csv** — evidence master index (EV-001..EV-015)  
5) **03_Audit_Pack/AUD-005** + **AUD-008** — findings + closure verification  
6) **02_Registers/ISMS-005_SoA...csv** — controls + implementation status + evidence IDs  
7) Run: `python3 healthcheck.py` — validates evidence traceability and basic audit-grade rules

## Repository structure
- `01_ISMS_Core/` — core ISMS documents + procedures + records (IR/BC/TRN/VULN/SUP/etc.)
- `02_Registers/` — Risk Register, SoA, Document Register, Supplier Register, Vulnerability Log
- `03_Audit_Pack/` — Audit program, plan, checklist, evidence log, findings, CAPA, follow-up
- `04_Evidence/` — screenshots and proof files + Evidence Index (EV-INDEX)
- `NIST-CSF-MAP.md` + `SOC2-SECURITY-MAP.md` — high-level crosswalks (optional)

## What this portfolio proves (skills)
- Can build an ISMS set that matches ISO 27001 clauses 4–10 (portfolio scenario)
- Can maintain **traceability**: Risk → SoA control → Evidence → Audit → CAPA → Verification
- Can write audit-grade artifacts: findings quality (Requirement/Evidence/Gap/Impact/Class)
- Can document operational controls: IR plan & tabletop, backup/restore test, supplier assessment, vulnerability workflow, access review, training records

## Notes
- CloudFin is fictional; records are portfolio-simulated but structured to real audit expectations.
- No secrets are included; all evidence is safe for public viewing.
