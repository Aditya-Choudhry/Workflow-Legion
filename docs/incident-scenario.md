# Incident Scenario: WL-INC-001

## Title

Suspicious PowerShell Activity and Possible Data Exfiltration

## Summary

A suspicious PowerShell process was detected on workstation FIN-042, followed by failed login attempts, outbound traffic to an unknown IP, and access to sensitive finance files.

## Affected Asset

- Host: FIN-042
- User: j.morgan
- Department: Finance
- Severity: Pending agent review

## Synthetic Indicators

- Suspicious process: powershell.exe
- Suspicious file: invoice_update.exe
- Destination IP: 185.199.108.153
- Possible target file: finance_q4_forecast.xlsx

## Demo Goal

Show the Triage Agent using Band to coordinate Threat Intel, Forensics, Compliance, and Incident Commander agents.
