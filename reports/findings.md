# Findings Report

## Summary

Analysis of the authentication logs revealed multiple failed SSH login attempts originating from a single source IP address.

The activity was consistent with a brute-force password attack targeting the SSH service.

---

## Observations

* High volume of failed login attempts.
* Repeated authentication failures against the same user account.
* Successful login observed after multiple failed attempts.
* Source IP remained consistent throughout the attack.

---

## Indicators of Compromise (IOCs)

### Source IP

192.168.150.129

### Target Service

SSH (Port 22)

### Log Evidence

Failed password for soc-analyst from 192.168.150.129

Accepted password for soc-analyst from 192.168.150.129

---

## Risk Assessment

Risk Level: Medium

The attacker successfully authenticated after multiple failed attempts, indicating weak password security and exposure to brute-force attacks.

---

## Recommendations

* Implement strong password policies.
* Enable SSH key authentication.
* Disable password authentication when possible.
* Deploy Fail2Ban.
* Restrict SSH access through firewall rules.
* Monitor authentication logs continuously.
