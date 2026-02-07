# AUD-005 — Internal Audit Report & Findings (ISMS Baseline Audit)
**Document ID:** AUD-005  
**Title:** Internal Audit Report & Findings (ISMS Baseline Audit)  
**Organization:** CloudFin Analytics (B2B SaaS)  
**Audit Lead / Auditor:** Badr Karim  
**Version:** v0.1  
**Status:** Draft  
**Report Date:** 2026-02-07  
**Planned Audit Date:** 2026-02-14  

---

## 1. Executive Summary
A baseline internal audit was performed to evaluate the CloudFin Analytics ISMS documentation, risk management records, control applicability (SoA), and evidence traceability for the initial SaaS assurance portfolio.

Overall status:
- **Strengths observed:** Foundational ISMS documentation exists (Scope, Policy, Risk Method). Evidence-based change management controls are implemented through GitHub protected branch and PR workflow.
- **Key gaps:** Measurable information security objectives are not yet documented; corrective action tracking is not yet formalized; several Annex A controls are declared as Planned without supporting procedures/records.

This report records audit findings and required corrective actions.

---

## 2. Audit Details
### 2.1 Audit Objective
- Determine conformity of the ISMS with ISO/IEC 27001 Clauses 4–10 (baseline readiness)
- Confirm declared Annex A control statuses in ISMS-005 are supported by evidence
- Identify nonconformities and improvement opportunities and initiate corrective actions

### 2.2 Audit Scope
The audit covered the ISMS scope defined in ISMS-001 with emphasis on:
- ISMS documented information (ISMS-001/002/003)
- Risk Register and SoA traceability (ISMS-004/005)
- Evidence Index and supporting evidence records (EV-001 to EV-004)
- Audit program and planning (AUD-001/002/003/004)

### 2.3 Audit Criteria
- ISO/IEC 27001 requirements (Clauses 4–10)
- Annex A controls listed in ISMS-005 (SoA)
- CloudFin ISMS documents and records: ISMS-001 to ISMS-005; EV-INDEX; AUD-001 to AUD-004

### 2.4 Evidence Reviewed (sample)
- ISMS-001 Scope; ISMS-002 Policy; ISMS-003 Risk Method
- ISMS-004 Risk Register; ISMS-005 SoA
- EV-001 GitHub repo created
- EV-002 Protected branch enforced
- EV-003 Dependabot enabled
- EV-004 PR workflow evidence
- AUD-001 Audit Program; AUD-002 Audit Plan; AUD-003 Checklist; AUD-004 Evidence Log

---

## 3. Positive Observations (Strengths)
- **Controlled change workflow is evidenced.** GitHub protected branch and PR review workflow supports change management (SoA A.8.32 marked Implemented) with evidence EV-002 and EV-004.
- **Risk methodology is defined and consistent.** Likelihood/impact scales and treatment thresholds are documented in ISMS-003 and applied in ISMS-004.
- **Traceability structure is established.** Evidence Index (EV-INDEX) exists and evidence items are uniquely identified (EV-###), enabling audit-ready traceability.

---

## 4. Audit Findings Summary
**Total findings:** 5  
- **Minor Nonconformities (Minor NC):** 2  
- **Opportunities for Improvement (OFI):** 3  
- **Major NC:** 0

---

## 5. Detailed Findings

### F-001 — OFI: Information Security Objectives not yet documented
- **Requirement:** ISO 27001 Clause 6.2 (Information security objectives and planning to achieve them)
- **Evidence reviewed:** AUD-003 Check CL-011 indicates objectives are "Not yet documented"; ISMS core documents do not include objectives.
- **Gap:** Measurable information security objectives and a plan to achieve them (owner, metric, target, frequency) are not documented.
- **Impact:** Without objectives, it is harder to measure ISMS performance and demonstrate continual improvement.
- **Classification:** **OFI**
- **Corrective action (recommended):** Create ISMS-006 "ISMS Objectives & Metrics" with 5–7 measurable objectives (e.g., vulnerability remediation SLA, access review completion, backup test cadence).

### F-002 — Minor NC: Corrective action process (CAPA) not established
- **Requirement:** ISO 27001 Clause 10.1 (Nonconformity and corrective action)
- **Evidence reviewed:** AUD-003 Check CL-019 indicates CAPA tracker/process is "Not yet documented".
- **Gap:** A documented method to record nonconformities, assign root cause analysis, define corrective actions, and verify effectiveness is missing.
- **Impact:** Findings may not be consistently tracked to closure, reducing assurance reliability and continual improvement effectiveness.
- **Classification:** **Minor NC**
- **Corrective action (required):** Create AUD-006 CAPA Tracker and a simple CAPA procedure section in AUD-005 or a dedicated procedure document.

### F-003 — OFI: Management Review process not yet defined
- **Requirement:** ISO 27001 Clause 9.3 (Management review)
- **Evidence reviewed:** AUD-003 Check CL-018 indicates management review is "Not yet documented".
- **Gap:** A management review template defining inputs (audit results, risk status, incidents, objectives performance) and outputs (decisions, action items) is missing.
- **Impact:** Leadership oversight and ISMS governance evidence is weaker without a structured review record.
- **Classification:** **OFI**
- **Corrective action (recommended):** Create a one-page Management Review template and schedule quarterly reviews aligned with AUD-001.

### F-004 — Minor NC: Vulnerability management process incomplete (tool enabled but tracking not defined)
- **Requirement:** Annex A A.8.8 (Management of technical vulnerabilities) and ISMS-005 declared status
- **Evidence reviewed:** EV-003 shows Dependabot enabled; ISMS-005 marks A.8.8 as Partial; no remediation SLA/tracking records exist yet.
- **Gap:** While identification is implemented (Dependabot), a defined remediation process (triage, severity, SLA targets, tracking, closure evidence) is not documented.
- **Impact:** Vulnerabilities may remain unresolved and risk acceptance decisions may be unclear, increasing likelihood of exploitation.
- **Classification:** **Minor NC**
- **Corrective action (required):** Create a Vulnerability Management Procedure and start a simple vulnerability log (issue-based) with SLA targets; capture one worked example as evidence (new EV).

### F-005 — OFI: Source code access governance lacks periodic access review record
- **Requirement:** Annex A A.8.4 (Access to source code) and principle of least privilege
- **Evidence reviewed:** EV-002 and EV-004 support PR controls; ISMS-005 marks A.8.4 as Partial with note requiring periodic access review record.
- **Gap:** There is no documented periodic review of who has access to the repository and what permissions they hold.
- **Impact:** Excessive or stale access increases risk of unauthorized changes and data leakage if accounts are compromised.
- **Classification:** **OFI**
- **Corrective action (recommended):** Create an "Access Review Record" template and perform a quarterly repository access review; store as evidence EV.

---

## 6. Conclusion
The CloudFin ISMS portfolio demonstrates a solid baseline with clear scope, policy, risk methodology, and evidence-backed change management controls. To strengthen ISMS readiness and improve hiring credibility, the next priority is to establish objectives, CAPA tracking, management review records, and a documented vulnerability remediation process supported by new evidence items.

