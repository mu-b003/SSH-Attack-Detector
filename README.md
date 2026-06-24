# SSH Attack Detector

## Project Overview

This project simulates and analyzes an SSH brute-force attack against an Ubuntu server in a controlled lab environment.

The objective is to demonstrate how a SOC Analyst can detect malicious SSH login attempts, identify the attacking source, analyze authentication logs, and document findings through an incident response process.

---

## Objectives

* Simulate an SSH brute-force attack.
* Collect authentication logs from Ubuntu.
* Detect failed and successful login attempts.
* Identify source IP addresses involved in the attack.
* Generate a simple detection report using Python.
* Produce an incident response report.

---

## Lab Environment

### Attacker Machine

* Kali Linux

### Victim Machine

* Ubuntu Server
* OpenSSH Server Enabled

---

## Attack Simulation

Hydra was used to perform a password guessing attack against the SSH service.

Example:

hydra -l testuser -P passwords.txt ssh://TARGET_IP

---

## Detection Method

Authentication logs were collected from:

/var/log/auth.log

A Python script was developed to:

* Count failed login attempts.
* Count successful logins.
* Identify source IP addresses.
* Generate a basic SSH attack report.

---

## Project Structure

SSH-Attack-Detector/
├── logs/
├── scripts/
├── reports/
├── screenshots/
└── README.md

---

## Key Findings

* Multiple failed SSH login attempts detected.
* Brute-force behavior observed.
* Source IP identified.
* Successful login recorded after repeated failures.

---

## Skills Demonstrated

* Linux Log Analysis
* SSH Security Monitoring
* Brute Force Detection
* Python Log Parsing
* Incident Response Documentation
* SOC Analyst Workflow

---

## Author

Cybersecurity Student – SOC Analyst Path
