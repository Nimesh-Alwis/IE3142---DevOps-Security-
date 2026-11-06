# IE3142 — DevOps Security: Comprehensive Extracted Lecture Notes (Lectures 01–09)

**Module:** IE3142 – DevOps Security  
**Scope:** Lecture 01 to Lecture 09 (Weeks 1 to 9)  
**Primary Source:** Official SLIIT Lecture Slide PDFs (`LEC slids/`) and Lecture Notes  
**Status:** Authoritative Synthesis for Reference Sheet Generation & Exam Preparation  

---

## Table of Contents
1. [Lecture 01: Introduction to DevSecOps](#lecture-01-introduction-to-devsecops)
2. [Lecture 02: Secure Software Development Practices](#lecture-02-secure-software-development-practices)
3. [Lecture 03: Secure Design Principles and Patterns](#lecture-03-secure-design-principles-and-patterns)
4. [Lecture 04: Infrastructure Security](#lecture-04-infrastructure-security)
5. [Lecture 05: Containerization, Orchestration and Secure CI/CD](#lecture-05-containerization-orchestration-and-secure-cicd)
6. [Lecture 06: Secure Continuous Integration and Deployment](#lecture-06-secure-continuous-integration-and-deployment)
7. [Lecture 07: Continuous Monitoring and Incident Response](#lecture-07-continuous-monitoring-and-incident-response)
8. [Lecture 08: Compliance and Governance](#lecture-08-compliance-and-governance)
9. [Lecture 09: Secure Cloud Services and Serverless Architectures](#lecture-09-secure-cloud-services-and-serverless-architectures)

---

## Lecture 01: Introduction to DevSecOps

### 1.1 Motivation & Why Software Security Matters
- Software powers critical infrastructure, financial institutions, healthcare, and enterprise commerce, handling sensitive personal, financial, and confidential data.
- Breaches cause: massive financial losses, legal liabilities, regulatory fines, customer churn, and irreversible reputational damage.
- Modern architectures (cloud computing, microservices, third-party libraries, containerization, public APIs) drastically expand the **attack surface**.
- In traditional development, security was treated as an afterthought or a final gate before deployment. Discovering flaws (SQL injection, broken access control, hard-coded credentials) at this late stage causes release delays, expensive emergency patching, and friction between development and operations.

### 1.2 Comparison: Traditional SDLC vs. DevOps vs. DevSecOps
| Dimension | Traditional SDLC (Waterfall) | DevOps | DevSecOps |
| :--- | :--- | :--- | :--- |
| **Philosophy** | Siloed, sequential stages (Reqs → Design → Dev → Test → Ops). | Collaborative Dev & Ops, continuous delivery, rapid feedback. | Development, Security, and Operations share ownership across all stages. |
| **Security Timing** | At the very end (pre-release security testing gate). | Often omitted or treated as an external blocker to speed. | **Shift Left**: Integrated into every stage from initial design to production. |
| **Velocity** | Slow, infrequent release cycles (months to years). | Fast, automated releases (daily/hourly). | Fast, automated, secure releases without compromising agility. |
| **Vulnerability Cost** | Exponentially high to remediate in late test or production. | High if security issues bypass automated pipelines. | Low; detected and remediated immediately at commit/build time. |

### 1.3 The DevOps & DevSecOps Lifecycle
- **DevOps Stages:** `Plan → Code → Build → Test → Release → Deploy → Operate → Monitor` (continuous feedback loop to Plan).
- **CI/CD Definition:** Continuous Integration (automated build & testing of code commits) + Continuous Delivery/Deployment (automated artifact packaging, staging, and deployment).
- **DevSecOps Integration:** Adding security activities into every single stage rather than treating security as an isolated checkpoint.

### 1.4 Four Core DevSecOps Principles
1. **Shared Responsibility:** Security is no longer solely the security team's responsibility; developers, QA, DevOps engineers, and operations personnel all share accountability for security.
2. **Security Automation:** Manual security assessments cannot keep pace with CI/CD velocity. Security testing (SAST, SCA, secrets scanning, DAST, container scanning, IaC scanning) must be automated inside pipelines.
3. **Continuous Security:** Security checks occur continuously throughout every iteration of the software lifecycle, from requirements and coding through runtime.
4. **Continuous Monitoring:** Ongoing observability of runtime environments, user authentication, network flows, and system configurations with real-time alerting and automated incident response.

### 1.5 Shift Left Security
- **Definition:** Moving security decisions, tests, and verifications to the earliest possible stages of the SDLC (to the "left" on a linear timeline).
- **Cost Multiplier Principle:** Fixing a defect during requirements/design costs up to 10–100× less than fixing it after deployment in production.
- **Benefits:**
  - Dramatically cheaper and faster remediation.
  - Rapid feedback to developers while the code is fresh in their minds.
  - Elimination of release bottlenecks and deployment freezes.
  - Proactive vulnerability prevention rather than reactive patching.

### 1.6 Security Integration per SDLC Phase
- **Requirements:** Identify security requirements, regulatory constraints, privacy rules, and abuse cases / threat scenarios.
- **Design:** Architectural threat modeling, trust boundaries, defense-in-depth design, and secure design patterns.
- **Coding:** Secure coding guidelines, IDE linters, peer code reviews, input validation, output encoding, and SAST.
- **Testing:** Automated SAST, SCA dependency checking, secrets detection, and DAST in staging environments.
- **Deployment:** Hardened configurations, automated security policy gates, secrets management, and cryptographic signing.
- **Operations:** Continuous runtime monitoring, log analysis, vulnerability scanning, intrusion detection, and incident response.

---

## Lecture 02: Secure Software Development Practices

### 2.1 Secure SDLC Overview
- A structured methodology that injects security milestones and quality gates into every phase of traditional and agile software development lifecycles.
- Replaces reactive vulnerability patching with systematic prevention.

### 2.2 Secure Coding Fundamentals
- **Definition:** Writing source code in a manner that resists attack, preserves the CIA triad (Confidentiality, Integrity, Availability), and prevents common software security flaws.
- **Common Weaknesses (OWASP Top 10):**
  - Injection (SQLi, Command Injection, LDAP injection)
  - Cross-Site Scripting (XSS: Stored, Reflected, DOM-based)
  - Cross-Site Request Forgery (CSRF)
  - Broken Authentication and Session Management
  - Sensitive Data Exposure / Cryptographic Failures
  - Security Misconfigurations
  - Insecure Deserialization
  - Using Components with Known Vulnerabilities

### 2.3 Four Core Secure Coding Habits
#### A. Input Validation
- All external data (form fields, query strings, headers, cookies, API payloads, file uploads) is **untrusted**.
- **Allow-list (Whitelisting) over Block-list (Blacklisting):** Define explicitly what is allowed (data type, character set, min/max length, regex format, numeric range). Blocklists fail because attackers use obfuscation and novel encodings.
- **Canonicalization & Normalization:** Decode and resolve data into its canonical form *before* validation (prevents Unicode evasion, URL double-encoding, directory traversal `../` tricks).
- Leverage established, framework-provided validation libraries.

#### B. Parameterized Queries / Prepared Statements
- The primary and mandatory defense against SQL Injection (SQLi).
- **Mechanism:** Separates code from data. The database engine compiles the SQL query structure first; user input is passed strictly as parameters/literals and is never interpreted as executable SQL syntax.
- **Anti-pattern:** String concatenation or formatting (`"SELECT * FROM users WHERE name='" + user + "'"`).
- **Best Practice:** Parameterized queries or Object-Relational Mappers (ORMs) using prepared statements.

#### C. Context-Aware Output Encoding
- The primary defense against Cross-Site Scripting (XSS).
- **Mechanism:** Converts untrusted characters into safe, harmless display representations before rendering them in the browser (e.g., `<` becomes `&lt;`, `>` becomes `&gt;`).
- Must be **context-aware**: HTML body, HTML attributes, JavaScript context, CSS context, and URL query strings require distinct encoding schemes.
- Modern frontend frameworks (React, Angular) automatically escape HTML in data-binding expressions.

#### D. Principle of Least Privilege (PoLP)
- Applications, database connections, service accounts, and processes must run with the bare minimum permissions necessary to perform their legitimate function.
- Database accounts used by web apps should never possess administrative privileges (`DBA`, `DROP TABLE`, `ALTER`).
- **Impact:** Drastically minimizes the attacker's **blast radius** if a component is compromised.

### 2.4 Authentication vs. Authorization
| Feature | Authentication (AuthN) | Authorization (AuthZ) |
| :--- | :--- | :--- |
| **Question** | *Who are you?* (Verifying claimed identity). | *What are you allowed to do?* (Permissions & access rights). |
| **Mechanisms** | Passwords, Multi-Factor Authentication (MFA), biometric scans, certificates. | Role-Based Access Control (RBAC), Attribute-Based Access Control (ABAC), ACLs. |
| **Best Practices** | Strong password policies, rate-limiting login attempts, MFA, slow salted hashing. | Default deny, re-check authorization on every single request, prevent IDOR. |
| **Password Hashing** | Use modern memory-hard cryptographic hash functions: **Argon2id**, **bcrypt**, **PBKDF2**. Never MD5/SHA-1. | Verify user ownership of requested object ID to eliminate IDOR flaws. |

### 2.5 Secure Logging and Sensitive Data Handling
- **What to Log:** Authentication attempts (successes and repeated failures), privilege changes, access control failures, critical administrative actions, and system errors.
- **What NEVER to Log:** Plaintext passwords, authentication tokens, API keys, full credit card numbers (PAN), CVVs, and sensitive PII.
- **Audit Trails:** Centralized, timestamped, tamper-resistant logs enable forensics and non-repudiation.

---

## Lecture 03: Secure Design Principles and Patterns

### 3.1 Secure Design vs. Secure Coding
- **Secure Design:** Focuses on architecture, system structure, component relationships, trust boundaries, and threat modeling *before* code is written.
- **Secure Coding:** Focuses on tactical implementation, syntax, input validation, and bug-free execution during development.
- Architectural design flaws cannot be fixed simply by writing cleaner code; they require structural redesign.

### 3.2 The Twelve Secure Design Principles (Saltzer & Schroeder + Modern Extensions)
1. **Defense in Depth:** Implement multiple layered security controls. If one defensive layer fails, subsequent layers prevent a complete compromise.
2. **Fail Securely:** When a system fails or encounters an unhandled exception, it must transition into a secure, closed state rather than an open, vulnerable state.
3. **Least Privilege:** Entities possess only the permissions required to complete their designated tasks, for the shortest required duration.
4. **Fail-Safe Defaults:** Default to **deny** access. Explicit permission must be required for any access to be granted.
5. **Secure Defaults:** Out-of-the-box installations and configurations must be secure by default (e.g., ports closed, passwords forced to change, TLS enabled).
6. **Minimize Attack Surface:** Reduce the number of exposed entry points, open ports, public APIs, unnecessary services, and protocols.
7. **Separation of Duties:** Critical, high-risk operations require authorization from more than one individual or role to prevent fraud and single-point compromise.
8. **Complete Mediation:** Every access request to every resource must be checked and authorized every single time; never rely on cached or prior checks.
9. **Economy of Mechanism:** Keep the security design as simple, small, and straightforward as possible. Simplicity reduces bugs and makes verification feasible.
10. **Open Design:** Security must not depend on the secrecy of the design or algorithm (Kerckhoffs's Principle). Security relies on secret keys, not obscurity.
11. **Least Common Mechanism:** Minimize the sharing of mechanisms and resources between multiple users/tenants to avoid unintended shared channels or cross-contamination.
12. **Psychological Acceptability:** Security mechanisms must be intuitive, usable, and unobtrusive so that legitimate users do not seek workarounds or bypasses.

### 3.3 Security Design Patterns
- **Role-Based Access Control (RBAC):** Assign permissions to roles, and assign users to roles.
- **Secure Gateway / API Gateway:** Centralized policy enforcement point handling TLS termination, AuthN/AuthZ, rate limiting, and request sanitization.
- **Defense in Depth Pattern:** Perimeter firewall → WAF → DMZ gateway → Internal microservices authentication (mTLS) → Database access control & encryption.

### 3.4 Threat Modeling
- **Definition:** A proactive, structured engineering technique to identify assets, enumerate potential threats, analyze attack paths, and define risk mitigations *before* deployment.
- **Core Workflow:**
  1. *Identify Assets & Objectives:* Pinpoint data, infrastructure, and business logic to protect.
  2. *Deconstruct Architecture (DFD):* Map external entities, processes, data stores, data flows, and **trust boundaries**.
  3. *Identify Threats:* Apply structured frameworks such as **STRIDE**.
  4. *Assess & Prioritize Risk:* Evaluate likelihood and impact.
  5. *Determine Mitigations:* Apply security controls and design patterns.
  6. *Validate & Review:* Verify that threats are resolved and design matches implementation.
- **Trust Boundary:** Any interface where data or control transitions between different levels of privilege or trust (e.g., public internet to DMZ, DMZ to internal database).

### 3.5 STRIDE Threat Model
| Threat Category | Property Violated | Definition | Example Scenario | Standard Mitigation |
| :--- | :--- | :--- | :--- | :--- |
| **S – Spoofing** | Authenticity | Impersonating an entity, user, or process. | Attacker uses stolen credentials or forged tokens. | Strong AuthN, MFA, digital certificates, mTLS. |
| **T – Tampering** | Integrity | Unauthorized modification of data or code in transit or at rest. | Modifying transaction amount in HTTP parameter. | Cryptographic hashing, HMAC, digital signatures, TLS. |
| **R – Repudiation** | Non-Repudiation | An entity falsely denies having performed an action. | User denies sending funds transfer; no proof. | Tamper-evident audit logging, digital signatures, SIEM. |
| **I – Information Disclosure** | Confidentiality | Exposing sensitive information to unauthorized actors. | Unencrypted database backup leaked or intercepted. | Encryption at rest and in transit (AES-256, TLS 1.3), ACLs. |
| **D – Denial of Service** | Availability | Exhausting resources to make systems unavailable to legitimate users. | SYN flood, API request bombardment. | Rate limiting, DDoS protection (Cloudflare, AWS Shield), caching. |
| **E – Elevation of Privilege**| Authorization | Gaining higher permissions or capabilities than authorized. | Normal customer accesses administrative dashboard. | Strict AuthZ checks, least privilege, RBAC, input sanitization. |

### 3.6 Risk Assessment & Treatment
- **Risk Formula:** $\text{Risk} = \text{Likelihood} \times \text{Impact}$.
- **Four Risk Treatment Strategies:**
  1. **Mitigate (Reduce):** Implement technical or operational controls to lower likelihood or impact.
  2. **Avoid:** Eliminate the risk source entirely (e.g., disable an unnecessary high-risk feature).
  3. **Transfer (Share):** Shift financial/operational risk to a third party (cyber insurance, SaaS vendor contract).
  4. **Accept:** Acknowledge and retain residual risk with formal, documented business leadership approval.

---

## Lecture 04: Infrastructure Security

### 4.1 Foundations of Infrastructure Security
- Protects the underlying computing fabric: physical servers, operating systems, networks, hypervisors, virtualization, storage, and cloud environments.
- Protects confidentiality, integrity, availability, and business continuity.

### 4.2 Cloud Computing Foundations & Characteristics (NIST SP 800-145)
1. **On-Demand Self-Service:** Automated provisioning without human CSP intervention.
2. **Broad Network Access:** Capabilities available over standard network mechanisms across diverse client platforms.
3. **Resource Pooling:** Multi-tenant pooled physical and virtual resources dynamically assigned.
4. **Rapid Elasticity:** Capabilities provisioned and released elastically to match demand.
5. **Measured Service:** Resource usage metered, reported, and billed transparently.

### 4.3 Cloud Service & Deployment Models
- **Service Models:**
  - **IaaS (Infrastructure as a Service):** CSP manages physical datacenter, hypervisor, hardware. Customer manages OS, runtime, middleware, applications, data, IAM. (e.g., AWS EC2, Azure VMs).
  - **PaaS (Platform as a Service):** CSP manages hardware, OS, runtime, scaling, database engine. Customer manages application code and data. (e.g., AWS Elastic Beanstalk, Azure App Service).
  - **SaaS (Software as a Service):** CSP manages entire application stack. Customer manages user access and configuration. (e.g., Microsoft 365, Salesforce).
- **Deployment Models:** Public, Private, Hybrid, Community Cloud.
- **Shared Responsibility Model:**
  - CSP is responsible for **Security OF the Cloud** (physical datacenters, host hardware, hypervisors, networking cables, physical facilities).
  - Customer is responsible for **Security IN the Cloud** (customer data, IAM, OS patches in IaaS, network firewall rules, application code, data encryption).

### 4.4 AWS vs. Azure Security Services Mapping
| Capability | AWS Service | Azure Service | Key Function |
| :--- | :--- | :--- | :--- |
| **Identity & Access** | AWS IAM | Microsoft Entra ID (Azure AD) | Users, roles, policies, MFA, SSO. |
| **Activity Auditing** | AWS CloudTrail | Azure Activity Log | Immutable API and management event logging. |
| **Monitoring & Metrics** | AWS CloudWatch | Azure Monitor | Resource metrics, system telemetry, alarms. |
| **Security Posture** | AWS Security Hub / GuardDuty | Microsoft Defender for Cloud | Threat detection, CSPM, posture scoring. |
| **Secrets & Keys** | AWS KMS & Secrets Manager | Azure Key Vault | Hardware security module (HSM) keys, automated secret rotation. |
| **Network Firewall** | Security Groups & Network ACLs | NSGs & Azure Firewall | Stateful host filtering & stateless subnet filtering. |

### 4.5 Data Protection & Business Resilience
- **Data Protection:**
  - **At Rest:** Transparent disk encryption, database-level column encryption, object storage encryption using AES-256.
  - **In Transit:** TLS 1.2/1.3, IPSec, SSH; disable deprecated ciphers (SSLv3, TLS 1.0).
- **Business Continuity Metrics:**
  - **RTO (Recovery Time Objective):** Maximum acceptable duration of downtime before service must be restored.
  - **RPO (Recovery Point Objective):** Maximum acceptable age of data that can be lost when unexpected disaster occurs (data loss window).

### 4.6 Network Security Architecture
- **Firewalls:** Stateful packet inspection (tracks connection states) vs. Stateless ACLs.
- **Web Application Firewall (WAF):** Operates at Layer 7 (HTTP/HTTPS) to inspect payloads and filter OWASP Top 10 web attacks (SQLi, XSS).
- **IDS vs. IPS:**
  - **IDS (Intrusion Detection System):** Passive, out-of-band monitoring. Analyzes traffic, logs, and alerts administrators. Does not stop packets.
  - **IPS (Intrusion Prevention System):** Active, inline in traffic path. Detects attacks and immediately drops/resets malicious packets.
  - **Detection Engines:** Signature-based (known attack patterns) vs. Anomaly-based (statistical deviation from established baseline).
- **Virtual Private Network (VPN):** Encrypted tunneling protocol over untrusted networks. Remote-access (client-to-site) vs. Site-to-site (network-to-network).

### 4.7 Identity and Access Management (IAM)
- **Four Access Control Models:**
  - **RBAC (Role-Based Access Control):** Permissions assigned to roles; subjects assigned to roles based on job responsibilities.
  - **ABAC (Attribute-Based Access Control):** Dynamic access evaluated using subject attributes, resource tags, action, and environment context (time, location, device health).
  - **DAC (Discretionary Access Control):** Resource owner specifies access permissions.
  - **MAC (Mandatory Access Control):** Central authority enforces access using fixed security labels and clearances (military grade).
- **MFA Factors:** Something you know (password, PIN), Something you have (hardware token, authenticator app, smartcard), Something you are (biometrics).

### 4.8 Hardening and Infrastructure as Code (IaC)
- **Hardening:** Disabling unnecessary services/ports, removing default credentials, applying OS security baselines (CIS Benchmarks), updating kernel patches.
- **IaC (Terraform, CloudFormation, Ansible):** Defines infrastructure in version-controlled declarative code. Enables automated security scanning, auditable peer reviews, eliminates manual drift, and ensures repeatable secure configurations.

---

## Lecture 05: Containerization, Orchestration and Secure CI/CD

### 5.1 Containerization vs. Virtualization
| Feature | Virtual Machines (VMs) | Containers (Docker) |
| :--- | :--- | :--- |
| **Virtualization Level** | Hardware virtualization via Hypervisor (Type 1 or 2). | OS-level virtualization using Linux Kernel cgroups and namespaces. |
| **Operating System** | Each VM runs a full guest OS with its own kernel. | Containers share the host OS kernel; contain only user-space binaries. |
| **Startup Time** | Minutes (boots full virtualized OS). | Seconds or milliseconds (launches isolated process). |
| **Resource Overhead** | High (memory, CPU, disk overhead per VM). | Extremely lightweight and efficient. |
| **Isolation Boundary** | Hardware-enforced, strong VM boundary. | Process-level isolation; container escape threatens host kernel. |

### 5.2 Docker Architecture and Lifecycle
- **Components:**
  - **Docker Client:** CLI interface issuing commands (`docker build`, `docker run`).
  - **Docker Daemon (dockerd):** Background service managing images, containers, networks, and storage.
  - **Dockerfile:** Text manifest containing declarative build instructions.
  - **Image:** Immutable, layered template consisting of read-only filesystems.
  - **Container:** Runnable, isolated instance of an image with a thin writeable layer.
  - **Registry:** Centralized repository for storing, versioning, and distributing images (Docker Hub, AWS ECR, Harbor).
- **Flow:** `Dockerfile → (docker build) → Image → (docker push) → Registry → (docker pull) → (docker run) → Container`.

### 5.3 Container Security Threats & Hardening Controls
- **Vulnerable Base Images:** Use minimal base images (Alpine, Distroless), scan for CVEs, and patch base layers regularly.
- **Privileged Containers & Root Execution:** Running containers as root (`UID 0`) is dangerous. Enforce non-root execution (`USER nonroot`), avoid `--privileged` flag, and drop unnecessary Linux capabilities (`--cap-drop=ALL`).
- **Exposed Docker Socket:** Mounting `/var/run/docker.sock` inside a container gives the container root control over the host daemon, enabling container escape.
- **Secrets in Image Layers:** Hard-coding secrets in `Dockerfile` commands (`ENV`, `ARG`, `RUN`) leaves secrets in immutable image layer history. Inject secrets at runtime via vault systems.
- **Runtime Confinement:** Enforce Linux security modules: **AppArmor**, **SELinux**, and **seccomp** profiles to restrict available system calls. Mount filesystems as read-only (`--read-only`).

### 5.4 Kubernetes (K8s) Architecture & Components
- **Container Orchestration:** Automates scheduling, deployment, scaling, health monitoring, service discovery, and networking across clusters.
- **Control Plane (Master Node):**
  - **kube-apiserver:** Central REST API gateway; authenticates and authorizes all cluster operations.
  - **etcd:** Distributed, consistent key-value store maintaining cluster configuration and state.
  - **kube-scheduler:** Assigns unscheduled Pods to suitable worker nodes based on resource constraints.
  - **kube-controller-manager:** Runs core control loops (Node Controller, ReplicaSet Controller).
- **Worker Node:**
  - **kubelet:** Primary node agent ensuring Pods and containers are running as specified in PodSpecs.
  - **kube-proxy:** Manages network routing and IP translation for Kubernetes Services.
  - **Container Runtime:** Executes containers (containerd, CRI-O).
  - **Pod:** The smallest deployable computing unit in Kubernetes; encapsulates one or more co-located containers sharing network namespace and storage.

### 5.5 Kubernetes Security Best Practices
- **Kubernetes RBAC:** Define granular permissions using `Role` / `ClusterRole` and bind to subjects via `RoleBinding` / `ClusterRoleBinding`. Avoid default administrative service accounts.
- **Secrets Management:** Encrypt secrets stored in etcd at rest. Restrict secret access via RBAC; integrate with external vaults (HashiCorp Vault, cloud KMS).
- **NetworkPolicies:** Kubernetes networking is open by default. Implement `NetworkPolicy` resources to enforce default-deny ingress/egress rules between Pods and namespaces.
- **Pod Security Standards (PSS / PSA):** Enforce `Privileged`, `Baseline`, or `Restricted` security profiles to block privileged Pods, host network sharing, and host volume mounts.
- **API Server Hardening:** Disable anonymous authentication, enforce mTLS for all control plane communication, and enable Kubernetes audit logging.

---

## Lecture 06: Secure Continuous Integration and Deployment

### 6.1 CI / CD Terminology & Pipeline Stages
- **Continuous Integration (CI):** Developers frequently integrate code into a shared repository. Every commit automatically triggers automated builds, unit tests, and security scans.
- **Continuous Delivery (CD):** Automated pipeline compiles, tests, and stages code, ensuring the software is in a releasable state at all times. Deployment to production requires a manual approval trigger.
- **Continuous Deployment:** Every change that passes all automated pipeline gates is deployed directly and automatically to production with zero manual intervention.

### 6.2 Security Activity Mapping across Pipeline Stages
```text
[Developer Workstation] -> Pre-commit Hooks, IDE Linters, Secret Scanning
         ↓
[Commit & Push]        -> Git Branch Protection, Commit Signing
         ↓
[CI Build Stage]       -> SAST (Static Analysis), SCA (Dependency Check), Secrets Detection
         ↓
[Artifact Packaging]   -> Container Image Scanning, Cryptographic Artifact Signing (Cosign)
         ↓
[Staging / Test Env]   -> IaC Security Scanning, DAST (Dynamic Web Scanning), Compliance Checks
         ↓
[Security Quality Gate]-> Automated Pass/Fail Evaluation (Policy Enforcement)
         ↓
[Production Deploy]    -> GitOps Deployment, Runtime Monitoring, Continuous Auditing
```

### 6.3 Security Testing Technologies Comparison
| Testing Class | Full Name | Analyzes | Execution Req. | Best Phase | Detects | Tool Examples |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **SAST** | Static Application Security Testing | Source code, byte-code, AST | No (White-Box, static) | Code / Build | Insecure functions, SQLi syntax, hard-coded tokens, logic flaws | SonarQube, Semgrep, Checkmarx |
| **DAST** | Dynamic Application Security Testing | Running web application, HTTP APIs | Yes (Black-Box, dynamic) | Staging / Test | Runtime flaws, XSS execution, authentication bypass, header misconfigurations | OWASP ZAP, Burp Suite |
| **SCA** | Software Composition Analysis | Open-source dependencies, manifests | No (Dependency graph) | Build / Package | Known CVEs in packages, outdated versions, license compliance | Snyk, Dependabot, OWASP Dependency-Check |
| **Secret Scan** | Secret Detection | Git history, commits, files | No (Pattern & entropy) | Pre-commit / CI | Committed API keys, private certificates, AWS tokens, passwords | TruffleHog, GitGuardian, Gitleaks |
| **IaC Scan** | Infrastructure as Code Scanning | Terraform, Helm, K8s manifests | No (Static configuration) | Build / Deploy | Open security groups, unencrypted storage, excessive cloud privileges | Checkov, tfsec, KubeLinter |

### 6.4 Security Quality Gates
- **Definition:** Predefined criteria and automated thresholds built into CI/CD pipelines that automatically halt deployment if security violations occur.
- **Threshold Examples:** Fail pipeline on Critical or High CVEs with known exploits; fail if hard-coded secrets are detected; fail if code coverage drops below baseline.
- **Benefits:** Prevents flawed builds from reaching production environments without manual oversight.

### 6.5 Software Supply Chain Security
- **Definition:** Securing all components, dependencies, build tools, container registries, and pipelines involved in software delivery.
- **Attacks:** Dependency confusion, typosquatting, compromised third-party packages (e.g., SolarWinds, log4j), hijacked CI runners.
- **Mitigations:**
  - Generate and verify a **Software Bill of Materials (SBOM)** (CycloneDX, SPDX).
  - Cryptographically sign artifacts and container images using **Cosign** / Sigstore.
  - Pin dependency versions and hashes; use internal private mirrored package repositories.
  - Isolate CI build agents with ephemeral, least-privileged runners.

---

## Lecture 07: Continuous Monitoring and Incident Response

### 7.1 Continuous Security Monitoring (CSM)
- Deploying to production is not the end of security. Systems change, zero-day vulnerabilities emerge, and threats evolve continuously.
- **CSM Definition:** The ongoing, automated collection, analysis, and alerting of security telemetry across applications, cloud infrastructure, network traffic, and identities.
- **Feedback Loop:** Telemetry from runtime monitoring feeds back into the `Plan` and `Design` phases of the SDLC to guide proactive hardening.

### 7.2 Log Management & Audit Trails
- **Log Definition:** A time-sequenced record of system events, user interactions, or network communications.
- **Essential Log Fields:** Timestamp (synchronized via NTP in UTC), Source IP address, User/Identity, Action performed, Target resource, HTTP status / result code, Event severity.
- **Secure Logging Requirements:**
  - Centralize logs into write-once, tamper-resistant storage (WORM / S3 Object Lock).
  - Protect log integrity using cryptographic hashes.
  - Enforce strict access control to prevent attackers from deleting audit trails.
  - **Data Sanitization:** Mask and redact passwords, PII, payment card data, and tokens before writing to logs.

### 7.3 SIEM (Security Information and Event Management)
- **Function:** Aggregates, normalizes, and correlates logs and security events across disparate enterprise sources (firewalls, servers, cloud audit trails, endpoints).
- **Core Workflow:** `Collection → Normalization → Correlation Rules & ML → Threat Detection → Alerting → SOC Analyst Investigation`.
- **False Positives vs. False Negatives:**
  - **False Positive:** Benign event flagged as malicious (wastes analyst time, causes alert fatigue).
  - **False Negative:** Malicious attack undetected (dangerous; leaves breach undiscovered).

### 7.4 Network Detection: IDS vs. IPS
| Characteristic | IDS (Intrusion Detection System) | IPS (Intrusion Prevention System) |
| :--- | :--- | :--- |
| **Deployment Mode** | Passive, out-of-band (mirrored span port). | Active, inline directly in traffic flow. |
| **Action Taken** | Generates alerts; logs event. Does NOT drop traffic. | Automatically blocks, drops packets, or resets sessions. |
| **Operational Risk** | Low disruption risk; will not block legitimate traffic. | High disruption risk if false positives occur. |
| **Detection Methods** | **Signature-based** (matches known byte sequences) vs. **Anomaly-based** (flags statistical baseline anomalies). |

### 7.5 Incident Response (IR) Lifecycle (NIST SP 800-61 / ISO 27035)
1. **Preparation:** Formulate incident response plan (IRP), establish CSIRT roles, configure logging and tools, conduct tabletop simulation drills.
2. **Identification (Detection & Analysis):** Verify alert authenticity, correlate IOCs (Indicators of Compromise), determine scope, classify severity.
3. **Containment:**
   - *Short-term:* Isolate infected subnet, revoke compromised IAM credentials, terminate malicious sessions, block malicious IP on firewall.
   - *Long-term:* Apply temporary patches, redirect traffic, preserve volatile forensic evidence.
4. **Eradication:** Remove malware, close unauthorized backdoors, patch vulnerabilities, rebuild systems from known clean golden images.
5. **Recovery:** Restore systems from clean backups, validate system integrity, test business functionality, return to production, enhance monitoring for recurrence.
6. **Lessons Learned (Post-Incident Review):** Document root cause, evaluate team response efficiency, update security controls, and refine the incident response playbook within two weeks.

### 7.6 Digital Forensics & Evidence Handling
- **Digital Forensics:** Scientific identification, preservation, collection, validation, analysis, and presentation of digital evidence.
- **Chain of Custody:** Meticulous documentation accounting for the chronological custody, transfer, analysis, and disposition of physical and digital evidence.
- **Forensic Principles:** Work exclusively on bit-stream forensic disk copies (never live originals), calculate cryptographic hashes (SHA-256) before and after handling to prove integrity, record strict timestamps.

---

## Lecture 08: Compliance and Governance

### 8.1 Governance, Risk, and Compliance (GRC) Framework
- **Governance:** Strategic leadership, executive oversight, organizational structure, and security policies aligning cybersecurity with business objectives.
- **Risk Management:** Structured process of identifying, evaluating, treating, and monitoring information security risks to an acceptable level.
- **Compliance:** Demonstrating adherence to relevant external laws, statutory regulations, industry standards, and internal organizational policies.
- **GRC Integration:** Ensures security investments satisfy legal obligations while defending business-critical operations.

### 8.2 Classification: Laws, Standards, Frameworks, and Agencies
| Category | Definition | Legal Force | Key Examples |
| :--- | :--- | :--- | :--- |
| **Statutory Law / Regulation** | Legally binding rules enacted by government bodies. | Mandatory (penalties, civil/criminal fines). | GDPR, HIPAA, Sarbanes-Oxley (SOX), CCPA. |
| **Industry Standard** | Documented technical specifications and benchmarks. | Mandatory via contractual/industry mandate. | PCI-DSS, ISO/IEC 27001, SOC 2. |
| **Management Framework** | High-level structured methodology for managing cyber risk. | Voluntary adoption (best practice). | NIST Cybersecurity Framework (CSF), CIS Controls. |
| **Guidance Agency** | Public organizations issuing advisories and security research. | Non-binding guidance (informational). | ENISA, CISA, NCSC. |

### 8.3 General Data Protection Regulation (GDPR)
- **Jurisdiction:** Enacted by the European Union (EU); applies extraterritorially to any organization globally processing the personal data of individuals located in the EU/EEA.
- **Seven Core Principles (Article 5):**
  1. *Lawfulness, Fairness, and Transparency:* Valid legal basis and clear notices.
  2. *Purpose Limitation:* Data collected for specified, explicit, legitimate purposes.
  3. *Data Minimization:* Adequate, relevant, and limited to what is strictly necessary.
  4. *Accuracy:* Kept up to date; inaccurate data erased or rectified immediately.
  5. *Storage Limitation:* Kept in identifiable form no longer than necessary.
  6. *Integrity and Confidentiality:* Protected against unauthorized processing, loss, or destruction using technical controls.
  7. *Accountability:* The data controller is responsible for demonstrating compliance.
- **Key Requirements:**
  - Data Protection by Design and by Default (Article 25).
  - Mandatory Data Breach Notification: Report severe breaches to the supervisory authority **within 72 hours** of becoming aware (Article 33).
  - Data Subject Rights: Right of access, rectification, erasure ("right to be forgotten"), and data portability.

### 8.4 Health Insurance Portability and Accountability Act (HIPAA)
- **Jurisdiction:** United States federal law protecting **Protected Health Information (PHI / ePHI)**.
- **Scope:** Applies to **Covered Entities** (hospitals, doctors, health plans, healthcare clearinghouses) and **Business Associates** (cloud vendors, software providers handling PHI).
- **Three Core Rules:**
  - **Privacy Rule:** Sets national standards for the rights of individuals over their health information and controls permissible uses and disclosures of PHI.
  - **Security Rule:** Establishes mandatory security safeguards for electronic PHI (ePHI):
    - *Administrative Safeguards:* Security management process, workforce training, incident procedures.
    - *Physical Safeguards:* Facility access controls, workstation security, device media controls.
    - *Technical Safeguards:* Access control, unique user identification, emergency access, automatic logoff, encryption and decryption, audit controls, transmission security.
  - **Breach Notification Rule:** Requires notification to affected individuals, the HHS Secretary, and media following a breach of unsecured PHI.

### 8.5 ENISA (European Union Agency for Cybersecurity)
- **Role:** ENISA is an EU agency dedicated to fostering cybersecurity expertise, producing threat landscape reports, recommending good security practices, and coordinating member state cyber incident responses.
- **Critical Exam Distinction:** **ENISA is an advisory agency, NOT a regulatory law or enforceable statute.**

### 8.6 Audits, Assessments, and Evidence Collection
- **Audit:** An independent, formal, systematic examination to determine whether activities and controls comply with planned criteria and regulatory standards.
- **Assessment:** An internal evaluation of risk postures, control efficiencies, and identified gaps.
- **Evidence:** Concrete, verifiable artifacts (signed policy documents, automated vulnerability scan reports, IAM entitlement exports, firewall rule listings, backup restoration test logs).
- **Core Principle:** **Compliance is NOT equal to Security.** An organization can be fully compliant on paper while remaining vulnerable to sophisticated attacks. Compliance establishes a baseline; continuous security defends the system.

---

## Lecture 09: Secure Cloud Services and Serverless Architectures

### 9.1 Cloud-Native Foundations
- Cloud-native applications are purposefully architected to exploit the dynamic scale, managed services, and elasticity of cloud computing.
- Core pillars: Microservices architecture, containerization, declarative APIs, automated CI/CD pipelines, and **serverless compute**.

### 9.2 Serverless Computing & Function-as-a-Service (FaaS)
- **Definition:** An execution model where the cloud provider dynamically manages the provisioning, scaling, OS patching, and hardware execution of compute resources.
- **Core Truth:** *"Serverless does not mean there are no servers; it means developers do not manage, provision, or maintain the underlying servers."*
- **Characteristics:**
  - Event-driven execution (functions execute only in response to triggers).
  - Ephemeral, stateless execution environment.
  - Automatic, seamless horizontal scaling (from zero to thousands of concurrent requests).
  - True consumption-based pricing (pay strictly for compute execution time in milliseconds).
- **Prominent Services:** **AWS Lambda**, **Azure Functions**, Google Cloud Functions.

### 9.3 Event-Driven Serverless Execution Flow
```text
[Event Source]
(HTTP API Gateway / S3 File Upload / SQS Queue / DynamoDB Stream / Cron Timer)
       ↓ (Invokes Function with Event Payload)
[FaaS Execution Environment]
(AWS Lambda / Azure Function Instance)
       ↓ (Per-Function Scoped IAM Role)
[Backend Services]
(Cloud SQL / DynamoDB / S3 Bucket / External Third-Party APIs)
       ↓ (Telemetry & Tracing)
[Observability]
(AWS CloudWatch Logs / AWS X-Ray / Azure Application Insights)
```

### 9.4 Shared Responsibility in Serverless Computing
- **Cloud Provider Manages:**
  - Physical datacenters, server hardware, virtualization hypervisor.
  - Host operating system, OS security patches, container execution fleet.
  - Runtime environment maintenance and language patches.
  - Automatic scaling, high availability, and network routing.
- **Customer Manages:**
  - Application code quality, logic, and input validation.
  - Function-level Identity and Access Management (IAM execution roles).
  - API Gateway configurations, authentication, and throttling policies.
  - Third-party software dependencies and libraries (SCA).
  - Secrets storage and credential management.
  - Data encryption (at rest and in transit).
  - Event payload validation and application monitoring.

### 9.5 Serverless Security Threats & Defensive Controls
1. **Insecure Application Code:** Injection attacks (SQLi, NoSQLi, OS Command Injection) occur inside functions if untrusted event inputs are concatenated into queries.
   - *Control:* Input validation, parameterized queries, and output encoding.
2. **Excessive Function Permissions:** Granting functions wildcard permissions (`*`) allows an attacker compromising one function to manipulate unrelated cloud infrastructure.
   - *Control:* Enforce granular, per-function IAM roles adhering to Least Privilege. Separate read, write, and administrative roles.
3. **Insecure API Triggers:** Exposing public HTTP endpoints without authentication allows arbitrary invocation and abuse.
   - *Control:* Secure API Gateways with OAuth2, JWT verification, API keys, and mutual TLS.
4. **Vulnerable Third-Party Dependencies:** Serverless functions rely heavily on external package ecosystems (npm, PyPI) that may harbor known vulnerabilities.
   - *Control:* Run Software Composition Analysis (SCA) in build pipelines; pin dependency versions.
5. **Hard-Coded / Exposed Secrets:** Storing database passwords or API keys as plaintext environment variables risks accidental leakage via logs, console views, or config exports.
   - *Control:* Retrieve credentials at runtime from dedicated secret vaults (**AWS Secrets Manager**, **AWS Systems Manager Parameter Store**, **Azure Key Vault**).
6. **Event Injection:** Attackers pass malicious payloads through indirect event triggers (cloud storage uploads, message queues, IoT streams).
   - *Control:* Treat all event objects as untrusted input; validate schemas rigorously.
7. **Denial of Wallet (DoW):** Attackers flood event triggers or API endpoints with millions of requests. While serverless platforms scale automatically, the customer incurs catastrophic financial cloud billing costs.
   - *Control:* Implement API Gateway rate limiting, throttling limits, function concurrency execution limits, billing alarms, and budget kill-switches.
8. **Insufficient Logging and Observability:** Ephemeral containers vanish upon execution, making post-incident investigation impossible without centralized logging.
   - *Control:* Emit structured JSON logs to centralized monitoring services (CloudWatch, Azure Monitor) and enable distributed tracing (**AWS X-Ray**).

---
*End of Extracted Notes for IE3142 — DevOps Security.*


---

## 10. Final Examination Scenario Synthesis & Cheat Sheet

### 10.1 Structured Question Scenario: Online Examination System (Q2 Focus)
- **Context:** University portal where students take exams and view marks; lecturers upload questions and marks; administrators manage accounts.
- **Assets to Protect:**
  1. Student personal details & login credentials.
  2. Examination questions before exam release.
  3. Student exam submissions / answers.
  4. Final marks and academic transcripts.
  5. Audit logs recording mark modifications.
- **STRIDE Threat Mapping & Mitigations:**
  - *Spoofing:* Attacker logs in with stolen lecturer password &rarr; MFA, strong password policy, account lockout.
  - *Tampering:* Student intercepts API request to alter their own marks &rarr; Server-side authorization check, HMAC, digital signatures.
  - *Repudiation:* Lecturer denies altering a mark &rarr; Immutable, tamper-evident audit logs with NTP UTC timestamps and user IDs.
  - *Information Disclosure:* SQL injection dumps exam questions or student records &rarr; Parameterized queries, AES-256 database encryption at rest, TLS 1.3 in transit.
  - *Denial of Service:* Traffic flood crashes results portal on release day &rarr; API rate limiting, Web Application Firewall (WAF), autoscaling.
  - *Elevation of Privilege:* Student calls `/admin/users` or lecturer endpoints directly &rarr; Role-Based Access Control (RBAC), Complete Mediation on every request.
- **Why Design Phase?** Threat modeling must occur during the design phase (Shift-Left) because fixing architectural security flaws early costs up to 10&times;&ndash;100&times; less than fixing them in testing or production, prevents costly rework, and establishes security requirements and test cases before coding begins.

### 10.2 Essay Scenario 1: LankaPay Online Banking Application (Q3 Focus)
- **Context:** Fintech mobile wallet for transfers, bill payments, and merchant checkouts with AWS backend (RDS, S3, REST APIs). Previous development followed traditional waterfall with late penetration testing (resulting in a 5-week release delay).
- **Shift-Left Rationale:** Moving security from late testing to early SDLC stages. Defect cost curve: Requirements ($1\times$), Design ($5\times$), Coding ($10\times$), Testing ($15\times$), Production ($100\times$). Continuous automated testing in CI/CD gives developers immediate feedback and prevents deployment delays.
- **Five Core Secure Coding Practices:**
  1. *Parameterized Queries (Prepared Statements):* Eliminates SQL injection by treating input as literal data.
  2. *Allow-list Input Validation:* Strict regex (`/^[a-zA-Z0-9_]{3,20}$/`), type, and length checks; fails closed.
  3. *Context-Aware Output Encoding:* Converts HTML special characters to safe entities (`&lt;`, `&gt;`, `&amp;`) to defeat XSS.
  4. *Memory-Hard Password Hashing:* Argon2id or bcrypt with unique salt and work factor &ge; 12; never MD5/SHA.
  5. *Complete Mediation & Server-Side Authorization:* Check user authentication and role on *every* protected request (`if user.role != 'ADMIN': return 403`).
  - *Database Least Privilege:* App DB user has only `SELECT, INSERT, UPDATE` (never `DROP` or `GRANT`).
  - *Secrets Management:* Never hardcode API keys or DB passwords; load at runtime from AWS Secrets Manager.
- **Three Core Infrastructure Security Measures:**
  1. *Network Segmentation:* RDS database in private subnet with no public IP; Security Groups restrict port 3306 exclusively to the API tier; AWS WAF on public Application Load Balancers.
  2. *IAM Least Privilege & MFA:* Stop using the root account; issue short-lived STS/SSO role credentials instead of long-lived access keys; enforce MFA for all users.
  3. *Data Encryption & Protection:* S3 Block Public Access; encrypt S3 buckets and RDS storage using AWS KMS (AES-256); enforce TLS 1.3 in transit.
  - *Shift-Left IaC:* Write infrastructure in Terraform/CloudFormation and scan in CI/CD using Checkov/tfsec before provisioning.

### 10.3 Essay Scenario 2: MediCare Plus Cloud Healthcare System (Q4 Focus)
- **Context:** Private hospital with EU medical-tourism patients; microservices in Docker containers on Kubernetes; GitHub CI/CD pipeline. Previous breach: leaked GitHub token &rarr; malicious dependency &rarr; privileged root container &rarr; container escape &rarr; `cluster-admin` service account read all K8s secrets &rarr; 40,000 patient records exfiltrated.
- **DevSecOps 6-Stage CI/CD Pipeline & Tools:**
  1. *Code / Commit:* Pre-commit hooks, secret scanning (Gitleaks, TruffleHog), signed Git commits.
  2. *Build:* SAST (SonarQube, Semgrep) + SCA (Snyk, OWASP Dependency-Check, Dependabot).
  3. *Package:* Container image scanning (Trivy, Grype), SBOM generation (CycloneDX, SPDX), image signing (Cosign/Sigstore).
  4. *Test / Staging:* DAST (OWASP ZAP) + IaC scanning (Checkov, tfsec, KICS).
  5. *Deploy:* Admission controllers (OPA Gatekeeper, Kyverno) enforcing signed images and non-root pods; automated Security Gates blocking deployment on Critical CVEs or exposed secrets.
  6. *Runtime:* Continuous runtime threat monitoring (Falco, Wazuh) and SIEM (Microsoft Sentinel, Splunk).
- **Four Docker Container Risks & Controls:**
  1. *Running as Root:* Compromising container yields root on worker node &rarr; `USER nonroot` (UID 10001), drop capabilities (`--cap-drop=ALL`).
  2. *Privileged Containers / Docker Socket:* `--privileged` or mounting `/var/run/docker.sock` allows full container escape &rarr; Disable privileged containers; never mount docker.sock.
  3. *Secrets Baked into Images:* `ENV` or `ARG` passwords persist in image layers &rarr; Inject at runtime via Kubernetes Secrets or HashiCorp Vault; use `.dockerignore`.
  4. *Vulnerable / Bloated Images:* Unpinned tags (`:latest`) contain thousands of outdated packages &rarr; Use minimal pinned base images (`python:3.12-slim`), multi-stage builds, and Trivy image scanning.
- **Kubernetes RBAC Access Controls:**
  - *Developer:* Namespaced `Role` in `dev` namespace (`get, list, create, update` on `pods, services, deployments`). **No access to Secrets, no cluster-admin!**
  - *Administrator:* `ClusterRoleBinding` to `cluster-admin` strictly restricted to authorized platform engineers with mandatory MFA.
  - *Service Accounts:* Dedicated per application; disable token automounting (`automountServiceAccountToken: false`) when pods do not need Kubernetes API access.
  - *NetworkPolicies:* Default-deny ingress & egress; permit only Frontend &rarr; Backend &rarr; Database; block egress to arbitrary internet IPs to prevent data exfiltration.
  - *Pod Security Standards:* Set `privileged: false`, `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, and CPU/memory limits.
- **Healthcare Governance & Compliance (GRC):**
  - *GDPR Article 33:* Mandatory 72-hour notification to supervisory authority upon discovering a personal data breach; extraterritorial reach applies to EU patient records.
  - *HIPAA Safeguards:* Administrative (access review policies, staff training), Physical (data center badges, device disk encryption), and Technical (AES-256 encryption at rest, TLS 1.3, MFA, RBAC).
  - *Three Protection Controls:* 1. Technical (encryption at rest/transit, MFA, RBAC); 2. Administrative (least privilege audits, IR policy); 3. Physical (secure facility access, laptop BitLocker).
  - *ENISA:* European Union Cybersecurity Agency &rarr; Advisory agency providing best practices and threat reports (**NOT statutory law**).
  - *Compensating Control:* Alternative security measure implemented when primary control is infeasible (e.g. isolated network segment when legacy system lacks MFA).
- **Continuous Security Monitoring (CSM):**
  - Centralized log aggregation into SIEM (Microsoft Sentinel, Splunk, Elastic) with UTC clock synchronization (NTP).
  - Anomaly detection on outbound egress traffic (to immediately catch data exfiltration).
  - Detection of privilege escalation, bulk secret reading, and unauthorized container creations.
- **Incident Response 6-Phase Lifecycle:**
  1. *Preparation:* IR policy, designated incident response team, playbooks, verified offline backups.
  2. *Detection & Analysis:* Alert triage, SIEM correlation, scope determination (40,000 patient records), identifying IOCs.
  3. *Containment:* Short-term: revoke leaked GitHub token, isolate compromised pods/worker nodes, block attacker IP address. Long-term: apply NetworkPolicies to prevent lateral spread.
  4. *Eradication:* Remove malicious package from `requirements.txt`, patch vulnerabilities, re-image compromised nodes, rotate database password and all Kubernetes Secrets.
  5. *Recovery:* Redeploy clean, signed images from approved registry; restore database from clean backup; verify service health; heighten monitoring.
  6. *Lessons Learned:* Post-mortem root cause analysis (RCA), update pipeline security gates (mandatory secret scanning and SCA), notify EU data protection authority within 72 hours under GDPR Article 33.
  - *Digital Forensics & Chain of Custody:* Create bit-stream disk/memory images; verify SHA-256 hashes; work strictly on copies (never live original); document every transfer and custodian to ensure evidence admissibility in legal proceedings.
