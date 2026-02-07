# AUD-001 — Internal Audit Program (ISMS)
**Document ID:** AUD-001  
**Title:** Internal Audit Program (ISMS)  
**Organization:** CloudFin Analytics (B2B SaaS)  
**Owner:** Badr Karim  
**Version:** v0.1  
**Status:** Draft  
**Date:** 2026-02-07  

---

## 1. Purpose
This document defines the internal audit program for the CloudFin Analytics ISMS to evaluate conformity to ISO/IEC 27001 requirements and to CloudFin ISMS documented information, and to support continual improvement through corrective actions.

## 2. Audit Criteria (What we audit against)
Internal audits will assess conformity against:
- ISO/IEC 27001 requirements (Clauses 4–10)
- Applicable Annex A controls recorded in the Statement of Applicability (ISMS-005)
- CloudFin ISMS documented information (ISMS-001, ISMS-002, ISMS-003, ISMS-004, ISMS-005)
- Relevant records and evidence referenced in the Evidence Index (EV-INDEX)

## 3. Audit Scope (What areas are covered)
Internal audits cover the ISMS scope defined in ISMS-001, including:
- Governance and ISMS documentation control
- Risk assessment, risk treatment, and SoA maintenance
- Change management and secure development workflow (GitHub/CI-CD controls)
- Vulnerability identification and remediation approach
- Logging/monitoring, backup, incident management readiness (as implemented)
- Supplier security and remote working controls (as implemented)

## 4. Audit Frequency and Schedule (2026)
The ISMS will be audited at least quarterly. The schedule below is risk-based and may be adjusted after major changes or incidents.

### 4.1 Planned Audit Events
- **Q1 Internal Audit:** 2026-02-14 (initial ISMS baseline audit)
- **Q2 Internal Audit:** 2026-05-15 (follow-up: verify CAPA closure + expansion of technical controls evidence)
- **Q3 Internal Audit:** 2026-08-14 (supplier security + incident readiness focus)
- **Q4 Internal Audit:** 2026-11-13 (full ISMS readiness review)

## 5. Roles, Independence, and Competence
- **Audit Lead / Auditor:** Badr Karim (Security/GRC)
- Where independence is needed beyond a single-person scenario, review/approval of audit outputs can be performed by a designated management role (simulated for portfolio purposes).
- Auditor competence is supported through ISO 27001 study and structured audit method, including evidence-based sampling and formal findings documentation.

## 6. Audit Method (How audits are performed)
Audits are conducted using:
- Document review (policies, registers, SoA, records)
- Evidence review (screenshots, tickets, PRs, configuration records)
- Interviews (engineering, platform/devops, support) as applicable to the scenario
- Sampling (select representative records rather than 100% review)

## 7. Audit Outputs (Records)
Each audit produces:
- Audit Plan (AUD-002)
- Audit Checklist (AUD-003)
- Evidence Log (AUD-004)
- Audit Report & Findings (AUD-005)
- CAPA Tracker (AUD-006)

## 8. Review of the Audit Program
This audit program is reviewed at least annually and updated after significant changes, incidents, or repeated nonconformities.

