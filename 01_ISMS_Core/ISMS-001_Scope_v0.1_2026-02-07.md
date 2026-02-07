# ISMS-001 — ISMS Scope (CloudFin Analytics)
**Document ID:** ISMS-001  
**Title:** ISMS Scope  
**Organization:** CloudFin Analytics (B2B SaaS)  
**Owner:** Badr Karim  
**Version:** v0.1  
**Status:** Draft  
**Date:** 2026-02-07  

---

## 1. Purpose
This document defines the scope and boundaries of the Information Security Management System (ISMS) for CloudFin Analytics to protect the confidentiality, integrity, and availability of information processed, stored, or transmitted in support of the CloudFin SaaS service.

## 2. Organization Overview
CloudFin Analytics is a B2B SaaS provider delivering a cloud-hosted financial analytics platform to SMB customers. The service processes customer account data, subscription/billing information, support ticket content (which may include PII), and operational telemetry such as application and security logs.

## 3. ISMS Scope Statement
The ISMS applies to the people, processes, technology, and information assets used to develop, operate, and support the CloudFin Analytics SaaS platform, including:
- SaaS application components (web application and APIs)
- Source code repositories and CI/CD pipeline used to build and deploy the service
- Production hosting environment and configurations used to run the service
- Identity and access management for corporate and production systems
- Logging, monitoring, incident management, and event reporting processes
- Backup and restore processes for in-scope information and service components
- Customer support operations, including handling and retention of support records
- Supplier and third-party service management for tools and services used in scope

## 4. In-Scope Functions, Teams, and Tools
In scope are the following functions and teams:
- Engineering (application development and maintenance)
- Platform/DevOps (deployment, configuration, and operational stability)
- Customer Support (customer communications and ticket handling)
- Security/GRC (ISMS governance, risk management, assurance activities)
- Management (oversight, objectives, and ISMS resourcing)

Supporting tools and services used to deliver the above are considered in scope where they store, process, or provide access to in-scope information.

## 5. Locations and Working Model
CloudFin Analytics operates as a remote-first organization. The scope includes remote access to corporate and production systems through approved identities and controlled access methods.

## 6. Out-of-Scope Items
The following are explicitly out of scope for this ISMS:
- Customer-owned endpoints, customer internal networks, and customer-managed configurations
- Third-party systems not used to develop, host, or support the CloudFin SaaS service
- Personal devices not enrolled in company security controls (addressed via policy requirements for remote work and access)

## 7. Interested Parties
Key interested parties relevant to the ISMS include:
- Customers (expect security and service reliability)
- Employees and contractors (require controlled access, clear procedures, and awareness)
- Suppliers and service providers (must meet contractual and security expectations)
- Applicable contractual or regulatory obligations relevant to customer data and service delivery

## 8. Interfaces and Dependencies
The CloudFin service depends on third-party services for selected operational capabilities (e.g., source control, ticketing, communications, cloud hosting). Supplier security requirements and ongoing supplier oversight are managed through the ISMS.

