# IE3142 – DevOps Security
## Revision Paper 04
[← Previous: Revision Paper 03](IE3142_Revision_Paper_03.md) | [Next: Revision Paper 05 →](IE3142_Revision_Paper_05.md)
**Duration:** 2 Hours  
**Total Marks:** 75 *(MCQ section intentionally omitted)*

# Question 2 – Structured Questions (25 Marks)

## (i) Threat Modelling – STRIDE Only (8 Marks)

A food-delivery application allows customers to register, place orders and make payments. Delivery staff update order status. Administrators manage restaurants, users and orders. The system stores personal and transaction data.

**a)** Identify four important assets. **(2 marks)**  
**b)** Identify four threats using STRIDE. **(2 marks)**  
**c)** Suggest one security control for each threat. **(2 marks)**  
**d)** Explain why threat modelling should be completed during the design stage. **(2 marks)**

## (ii) CI/CD Security (9 Marks)

A development team has automated build and deployment but does not perform security validation. A review finds hardcoded credentials, vulnerable libraries and application vulnerabilities.

**a)** Explain the purpose of CI/CD. **(2 marks)**  
**b)** Explain SAST, SCA and DAST and the type of weakness each can identify. **(3 marks)**  
**c)** Identify three security checks that should be integrated. **(2 marks)**  
**d)** Explain Security Gates and how they can prevent insecure deployment. **(2 marks)**

## (iii) Docker Architecture (8 Marks)

A company wants to run its customer-facing application in containers.

**a)** What is Docker? State two advantages. **(2 marks)**  
**b)** Draw and explain Docker Client, Docker Daemon/Engine, Docker Image, Container and Registry. **(3 marks)**  
**c)** Explain the difference between an image and a container. **(1 mark)**  
**d)** Identify two Docker security risks and suitable controls. **(2 marks)**

# Question 3 – Essay Question (25 Marks)

A telecommunications company is developing a customer self-service portal. Security testing is performed at the end of the project. The final review finds input-validation weaknesses, insecure database queries, authentication problems, authorization failures and weak logging.

**a)** Explain Shift-Left security and show how it can be applied throughout the SDLC. **(5 marks)**  
**b)** Explain five secure coding practices and give suitable examples. **(5 marks)**  
**c)** Use STRIDE to identify five possible threats and provide suitable controls. **(8 marks)**  
**d)** Explain three infrastructure-security measures. **(3 marks)**  
**e)** Explain how continuous security integration reduces development cost and improves security. **(4 marks)**

# Question 4 – Essay Question (25 Marks)

A government healthcare service uses a cloud platform, GitHub, CI/CD, Docker and Kubernetes. The security assessment identifies exposed secrets, outdated software in images, excessive Kubernetes privileges, weak security governance, insufficient monitoring and no incident-response plan.

**a)** Explain how security checks can be integrated into the CI/CD pipeline from source code to deployment. **(6 marks)**  
**b)** Identify four Docker/container risks and explain suitable controls. **(4 marks)**  
**c)** Explain Kubernetes RBAC and show how permissions can be separated between developers and administrators. **(4 marks)**  
**d)** Explain governance and compliance requirements for protecting sensitive healthcare information. Mention three controls. **(4 marks)**  
**e)** Explain the importance of continuous monitoring and mention suitable monitoring technologies. **(3 marks)**  
**f)** Explain the six phases of incident response that should be followed after a security breach. **(4 marks)**
