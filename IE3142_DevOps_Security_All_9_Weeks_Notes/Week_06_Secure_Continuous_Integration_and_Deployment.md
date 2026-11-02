# IE3142 DevOps Security — Week 06: Secure Continuous Integration and Deployment

**Language:** Sinhala + English | **Purpose:** Complete compact lecture revision notes

> **Exam tip:** English keywords and definitions මතක තියාගෙන, explanations Sinhala-English mix එකෙන් understand කරන්න. මේවා lecture concepts simplify කළ revision notes; original slides replace කරන full transcript එකක් නෙවෙයි.

## 1. CI/CD definitions
- **CI – Continuous Integration:** frequently merge code to shared repo; auto build, unit/integration tests, quality + security checks.
- **Continuous Delivery:** validated software **ready for release**, often manual approval before production.
- **Continuous Deployment:** validated software **automatically deployed to production**.
- Pipeline: `Developer → Git → Build → Test → Security Checks → Package → Deploy → Production → Monitor`.

## 2. Why integrate security?
- Late testing → expensive fixes and delayed releases.
- **Shift Left:** security earlier. Benefits: early vulnerability detection, consistent security, fast feedback, less human error, lower fix cost.

## 3. Security activity per stage
| Stage | Security activity |
|---|---|
| Code | SAST + secret scanning |
| Third-party dependencies | SCA |
| Build | Secure/reproducible build validation |
| Container | Image vulnerability scanning |
| Test environment | DAST/security tests |
| Infrastructure | IaC scanning |
| Deploy | Policy/security gates |
| Production | Continuous monitoring + threat detection |

## 4. Important security testing terms
- **SAST (Static Application Security Testing)**: scans source/compiled code **without running** app. Examples: Semgrep, SonarQube, Checkmarx, Fortify. Can find dangerous code patterns, insecure functions, hard-coded values.
- **DAST (Dynamic Application Security Testing)**: tests **running** application externally; HTTP request/response based; examples include OWASP ZAP.
- **SCA (Software Composition Analysis)**: inventories third-party dependencies, known vulnerable versions, outdated packages, licenses.
- **Secret scanning**: looks for accidentally committed passwords, API tokens, cloud keys; rotate exposed credential (deleting commit alone is not enough).
- **IaC scanning**: Terraform/CloudFormation/K8s manifests config checks before infrastructure deployment.
- **Container scan:** base OS + library CVEs; prevent vulnerable images reaching registry or production.

## 5. SAST vs DAST vs SCA
| Tool class | Analyzes | Needs running app? | Finds |
|---|---|---|---|
| SAST | Source/binary | No | Code-level weaknesses |
| DAST | Runtime web/app interface | Yes | Externally observable exploitable behavior |
| SCA | Dependencies | No | Known package CVEs/licenses |
- None replaces the others: **combine all** as defense in depth.

## 6. Security gates and automation
- **Security gate** = predefined pass/fail condition; severe findings can **stop deployment**.
- Automated scan + actionable reports + defined severity thresholds + exception/approval flow.
- Security automation can include source checks, dependency scan, image scan, policy checks, continuous monitoring.

## 7. Pipeline and software supply-chain threats
- Threats: malicious dependency, hijacked build agent, stolen CI credentials, altered artifacts, compromised source repo, secrets leaked in logs.
- Controls: least privilege for pipeline identities, protected branches, approvals, secrets vault, isolate build runners, trusted dependencies, artifact signing/integrity checks.
- **Software supply chain** = source + packages + build tools + CI/CD + registries + deployment dependencies.
- **Build artifact** = executable/package/container image created by pipeline. Store in controlled artifact registry and verify integrity.

## 8. Example secure pipeline
```text
Git push
  ↓ Secret scan + SAST
  ↓ SCA (libraries)
  ↓ Build + unit tests
  ↓ Container/image scan
  ↓ IaC scan + DAST on test environment
  ↓ Policy / security gate
  ↓ Signed artifact + approved deployment
  ↓ Logs + security monitoring
```
- Exam line: *Secure CI/CD automates security testing and policy enforcement at each software-delivery stage.*
