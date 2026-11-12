# ISO/IEC 27001:2022 maturity assessment — Velmora Payments (fictional)

> Fictional company and data, created for portfolio purposes only.

**Overall maturity:** 1.7 / 5 (Repeatable)  
**Control areas assessed:** 20  
**High-priority actions:** 11

## Maturity by domain

| Domain | Current | Target | Gap |
|---|---|---|---|
| Risk | 0.5 | 4.0 | 3.5 |
| Suppliers | 1.0 | 4.0 | 3.0 |
| Incidents | 1.0 | 4.0 | 3.0 |
| Governance | 1.0 | 3.7 | 2.7 |
| Assets | 1.5 | 3.5 | 2.0 |
| Continuity | 1.5 | 3.5 | 2.0 |
| People | 2.0 | 4.0 | 2.0 |
| Identity and access | 2.3 | 4.3 | 2.0 |
| Operations | 2.3 | 4.0 | 1.7 |
| Cryptography | 3.0 | 4.0 | 1.0 |
| Development | 3.0 | 4.0 | 1.0 |

## Prioritised roadmap

| # | Priority | Area | ISO 27001 | Regulation | Action |
|---|---|---|---|---|---|
| 1 | High | Risk treatment and SoA | cl. 6.1.3 | NIS2 21(2)(a) | Build the SoA and a risk treatment plan with deadlines |
| 2 | High | Roles and responsibilities | A.5.2; cl. 5.3 | NIS2 Art. 20; DORA Art. 5 | Appoint a security owner and publish a RACI for security activities |
| 3 | High | Risk assessment method | cl. 6.1.2 | NIS2 21(2)(a); DORA Art. 6 | Define a 5x5 likelihood/impact method and assign an owner to every risk |
| 4 | High | Supplier security | A.5.19; A.5.20; A.5.22 | NIS2 21(2)(d); DORA Art. 28 | Create a register of ICT providers and add security and exit clauses at renewal |
| 5 | High | Incident management process | A.5.24; A.5.25; A.5.26 | NIS2 Art. 23; DORA Art. 17-19 | Define the incident process with classification criteria and the 24h/72h reporting steps |
| 6 | High | Information security policy | A.5.1 | NIS2 21(2)(a); DORA Art. 6 | Approve the policy in a management meeting and set a yearly review date |
| 7 | High | Access control policy | A.5.15; A.5.18 | NIS2 21(2)(i); DORA Art. 9 | Run quarterly access reviews for critical systems and record them |
| 8 | High | Multi-factor authentication | A.8.5 | NIS2 21(2)(j); DORA Art. 9 | Enforce MFA on all administrative and developer accounts |
| 9 | High | Privileged access | A.8.2 | DORA Art. 9 | Reduce standing admin rights; use time-limited elevation and log its use |
| 10 | High | Vulnerability management | A.8.8 | NIS2 21(2)(e); DORA Art. 9 | Set patch deadlines per severity and track them to closure |
| 11 | High | Backups and restore tests | A.8.13 | NIS2 21(2)(c); DORA Art. 12 | Perform and document a restore test every quarter |
| 12 | Medium | Management review | cl. 9.3 | NIS2 Art. 20; DORA Art. 6 | Hold a first management review using the cl. 9.3 inputs and record decisions |
| 13 | Medium | Asset inventory | A.5.9 | DORA Art. 8 | Extend the inventory to SaaS and data; add owner and classification columns |
| 14 | Medium | Information classification | A.5.12; A.5.13 | DORA Art. 8 | Adopt a 3-level scheme (Public / Internal / Confidential) and label key repositories |
| 15 | Medium | Logging and monitoring | A.8.15; A.8.16 | DORA Art. 10 | Centralise logs and alert on privileged and authentication events |
| 16 | Medium | ICT continuity plan | A.5.29; A.5.30 | NIS2 21(2)(c); DORA Art. 11 | Write a recovery plan with RTO/RPO for critical services and test it once a year |
| 17 | Medium | Awareness and training | A.6.3 | NIS2 Art. 20 and 21(2)(g) | Run a yearly awareness programme including a session for management |
| 18 | Medium | Change management | A.8.32 | DORA Art. 9 | Apply the same review and approval flow to infrastructure changes |
| 19 | Medium | Secure development | A.8.25; A.8.28; A.8.29 | NIS2 21(2)(e) | Add secret scanning and a security test step to the release pipeline |
| 20 | Low | Encryption of data | A.8.24 | NIS2 21(2)(h); DORA Art. 9 | Document key ownership rotation and revocation |

## Detailed findings

### G-01 — Information security policy (2/5 → 4/5)
- **Evidence reviewed:** Draft policy v0.3; no approval record
- **Finding:** Policy exists in draft but was never approved by management
- **Recommendation:** Approve the policy in a management meeting and set a yearly review date

### G-02 — Roles and responsibilities (1/5 → 4/5)
- **Evidence reviewed:** Org chart; interviews
- **Finding:** No named security owner; responsibilities shared informally between IT and the CTO
- **Recommendation:** Appoint a security owner and publish a RACI for security activities

### G-03 — Management review (0/5 → 3/5)
- **Evidence reviewed:** None available
- **Finding:** No management review of security has taken place
- **Recommendation:** Hold a first management review using the cl. 9.3 inputs and record decisions

### R-01 — Risk assessment method (1/5 → 4/5)
- **Evidence reviewed:** Spreadsheet of 9 risks
- **Finding:** Risks listed without a defined scale or owners
- **Recommendation:** Define a 5x5 likelihood/impact method and assign an owner to every risk

### R-02 — Risk treatment and SoA (0/5 → 4/5)
- **Evidence reviewed:** None available
- **Finding:** No Statement of Applicability and no treatment plan
- **Recommendation:** Build the SoA and a risk treatment plan with deadlines

### A-01 — Asset inventory (2/5 → 4/5)
- **Evidence reviewed:** Cloud console export; laptop list
- **Finding:** Cloud resources and laptops are listed but SaaS tools and data stores are missing
- **Recommendation:** Extend the inventory to SaaS and data; add owner and classification columns

### A-02 — Information classification (1/5 → 3/5)
- **Evidence reviewed:** Interviews
- **Finding:** No classification scheme; customer data handled like any other file
- **Recommendation:** Adopt a 3-level scheme (Public / Internal / Confidential) and label key repositories

### I-01 — Access control policy (2/5 → 4/5)
- **Evidence reviewed:** Onboarding checklist
- **Finding:** Access granted on request without periodic review
- **Recommendation:** Run quarterly access reviews for critical systems and record them

### I-02 — Multi-factor authentication (3/5 → 5/5)
- **Evidence reviewed:** Identity provider settings
- **Finding:** MFA enforced for email; not yet enforced for the cloud console and code repository
- **Recommendation:** Enforce MFA on all administrative and developer accounts

### I-03 — Privileged access (2/5 → 4/5)
- **Evidence reviewed:** Admin account list
- **Finding:** Several standing administrator accounts with no expiry
- **Recommendation:** Reduce standing admin rights; use time-limited elevation and log its use

### C-01 — Encryption of data (3/5 → 4/5)
- **Evidence reviewed:** Storage and TLS settings
- **Finding:** Encryption at rest and TLS in place by default; no key-management procedure
- **Recommendation:** Document key ownership rotation and revocation

### O-01 — Vulnerability management (2/5 → 4/5)
- **Evidence reviewed:** Scanner reports (2 months)
- **Finding:** Scans run occasionally; no remediation deadlines by severity
- **Recommendation:** Set patch deadlines per severity and track them to closure

### O-02 — Logging and monitoring (2/5 → 4/5)
- **Evidence reviewed:** Log settings
- **Finding:** Logs collected but nobody reviews them; no alerting on admin actions
- **Recommendation:** Centralise logs and alert on privileged and authentication events

### O-03 — Change management (3/5 → 4/5)
- **Evidence reviewed:** Pull-request history
- **Finding:** Code changes are peer-reviewed; infrastructure changes are not tracked
- **Recommendation:** Apply the same review and approval flow to infrastructure changes

### B-01 — Backups and restore tests (2/5 → 4/5)
- **Evidence reviewed:** Backup job settings
- **Finding:** Daily backups configured; no restore test ever performed
- **Recommendation:** Perform and document a restore test every quarter

### B-02 — ICT continuity plan (1/5 → 3/5)
- **Evidence reviewed:** None available
- **Finding:** No documented continuity or recovery plan for the payment platform
- **Recommendation:** Write a recovery plan with RTO/RPO for critical services and test it once a year

### S-01 — Supplier security (1/5 → 4/5)
- **Evidence reviewed:** Contract folder
- **Finding:** No list of ICT providers and no security clauses in contracts
- **Recommendation:** Create a register of ICT providers and add security and exit clauses at renewal

### N-01 — Incident management process (1/5 → 4/5)
- **Evidence reviewed:** Chat channel history
- **Finding:** Incidents handled ad hoc in chat; no classification or regulatory reporting procedure
- **Recommendation:** Define the incident process with classification criteria and the 24h/72h reporting steps

### H-01 — Awareness and training (2/5 → 4/5)
- **Evidence reviewed:** Onboarding slides
- **Finding:** Security covered once at onboarding only; no training for management
- **Recommendation:** Run a yearly awareness programme including a session for management

### D-01 — Secure development (3/5 → 4/5)
- **Evidence reviewed:** CI pipeline configuration
- **Finding:** Dependency scanning in CI; no secret scanning and no security testing before release
- **Recommendation:** Add secret scanning and a security test step to the release pipeline

## Scale

- **0** — Non-existent
- **1** — Initial
- **2** — Repeatable
- **3** — Defined
- **4** — Managed
- **5** — Optimised
