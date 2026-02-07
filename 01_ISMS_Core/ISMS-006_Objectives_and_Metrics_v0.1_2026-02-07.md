# ISMS-006 — Information Security Objectives & Metrics
**Document ID:** ISMS-006  
**Title:** Information Security Objectives & Metrics  
**Organization:** CloudFin Analytics (B2B SaaS)  
**Owner:** Badr Karim  
**Version:** v0.1  
**Status:** Draft  
**Date:** 2026-02-07  

---

## 1. Purpose
Define measurable information security objectives and how CloudFin Analytics will track progress to support continual improvement.

## 2. Objectives and Metrics
| Objective ID | Objective | Metric | Target | Frequency | Owner | Evidence / Records |
|---|---|---|---|---|---|---|
| OBJ-001 | Enforce controlled changes to production-related assets | % of merges to main completed via PR with review | 100% | Monthly | Platform/DevOps Lead | EV-002, EV-004 (protected branch + PR evidence) |
| OBJ-002 | Reduce exposure to known vulnerable dependencies | % of “high/critical” dependency alerts triaged within SLA | ≥ 90% within SLA | Monthly | Engineering Lead | EV-003 + VULN-LOG-001 + EV-008 |
| OBJ-003 | Ensure privileged/source access is reviewed | Completion of repository access review | 100% per quarter | Quarterly | Platform/DevOps Lead | AR-002 + EV-009 |
| OBJ-004 | Improve recovery readiness | Backup restore test completion | 1 successful test / quarter | Quarterly | Platform/DevOps Lead | BC-001 + EV-012 |
| OBJ-005 | Improve incident response readiness | Time to triage security event | ≤ 1 business day | Quarterly | Security/GRC (Badr) | IR-001 + IR-002 + EV-011 |
| OBJ-006 | Increase security awareness in remote-first environment | Training completion rate | 100% | Quarterly | Security/GRC (Badr) | Training record (future EV) |

## 3. Review
Objectives are reviewed during Management Review and updated when risk profile, systems, or business requirements change.

