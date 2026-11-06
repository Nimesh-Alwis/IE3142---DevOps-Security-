# IE3142 — DevOps Security: Comprehensive Topic Router & Final Exam Index (V2)

**Module:** IE3142 – DevOps Security  
**Lectures Covered:** Lecture 01 to Lecture 10  
**Version:** V2 (Exam-Oriented Master Release aligned with Final Examination Structure)  
**Purpose:** Rapid exam-time lookup mapping key terms, questions, acronyms, and scenarios to specific lectures, reference sheet sections, and examination questions.

---

## 1. Final Examination Question-to-Lecture Router

| Question & Format | Marks | Primary Lectures | Core Focus & Tested Concepts | Reference Sheet Location |
| :--- | :---: | :---: | :--- | :--- |
| **Question 1: MCQs (25 Qs)** | **25** | **All Lectures (01–10)** | Broad high-yield facts: Shift-Left, SDLC phases, Prepared statements, Allow-lists, Output encoding, 12 Design Principles, STRIDE properties, DREAD formula, Cloud Shared Responsibility (IaaS/PaaS/SaaS), RPO/RTO, IDS/IPS anomaly vs signature, Container shared kernel, Dockerfile ENV risks, SBOM, SAST vs DAST vs SCA vs IaC, Security Gates & key rotation, IR 6-phases, Forensics Chain of Custody, GDPR Art. 33 (72h), Compensating controls, Serverless Denial of Wallet (DoW). | **Side A & Side B** (All cards) |
| **Question 2(i): Threat Modelling (Structured)** | **8** | **Lecture 03** | Online Examination System: 4 assets (student details, exam questions, marks, audit logs); 4 STRIDE threats; suitable controls (MFA, encryption, digital signatures, RBAC); why design phase (Shift-Left, low-cost architectural fix, defines security requirements). | **Side A — Card 4** |
| **Question 2(ii): CI/CD Security (Structured)** | **9** | **Lecture 06** | Online Shopping Pipeline: CI/CD purpose (automated build, test, package, deploy); SAST (white-box source code) vs SCA (3rd party libraries) vs DAST (black-box runtime); 3 security checks (secret scanning, SAST, SCA); Security Gate definition & how it halts insecure deployment. | **Side B — Card 8** |
| **Question 2(iii): Docker Architecture (Structured)** | **8** | **Lecture 05** | Docker definition & 2 advantages (portability, consistency, rapid startup); Architecture diagram & components (Client, Daemon `dockerd`, Images, Containers, Registry); Image vs Container distinction; 2 container security risks & controls (root execution &rarr; `USER nonroot`; vulnerable base images &rarr; minimal pinned tags & scanning). | **Side B — Card 6** |
| **Question 3: Online Banking Essay (Scenario 1)** | **25** | **Lecture 01, 02, 03, 04** | LankaPay Mobile Wallet: Shift-Left concept & why quarterly late testing failed (cost curve 1x to 100x); 5 secure coding practices with code (Parameterized queries, Allow-list validation, Context-aware output encoding, Strong password hashing [Argon2id/bcrypt], Complete mediation/server-side auth); STRIDE threat model on "Send Money" (5 threats + controls) + DREAD scoring formula; 3 Infrastructure measures (Private subnets/RDS, IAM least privilege/MFA, AWS KMS encryption); SDLC security cost/benefit. | **Side A — Cards 1, 2, 4 & 5** |
| **Question 4: Cloud Healthcare Essay (Scenario 2)** | **25** | **Lecture 05, 06, 07, 08** | MediCare Plus Patient Management System: CI/CD security integration across 6 stages with checks & tools (Gitleaks, SonarQube, Snyk, Trivy, Cosign, OWASP ZAP, Checkov); 4 Docker container risks (root execution, `--privileged` flag, docker.sock mount, hardcoded secrets); Kubernetes RBAC (Developer namespaced Role vs Admin `cluster-admin`, service account token disabling, NetworkPolicy default-deny, Pod Security Standards); Governance & Compliance (GDPR Art. 33 72-hour breach notice, HIPAA Administrative/Physical/Technical safeguards, 3 patient protection controls); Continuous monitoring (SIEM, egress anomaly alerts); Incident Response 6-phase lifecycle (Prep, Detect, Contain, Eradicate, Recover, Lessons) + Forensics Chain of Custody. | **Side B — Cards 6, 7, 8, 9, 10 & 11** |

---

## 2. Master Topic & Concept Lookup Router

| Topic / Keyword | Primary Lecture | Core Focus & Exam Key Points | Ref Sheet Location |
| :--- | :--- | :--- | :--- |
| **12 Secure Design Principles** | **Lecture 03** | Saltzer & Schroeder: Defense in Depth, Fail Securely, Least Privilege, Fail-Safe Defaults, Secure Defaults, Minimize Surface, Separation of Duties, Complete Mediation, Economy of Mechanism, Open Design, Least Common Mechanism, Psychological Acceptability | **Side A — Card 3** |
| **ABAC vs RBAC vs DAC vs MAC** | **Lecture 04** | RBAC = role-based; ABAC = attributes/context (time, device, IP); DAC = owner discretion; MAC = mandatory security labels (military/confidential) | **Side A — Card 5** |
| **Admission Controllers (K8s)** | **Lecture 05, 06** | OPA Gatekeeper, Kyverno; intercept API requests before etcd persistence; enforce signed images & non-root pods | **Side B — Card 7 & 8** |
| **Allow-List Input Validation** | **Lecture 02** | Define exact allowed characters/regex (`/^[a-zA-Z0-9_]{3,20}$/`); **fails closed**; reject invalid input; decode/canonicalize first | **Side A — Card 2** |
| **Anomaly vs Signature Detection** | **Lecture 04, 07** | Signature = known patterns (low false positives); Anomaly = baseline deviation (catches 0-days, higher false positives) | **Side A — Card 5** |
| **Argon2id / bcrypt / PBKDF2** | **Lecture 02** | Memory-hard & CPU-intensive password hashing with salt and work factor; defeats GPU/ASIC rainbow table attacks | **Side A — Card 2** |
| **Assets (Threat Modeling)** | **Lecture 03** | High-value data or resources: credentials, exam questions, student marks, patient medical records, payment API keys | **Side A — Card 4** |
| **Chain of Custody** | **Lecture 07** | Chronological documentation proving evidence integrity: who collected it, when, transfers, tamper-proof storage | **Side B — Card 10** |
| **Checkov / tfsec / KICS** | **Lecture 04, 06** | Static IaC security scanners checking Terraform/K8s files for open security groups, public S3 buckets, root pods | **Side A — Card 5, Side B — Card 8** |
| **CI vs CD vs Continuous Deploy** | **Lecture 06** | CI = frequent commit & auto test; CD (Delivery) = deployable artifact + manual gate; Continuous Deployment = auto to prod | **Side B — Card 8** |
| **Cloud Shared Responsibility** | **Lecture 04, 10** | CSP: Security **OF** the Cloud (hardware, hypervisors); Customer: Security **IN** the Cloud (OS, data, IAM, apps, firewalls) | **Side A — Card 5** |
| **Compensating Controls** | **Lecture 08** | Alternative security control implemented when the preferred primary control (e.g. MFA) is technically infeasible | **Side B — Card 11** |
| **Complete Mediation** | **Lecture 02, 03** | Verify authorization on **every access attempt**; never cache past permission checks; check role server-side | **Side A — Card 2 & 3** |
| **Container Escape** | **Lecture 05** | Attacker breaks out of container to host kernel; caused by `--privileged`, root execution, or `/var/run/docker.sock` mount | **Side B — Card 6** |
| **Continuous Security Monitoring** | **Lecture 07** | Real-time observability of telemetry across apps, nodes, containers, and cloud APIs; feeds back into SDLC planning | **Side B — Card 9** |
| **Cosign / Sigstore / SBOM** | **Lecture 06** | Software supply chain integrity: CycloneDX/SPDX SBOM gives package visibility; Cosign signs and verifies images | **Side B — Card 8** |
| **DAST (Dynamic Testing)** | **Lecture 06** | Black-box testing of a running web application via simulated HTTP attacks (OWASP ZAP); finds XSS, auth flaws | **Side B — Card 8** |
| **Denial of Wallet (DoW)** | **Lecture 10** | Serverless/cloud billing exhaustion caused by automated event flooding; defended via rate-limits, concurrency caps, billing alarms | **Side B — Card 12** |
| **Digital Forensics Principles** | **Lecture 07** | Work on **bit-stream forensic copies** (never live original); compute & verify SHA-256 hashes; maintain Chain of Custody | **Side B — Card 10** |
| **Docker Architecture & Engine** | **Lecture 05** | Docker Client (CLI) &rarr; Docker Daemon (`dockerd`) &rarr; Images (read-only layers) &rarr; Containers (running instance) &harr; Registry | **Side B — Card 6** |
| **Docker Security Hardening** | **Lecture 05** | `USER nonroot` (UID 10001); `--cap-drop=ALL`; `--privileged=false`; never mount docker.sock; read-only rootfs; `.dockerignore` | **Side B — Card 6** |
| **DREAD Risk Scoring** | **Lecture 03** | Risk score = $(D + R + E + A + D) / 5$ (Damage, Reproducibility, Exploitability, Affected Users, Discoverability). Score &ge; 7.0 = High | **Side A — Card 4** |
| **ENISA (EU Cybersecurity Agency)** | **Lecture 08** | **Advisory Agency (NOT law!)**; produces cybersecurity guidelines, threat landscapes, and recommendations | **Side B — Card 11** |
| **Fail Securely vs Fail-Safe Defaults**| **Lecture 03** | Fail Securely = system locks down on error (fail closed); Fail-Safe Defaults = default access state is deny-all | **Side A — Card 3** |
| **GDPR (Article 33 & 7 Principles)** | **Lecture 08** | EU Law; extraterritorial; protect personal data; **72-hour breach notification to supervisory authority** (Article 33) | **Side B — Card 11** |
| **Gitleaks / TruffleHog** | **Lecture 06** | Automated secret scanners detecting API keys, tokens, and private keys committed to Git repositories | **Side B — Card 8** |
| **HIPAA (Privacy, Security, Breach)**| **Lecture 08** | US Law protecting **PHI / ePHI**; 3 Security Safeguards: **Administrative, Physical, and Technical** | **Side B — Card 11** |
| **IaC Scanning** | **Lecture 04, 06** | Scanning declarative code (Terraform, CloudFormation, K8s manifests) for misconfigurations before deployment | **Side A — Card 5, Side B — Card 8** |
| **IDS vs IPS** | **Lecture 04, 07** | IDS = passive detection & out-of-band alerting; IPS = active inline packet filtering & traffic dropping | **Side A — Card 5** |
| **Incident Response (6 Phases)** | **Lecture 07** | 1. Preparation &rarr; 2. Detection & Analysis &rarr; 3. Containment &rarr; 4. Eradication &rarr; 5. Recovery &rarr; 6. Lessons Learned | **Side B — Card 10** |
| **Kubernetes RBAC** | **Lecture 05** | Subjects bound to Roles/ClusterRoles via RoleBindings; Developer = namespaced least priv; Admin = `cluster-admin` via MFA | **Side B — Card 7** |
| **Least Privilege Principle** | **Lecture 02, 03** | Grant only the minimum permissions necessary for the specific task and time required; limit blast radius | **Side A — Card 2 & 3** |
| **NetworkPolicy (Kubernetes)** | **Lecture 05** | Pod-to-pod firewalling; default-deny ingress and egress; permits only frontend &rarr; backend &rarr; database | **Side B — Card 7** |
| **Output Encoding (Context-Aware)** | **Lecture 02** | Converts HTML special characters (`<`, `>`, `&`, `"`) to safe entities; primary mitigation against Cross-Site Scripting (XSS) | **Side A — Card 2** |
| **Parameterized Queries** | **Lecture 02** | Prepared statements separating SQL structure from untrusted user input; definitive defense against SQL Injection | **Side A — Card 2** |
| **Risk Formula & 4 Treatments** | **Lecture 03** | $\text{Risk} = \text{Likelihood} \times \text{Impact}$. Treatments: **Mitigate** (controls), **Avoid**, **Transfer** (insurance), **Accept** | **Side A — Card 4** |
| **RTO vs RPO** | **Lecture 04** | RTO = Recovery Time Objective (max downtime duration); RPO = Recovery Point Objective (max acceptable data loss time) | **Side A — Card 5** |
| **SAST vs SCA vs DAST** | **Lecture 06** | SAST = white-box source code; SCA = 3rd party open-source dependencies; DAST = black-box running app | **Side B — Card 8** |
| **Security Gates** | **Lecture 06** | Automated pass/fail pipeline conditions halting deployment if security policies (0 critical CVEs, no secrets) are breached | **Side B — Card 8** |
| **Shift Left Security** | **Lecture 01** | Moving security to Requirements and Design phases; reduces defect fix costs from $100\times$ (prod) to $1\times$–$5\times$ (early) | **Side A — Card 1** |
| **SIEM (Security Info & Event Mgmt)**| **Lecture 07** | Centralizes, normalizes, and correlates logs from multiple systems; tools: Microsoft Sentinel, Splunk, Elastic | **Side B — Card 9** |
| **STRIDE Threat Modeling** | **Lecture 03** | Spoofing (AuthN), Tampering (Integrity), Repudiation (Accountability), Info Disclosure (Confidentiality), DoS (Availability), Elevation of Privilege (AuthZ) | **Side A — Card 4** |

---

## 3. Alphabetical Keyword Index
- **ABAC:** Lecture 04, Side A (Card 5)
- **Admission Controllers:** Lecture 05 & 06, Side B (Card 7 & 8)
- **Allow-list:** Lecture 02, Side A (Card 2)
- **Argon2id:** Lecture 02, Side A (Card 2)
- **Assets:** Lecture 03, Side A (Card 4)
- **Audit Logs:** Lecture 02 & 07, Side A (Card 2), Side B (Card 9)
- **AWS KMS / Azure Key Vault:** Lecture 04, Side A (Card 5)
- **bcrypt:** Lecture 02, Side A (Card 2)
- **Chain of Custody:** Lecture 07, Side B (Card 10)
- **Checkov:** Lecture 04 & 06, Side A (Card 5), Side B (Card 8)
- **CI/CD Pipeline:** Lecture 06, Side B (Card 8)
- **CloudTrail / CloudWatch:** Lecture 04 & 07, Side A (Card 5), Side B (Card 9)
- **Compensating Controls:** Lecture 08, Side B (Card 11)
- **Complete Mediation:** Lecture 02 & 03, Side A (Card 2 & 3)
- **Container Escape:** Lecture 05, Side B (Card 6)
- **Continuous Delivery vs Deployment:** Lecture 06, Side B (Card 8)
- **Cosign / Sigstore:** Lecture 06, Side B (Card 8)
- **DAST (OWASP ZAP):** Lecture 06, Side B (Card 8)
- **Defense in Depth:** Lecture 03, Side A (Card 3)
- **Denial of Wallet (DoW):** Lecture 10, Side B (Card 12)
- **Docker Architecture (Client, Daemon, Image, Container, Registry):** Lecture 05, Side B (Card 6)
- **DREAD Scoring:** Lecture 03, Side A (Card 4)
- **ENISA:** Lecture 08, Side B (Card 11)
- **Fail Securely:** Lecture 03, Side A (Card 3)
- **GDPR Article 33 (72h Notice):** Lecture 08, Side B (Card 11)
- **Gitleaks / TruffleHog:** Lecture 06, Side B (Card 8)
- **HIPAA Safeguards:** Lecture 08, Side B (Card 11)
- **IaaS vs PaaS vs SaaS:** Lecture 04, Side A (Card 5)
- **IaC Security:** Lecture 04 & 06, Side A (Card 5), Side B (Card 8)
- **IDS vs IPS:** Lecture 04 & 07, Side A (Card 5)
- **Incident Response (6 Phases):** Lecture 07, Side B (Card 10)
- **Kubernetes RBAC:** Lecture 05, Side B (Card 7)
- **Least Privilege:** Lecture 02 & 03, Side A (Card 2 & 3)
- **NetworkPolicy:** Lecture 05, Side B (Card 7)
- **Output Encoding:** Lecture 02, Side A (Card 2)
- **Parameterized Queries:** Lecture 02, Side A (Card 2)
- **Pod Security Standards (PSS):** Lecture 05, Side B (Card 7)
- **Risk Treatments:** Lecture 03, Side A (Card 4)
- **RTO vs RPO:** Lecture 04, Side A (Card 5)
- **SAST (SonarQube/Semgrep):** Lecture 06, Side B (Card 8)
- **SCA (Snyk/Dependabot):** Lecture 06, Side B (Card 8)
- **Security Gates:** Lecture 06, Side B (Card 8)
- **Shift Left SDLC:** Lecture 01, Side A (Card 1)
- **SIEM (Sentinel/Splunk):** Lecture 07, Side B (Card 9)
- **STRIDE Threat Framework:** Lecture 03, Side A (Card 4)
- **Trust Boundary:** Lecture 03, Side A (Card 4)
- **VM vs Container:** Lecture 05, Side B (Card 6)
