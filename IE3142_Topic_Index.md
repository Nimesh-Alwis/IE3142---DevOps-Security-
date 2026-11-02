# IE3142 — DevOps Security: Comprehensive Topic Router & Exam Index

**Module:** IE3142 – DevOps Security  
**Lectures Covered:** Lecture 01 to Lecture 09  
**Purpose:** Rapid exam-time lookup mapping key terms, questions, acronyms, and scenarios to specific lectures and core concepts.

---

## 1. Quick Master Topic Router
| Topic / Concept | Primary Lecture | Core Focus & Keywords | Page on Ref Sheet |
| :--- | :--- | :--- | :--- |
| **DevSecOps Core Principles** | **Lecture 01** | Shared Responsibility, Security Automation, Continuous Security, Continuous Monitoring | **Side A (P1)** |
| **Shift Left Security** | **Lecture 01** | Early testing, cost multiplier (10–100x), proactive prevention | **Side A (P1)** |
| **Traditional vs DevOps vs DevSecOps** | **Lecture 01** | Siloed vs speed vs shared secure delivery | **Side A (P1)** |
| **Secure SDLC Phases** | **Lecture 01, 02** | Reqs (abuse cases) → Design (threat model) → Code (SAST) → Test (DAST) → Deploy (gates) → Ops (monitor) | **Side A (P1)** |
| **Input Validation** | **Lecture 02** | Allow-list > Block-list, canonicalization first, format/type/length check | **Side A (P1)** |
| **Parameterized Queries** | **Lecture 02** | Separates code from data, primary SQL Injection (SQLi) defense | **Side A (P1)** |
| **Output Encoding** | **Lecture 02** | Context-aware encoding (HTML, JS, URL), primary XSS defense | **Side A (P1)** |
| **Authentication vs Authorization** | **Lecture 02** | Who you are (AuthN, MFA, Argon2) vs What you can do (AuthZ, RBAC, IDOR prevention) | **Side A (P1)** |
| **Password Hashing** | **Lecture 02** | Memory-hard hashes: Argon2id, bcrypt, PBKDF2 (never MD5/SHA) | **Side A (P1)** |
| **Secure Logging Rules** | **Lecture 02, 07** | Log security events; NEVER log passwords, tokens, full PAN, or PII | **Side A (P1)** |
| **12 Secure Design Principles** | **Lecture 03** | Defense in Depth, Fail Securely, Least Privilege, Fail-Safe Defaults, Secure Defaults, Open Design, etc. | **Side A (P1)** |
| **Threat Modeling Workflow** | **Lecture 03** | Assets → DFD → Trust Boundaries → STRIDE → Risk Assessment → Mitigate → Validate | **Side A (P1)** |
| **STRIDE Threat Framework** | **Lecture 03** | Spoofing, Tampering, Repudiation, Information Disclosure, Denial of Service, Elevation of Privilege | **Side A (P1)** |
| **Risk Formula & 4 Treatments** | **Lecture 03** | Risk = Likelihood × Impact. Treatments: Mitigate, Avoid, Transfer, Accept | **Side A (P1)** |
| **Cloud Service Models** | **Lecture 04** | IaaS (OS down), PaaS (Runtime down), SaaS (All managed except data/access) | **Side B (P2)** |
| **Shared Responsibility Model** | **Lecture 04, 09** | CSP: Security OF the Cloud; Customer: Security IN the Cloud | **Side B (P2)** |
| **AWS vs Azure Security Services** | **Lecture 04** | IAM vs Entra ID; CloudTrail vs Activity Log; CloudWatch vs Azure Monitor; KMS vs Key Vault; SGs vs NSGs | **Side B (P2)** |
| **RTO vs RPO** | **Lecture 04** | RTO = Max acceptable downtime; RPO = Max acceptable data loss time window | **Side B (P2)** |
| **Network Controls (Firewall/WAF/VPN)**| **Lecture 04** | Stateful vs stateless, WAF at L7, Remote-access vs Site-to-site VPN | **Side B (P2)** |
| **IDS vs IPS** | **Lecture 04, 07** | IDS = Passive, alert only; IPS = Inline, actively drops/blocks malicious traffic | **Side B (P2)** |
| **Access Control Models** | **Lecture 04** | RBAC (roles), ABAC (attributes/context), DAC (owner), MAC (security labels) | **Side B (P2)** |
| **IaC & Hardening** | **Lecture 04** | Baseline configs, disable unused ports/services, eliminate drift via code | **Side B (P2)** |
| **VM vs Container Comparison** | **Lecture 05** | Hardware virtualization (Hypervisor + Guest OS) vs OS virtualization (cgroups/namespaces + shared kernel) | **Side B (P2)** |
| **Docker Components & Flow** | **Lecture 05** | Dockerfile → docker build → Image (layers) → Registry → docker run → Container | **Side B (P2)** |
| **Container Hardening** | **Lecture 05** | Non-root USER, drop capabilities, no `--privileged`, no docker.sock mount, read-only rootfs | **Side B (P2)** |
| **Kubernetes Architecture** | **Lecture 05** | Control Plane: API Server, etcd, Scheduler, Controller Manager. Node: kubelet, kube-proxy, Pod | **Side B (P2)** |
| **Kubernetes Security Controls** | **Lecture 05** | RBAC, etcd encryption, NetworkPolicy (default deny), Pod Security Standards | **Side B (P2)** |
| **CI vs CD vs Continuous Deploy** | **Lecture 06** | CI = frequent integration + auto test; Delivery = deployable build + manual gate; Deployment = auto to prod | **Side B (P2)** |
| **Security Testing: SAST vs DAST vs SCA**| **Lecture 06** | SAST (white-box, code, no run) vs DAST (black-box, running app, HTTP) vs SCA (open-source dependencies, CVEs) | **Side B (P2)** |
| **Secrets Scanning** | **Lecture 06** | Scanning commits for leaked API keys/tokens (TruffleHog, Gitleaks); revoking exposed secrets | **Side B (P2)** |
| **Security Gates** | **Lecture 06** | Automated pass/fail policy checks halting pipeline on High/Critical findings | **Side B (P2)** |
| **Software Supply Chain Security** | **Lecture 06** | SBOM (CycloneDX), artifact signing (Cosign), pinned dependencies, isolated runners | **Side B (P2)** |
| **Continuous Security Monitoring (CSM)**| **Lecture 07** | Ongoing telemetry collection, real-time threat detection, feedback to SDLC Plan | **Side B (P2)** |
| **SIEM & Alert Correlation** | **Lecture 07** | Centralize, normalize, correlate logs, alert on IOCs; False Positives vs False Negatives | **Side B (P2)** |
| **Incident Response (IR) 6 Phases** | **Lecture 07** | 1. Preparation → 2. Identification → 3. Containment → 4. Eradication → 5. Recovery → 6. Lessons Learned | **Side B (P2)** |
| **Digital Forensics Principles** | **Lecture 07** | Chain of custody, bit-stream copies, hash verification (SHA-256), timeline analysis | **Side B (P2)** |
| **GRC Fundamentals** | **Lecture 08** | Governance (direction/oversight) + Risk (identification/treatment) + Compliance (legal proof) | **Side B (P2)** |
| **Statute vs Standard vs Agency** | **Lecture 08** | Statute = binding law (GDPR, HIPAA); Standard = PCI-DSS/ISO 27001; Agency = advisory (ENISA) | **Side B (P2)** |
| **GDPR 7 Principles & 72-Hour Rule** | **Lecture 08** | Lawfulness, Purpose limitation, Data minimization, Accuracy, Storage, Integrity, Accountability; 72h breach notice | **Side B (P2)** |
| **HIPAA Rules & Safeguards** | **Lecture 08** | Privacy Rule, Security Rule (Administrative, Physical, Technical), Breach Notification Rule; protects PHI/ePHI | **Side B (P2)** |
| **ENISA Role** | **Lecture 08** | European Union Agency for Cybersecurity; produces guidelines and threat analysis (NOT law) | **Side B (P2)** |
| **Audit vs Assessment vs Evidence** | **Lecture 08** | Formal audit vs internal assessment; evidence = verifiable artifacts; Compliance ≠ Security | **Side B (P2)** |
| **Cloud-Native & Serverless / FaaS** | **Lecture 09** | Event-driven, ephemeral, dynamic auto-scaling, pay-per-millisecond (AWS Lambda, Azure Functions) | **Side B (P2)** |
| **Shared Responsibility in Serverless**| **Lecture 09** | CSP manages infra, OS, runtime, scaling; Customer manages code, IAM, APIs, data, dependencies | **Side B (P2)** |
| **Serverless Top Threats & Mitigations**| **Lecture 09** | Insecure code, excessive IAM, insecure APIs, secrets exposure, event injection, Denial of Wallet (DoW) | **Side B (P2)** |
| **Denial of Wallet (DoW)** | **Lecture 09** | Financial exhaustion via abusive serverless triggers; defended via throttling, concurrency caps, billing alerts | **Side B (P2)** |

---

## 2. Alphabetical Keyword Quick-Lookup Index
- **ABAC / RBAC / DAC / MAC:** Lecture 04 (Section 4.7)
- **AppArmor / seccomp / SELinux:** Lecture 05 (Section 5.3)
- **Argon2id / bcrypt / PBKDF2:** Lecture 02 (Section 2.4)
- **AWS KMS / Azure Key Vault:** Lecture 04 (Section 4.4), Lecture 09 (Section 9.5)
- **AWS Lambda / Azure Functions:** Lecture 09 (Section 9.2)
- **Chain of Custody:** Lecture 07 (Section 7.6)
- **CI/CD Security Gates:** Lecture 06 (Section 6.4)
- **CloudTrail / CloudWatch:** Lecture 04 (Section 4.4)
- **Complete Mediation Principle:** Lecture 03 (Section 3.2)
- **Container Escape:** Lecture 05 (Section 5.3)
- **Continuous Security Monitoring (CSM):** Lecture 07 (Section 7.1)
- **Cosign / Sigstore / SBOM:** Lecture 06 (Section 6.5)
- **DAST (Dynamic Testing):** Lecture 06 (Section 6.3)
- **Defense in Depth Principle:** Lecture 03 (Section 3.2), Lecture 04 (Section 4.1)
- **Denial of Wallet (DoW):** Lecture 09 (Section 9.5)
- **DFD & Trust Boundaries:** Lecture 03 (Section 3.4)
- **Digital Forensics:** Lecture 07 (Section 7.6)
- **Docker Architecture (Daemon, Image layers, Container):** Lecture 05 (Section 5.2)
- **Economy of Mechanism Principle:** Lecture 03 (Section 3.2)
- **ENISA (EU Cybersecurity Agency):** Lecture 08 (Section 8.5)
- **Fail Securely vs Fail-Safe Defaults:** Lecture 03 (Section 3.2)
- **False Positive vs False Negative:** Lecture 07 (Section 7.3)
- **GDPR 7 Principles & Article 33 Breach Rule:** Lecture 08 (Section 8.3)
- **HIPAA Rules & ePHI Safeguards:** Lecture 08 (Section 8.4)
- **IaaS vs PaaS vs SaaS:** Lecture 04 (Section 4.3)
- **IaC Scanning (Terraform / Checkov):** Lecture 04 (Section 4.8), Lecture 06 (Section 6.3)
- **IDS vs IPS:** Lecture 04 (Section 4.6), Lecture 07 (Section 7.4)
- **Incident Response 6 Stages:** Lecture 07 (Section 7.5)
- **Input Validation (Allow-list):** Lecture 02 (Section 2.3)
- **Kubernetes Control Plane & Worker Nodes:** Lecture 05 (Section 5.4)
- **Kubernetes RBAC & NetworkPolicy:** Lecture 05 (Section 5.5)
- **Least Privilege Principle:** Lecture 02 (Section 2.3), Lecture 03 (Section 3.2)
- **Log Management & Secure Fields:** Lecture 07 (Section 7.2)
- **Output Encoding (Context-aware):** Lecture 02 (Section 2.3)
- **OWASP Top 10 Web Vulnerabilities:** Lecture 02 (Section 2.2)
- **Parameterized Queries (Prepared Statements):** Lecture 02 (Section 2.3)
- **Pod Security Standards (PSS):** Lecture 05 (Section 5.5)
- **Risk Formula & Treatments (Mitigate, Avoid, Transfer, Accept):** Lecture 03 (Section 3.6)
- **RTO vs RPO:** Lecture 04 (Section 4.5)
- **SAST (Static Testing):** Lecture 06 (Section 6.3)
- **SCA (Dependency Scanning):** Lecture 06 (Section 6.3)
- **Secret Scanning (TruffleHog / Gitleaks):** Lecture 06 (Section 6.3)
- **Shared Responsibility Model:** Lecture 04 (Section 4.3), Lecture 09 (Section 9.4)
- **Shift Left Security:** Lecture 01 (Section 1.5)
- **SIEM Workflow:** Lecture 07 (Section 7.3)
- **STRIDE Threat Modeling Categories:** Lecture 03 (Section 3.5)
- **Trust Boundaries:** Lecture 03 (Section 3.4)
- **Virtual Machines vs Containers:** Lecture 05 (Section 5.1)
- **WAF (Layer 7 Inspection):** Lecture 04 (Section 4.6)

---
*End of Topic Index.*
