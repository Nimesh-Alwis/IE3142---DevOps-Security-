# IE3142 – DevOps Security
## Mock Final Paper 05
[← Previous: Mock Paper 04](IE3142_Mock_Paper_04.md) | [All Mock Papers →](../../README.md#mock-papers-5)
### Duration: 2 Hours
### Instructions
- Follows the provided final-exam structure.
- **No MCQ section is included.**
- Answer Q2, Q3 and Q4.

# Question 2 – Structured Question

## 2.1 Threat Modelling – STRIDE Model Only

An online banking support portal allows customers to authenticate, view account information and submit service requests. Support staff manage customer requests and administrators manage user accounts and system settings.

Using the **STRIDE model only**:
1. Identify important assets.
2. Identify suitable STRIDE threats.
3. Explain the possible impact.
4. Recommend suitable security controls.

## 2.2 CI/CD Pipeline

A company wants to implement DevSecOps for a customer-facing application. The organization is concerned about source-code vulnerabilities, vulnerable third-party dependencies, exposed credentials, insecure containers and infrastructure misconfigurations.

Design a secure CI/CD pipeline that includes:
- Secret scanning
- SAST
- SCA
- DAST
- Container scanning
- IaC scanning
- Security Gate

Explain how each activity contributes to secure software delivery.

## 2.3 Docker

A development team plans to deploy a web application using Docker.

Explain:
1. The purpose of Docker.
2. Docker Client.
3. Docker Daemon/Engine.
4. Docker Image.
5. Docker Container.
6. Docker Registry.
7. Image versus Container.
8. Important Docker/container security risks and controls.

# Question 3 – Scenario 1

A financial services organization is developing a mobile and web customer platform. Security testing is mostly performed after development. The organization has experienced insecure database queries, weak authentication and authorization problems.

### 3.1 Shift-Left Security
Explain how a Shift-Left security approach can improve the SDLC.

### 3.2 Secure Coding Practices
Recommend secure coding practices that can reduce the identified vulnerabilities.

### 3.3 Threat Modelling – STRIDE Only
Apply the STRIDE model only to the financial-services platform. Identify threats and propose appropriate controls.

### 3.4 Infrastructure Security
Recommend infrastructure-security controls to protect the platform, users and supporting systems.

# Question 4 – Scenario 2

A healthcare provider operates a cloud-based platform for managing patient appointments and medical information. The platform uses GitHub, CI/CD, Docker containers and Kubernetes. A security assessment discovers hardcoded credentials, vulnerable dependencies, vulnerable container images, excessive Kubernetes permissions, unclear security responsibilities and inadequate monitoring. The organization also has no documented incident-response process.

### 4.1 CI/CD Pipeline
Design a secure CI/CD pipeline that identifies and blocks security problems before production deployment.

### 4.2 Docker / Containers
Explain the security risks associated with Docker containers and recommend suitable controls.

### 4.3 Kubernetes Access Controls
Explain how Kubernetes RBAC and least privilege should be implemented for developers, operations staff and administrators.

### 4.4 Governance Security
Explain how security governance and compliance responsibilities should be established for a healthcare environment.

### 4.5 Security Monitoring and Incident Response
Explain how continuous security monitoring should be implemented and describe the incident-response phases for a confirmed patient-information breach.
