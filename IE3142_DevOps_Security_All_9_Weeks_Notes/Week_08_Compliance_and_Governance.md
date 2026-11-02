# IE3142 DevOps Security — Week 08: Compliance and Governance

**Language:** Sinhala + English | **Purpose:** Complete compact lecture revision notes

> **Exam tip:** English keywords and definitions මතක තියාගෙන, explanations Sinhala-English mix එකෙන් understand කරන්න. මේවා lecture concepts simplify කළ revision notes; original slides replace කරන full transcript එකක් නෙවෙයි.

## 1. Governance, Risk, Compliance (GRC)
- **Governance** = direction, accountability, policy and decisions about security aligned with business goals.
- **Risk management** = identify threats/vulnerabilities, assess likelihood/impact, select treatment.
- **Compliance** = demonstrate laws, regulations, contracts, policies, standards followed.
- **GRC** brings these together. Security is not tools only; evidence + ownership + monitoring needed.

## 2. Rules, standards, frameworks, guidance
| Category | Meaning | Example |
|---|---|---|
| Law/regulation | Legally binding requirements | GDPR |
| Sector-specific law | Applies particular sector/entity | HIPAA (U.S. healthcare) |
| Standard | Documented requirements/practices | ISO/IEC 27001 |
| Framework | Structured management approach | NIST CSF |
| Guidance agency | Recommendations, threat reports | ENISA |

## 3. GDPR (European data protection)
- **GDPR** regulates processing personal data in EU/EEA; can apply outside EU under specified conditions.
- Seven principles: **lawfulness/fairness/transparency; purpose limitation; data minimization; accuracy; storage limitation; integrity/confidentiality; accountability**.
- Core obligations: lawful processing basis, privacy notices, support applicable rights (access, correction, erasure), protection by design/default, records and appropriate safeguards.
- **Certain personal-data breaches require notice to authority within 72 hours after awareness when Article 33 applies**; not every breach automatically.

## 4. HIPAA
- **HIPAA** = U.S. health-information law relevant to **PHI**, especially covered entities/business associates.
- **Privacy Rule:** uses/disclosures of PHI + individual rights.
- **Security Rule:** safeguards for **ePHI** (electronic protected health information).
- **Breach Notification Rule:** notifications for certain breaches of unsecured PHI.
- Safeguards: **Administrative** (risk analysis, policies/training), **Physical** (facility/device controls), **Technical** (access, audit, integrity, transmission protection).

## 5. ENISA
- **ENISA** = EU Agency for Cybersecurity, **not a law/regulation**.
- Publishes cybersecurity guidance, good practices, reports and assists EU cyber capabilities.
- **Memory:** GDPR = personal data regulation; HIPAA = U.S. healthcare law; ENISA = EU cyber guidance agency.

## 6. Security controls for compliance
- **Administrative:** governance policies, asset owners, staff training, risk process.
- **Technical:** IAM/MFA, encryption, monitoring, logging, backups, patching.
- **Physical:** secure rooms, locks, asset controls.
- Choose controls by obligation, data sensitivity, risk and documentation needs.

## 7. Audit, assessment and evidence
- **Audit** = systematic evaluation of whether controls meet defined requirements.
- **Assessment** = evaluate risks/control effectiveness/gaps.
- **Evidence** = policies, screenshots/config exports, IAM reviews, scan reports, backup tests, signed training records, log samples.
- Practical flow: `Requirement → Control → Owner → Implementation → Evidence → Test → Finding → Remediation → Re-test/report`.
- **Compliance ≠ automatically secure.** It establishes baseline and evidence, while continuous risk management still needed.

## 8. Scenario: patient management cloud app
- Need access restrictions, encryption, secure logging, incident plans, evidence of controls and data governance.
- Use **HIPAA** only if legally applicable to covered entity/associate; GDPR if applicable to EU-personal-data processing.
- Exam line: *Governance sets responsibility, risk management selects controls, compliance demonstrates obligations are met.*
