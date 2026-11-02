# IE3142 DevOps Security — Week 01: Introduction to DevSecOps

**Language:** Sinhala + English | **Purpose:** Complete compact lecture revision notes

> **Exam tip:** English keywords and definitions මතක තියාගෙන, explanations Sinhala-English mix එකෙන් understand කරන්න. මේවා lecture concepts simplify කළ revision notes; original slides replace කරන full transcript එකක් නෙවෙයි.

## 1. Why Software Security?
- Applications store **personal, financial, medical information**. Breach එකකින් financial loss, customer trust loss, legal issues, reputation damage එන්න පුළුවන්.
- Traditional development වල security **end එකේ testing** කරන නිසා SQLi, broken authentication, weak password storage වැනි flaws late discover වෙනවා → fixing cost + release delay.
- Modern systems cloud, APIs, continuous releases, third-party libraries නිසා attack surface වැඩියි.

## 2. Traditional SDLC vs DevOps vs DevSecOps
| Approach | Main focus | Weakness / advantage |
|---|---|---|
| Traditional SDLC | Requirements → Design → Development → Testing → Deployment → Maintenance | Sequential silos, late feedback, security late |
| DevOps | Development + Operations collaboration; automation + fast delivery | Security automatically guaranteed නෑ |
| DevSecOps | Development + Security + Operations throughout SDLC | Early, continuous and shared security |
- **DevOps** = culture/practices combining Development and Operations to deliver software quickly and reliably.
- **DevSecOps** = integrate security into **every stage** of software delivery rather than final test එකක් විතරක් කරන්නෙ නැහැ.

## 3. DevOps lifecycle
`Plan → Code → Build → Test → Release → Deploy → Operate → Monitor → (feedback to Plan)`
- **CI/CD**: code integration, testing, release/deployment automate කිරීම.
- Benefits: faster releases, better cooperation, repeatability, quick feedback, fewer manual errors.

## 4. Four central DevSecOps principles
1. **Shared Responsibility** — Developers, Security, Operations හැමෝම security own කරනවා. Security team එකේ විතරක් job එකක් නෙවෙයි.
2. **Security Automation** — SAST, dependency scan, secret scan, configuration scan pipelines වල automate කරන්න.
3. **Continuous Security** — planning සිට maintenance දක්වා security checks repeat වෙනවා.
4. **Continuous Monitoring** — logs, configurations, access, vulnerabilities track කර alerts + response කරන්න.

## 5. Shift Left Security
- **Shift left** = security tests & decisions SDLC එකේ **earlier** stages වලට ගෙනයාම.
- Traditional: `Code → Test → Deploy → Security review (late)`
- Shift left: `Security requirements → Threat model → Secure code → Automated tests → Secure deployment`.
- Benefits: cheaper fixes, faster feedback, reduced release delays, prevention rather than late repair.

## 6. Security integrated in SDLC
| Phase | Security activities |
|---|---|
| Requirements | Define security requirements, data privacy, abuse cases |
| Design | Threat modeling, access controls, secure architecture |
| Coding | Secure coding, code review, SAST, input validation |
| Testing | DAST, vulnerability testing, security verification |
| Deployment | Secrets management, hardened configs, access restrictions |
| Operations | Monitoring, patching, incident handling, ongoing scanning |

## 7. Scenario answer: Online shopping/banking application
- **Issue:** security only before release → SQLi, weak authentication etc. identified late.
- **Recommendation:** design-phase threat modeling, parameterized queries, password hashing, authorization checks, automated SAST/DAST, secure deployment, monitoring.
- **Exam line:** *DevSecOps embeds shared, automated, continuous security in every SDLC phase and reduces late-stage vulnerabilities.*
