# IE3142 DevOps Security — Week 04: Infrastructure Security

**Language:** Sinhala + English | **Purpose:** Complete compact lecture revision notes

> **Exam tip:** English keywords and definitions මතක තියාගෙන, explanations Sinhala-English mix එකෙන් understand කරන්න. මේවා lecture concepts simplify කළ revision notes; original slides replace කරන full transcript එකක් නෙවෙයි.

## 1. Infrastructure Security overview
- Infrastructure security = applications support කරන **physical/virtual infrastructure** (servers, VMs, networks, cloud, OS, databases, storage, containers, IAM) protect කිරීම.
- Goals: CIA triad, availability, continuity, authorized access, regulatory compliance.
- **Defense in depth:** network segmentation + firewall + IAM/MFA + encryption + IDS/IPS + monitoring + hardened configuration.

## 2. Cloud computing foundations
- Cloud computing = on-demand shared computing resources over networks.
- Characteristics: **on-demand self service, broad network access, resource pooling, rapid elasticity, measured service**.
- Pros: scalability, agility, reduced capital investment; risks: misconfiguration, exposed APIs, identity compromise, shared infrastructure, visibility challenges.

## 3. Cloud service/deployment models
| Service model | Provider manages | Customer main responsibility |
|---|---|---|
| **IaaS** | Physical hardware & virtualization | Guest OS, apps, identities, data/config |
| **PaaS** | Platform/runtime + underlying infrastructure | App code, identities, data/config |
| **SaaS** | Hosted app + platform | User access, configuration, data governance |
- Deployment models: **Public, Private, Hybrid, Community** cloud.
- **Shared Responsibility Model:** Provider protects **security OF the cloud**; customer manages their part **IN the cloud**. Exact split service-dependent.

## 4. AWS and Azure security services
| Purpose | AWS | Azure |
|---|---|---|
| IAM / identities | AWS IAM | Microsoft Entra ID |
| Activity audit | CloudTrail | Azure Activity Log |
| Monitoring | CloudWatch | Azure Monitor |
| Threat/overall posture | GuardDuty / Security Hub | Defender for Cloud |
| Keys / secrets | KMS / Secrets Manager | Key Vault |
| Network firewall | Security Groups / network ACLs | NSGs / Azure Firewall |
- **Misconfiguration** (public bucket, permissive network access, weak roles) is a major cloud risk.

## 5. Data protection + resilience
- **Encryption at rest** (stored data) / **in transit** (TLS/HTTPS).
- Data classification: public, internal, confidential, restricted; control access accordingly.
- Backup + disaster recovery: test restore, secure off-site backups, retention and monitoring.
- **RTO (Recovery Time Objective)** = maximum acceptable time to restore service.
- **RPO (Recovery Point Objective)** = maximum acceptable data-loss time window.
- Example: RTO 2h → restore within ~2h; RPO 15min → at most ~15min data loss target.

## 6. Network security
- Network security ensures **Confidentiality, Integrity, Availability** in traffic/networks.
- **Firewall:** filters traffic using policy; packet filter / stateful / application-aware options.
- **WAF:** HTTP/HTTPS application request protection.
- **IDS:** detect and alert suspicious traffic (doesn't automatically block).
- **IPS:** inline detect **and block** attacks.
- Detection: **signature-based** known patterns; **anomaly-based** deviations from normal.
- **VPN:** encrypted tunnel over untrusted network. Remote-access VPN connects user→office, site-to-site connects network→network.
- Other controls: network segmentation, ACLs, secure DNS, monitoring, least-exposed ports.

## 7. Identity and Access Management (IAM)
- **IAM** controls digital identities and permissions (authentication, authorization, auditing/accountability).
- **RBAC** = permission based on roles; **ABAC** = attributes; **DAC** = resource owner control; **MAC** = centrally enforced security labels.
- **PoLP:** minimum permissions and temporary elevated privileges if required.
- **MFA factors:** something you know / have / are.
- **Federation:** external identity provider trust; **SSO:** one sign-on for several services.
- Threats: overly broad roles, dormant accounts, leaked access keys, missing MFA, insecure service accounts.
- Best practices: deny by default, periodic role reviews, remove unused identities, key rotation, audit logs, MFA for privileged access.

## 8. Hardening and secure configuration
- **Hardening** = unnecessary services/ports remove, patches apply, secure baseline set, privileged access reduce, encryption/logging enable.
- **Configuration management** = standard approved, repeatable, auditable settings; detect drift.
- **IaC (Infrastructure as Code)** can make configurations version-controlled, reviewable and scannable.
- Exam answer structure: *Assets → Threats → IAM/network/encryption/hardening → Monitor/backup → Justification.*
