# IE3142 – DevOps Security
## Mock Final Paper 02
### Duration: 2 Hours
### Instructions
- Follows the provided final-exam structure.
- **No MCQ section is included.**
- Answer Q2, Q3 and Q4.

# Question 2 – Structured Question

## 2.1 Threat Modelling – STRIDE Model Only

An e-commerce platform allows customers to register, log in, place orders and make payments. Administrators manage products, orders and customer accounts. The system stores customer information, order information and payment-related data.

Using the **STRIDE model only**:
1. Identify important assets.
2. Identify suitable STRIDE threats.
3. Explain the possible impact of each threat.
4. Recommend security controls.

## 2.2 CI/CD Pipeline

A company has continuous integration and continuous delivery for an API application. Every commit should be checked before deployment.

Design a DevSecOps CI/CD security pipeline using:
- Secret scanning
- SAST
- SCA
- DAST
- Container scanning
- IaC scanning
- Security Gate

Explain what each check detects and why security gates are useful before deployment.

## 2.3 Docker

A company uses Docker to package a microservice application.

Explain the Docker architecture and the interaction between Docker Client, Docker Daemon/Engine, Docker Images, Docker Containers and Docker Registry. Then identify common container-security risks and suitable controls.

# Question 3 – Scenario 1

A software company is developing a payroll application. Security testing is performed only after the application is almost completely developed. The company frequently discovers vulnerabilities late, causing expensive rework and deployment delays.

### 3.1 Shift-Left Security
Explain how Shift-Left security improves the development process and reduces vulnerability-fixing cost.

### 3.2 Secure Coding Practices
Recommend secure coding practices for protecting employee information, authentication and database operations.

### 3.3 Threat Modelling – STRIDE Only
Use the STRIDE model only to identify threats against the payroll application and recommend controls.

### 3.4 Infrastructure Security
Explain the infrastructure-security controls required to protect the payroll system, servers, networks and access points.

# Question 4 – Scenario 2

A retail organization operates a cloud application using GitHub, automated CI/CD, Docker and Kubernetes. The security team discovers hardcoded credentials, outdated dependencies, vulnerable container images and Kubernetes accounts with unnecessary permissions. Security logs are not reviewed regularly.

### 4.1 CI/CD Pipeline
Explain how security checks can be integrated throughout the CI/CD pipeline to prevent insecure software from reaching production.

### 4.2 Docker / Containers
Explain major Docker/container security risks and recommend controls for secure deployment.

### 4.3 Kubernetes Access Controls
Explain how Kubernetes RBAC and least privilege reduce unauthorized actions.

### 4.4 Governance Security
Explain how security governance, policies, responsibilities and accountability improve the security posture.

### 4.5 Security Monitoring and Incident Response
Design a basic monitoring approach and explain how the organization should respond if an attacker compromises a production account.
