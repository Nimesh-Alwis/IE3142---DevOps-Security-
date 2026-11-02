# IE3142 DevOps Security — Week 05: Containerization Orchestration and Secure CI-CD

**Language:** Sinhala + English | **Purpose:** Complete compact lecture revision notes

> **Exam tip:** English keywords and definitions මතක තියාගෙන, explanations Sinhala-English mix එකෙන් understand කරන්න. මේවා lecture concepts simplify කළ revision notes; original slides replace කරන full transcript එකක් නෙවෙයි.

## 1. Containerization
- Container = application + runtime + libraries + dependencies packaged as an isolated unit.
- Pros: **portability, environment consistency, efficiency, fast startup, isolation, scaling**.
- Container is NOT automatically secure; containers **share host OS kernel**.
| VM | Container |
|---|---|
| Hardware virtualization, own guest OS | OS-level virtualization, shared kernel |
| Heavier, slower startup | Lightweight, fast startup |
| Stronger OS boundary | Process/namespace isolation |

## 2. Docker components and flow
- **Docker Client** issues commands; **Docker Engine/daemon** builds/manages containers.
- **Dockerfile** = build instructions; **Image** = immutable-ish layered template; **Container** = runtime instance; **Registry** = image repository.
- Flow: `Dockerfile → docker build → Image → Registry → docker pull/run → Container`.
- Images made of **layers**. Added secrets may remain in image history/layers even after later delete.

## 3. Container security threats + mitigations
| Threat | Main defense |
|---|---|
| Vulnerable/base images | Trusted minimal images, image scan, patch |
| Root/privileged containers | Non-root users, no privileged flag, drop capabilities |
| Exposed Docker daemon/socket | Restrict Docker API/socket, strong host controls |
| Secrets in image/environment | Secret manager, no hard-coded secrets |
| Container escape | Patch host/kernel/runtime, confinement |
| Unrestricted inter-container traffic | Segment networks; policies |
| Malicious registry image | Trusted registry, image signing/verification |
- Container lifecycle: **Develop → Build → Test → Store → Deploy → Run → Monitor**.
- Scanners can identify known CVEs in OS packages and dependencies; signing checks provenance/integrity.

## 4. Runtime + registry protections
- Runtime: non-root, read-only filesystem when feasible, resource limits, seccomp/AppArmor/SELinux where available, monitor processes.
- Registry: authentication, RBAC, private repos, scan images, verify signatures, protect credentials.
- **Container escape:** attacker gains access beyond isolated container into host/other workloads.

## 5. Kubernetes introduction and architecture
- **Orchestration** = automated deployment, scheduling, scaling, restart, networking of containers.
- **Kubernetes (K8s)** = container orchestration platform.
- **Control plane:** API Server, etcd (cluster state), Scheduler, Controller Manager.
- **Worker node:** kubelet, kube-proxy/networking, container runtime; **Pods** host containers.
- Pod = smallest deployable K8s unit; Deployment maintains desired pod replicas; Service provides stable access.

## 6. Kubernetes security
- Risks: exposed API, permissive RBAC, secret leakage, privileged pods, weak network isolation, vulnerable images.
- **RBAC:** Role/ClusterRole contains permissions; RoleBinding/ClusterRoleBinding grants them to subjects.
- **Kubernetes Secrets:** sensitive objects; secure with etcd encryption, RBAC, external secret stores.
- **NetworkPolicy:** restrict ingress/egress between Pods/namespaces where supported by network plugin.
- **Pod security:** avoid privileged/root, minimize capabilities, limit host mounts, use non-root and read-only FS.
- Limit access to API server and audit administrative activities.

## 7. Container security integrated into DevSecOps
`Source → SAST/Secrets/SCA → Build image → Scan image → Sign → Registry → Deploy with policy → Runtime monitor`
- **CI/CD security gates** can reject high-risk findings or unauthorized artifacts.
- Lecture 05 also introduces SAST, SCA, DAST, IaC scanning, pipeline security and supply-chain security. Detailed comparison in **Week 06**.

## 8. Scenario: online shopping application
- Developer commits code → automatic scans → Docker build/scan → approval/security gate → restricted K8s deployment → logs/alerts.
- Exam line: *Protect container images, registries, orchestration, runtime, networks, and secrets throughout the entire lifecycle.*
