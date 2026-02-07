# IR-002 — Incident Response Tabletop Exercise Record
**Record ID:** IR-002  
**Scenario:** Compromised developer token leads to unauthorized repo access  
**Date:** 2026-02-07  
**Facilitator:** Badr Karim  
**Attendees:** Security/GRC, Engineering Lead (Simulated), Platform/DevOps Lead (Simulated)

## Timeline Decisions
- Detection: unusual access flagged, review audit logs  
- Containment: revoke token, enforce MFA, rotate secrets  
- Eradication: remove compromised access, review permissions  
- Recovery: verify no malicious changes merged (branch protection)  
- Lessons learned: add periodic access review record and security training refresh

## Outputs
- Action: confirm quarterly access reviews (AR-002)  
- Action: update training record (TRN-001 planned)

