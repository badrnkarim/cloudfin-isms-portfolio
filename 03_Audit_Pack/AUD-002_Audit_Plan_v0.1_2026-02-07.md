# AUD-002 — Internal Audit Plan (ISMS Baseline Audit)
**Document ID:** AUD-002  
**Title:** Internal Audit Plan (ISMS Baseline Audit)  
**Organization:** CloudFin Analytics (B2B SaaS)  
**Owner / Audit Lead:** Badr Karim  
**Version:** v0.1  
**Status:** Draft  
**Date:** 2026-02-07  
**Planned Audit Date:** 2026-02-07  

---

## 1. Audit Objective
The objective of this internal audit is to:
- Determine conformity of the ISMS with ISO/IEC 27001 requirements (Clauses 4–10)
- Confirm that applicable Annex A controls recorded in the SoA (ISMS-005) are implemented to the declared status and supported by evidence
- Identify improvement opportunities and nonconformities, and initiate corrective actions (CAPA)

## 2. Audit Scope
This audit covers the ISMS scope defined in ISMS-001, focusing on:
- ISMS documented information and governance (scope, policy, risk method)
- Risk assessment outputs (risk register) and control applicability (SoA)
- Change management evidence in GitHub and operational records (EV-INDEX)
- Vulnerability management evidence in GitHub (Dependabot) and tracking approach
The audit does not attempt to validate all technical controls in-depth; it validates declared implementation status and evidence traceability for the baseline portfolio.

## 3. Audit Criteria
- ISO/IEC 27001 requirements (Clauses 4–10)
- Statement of Applicability (ISMS-005) and its declared implementation status
- CloudFin internal documents: ISMS-001, ISMS-002, ISMS-003, ISMS-004, ISMS-005
- Evidence records in EV-INDEX (EV-###)

## 4. Audit Team and Auditees
- **Audit Lead / Auditor:** Badr Karim
- **Auditees (scenario roles):** Engineering Lead, Platform/DevOps Lead, Customer Support Lead, Management (simulated)

## 5. Audit Method and Sampling
- Review of documented information (ISMS core documents and registers)
- Review of evidence records (screenshots of GitHub settings and PR workflow)
- Sampling approach: verify a representative set of controls and records:
  - Change management (A.8.32): verify protected branch rule + PR evidence
  - Technical vulnerability management (A.8.8): verify Dependabot enablement
  - Source code access (A.8.4): verify PR workflow and restrictions evidence
- Record findings using: Requirement → Evidence (EV-###) → Gap → Impact → Classification

## 6. Audit Agenda (Planned)
**09:00 – 09:15** Opening meeting (objective, scope, criteria, method)  
**09:15 – 10:00** ISMS documentation review (ISMS-001/002/003)  
**10:00 – 10:45** Risk & SoA review (ISMS-004/005) and traceability checks  
**10:45 – 11:30** Evidence review (EV-INDEX, EV-001 to EV-004)  
**11:30 – 12:00** Findings drafting + CAPA initiation  
**12:00 – 12:15** Closing meeting (results, next steps, CAPA owners/dates)

## 7. Audit Deliverables
- AUD-003 Audit Checklist (next document)
- AUD-004 Evidence Log (next document)
- AUD-005 Audit Report & Findings
- AUD-006 CAPA Tracker

