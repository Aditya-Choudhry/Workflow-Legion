# Agent Roles

## Alert Triage Agent

Receives the alert, classifies initial severity, summarizes the incident, and mentions Threat Intel and Forensics through Band.

## Threat Intel Agent

Enriches indicators, checks mock IOC records, identifies possible threat patterns, and posts findings to Band.

## Forensics Agent

Reviews synthetic endpoint and network logs, builds the event timeline, and posts evidence to Band.

## Compliance Agent

Reviews facts for audit, reporting, escalation, and evidence retention considerations.

## Incident Commander Agent

Reads all findings, resolves conflicts, and produces the final incident decision report.
