# IE3142 – DevOps Security
## Revision Paper 02
[← Previous: Revision Paper 01](IE3142_Revision_Paper_01.md) | [Next: Revision Paper 03 →](IE3142_Revision_Paper_03.md)
**Duration:** 2 Hours  
**Total Marks:** 75 *(MCQ section intentionally omitted)*

# Question 2 – Structured Questions (25 Marks)

## (i) Threat Modelling – STRIDE Only (8 Marks)

An e-commerce system allows customers to register, authenticate, add products to a cart and make payments. Administrators manage products and customer accounts. The system stores customer details, orders and payment information.

**a)** Identify four important assets. **(2 marks)**  
**b)** Identify four possible threats using **STRIDE only**. **(2 marks)**  
**c)** Give one suitable security control for each threat. **(2 marks)**  
**d)** Explain why threat modelling during system design is better than discovering threats only during final testing. **(2 marks)**

## (ii) CI/CD Security (9 Marks)

A development team uses GitHub and an automated pipeline. The application has exposed API keys, outdated dependencies and code-level vulnerabilities. The team currently deploys every successful build without a security decision point.

**a)** Explain the purpose of CI/CD in software delivery. **(2 marks)**  
**b)** Explain **SAST, SCA and DAST** and state what each examines. **(3 marks)**  
**c)** Identify three security checks that should be added to the pipeline. **(2 marks)**  
**d)** Explain the role of a **Security Gate** and what should happen when a critical vulnerability is detected. **(2 marks)**

## (iii) Docker Architecture (8 Marks)

A company is migrating a web application to Docker containers.

**a)** Define Docker and state two advantages. **(2 marks)**  
**b)** Draw and explain Docker Client, Docker Daemon/Engine, Image, Container and Registry. **(3 marks)**  
**c)** Compare a Docker image with a running Docker container. **(1 mark)**  
**d)** Identify two container-security risks and recommend controls. **(2 marks)**

# Question 3 – Essay Question (25 Marks)

A software company is developing a payroll management system. Security reviews are performed only after most development is complete. The final review finds insecure database queries, weak authentication, authorization failures, exposed sensitive data and insufficient logging.

**a)** Explain Shift-Left security and how it can be introduced throughout the SDLC. **(5 marks)**  
**b)** Explain five secure coding practices relevant to the payroll application, with examples. **(5 marks)**  
**c)** Using **STRIDE**, identify five threats and map each threat to a suitable control. **(8 marks)**  
**d)** Explain three infrastructure-security measures. **(3 marks)**  
**e)** Explain how early security integration can reduce remediation cost and improve security quality. **(4 marks)**

# Question 4 – Essay Question (25 Marks)

A hospital uses a cloud-based application for patient records. The environment includes GitHub, CI/CD, Docker, Kubernetes and cloud services. Security assessment finds hardcoded secrets, vulnerable dependencies, insecure container configurations, excessive Kubernetes permissions, weak governance and limited monitoring.

**a)** Explain how security checks can be integrated into the CI/CD pipeline from code through deployment. **(6 marks)**  
**b)** Identify four Docker/container risks and suitable security controls. **(4 marks)**  
**c)** Explain Kubernetes RBAC and least privilege. Give suitable developer and administrator examples. **(4 marks)**  
**d)** Explain healthcare security governance and compliance. Mention three controls that help protect patient data. **(4 marks)**  
**e)** Explain continuous security monitoring and mention suitable technologies. **(3 marks)**  
**f)** Explain the six phases of incident response for a confirmed patient-data compromise. **(4 marks)**
