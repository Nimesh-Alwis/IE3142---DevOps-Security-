# IE3142 – DevOps Security
## Revision Paper 05
[← Previous: Revision Paper 04](IE3142_Revision_Paper_04.md) | [All Revision Papers →](../README.md#revision-papers-5)
**Duration:** 2 Hours  
**Total Marks:** 75 *(MCQ section intentionally omitted)*

# Question 2 – Structured Questions (25 Marks)

## (i) Threat Modelling – STRIDE Only (8 Marks)

An online healthcare booking system allows patients to register, authenticate, book appointments and view appointment information. Doctors update appointment information, while administrators manage users and system settings.

**a)** Identify four important assets. **(2 marks)**  
**b)** Identify four possible threats using the STRIDE model. **(2 marks)**  
**c)** Suggest one suitable security control for each threat. **(2 marks)**  
**d)** Explain why identifying threats during design can reduce security problems later in development. **(2 marks)**

## (ii) CI/CD Security (9 Marks)

A software organization uses GitHub and an automated CI/CD pipeline for a cloud application. The organization is concerned about exposed secrets, vulnerable dependencies, insecure source code, vulnerable containers and infrastructure misconfiguration.

**a)** Explain the purpose of a CI/CD pipeline. **(2 marks)**  
**b)** Explain SAST, SCA and DAST and what each checks. **(3 marks)**  
**c)** Identify three security checks that should be integrated. **(2 marks)**  
**d)** Explain the purpose of a Security Gate and how it should handle a critical security finding. **(2 marks)**

## (iii) Docker Architecture (8 Marks)

A company wants to deploy a web application as a Dockerized service.

**a)** Define Docker and mention two advantages. **(2 marks)**  
**b)** Draw and explain Docker Client, Docker Daemon/Engine, Images, Containers and Registry. **(3 marks)**  
**c)** Explain the difference between a Docker image and a container. **(1 mark)**  
**d)** Identify two Docker/container security risks and recommend controls. **(2 marks)**

# Question 3 – Essay Question (25 Marks)

A financial services company is developing an online loan-management system. Security testing is performed late in development. The final review identifies SQL injection, weak authentication, unauthorized access, unprotected sensitive data and poor security monitoring.

**a)** Explain Shift-Left security and how it can help identify vulnerabilities earlier. **(5 marks)**  
**b)** Explain five secure coding practices with suitable examples. **(5 marks)**  
**c)** Using STRIDE, identify five possible threats and suggest a suitable control for each. **(8 marks)**  
**d)** Explain three infrastructure-security measures. **(3 marks)**  
**e)** Explain how integrating security throughout the SDLC can reduce development costs and improve security. **(4 marks)**

# Question 4 – Essay Question (25 Marks)

A hospital is developing a cloud-based patient-management platform using GitHub, CI/CD, Docker and Kubernetes. The system handles sensitive patient information. A security assessment identifies exposed API keys, vulnerable packages in Docker images, excessive Kubernetes permissions, insufficient monitoring, weak governance and no incident-response plan.

**a)** Explain how security can be integrated into each stage of the CI/CD pipeline. Mention suitable security checks and tools. **(6 marks)**  
**b)** Identify four Docker container-security risks and explain suitable measures to prevent them. **(4 marks)**  
**c)** Explain how Kubernetes RBAC can be used to control access. Give suitable examples for developers and administrators. **(4 marks)**  
**d)** Explain the importance of security governance and compliance in healthcare. Mention three controls that can protect patient information. **(4 marks)**  
**e)** Explain the importance of continuous security monitoring and mention suitable tools or technologies. **(3 marks)**  
**f)** A patient-information breach occurs. Explain the six phases of the incident-response process. **(4 marks)**
