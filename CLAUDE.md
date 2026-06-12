# CLAUDE.md - Workflow Legion Build Instructions

## Non-Negotiable Rule

Band is the inter-agent collaboration layer.

Do not build a hidden backend-only orchestrator where agents merely send final updates to Band. Agents must visibly coordinate through Band rooms, messages, mentions, handoffs, shared context, and task state.

## MVP Order

1. Confirm repo health.
2. Confirm Band SDK/API setup.
3. Create minimal FastAPI backend.
4. Create minimal dashboard.
5. Create Alert Triage Agent.
6. Prove one Band room message.
7. Prove Triage Agent can mention Threat Intel and Forensics.
8. Add Threat Intel, Forensics, Compliance, and Commander agents.
9. Generate final incident report.
10. Polish dashboard and README.

## Safety

Never commit secrets. Use .env locally and .env.example for documentation.

## Main Demo

Incident WL-INC-001: suspicious PowerShell activity and possible data exfiltration on FIN-042.
