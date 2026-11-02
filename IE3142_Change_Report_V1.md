# IE3142 — DevOps Security: Reference Sheet V1 Change & Synthesis Report

**Module:** IE3142 – DevOps Security  
**Version:** V1 (Initial Approved Master Reference Release)  
**Deliverables Date:** 2026-11-03  
**Target Output Format:** 2-Page Double-Sided A4 Reference Sheet (`IE3142_Reference_Sheet_V1.pdf`)

---

## 1. Executive Summary
This project synthesized all 9 weeks of lecture slides and study notes for **IE3142 DevOps Security** into a highly compact, professional, exam-oriented 2-page A4 reference sheet. The design strictly adheres to all constraints from the Master Prompt:
- **Strict A4 Dimensions:** Exactly $210 \times 297\text{ mm}$ portrait orientation with exact $5\text{ mm}$ margins on all four edges.
- **Exact 2-Page Length:** Page 1 (Side A) covers Foundations, Secure SDLC, Secure Coding, 12 Design Principles, and STRIDE; Page 2 (Side B) covers Infrastructure, Containerization, Kubernetes, Secure CI/CD, Monitoring, Incident Response, GRC (GDPR/HIPAA/ENISA), and Serverless Security.
- **Header & Footer Optimization:** Removed redundant module titles, giant banners, and decorative elements. Replaced with an ultra-compact micro-header and a 9-cell quick Topic Router.
- **Balanced Multi-Column Layout:** Employs a 3-column grid per page with subtle vertical dividers (`0.5px solid #e2e8f0`), consistent alignment, internal padding, and color-coded section headers for rapid recognition under exam pressure.
- **Preserved Handwritten Note Space:** Preserved dedicated, ruled note-taking areas ($25\text{ mm}$ height with $3.6\text{ mm}$ rule spacing) across the bottom of both pages for student annotations during exams.
- **Zero Information Loss:** Preserved original technical terminology, definitions, classifications, formulas, comparisons, and workflows.

---

## 2. Deliverables Inventory
| # | File Name | Description | Status |
| :-: | :--- | :--- | :---: |
| **1** | [IE3142_Reference_Sheet_V1.pdf](file:///f:/SLIIT%20Y3%20,%20S1/IE3142%20-%20DevOps%20Security%20%5B2026JUL%5D/IE3142---DevOps-Security-/IE3142_Reference_Sheet_V1.pdf) | Final printable 2-page A4 reference sheet. Verified 595 × 842 pt. | **Complete** |
| **2** | [IE3142_Reference_Sheet_V1_Source.html](file:///f:/SLIIT%20Y3%20,%20S1/IE3142%20-%20DevOps%20Security%20%5B2026JUL%5D/IE3142---DevOps-Security-/IE3142_Reference_Sheet_V1_Source.html) | Editable HTML/CSS source code with print styles and semantic markup. | **Complete** |
| **3** | [IE3142_Extracted_Notes.md](file:///f:/SLIIT%20Y3%20,%20S1/IE3142%20-%20DevOps%20Security%20%5B2026JUL%5D/IE3142---DevOps-Security-/IE3142_Extracted_Notes.md) | Exhaustive, structured synthesis of all 9 lecture slides and notes. | **Complete** |
| **4** | [IE3142_Topic_Index.md](file:///f:/SLIIT%20Y3%20,%20S1/IE3142%20-%20DevOps%20Security%20%5B2026JUL%5D/IE3142---DevOps-Security-/IE3142_Topic_Index.md) | Fast exam lookup router & alphabetical keyword index. | **Complete** |
| **5** | [IE3142_Lecture_Coverage_Checklist.md](file:///f:/SLIIT%20Y3%20,%20S1/IE3142%20-%20DevOps%20Security%20%5B2026JUL%5D/IE3142---DevOps-Security-/IE3142_Lecture_Coverage_Checklist.md) | Comprehensive audit checklist verifying 100% syllabus coverage. | **Complete** |
| **6** | [IE3142_Change_Report_V1.md](file:///f:/SLIIT%20Y3%20,%20S1/IE3142%20-%20DevOps%20Security%20%5B2026JUL%5D/IE3142---DevOps-Security-/IE3142_Change_Report_V1.md) | This report documenting design decisions, changes, and verification. | **Complete** |
| **7** | [IE3142_Reference_Sheet_V1_Page_1.png](file:///f:/SLIIT%20Y3%20,%20S1/IE3142%20-%20DevOps%20Security%20%5B2026JUL%5D/IE3142---DevOps-Security-/IE3142_Reference_Sheet_V1_Page_1.png) | High-resolution visual proof of Page 1 (Side A). | **Complete** |
| **8** | [IE3142_Reference_Sheet_V1_Page_2.png](file:///f:/SLIIT%20Y3%20,%20S1/IE3142%20-%20DevOps%20Security%20%5B2026JUL%5D/IE3142---DevOps-Security-/IE3142_Reference_Sheet_V1_Page_2.png) | High-resolution visual proof of Page 2 (Side B). | **Complete** |

---

## 3. Structural & Content Mapping per Page

### Page 1 (Side A)
- **Top Micro-Header & Topic Router:** Rapid orientation across all 9 lectures.
- **Lecture 01 (DevSecOps Foundations & Shift-Left):**
  - Definition & business impact of breaches.
  - Traditional SDLC vs. DevOps vs. DevSecOps comparison table.
  - Four Core Principles: Shared Responsibility, Security Automation, Continuous Security, Continuous Monitoring.
  - Shift-Left security rationale with cost multiplier ($1×, $5×, $10×, $15×, $100×).
  - Security integration across SDLC phases (Reqs to Ops).
- **Lecture 02 (Secure Software Development Practices):**
  - Secure Coding definition & OWASP Top 10 focus.
  - Four Core Secure Coding Habits (Allow-list Input Validation, Parameterized SQL Queries, Context-aware Output Encoding, Least Privilege).
  - SQLi vulnerable vs. secure code comparison.
  - Authentication (AuthN) vs. Authorization (AuthZ) comparison table.
  - Memory-hard password hashing (Argon2id, bcrypt, PBKDF2).
  - Secure logging checklist (what to log vs. what never to log).
- **Lecture 03 (Secure Design Principles & Threat Modeling):**
  - Secure Design vs. Secure Coding distinction.
  - **Complete 12 Secure Design Principles Table** (Defense in depth, Fail securely, Least privilege, Fail-safe defaults, Secure defaults, Minimize surface, Separation of duties, Complete mediation, Economy of mechanism, Open design, Least common mechanism, Psychological acceptability).
  - Threat Modeling workflow & Trust Boundary definition.
  - **STRIDE Threat Classification Table** (Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege with definitions & mitigations).
  - Risk formula ($\text{Risk} = \text{Likelihood} \times \text{Impact}$) & Four Risk Treatments (Mitigate, Avoid, Transfer, Accept).
  - Security Design Patterns (Secure Gateway, Defense-in-Depth layered model).
- **Preserved Writing Space:** $25\text{ mm}$ ruled notes box spanning the bottom of the page.

### Page 2 (Side B)
- **Top Micro-Header:** Clean page identification.
- **Lecture 04 (Infrastructure & Cloud Security):**
  - Cloud computing characteristics & deployment models.
  - Cloud Service Models (IaaS, PaaS, SaaS) comparison table.
  - Cloud Shared Responsibility Model (OF vs. IN the cloud).
  - AWS vs. Azure Security Services comparative mapping table.
  - Business resilience: RTO vs. RPO definitions.
  - Network security: Stateful firewall, Layer 7 WAF, IDS vs. IPS (passive vs. active inline), VPNs.
  - IAM access models (RBAC, ABAC, DAC, MAC), MFA factors, and hardening baselines.
- **Lecture 05 (Containers & Kubernetes):**
  - Virtual Machines vs. Containers architectural comparison table.
  - Docker components, image layers, and lifecycle flow.
  - Container threats & hardening controls (non-root, cap-drop, no `--privileged`, no `docker.sock` mount, read-only rootfs).
  - Kubernetes architecture: Control Plane (API Server, etcd, Scheduler, Controller Mgr) vs. Worker Nodes (kubelet, kube-proxy, Pods).
  - Kubernetes security controls: RBAC, etcd encryption, NetworkPolicy default deny, Pod Security Standards.
- **Lecture 06 (Secure CI/CD & Testing):**
  - CI vs. CD (Delivery) vs. Continuous Deployment definitions.
  - Comprehensive Security Testing Comparison Matrix (SAST vs. DAST vs. SCA vs. Secret Scanning vs. IaC Scanning).
  - Automated security quality gates and build-breaking thresholds.
  - Software Supply Chain Security: SBOM (CycloneDX/SPDX), Cosign/Sigstore signing, runner isolation.
- **Lecture 07 (Continuous Monitoring & Incident Response):**
  - Continuous Security Monitoring (CSM) & SDLC feedback loops.
  - Secure log management, mandatory log fields, redaction of sensitive data, WORM storage.
  - SIEM workflow, correlation engine, and False Positives vs. False Negatives.
  - Incident Response 6-Phase Lifecycle sequence (Prep, ID, Contain, Eradicate, Recover, Lessons Learned).
  - Digital Forensics: Chain of Custody, bit-stream copies, SHA-256 integrity hashing.
- **Lecture 08 (Compliance & Governance - GRC):**
  - GRC definitions and relationship (Governance + Risk + Compliance).
  - Core principle: *Compliance ≠ Security*.
  - Regulatory classification table: Statutory Law (GDPR, HIPAA) vs. Standard (ISO 27001, PCI-DSS) vs. Advisory Agency (ENISA).
  - GDPR 7 Core Principles, extraterritorial scope, and Article 33 72-hour breach notification rule.
  - HIPAA Privacy Rule, Security Rule (Administrative, Physical, Technical Safeguards), and Breach Rule.
  - ENISA's role as an advisory agency (NOT law).
  - Audit vs. Assessment vs. Evidence.
- **Lecture 09 (Secure Cloud Services & Serverless Architectures):**
  - Cloud-native architecture & Serverless / FaaS definition (AWS Lambda, Azure Functions).
  - Serverless Shared Responsibility split.
  - Common Serverless Threats & Mitigations (excessive IAM permissions, event injection, secrets in env vars, insecure APIs).
  - **Denial of Wallet (DoW):** Attack mechanism, financial exhaustion, and defensive throttling / concurrency / budget alarm controls.
- **Preserved Writing Space:** $25\text{ mm}$ ruled notes box spanning the bottom of the page.

---

## 4. Quality Assurance & Verification
1. **Dimension Verification:** The rendered PDF was audited via `pypdf`. Both pages report exact media boxes `RectangleObject([0, 0, 594.96, 841.92])`, precisely matching standard A4 dimensions ($210 \times 297\text{ mm}$).
2. **Page Count Verification:** Total page count is exactly **2 pages**. No spillover or orphan third page exists.
3. **Margin Verification:** All margins are set strictly to $5\text{ mm}$ (`@page { size: A4 portrait; margin: 5mm; }`).
4. **Visual Inspection:** High-resolution screenshots of both pages were generated and inspected. Typography is sharp and readable, card borders and vertical column dividers align cleanly, tables have crisp headers, and code snippets are cleanly styled.
5. **Blank Note Space Verification:** Generous ruled writing panels are preserved at the bottom of both pages for handwritten notes during examinations.

---
*Report certified for IE3142 DevOps Security Reference Sheet V1.*
