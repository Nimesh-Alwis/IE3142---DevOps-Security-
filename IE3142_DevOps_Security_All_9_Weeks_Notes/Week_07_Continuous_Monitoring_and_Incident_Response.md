# IE3142 DevOps Security — Week 07: Continuous Monitoring and Incident Response

**Language:** Sinhala + English | **Purpose:** Complete compact lecture revision notes

> **Exam tip:** English keywords and definitions මතක තියාගෙන, explanations Sinhala-English mix එකෙන් understand කරන්න. මේවා lecture concepts simplify කළ revision notes; original slides replace කරන full transcript එකක් නෙවෙයි.

## 1. Continuous Security Monitoring (CSM)
- Deploy වුණා කියලා security end නෑ. **CSM** = applications, infrastructure, identity, cloud, network and configuration continuously observe/analyze කිරීම.
- Goals: detect threats early, abnormal activities identify, alerts, visibility, faster incident response.
- Watch: API calls, failed logins, processes, file modifications, cloud actions, K8s changes, network traffic.
- Feedback loop: `Plan → Code → Build → Test → Deploy → Monitor → Detect → Respond → Improve → Plan`.

## 2. Logging and log management
- **Log** = event record. Typical fields: timestamp, username, source IP, action, target resource, result, error.
- Types: application, OS, network/firewall, cloud audit, container/K8s, IAM/database.
- **Log management** = collect → centralize → store/protect → analyze → retain logs.
- Logs can reveal brute-force attempts: many rapid failed logins from same IP.
- Secure log practice: accurate time, retention, access control, tamper resistance, no passwords/tokens in logs.

## 3. SIEM and alerts
- **SIEM (Security Information and Event Management)** = logs/events from multiple sources correlate/analyze to flag attacks and support investigation.
- Flow: `Sources → Collection → Normalization/Correlation → Detection rule → Alert → Analyst response`.
- **False positive:** harmless event incorrectly flagged. **False negative:** actual attack missed.
- Alert prioritization based on context, severity and asset importance.

## 4. IDS vs IPS
| IDS | IPS |
|---|---|
| Detect and alert suspicious activity | Detect and automatically block/prevent |
| Often out-of-band | Usually inline traffic path |
| Lower blocking risk | Incorrect rule may affect legitimate traffic |
- **Signature-based**: matches known threat patterns; **anomaly-based**: unusual deviations/baseline.

## 5. Incident response (IR)
- **Security incident** = confirmed/likely event threatening confidentiality, integrity or availability.
- Common structured lifecycle:
  1. **Preparation** — IR policy, roles, logs, backups, drills.
  2. **Identification/Detection & Analysis** — verify alert, determine scope and severity.
  3. **Containment** — isolate affected hosts/accounts, block malicious access.
  4. **Eradication** — remove malware, close vulnerability, revoke compromised tokens.
  5. **Recovery** — restore validated systems, monitor for recurrence.
  6. **Lessons learned** — root cause, report, improve controls.
- Evidence handling and communication are important at each stage.

## 6. Incident investigation and digital forensics
- **Digital forensics** = collect, preserve, analyze digital evidence to reconstruct what happened.
- Examples: server logs, cloud audit logs, disk images, process/network activity, suspicious binaries.
- **Chain of custody** documents who collected/handled evidence, when, and how.
- Preserve originals, record timestamps, calculate hashes, analyze copies when possible.
- **Timeline analysis:** sequence authentication → malicious API access → privilege escalation → data exfiltration.

## 7. Scenario: suspicious admin login
- SIEM detects many failed logins + sudden admin success from unusual IP.
- Verify alerts and affected identity → contain (disable/reset credentials, revoke sessions) → review scope/logs → remediate MFA policy and root cause → restore and monitor → post-incident report.
- Exam line: *Monitoring provides detection; incident response provides organized containment, eradication, recovery and improvement.*
