# IE3142 – DevOps Security
## Revision Paper 01
**Duration:** 2 Hours  
**Total Marks:** 75 *(MCQ section intentionally omitted)*

# Question 2 – Structured Questions (25 Marks)

## (i) Threat Modelling – STRIDE Only (8 Marks)

A university is developing a student examination portal. Students can log in, download examination papers, submit answers and view results. Lecturers can create examinations and update marks. The system stores student identities, examination papers, submitted answers and results.

**a)** Identify four important assets. **(2 marks)**  
**b)** Identify four possible security threats using the **STRIDE threat modelling approach**. **(2 marks)**  
**c)** Suggest one suitable security control for each threat identified. **(2 marks)**  
**d)** Explain why threat modelling should be performed during the design phase of the SDLC. **(2 marks)**

## (ii) CI/CD Security (9 Marks)

An online banking company uses an automated CI/CD pipeline. A review identifies hardcoded database credentials, vulnerable third-party libraries, SQL injection vulnerabilities and developers deploying code without security validation.

**a)** Explain the purpose of a CI/CD pipeline. **(2 marks)**  
**b)** Explain the purpose of **SAST, SCA and DAST**. **(3 marks)**  
**c)** Identify three security checks that should be included in the pipeline. **(2 marks)**  
**d)** Explain what a **Security Gate** is and how it prevents insecure code from being deployed. **(2 marks)**

## (iii) Docker Architecture (8 Marks)

A software company wants to deploy a web application using Docker.

**a)** What is Docker? Mention two advantages. **(2 marks)**  
**b)** Draw and explain Docker Client, Docker Daemon/Engine, Docker Images, Containers and Docker Registry. **(3 marks)**  
**c)** Explain the difference between a Docker image and a Docker container. **(1 mark)**  
**d)** Identify two Docker/container security risks and suggest suitable controls. **(2 marks)**

# Question 3 – Essay Question (25 Marks)

A financial institution is developing an online payment application. Security testing is performed only near the end of development. Testing discovers SQL injection, weak password handling, unauthorized account access, unencrypted sensitive information and poor security logging.

**a)** Explain the **Shift-Left approach** in DevSecOps and how it helps identify vulnerabilities earlier. **(5 marks)**  
**b)** Explain five secure coding practices with suitable examples. **(5 marks)**  
**c)** Using **STRIDE**, identify five possible threats and suggest a suitable control for each. **(8 marks)**  
**d)** Explain three infrastructure-security measures. **(3 marks)**  
**e)** Explain how integrating security throughout the SDLC can reduce development costs and improve security. **(4 marks)**

# Question 4 – Essay Question (25 Marks)

A healthcare organization is developing a cloud-based patient-management system using GitHub, CI/CD, Docker, Kubernetes and cloud infrastructure. A review identifies exposed credentials, vulnerable Docker images, excessive Kubernetes permissions, weak monitoring, no incident-response plan and possible patient-data exposure.

**a)** Explain how security can be integrated into each stage of a CI/CD pipeline. Mention suitable security checks/tools. **(6 marks)**  
**b)** Identify four Docker container-security risks and explain suitable preventive measures. **(4 marks)**  
**c)** Explain how Kubernetes **RBAC** can control access. Give suitable developer and administrator examples. **(4 marks)**  
**d)** Explain the importance of security governance and compliance in healthcare. Mention three controls that protect patient information. **(4 marks)**  
**e)** Explain continuous security monitoring and mention suitable monitoring technologies. **(3 marks)**  
**f)** An attacker steals patient information. Explain the **six phases of incident response**. **(4 marks)**
