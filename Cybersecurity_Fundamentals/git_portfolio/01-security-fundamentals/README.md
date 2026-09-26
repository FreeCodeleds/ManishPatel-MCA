# Module 01: Security Fundamentals

## 🎯 Objectives
- Understand and apply the **CIA Triad** (Confidentiality, Integrity, Availability) and the **DAD Triad** (Disclosure, Alteration, Denial).
- Identify defense-in-depth principles across physical, technical, and administrative controls.
- Explore threat modeling frameworks (STRIDE, PASTA, DREAD).
- Understand security policies, standards, guidelines, and compliance frameworks.

---

## 🔑 Core Concepts Summary

### 1. The CIA Triad vs. DAD Triad
- **Confidentiality:** Preventing unauthorized disclosure of information.
  - *Controls:* Encryption, access control lists (ACLs), multi-factor authentication (MFA).
  - *Counterpart:* **Disclosure**.
- **Integrity:** Assuring data accuracy, completeness, and prevention of unauthorized alteration.
  - *Controls:* Cryptographic hashing (SHA-256), digital signatures, file integrity monitoring (FIM).
  - *Counterpart:* **Alteration**.
- **Availability:** Ensuring reliable and timely access to resources for authorized entities.
  - *Controls:* Redundancy, failover clusters, load balancing, DDoS mitigation, regular backups.
  - *Counterpart:* **Denial**.

### 2. Defense in Depth
Layered security defense ensuring no single point of security failure:
1. **Perimeter:** Firewalls, edge routers, DDoS protection.
2. **Network:** VLAN segmentation, internal firewalls, IDS/IPS.
3. **Host:** OS hardening, endpoint detection and response (EDR), patch management.
4. **Application:** Input validation, secure coding (OWASP), authentication.
5. **Data:** Encryption at rest and in transit, DLP (Data Loss Prevention), access policies.

### 3. STRIDE Threat Model
| Threat Category | Violated Property | Definition | Example Countermeasure |
| :--- | :--- | :--- | :--- |
| **S**poofing | Authenticity | Pretending to be someone or something else | Strong authentication, PKI, digital signatures |
| **T**ampering | Integrity | Modifying data or code without authorization | Cryptographic hashes, digital signatures |
| **R**epudiation | Non-repudiation | Denying having performed an action | Centralized write-once audit logging |
| **I**nformation Disclosure | Confidentiality | Exposing sensitive data to unauthorized parties | End-to-end encryption, strict authorization |
| **D**enial of Service | Availability | Disrupting legitimate access to services | Rate limiting, filtering, load balancing |
| **E**levation of Privilege | Authorization | Gaining unauthorized capabilities | Least privilege principle, RBAC |

---

## 📝 Practice Exercise & Questions
- [ ] Define the primary threat categories for a student portal using STRIDE.
- [ ] Contrast symmetric and asymmetric encryption in fulfilling confidentiality and non-repudiation.
- [ ] Write a brief risk assessment matrix for an academic database server.
