# IE3142 – DevOps Security
## Mock Final Paper 01
[← All Mock Papers](../../README.md#mock-papers-5) | [Next: Mock Paper 02 →](IE3142_Mock_Paper_02.md)
### Duration: 2 Hours
### Instructions
- Follows the provided final-exam structure.
- **No MCQ section is included.**
- Answer Q2, Q3 and Q4.

# Question 2 – Structured Question

## 2.1 Threat Modelling – STRIDE Model Only

A university is developing an online examination platform. Students can log in, download examination papers, submit answers and view results. Lecturers can create examinations and publish marks. The system stores student identities, examination papers, submitted answers and results.

Using the **STRIDE model only**:
1. Identify four important assets.
2. Identify suitable STRIDE threats.
3. Explain the impact of each threat.
4. Propose a suitable security control for each threat.

## 2.2 CI/CD Pipeline

A software team uses GitHub and an automated CI/CD pipeline. Developers frequently push code and the pipeline automatically builds and deploys the application.

Explain how security should be integrated into the CI/CD pipeline. Include:
- Secret scanning
- SAST
- SCA
- DAST
- Container security scanning
- Infrastructure as Code (IaC) scanning
- Security Gate

Show a logical order and explain the purpose of each major check.

## 2.3 Docker

A development team packages a web application using Docker containers.

Explain:
1. What Docker is.
2. The roles of Docker Client, Docker Daemon/Engine, Docker Image, Docker Container and Docker Registry.
3. Image versus Container.
4. Four important Docker/container security risks.
5. Suitable controls for those risks.

# Question 3 – Scenario 1

A financial company is developing an online banking application. Most security testing is performed near the end of development. Final testing discovers SQL injection, weak authentication, insecure input handling and unauthorized access.

### 3.1 Shift-Left Security
Explain the Shift-Left security approach and how the company can move security activities earlier in the SDLC.

### 3.2 Secure Coding Practices
Recommend secure coding practices to reduce SQL injection, weak authentication and unauthorized access.

### 3.3 Threat Modelling – STRIDE Only
Apply the **STRIDE model only** to the online banking system. Identify threats and explain an appropriate control for each.

### 3.4 Infrastructure Security
Recommend important infrastructure-security controls for the banking application and supporting infrastructure.

# Question 4 – Scenario 2

A healthcare organization is developing a cloud-based patient-management platform using GitHub, CI/CD, Docker and Kubernetes. The platform stores sensitive patient information. A review discovers exposed secrets, vulnerable container images, excessive Kubernetes permissions, weak governance, insufficient monitoring and no well-defined incident-response process.

### 4.1 CI/CD Pipeline
Design a secure CI/CD pipeline and identify the security checks that should occur before deployment.

### 4.2 Docker / Containers
Identify important Docker/container security risks and propose suitable controls.

### 4.3 Kubernetes Access Controls
Explain how Kubernetes RBAC and least privilege can control developer and administrator permissions.

### 4.4 Governance Security
Explain the importance of security governance for a healthcare organization handling sensitive patient information.

### 4.5 Security Monitoring and Incident Response
Explain continuous security monitoring and describe the main phases of incident response for a patient-data breach.
