# IE3142 DevOps Security — Week 09: Secure Cloud Services and Serverless Architectures

**Language:** Sinhala + English | **Purpose:** Complete compact lecture revision notes

> **Exam tip:** English keywords and definitions මතක තියාගෙන, explanations Sinhala-English mix එකෙන් understand කරන්න. මේවා lecture concepts simplify කළ revision notes; original slides replace කරන full transcript එකක් නෙවෙයි.

## 1. Cloud-native architecture
- **Cloud-native** means apps designed to use cloud capabilities (not simply hosted on a cloud server).
- Features: elastic scaling, managed services, containers, microservices, APIs, automation, IaC, serverless.
- Example services: AWS Lambda/Azure Functions (compute); S3/Blob (storage); DynamoDB/Cosmos DB (database); EventBridge/SQS/Service Bus (events); API Gateway/API Management.

## 2. Serverless computing and FaaS
- **Serverless** = provider manages underlying servers/OS/runtime availability and much scaling. **Servers still exist**; customer doesn't directly manage them.
- **FaaS (Function as a Service)** = event-triggered functions execute on demand.
- Advantages: automatic scaling, pay-per-use, faster delivery, high availability, event-driven apps, less infrastructure management.
- Examples: **AWS Lambda**, **Azure Functions**.

## 3. Event-driven serverless flow
```text
Client / Cloud Event → API Gateway / Event Source
      → Lambda / Azure Function
      → Database / Object Storage / Other Services
      → Logs / Monitoring
```
- **Events** may come from HTTP APIs, queues, file uploads, schedulers, other cloud services.

## 4. Shared Responsibility in serverless
- **Provider:** physical hardware, host OS, runtime platform, managed execution infrastructure.
- **Customer:** function code/config, IAM, data, secrets, third-party dependencies, API security, logging choices.
- Serverless removes server maintenance; **does not remove application risks**.

## 5. Common serverless threats
| Threat | Why dangerous | Control |
|---|---|---|
| Insecure function code | Injection / unsafe parsing | Validate inputs, prepared SQL |
| Excessive IAM permissions | Function compromise spreads | Scoped per-function roles |
| Insecure APIs | Unauthorized invocation | AuthN + AuthZ, TLS, rate limits |
| Vulnerable dependencies | Known CVEs exploited | SCA, patch, trusted packages |
| Exposed secrets | Tokens/DB creds leak | Secrets Manager / Key Vault |
| Event injection | Malicious payload through queue/event | Validate event structure and origin |
| Misconfiguration | Public data/resources | IaC review and policy checks |
| Insufficient logging | Attacks unnoticed | Central logs, monitoring/alerts |

## 6. API and identity protections
- Each function gets **only permissions needed**; separate Upload, Payment, Report roles.
- API Gateway controls: strong authentication, per-request authorization, HTTPS, request limits, throttling, logging, WAF when appropriate.
- **Authentication** = who? **Authorization** = allowed action?

## 7. Secrets, dependencies, data
- Never hard-code `API_KEY` or `DB_PASSWORD`; use AWS Secrets Manager, AWS SSM Parameter Store, Azure Key Vault.
- Environment variables can leak via logs/config; don't log secrets, restrict access, rotate credentials.
- SCA, dependency pinning, SBOM (when needed), trusted repositories, artifact verification, secure pipeline.
- Encrypt data **at rest** and **in transit**, minimize collected/accessed data.

## 8. Resilience, cost and errors
- **Denial of Wallet:** abusive event/request volume increases paid function executions and cloud bill.
- Countermeasures: rate limits, API quotas, throttling, concurrency controls, budget alerts, WAF/DDoS protections.
- Set sane function **timeouts**, memory/resource limits and downstream service controls.
- User-facing errors generic; internal diagnostics useful but must not expose secrets.

## 9. Monitoring and incident response
- Log invocation failures, unusual requests, IAM changes, unexpected cost/resource spikes, API actions.
- Cloud logging/metrics + alerts help detection; incident handling: identify → contain (revoke role/key/block trigger) → eradicate → recover → review.
- Exam line: *Serverless shifts infrastructure management to the provider, while customers still secure code, IAM, events, APIs, secrets, dependencies and monitoring.*
