# IE3142 DevOps Security — Week 02: Secure Software Development Practices

**Language:** Sinhala + English | **Purpose:** Complete compact lecture revision notes

> **Exam tip:** English keywords and definitions මතක තියාගෙන, explanations Sinhala-English mix එකෙන් understand කරන්න. මේවා lecture concepts simplify කළ revision notes; original slides replace කරන full transcript එකක් නෙවෙයි.

## 1. Secure SDLC
`Requirements → Design → Development → Testing → Deployment → Maintenance`
| Phase | Core security question | Output |
|---|---|---|
| Requirements | Feature එක abuse කරන්න පුළුවන්ද? | Abuse cases, data classification |
| Design | Weak points මොනවාද? | Threat model |
| Implementation | Code secure ද? | Reviewed secure code |
| Testing | System break කරන්න පුළුවන්ද? | SAST/DAST results |
| Deployment | Config harden කරලාද? | Managed secrets, hardened config |
| Operations | Attack detect වෙනවද? | Logs, alerts, patches |

## 2. Secure Coding
- Secure coding = code ලියන විට vulnerabilities prevent කර confidentiality, integrity, availability, reliability protect කිරීම.
- Common weaknesses: **SQLi**, **XSS**, **CSRF**, **command injection**, **buffer overflow**, **broken authentication**, **sensitive-data exposure**.
- General habits: validate inputs, encode outputs, parameterized SQL, secure password hashes, least privilege, safe errors, patch dependencies, no hard-coded secrets.

## 3. Four core secure-coding habits
### A. Input validation
- Outside input (form, URL, files, API) **untrusted** කියලා assume කරන්න.
- Check **type, format, length, range, allowed characters**; invalid input reject කරන්න.
- **Allow-list** (explicitly permit valid format) > blocklist (known bad strings block), because variants evade blocklists.
- **Canonicalize/normalize first → validate → use** (URL encoding, Unicode, case tricks).
- Existing framework validation features prefer කරන්න.

### B. Parameterized queries / prepared statements
- SQL command එක සහ supplied data වෙන වෙනම send කරන නිසා user input query syntax එකට convert වෙන්නේ නෑ.
```python
# Weak: string concatenation
query = "SELECT * FROM users WHERE name='" + name + "'"
# Strong: parameterized query
cursor.execute('SELECT * FROM users WHERE name = ?', (name,))
```
- **SQLi** prevent කරන ප්‍රධාන coding control.

### C. Context-aware output encoding
- HTML/attribute/JavaScript/URL contexts අනුව output encode කර browser එක data **display** කරන්න, code **execute** නොකරන්න.
- XSS prevention: HTML body එකේ `<` → `&lt;`, `>` → `&gt;`; frameworks autoescape use කරන්න.
- Input validation AND output encoding දෙකම ඕන.

### D. Least privilege
- Every service/app/database user minimum permissions only. Read-only service එකට DROP/DELETE දෙන්න එපා.
- Impact: compromise උනත් attackerගේ **blast radius** සීමා වෙනවා.

## 4. Authentication vs Authorization
- **Authentication (AuthN)** = *Who are you?* (password/MFA/session).
- **Authorization (AuthZ)** = *What can you access?* (RBAC, deny-by-default, check every request).
- Strong password policy, adaptive login throttling, MFA, Argon2/bcrypt hashing, secure sessions.
- Every object request එකේ access check කරන්න; login වෙලා ඉඳීම alone enough නෑ (IDOR risk).

## 5. Secure logging and OWASP coding guidance
- Log authentication failures, access violations, security events; audit records investigation වලට useful.
- Never log plaintext passwords, API tokens, sensitive values.
- OWASP checklist includes validation, encoding, authentication, sessions, access control, crypto, error handling, logging, file/database security, transport security.

## 6. Weakness → Fix → test
| Weakness | Main defense | Typical check |
|---|---|---|
| Injection | Validation + parameterized queries | SAST/code review |
| XSS | Context-aware encoding | SAST/DAST |
| Privilege escalation | Least privilege + per-request authorization | IAM review, access tests |
| Credential leaks | Secrets manager + secret scanning | Repo scan |
| Known vulnerable library | Patch + dependency review | SCA |

## 7. Design and threat-model connection
- Secure coding controls **implementation**, secure design controls **architecture**. Both required.
- Code එක ලියන්න කලින් threat model එක කර attack paths identify කරන එක Shift Left strategy එකක්.
- Exam line: *Validate input, use parameterized queries, encode output, and apply least privilege to prevent common weaknesses.*
