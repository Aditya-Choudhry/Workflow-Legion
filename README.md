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

## Current Backend Progress

This branch adds a deterministic backend demo path that can run safely before live Band credentials are available.

Implemented:

- Typed incident, finding, evidence, timeline, and final report models.
- Deterministic outputs for Triage, Threat Intel, Forensics, Compliance, and Commander agents.
- In-memory incident state for the WL-INC-001 demo.
- Final incident report generation.
- Band.ai-safe client wrapper that only sends messages when credentials are configured.
- FastAPI endpoints for starting/resetting the demo, reading incident state, reading the final report, and testing Band delivery.

Useful endpoints:

- `GET /health`
- `GET /api/incidents/wl-inc-001`
- `POST /api/incidents/wl-inc-001/reset`
- `POST /api/incidents/wl-inc-001/start`
- `GET /api/incidents/wl-inc-001/report`
- `POST /api/band/test-message`

Issue coverage:

- Solves #28: deterministic mock outputs for all five agents.
- Solves most of #12: incident state and agent findings are stored in memory for the MVP demo.
- Solves #13: final incident report output is generated from agent findings.
- Supports #29: backend health, settings, provider router imports, and demo endpoints were verified locally.
- Prepares #3, #6, and #11: Band.ai configuration and a guarded Band message client are in place, but live completion still requires Band chat ID, agent API key, and exact mention handles.

Safety notes:

- Do not commit real Band, OpenAI, Anthropic, Featherless, or AI/ML API keys.
- Use `.env` locally and keep `.env.example` as placeholders only.
- `POST /api/band/test-message` returns a configuration error instead of attempting a live post when Band credentials are missing.
