# ISMS-003 — Information Security Risk Assessment Methodology
**Document ID:** ISMS-003  
**Title:** Information Security Risk Assessment Methodology  
**Organization:** CloudFin Analytics (B2B SaaS)  
**Owner:** Badr Karim  
**Version:** v0.1  
**Status:** Draft  
**Date:** 2026-02-07  

---

## 1. Purpose
This methodology defines how CloudFin Analytics identifies, analyzes, evaluates, and treats information security risks within the ISMS scope. The output of this process is used to select risk treatments and supporting controls (including Annex A controls) and to maintain a documented risk register.

## 2. Scope
This methodology applies to all in-scope information assets, processes, and supporting services described in ISMS-001 (ISMS Scope), including the CloudFin SaaS application, production environment, CI/CD pipeline, corporate tooling, customer support operations, and relevant suppliers.

## 3. Definitions
- **Asset/Process:** Anything of value that supports the service (e.g., production database, CI/CD pipeline, support ticket system).
- **Threat:** A potential cause of an unwanted incident (e.g., credential theft, misconfiguration, insider misuse).
- **Vulnerability:** A weakness that can be exploited (e.g., missing MFA, weak change control, excessive permissions).
- **Impact:** The potential consequence if the risk occurs (confidentiality, integrity, availability, legal, financial, reputational).
- **Likelihood:** The probability of the risk occurring given current controls.
- **Risk Owner:** The role responsible for managing the risk and ensuring treatment actions are implemented.

## 4. Risk Identification
Risks are identified using one or more of the following:
- Review of processes and assets within scope (engineering, platform, support, suppliers)
- Review of changes (new features, infrastructure changes, new vendors)
- Review of incidents, near-misses, and security events
- Review of known threat patterns relevant to SaaS environments (e.g., account takeover, data exposure)
Each risk is documented with: Asset/Process, Threat, Vulnerability, and a short risk statement.

## 5. Risk Analysis (Scoring)
CloudFin Analytics uses a 5x5 qualitative scoring model.

### 5.1 Likelihood Scale (1–5)
1. **Rare:** Highly unlikely; would require exceptional circumstances  
2. **Unlikely:** Not expected but possible  
3. **Possible:** Could occur under normal conditions  
4. **Likely:** Expected to occur in many circumstances  
5. **Almost Certain:** Expected to occur frequently

### 5.2 Impact Scale (1–5)
1. **Insignificant:** Minimal disruption; no sensitive data; no customer impact  
2. **Minor:** Limited internal impact; small service degradation; easily recoverable  
3. **Moderate:** Customer-visible impact; limited sensitive data exposure; measurable operational cost  
4. **Major:** Significant customer impact; sensitive data exposure; regulatory/contractual breach possible  
5. **Severe:** Large-scale data exposure or prolonged outage; major contractual/regulatory consequences; severe reputational damage

### 5.3 Risk Score Calculation
**Risk Score = Likelihood × Impact** (range 1–25)

## 6. Risk Evaluation (Risk Appetite & Treatment Thresholds)
Risk scores are interpreted as follows:
- **1–6 (Low):** Accept or monitor
- **7–14 (Medium):** Treat with planned controls and actions; monitor
- **15–25 (High):** Treat as priority; management attention required; monitor closely until reduced

## 7. Risk Treatment Options
For each risk, one or more of the following treatment approaches is selected:
- **Avoid:** Stop the activity that creates the risk
- **Reduce:** Apply controls to reduce likelihood and/or impact
- **Transfer:** Shift risk to a third party (e.g., contractual, insurance)
- **Accept:** Formally accept the risk within appetite, with documented justification

## 8. Control Selection and Traceability
When treating risks, controls are selected and documented with clear traceability:
- Risk Register entries reference treatment controls (including relevant Annex A controls)
- The Statement of Applicability (SoA) records which Annex A controls are applicable, justification, implementation status, and evidence references (EV-###)
- Operational records (evidence) are maintained to demonstrate control operation (e.g., branch protection settings, pull request approvals, vulnerability alerts)

## 9. Review Frequency
- The Risk Register is reviewed at least quarterly and upon significant changes (new vendors, major releases, incidents).
- High risks are reviewed more frequently until reduced to an acceptable level.

## 10. Outputs (Records)
This methodology produces and maintains:
- **ISMS-004 Risk Register**
- **ISMS-005 Statement of Applicability (SoA)**
- Supporting evidence records referenced in the Evidence Index (EV-INDEX)
