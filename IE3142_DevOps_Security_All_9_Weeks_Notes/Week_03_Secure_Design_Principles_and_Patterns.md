# IE3142 DevOps Security — Week 03: Secure Design Principles and Patterns

**Language:** Sinhala + English | **Purpose:** Complete compact lecture revision notes

> **Exam tip:** English keywords and definitions මතක තියාගෙන, explanations Sinhala-English mix එකෙන් understand කරන්න. මේවා lecture concepts simplify කළ revision notes; original slides replace කරන full transcript එකක් නෙවෙයි.

## 1. Secure Design
- **Secure design** = coding start වීමට පෙර architecture level එකේ security consider කිරීම.
- Includes **trust boundaries, data flows, access control, component interactions, failure behavior, attack surface, assumptions**.
- **Secure design vs secure coding:** architecture/RBAC policy **vs** implementation/parameterized SQL. Design is earlier in SDLC.

## 2. Twelve secure design principles (important)
| Principle | Sinhala-English simple meaning |
|---|---|
| **Defence in Depth** | Controls layers කිහිපයක්; එකක් fail වුණත් අනෙක් layer protect කරනවා |
| **Fail Securely** | Error/failure එකකදී unauthorized access නොදී safe state |
| **Least Privilege** | Minimum required permissions only |
| **Fail-Safe Defaults** | Default **deny**, explicitly grant access |
| **Secure Defaults** | Installation/configuration එකේ default settings secure |
| **Minimize Attack Surface** | Unnecessary ports, services, interfaces disable |
| **Separation of Duties** | Sensitive tasks split between people/roles |
| **Complete Mediation** | **Every request** authorization check (not once only) |
| **Economy of Mechanism** | Security design simple & understandable |
| **Open Design** | Security depend on key/secret; design secrecy මත නෙවෙයි |
| **Least Common Mechanism** | Minimize shared mechanisms/resources |
| **Psychological Acceptability** | Security controls usable; users bypass නොකරන ලෙස |

## 3. Security design patterns
- **RBAC**: permissions roles වලට; users roles assign වෙනවා.
- **Defense in depth**: firewall + authentication + authorization + encryption + monitoring.
- **Secure gateway/central entry control**: public-facing requests check before internal services.
- **Input validation and secure session patterns**: trusted boundaries and users protect කිරීම.

## 4. Threat Modeling
- **Threat modeling** = system එකේ threats, assets, attack paths, vulnerabilities *before attacks happen* identify/prioritize කරන structured analysis.
- Workflow: `Identify assets → Diagram architecture/data flows → Identify trust boundaries → List threats → Assess likelihood/impact → Select mitigations → Validate/review`.
- **DFD (Data Flow Diagram)**: external entities, processes, data stores, data flows, **trust boundaries** indicate කරන්න.
- **Trust boundary** = different trust levels cross වන ස්ථානය; e.g. Internet → API → internal database.

## 5. STRIDE threat categories
| STRIDE | Meaning | Example + defense |
|---|---|---|
| **S – Spoofing** | Impersonate identity | Fake login/session → MFA/AuthN |
| **T – Tampering** | Unauthorized modify data | Edited transaction → integrity checks |
| **R – Repudiation** | Deny performed action | Missing audit → tamper-resistant logs |
| **I – Information Disclosure** | Data exposure | Account leak → encryption/access control |
| **D – Denial of Service** | Service unavailable | Flood → rate limits/availability controls |
| **E – Elevation of Privilege** | Gain higher rights | User becomes admin → least privilege/AuthZ |

## 6. Risk assessment
- **Risk** relates to likelihood of a threat occurring AND impact if it occurs.
- Practical prioritization: identify **asset + threat + vulnerability + impact + likelihood**, classify low/medium/high, recommend treatment.
- Treatments: **Mitigate** (security control), **Avoid** (stop risky operation), **Transfer** (contract/insurance), **Accept** (documented approval).
- High likelihood + high impact = high priority.

## 7. Banking scenario
`Customer → Web/App API → Authentication service → Database`
- Risks: SQLi, account-IDOR, stolen passwords, data exposure, payment alteration.
- Controls: parameterized queries, MFA, per-account authorization, TLS, encryption, audit logs.
- Exam line: *Secure design proactively reduces architecture weaknesses by applying principles, threat modeling and risk-driven controls.*
