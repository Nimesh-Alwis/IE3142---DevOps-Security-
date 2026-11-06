# IE3142 – DevOps Security
## Mock Final Paper 03
[← Previous: Mock Paper 02](IE3142_Mock_Paper_02.md) | [Next: Mock Paper 04 →](IE3142_Mock_Paper_04.md)
### Duration: 2 Hours
### Instructions
- Follows the provided final-exam structure.
- **No MCQ section is included.**
- Answer Q2, Q3 and Q4.

# Question 2 – Structured Question

## 2.1 Threat Modelling – STRIDE Model Only

A university student-management system allows students to update profiles, register for courses and view grades. Lecturers can update grades and administrators manage user accounts.

Using the **STRIDE model only**:
1. Identify important system assets.
2. Identify threats using STRIDE.
3. Explain the security impact.
4. Recommend suitable security controls.

## 2.2 CI/CD Pipeline

A development team wants to automatically test security whenever code is pushed to its source-code repository.

Explain how the following can be incorporated into the CI/CD pipeline:
- Secret scanning
- SAST
- SCA
- DAST
- Container scanning
- IaC scanning
- Security Gate

Provide a logical pipeline flow and explain how a failed security gate should affect deployment.

## 2.3 Docker

A company is moving an existing web application into Docker containers.

Explain:
1. Docker and its purpose.
2. Docker Client and Docker Daemon/Engine.
3. Docker Images and Containers.
4. Docker Registry.
5. Image versus Container.
6. Container-security risks and appropriate controls.

# Question 3 – Scenario 1

An insurance company is developing a customer portal. Developers focus mainly on functionality and perform security testing at the final testing stage. The application later shows input-validation problems, insecure database queries and access-control weaknesses.

### 3.1 Shift-Left Security
Explain how a Shift-Left approach can be introduced from design through deployment.

### 3.2 Secure Coding Practices
Recommend secure coding practices for preventing the identified application vulnerabilities.

### 3.3 Threat Modelling – STRIDE Only
Apply the STRIDE model only to the customer portal. Identify threats and propose controls.

### 3.4 Infrastructure Security
Explain infrastructure-security measures required to protect the customer portal and supporting systems.

# Question 4 – Scenario 2

A hospital deploys a patient-record system using a cloud platform, GitHub, Docker and Kubernetes. The team discovers vulnerable dependencies and insecure container configurations. Several developers have excessive access to Kubernetes resources. Security logs are collected but rarely reviewed.

### 4.1 CI/CD Pipeline
Explain how a secure CI/CD pipeline should detect vulnerabilities before deployment.

### 4.2 Docker / Containers
Identify container-security risks and recommend controls.

### 4.3 Kubernetes Access Controls
Explain how RBAC, roles, role bindings and least privilege can control access.

### 4.4 Governance Security
Explain why security governance is important for sensitive healthcare information.

### 4.5 Security Monitoring and Incident Response
Explain how continuous monitoring can detect suspicious activity and describe the incident-response process after a confirmed incident.
