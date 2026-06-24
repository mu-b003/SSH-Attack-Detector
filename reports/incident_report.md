# Incident Response Report

## Incident Information

* Incident Type: SSH Brute Force Attack
* Status: Closed
* Severity: Medium
* Analyst: Mubarak Bashr
* Date: 06/25/2026

---

## Executive Summary

An SSH brute-force attack was detected against the Ubuntu server.

The attacker repeatedly attempted authentication using multiple passwords before successfully gaining access to the target account.

Log analysis confirmed the attack source and timeline of events.

---

## Timeline

### Initial Activity

Multiple failed SSH login attempts detected.

### Attack Escalation

Authentication failures increased over a short period.

### Successful Authentication

The attacker successfully authenticated using valid credentials.

### Detection

Authentication logs reviewed and analyzed.

### Containment

Password changed and monitoring increased.

---

## Indicators of Compromise

### Source IP Address

192.168.150.129

### Target User

soc-analyst

### Target Service

SSH (Port 22)

---

## Attack Analysis

The attacker used an automated password-guessing technique against the SSH service.

Evidence suggests a brute-force attack due to repeated login failures followed by a successful authentication event.

---

## Containment Actions

* Investigated authentication logs.
* Identified attack source.
* Reset compromised credentials.
* Recommended stronger authentication controls.

---

## Recommendations

1. Enforce strong passwords.
2. Enable multi-factor authentication where possible.
3. Use SSH key-based authentication.
4. Install Fail2Ban.
5. Limit SSH access to trusted IP addresses.
6. Continuously monitor authentication logs.

---

## Lessons Learned

Continuous monitoring of authentication logs is essential for detecting brute-force attacks at an early stage.

Automated detection scripts can significantly reduce investigation time and improve incident response efficiency.
