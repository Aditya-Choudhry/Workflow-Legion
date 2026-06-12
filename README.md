# Workflow Legion: Cyber Incident Command Room

Workflow Legion is a Band-native multi-agent incident response system for the Band of Agents Hackathon.

## Mission

Build a SOC-style cyber incident command room where specialized AI agents collaborate through Band to triage alerts, enrich threat intelligence, review forensic evidence, assess compliance risk, and produce an auditable incident commander decision.

## Core Principle

Band is the collaboration layer. Agents must communicate, share context, delegate, and hand off work through Band rooms and messages. Band is not a final notification channel.

## Agent Team

- Alert Triage Agent
- Threat Intel Agent
- Forensics Agent
- Compliance Agent
- Incident Commander Agent

## MVP Demo Flow

1. Start incident simulation.
2. Triage Agent posts the alert in Band.
3. Triage Agent mentions Threat Intel and Forensics.
4. Threat Intel enriches indicators.
5. Forensics reviews logs and builds a timeline.
6. Compliance checks audit and escalation risk.
7. Commander produces the final incident decision report.

## Proposed Stack

- Band SDK as the collaboration layer
- FastAPI backend
- Python agent workers
- Redis + ARQ for optional async jobs
- LangGraph only inside individual agents
- React / Next.js dashboard
- Supabase Postgres or SQLite fallback
