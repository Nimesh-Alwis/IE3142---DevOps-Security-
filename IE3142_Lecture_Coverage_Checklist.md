# IE3142 — DevOps Security: Comprehensive Lecture Coverage Checklist

**Module Code & Name:** IE3142 – DevOps Security  
**Lectures Inspected:** Lecture 01 through Lecture 09 (Weeks 1 to 9)  
**Verification Purpose:** Ensure 100% complete syllabus coverage with zero omitted topics or altered technical terminology.

---

## Master Lecture Coverage Verification Table

| Lecture | Slide File Name | Status | Verified Key Concepts & Technical Terminology | Notes / Action Taken |
| :---: | :--- | :---: | :--- | :--- |
| **01** | `Week 01 - Lecture 01 - Introduction to DevSecOps.pdf` | **VERIFIED** | • Motivation & software breach impact<br>• Traditional SDLC vs. DevOps vs. DevSecOps<br>• DevOps Lifecycle stages (Plan to Monitor)<br>• 4 DevSecOps Principles (Shared Resp, Automation, Continuous Sec, Continuous Mon)<br>• Shift Left Security (rationale, cost multiplier)<br>• Security mapping across SDLC phases | Fully represented in Extracted Notes, Topic Index, and Side A of Reference Sheet. |
| **02** | `Week 02 - Lecture 02 - Secure Software Development Practices.pdf` | **VERIFIED** | • Secure SDLC overview & questions per phase<br>• Secure Coding definition & OWASP Top 10 weaknesses<br>• 4 Secure Coding Habits (Input validation, Parameterized SQL, Context-aware output encoding, Least privilege)<br>• Allow-list vs. Block-list & Canonicalization<br>• AuthN vs. AuthZ (definitions, MFA, password hashing)<br>• Password hashing (Argon2id, bcrypt, PBKDF2)<br>• Secure logging rules (what to log / what not to log) | Fully integrated into Side A with comparison table and code example. |
| **03** | `Week 03 - Lecture 03 - Secure Design Principles and Patterns.pdf` | **VERIFIED** | • Secure Design vs. Secure Coding distinction<br>• 12 Secure Design Principles (Saltzer & Schroeder)<br>• Design patterns (RBAC, API Gateway, Defense in Depth)<br>• Threat Modeling workflow & DFD trust boundaries<br>• STRIDE framework (Spoofing, Tampering, Repudiation, Info Disclosure, DoS, Elevation of Privilege)<br>• Risk Formula ($\text{Likelihood} \times \text{Impact}$) & 4 Treatments (Mitigate, Avoid, Transfer, Accept) | Full 12-principle grid and STRIDE table embedded on Side A. |
| **04** | `Week 04 - Lecture 04 - Infrastructure Security.pdf` | **VERIFIED** | • Infrastructure security definition & CIA Triad<br>• 5 Cloud Characteristics (NIST SP 800-145)<br>• Cloud Service Models (IaaS, PaaS, SaaS) & Deployment Models<br>• Shared Responsibility Model (OF vs. IN the Cloud)<br>• AWS vs. Azure Security Services comparison<br>• Data protection (rest/transit) & RTO vs. RPO<br>• Network Security (Firewall, WAF, IDS vs. IPS, VPN)<br>• IAM Models (RBAC, ABAC, DAC, MAC) & MFA<br>• Hardening, CIS baselines, Configuration Drift, IaC | Integrated on Side B with comparative mapping and resilience metrics. |
| **05** | `Week 05 - Lecture 05 - Containerization, Orchestration and Secure CI-CD.pdf` | **VERIFIED** | • Container vs. Virtual Machine comparison<br>• Docker Architecture (Client, Daemon, Dockerfile, Image, Container, Registry)<br>• Image layers & Docker build flow<br>• Container Security Threats & Controls (non-root, cap-drop, no privileged flag, no docker.sock mount, read-only rootfs)<br>• AppArmor, SELinux, seccomp confinement<br>• Kubernetes Architecture (Control Plane vs. Worker Nodes)<br>• Kubernetes Security (RBAC, Secrets in etcd, NetworkPolicy, Pod Security Standards) | Integrated on Side B with VM vs Container comparison and K8s architecture. |
| **06** | `Week 06 - Lecture 06 - Secure Continuous Integration and Deployment.pdf` | **VERIFIED** | • CI vs. CD (Delivery) vs. Continuous Deployment definitions<br>• Security activities across pipeline stages<br>• Security Testing comparison (SAST vs. DAST vs. SCA vs. Secret Scanning vs. IaC Scanning)<br>• Security Quality Gates & automated thresholds<br>• Software Supply Chain Security (SBOM, Cosign/Sigstore signing, runner isolation) | Full comparison matrix and pipeline workflow diagram on Side B. |
| **07** | `Week 07 - Lecture 07 - Continuous Monitoring and Incident Response.pdf` | **VERIFIED** | • Continuous Security Monitoring (CSM) & feedback loop<br>• Log Management, mandatory log fields, redaction<br>• SIEM architecture, correlation rules, False Positives/Negatives<br>• Network detection: IDS (passive) vs. IPS (inline active)<br>• Incident Response (IR) 6-stage lifecycle (Prep, ID, Contain, Eradicate, Recover, Lessons Learned)<br>• Digital Forensics & Chain of Custody (hashing, working on copies) | Embedded IR lifecycle flow, SIEM concepts, and log rules on Side B. |
| **08** | `Week 08 - Lecture 08 - Compliance and Governance.pdf` | **VERIFIED** | • Governance, Risk, Compliance (GRC) framework<br>• Statute/Law vs. Standard vs. Framework vs. Guidance Agency<br>• GDPR 7 Core Principles & Article 33 72-hour breach notification rule<br>• HIPAA Privacy, Security (Admin, Physical, Technical), & Breach Notification Rules; PHI/ePHI<br>• ENISA (EU Cybersecurity Agency role - advisory, not law)<br>• Security controls classification (Administrative, Technical, Physical)<br>• Audit vs. Assessment vs. Evidence; Compliance ≠ Security | Regulatory comparison and GDPR/HIPAA/ENISA breakdown on Side B. |
| **09** | `Week 09 - Lecture 09 - Secure Cloud Services and Serverless Architectures.pdf` | **VERIFIED** | • Cloud-native characteristics & microservices<br>• Serverless & Function-as-a-Service (FaaS) definition (AWS Lambda, Azure Functions)<br>• Event-driven serverless architecture & execution flow<br>• Shared Responsibility Model in Serverless<br>• Serverless Threats: Insecure code, excessive IAM roles, insecure APIs, secrets exposure, event injection<br>• Denial of Wallet (DoW) threat & rate-limiting/budget mitigations<br>• Serverless secrets handling & runtime observability (X-Ray) | Serverless architecture, threat mitigations, and Denial of Wallet covered on Side B. |

---

## Specific Constraints & Prompt Directives Checklist

- [x] **A4 Page Dimensions:** Exactly $210 \times 297\text{ mm}$ verified.
- [x] **Page Count:** Exactly 2 pages (Side A = Page 1, Side B = Page 2).
- [x] **Margins:** Exactly $5\text{ mm}$ on all four edges.
- [x] **Header/Footer Optimization:** No redundant module titles, no oversized logos, no page-side labels; space repurposed for core technical content.
- [x] **Multi-Column Layout:** High-density, professional academic reference layout with subtle vertical borders and internal padding.
- [x] **Intentional Blank Space:** Dedicated, labeled note-taking regions provided on both Page 1 and Page 2 for exam-time handwritten notes.
- [x] **No Unnecessary Exam Guide Boxes:** Removed extraneous red-colored guidance boxes; preserved all genuine lecture concepts.
- [x] **Visual Design:** Clean typography, distinct hierarchical styling, monospace code snippets, and structured tables.

---
*Checklist completed and verified against all primary slide artifacts.*
