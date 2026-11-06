# IE3142 – DevOps Security
## Mock Final Paper 04
[← Previous: Mock Paper 03](IE3142_Mock_Paper_03.md) | [Next: Mock Paper 05 →](IE3142_Mock_Paper_05.md)
### Duration: 2 Hours
### Instructions
- Follows the provided final-exam structure.
- **No MCQ section is included.**
- Answer Q2, Q3 and Q4.

# Question 2 – Structured Question

## 2.1 Threat Modelling – STRIDE Model Only

A food-delivery platform allows customers to create accounts, place orders and track deliveries. Delivery staff update order status, while administrators manage customers, restaurants and delivery accounts.

Using the **STRIDE model only**:
1. Identify important assets.
2. Identify suitable threats.
3. Explain the possible impact.
4. Recommend appropriate controls.

## 2.2 CI/CD Pipeline

A DevOps team wants to prevent insecure code, vulnerable dependencies and exposed secrets from reaching production.

Design a CI/CD security pipeline using:
- Secret scanning
- SAST
- SCA
- DAST
- Container scanning
- IaC scanning
- Security Gate

Explain each security activity and what should happen when a critical vulnerability is detected.

## 2.3 Docker

A company deploys several services as Docker containers.

Explain the Docker architecture and the role of Docker Client, Docker Daemon/Engine, Images, Containers and Registry. Then explain common container-security risks and suitable controls.

# Question 3 – Scenario 1

A telecommunications company is developing a customer self-service application. The organization discovers that security activities are mainly performed at the end of development. Developers also use insecure coding practices and the infrastructure is protected by only basic access controls.

### 3.1 Shift-Left Security
Explain how the company can implement Shift-Left security across the SDLC.

### 3.2 Secure Coding Practices
Recommend secure coding practices developers should follow.

### 3.3 Threat Modelling – STRIDE Only
Use the STRIDE model only to identify threats affecting the application and recommend controls.

### 3.4 Infrastructure Security
Recommend infrastructure-security controls including access control, network protection and data protection.

# Question 4 – Scenario 2

A government organization develops a cloud-based service using GitHub, CI/CD, Docker and Kubernetes. A review identifies exposed secrets, vulnerable dependencies, insecure container images and excessive Kubernetes permissions. Security responsibilities are unclear and the organization lacks effective monitoring and incident-response procedures.

### 4.1 CI/CD Pipeline
Explain how security can be integrated into the CI/CD pipeline from source-code management through deployment.

### 4.2 Docker / Containers
Explain Docker/container security risks and suitable controls.

### 4.3 Kubernetes Access Controls
Explain how Kubernetes RBAC and least privilege can prevent excessive access.

### 4.4 Governance Security
Explain how security governance can establish security responsibilities, policies and accountability.

### 4.5 Security Monitoring and Incident Response
Explain how continuous monitoring detects incidents and describe the steps required to respond to a confirmed compromise.
