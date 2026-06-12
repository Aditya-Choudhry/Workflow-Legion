# AGENTS.md - Workflow Legion Codex Instructions

## Mission

Build Workflow Legion: Cyber Incident Command Room.

This is a Band-native multi-agent incident response system for the Band of Agents Hackathon.

## Non-Negotiable Architecture Rule

Band is the inter-agent collaboration layer.

Do not build a hidden backend-only orchestrator where agents merely send final updates to Band. Agents must visibly coordinate through Band rooms, messages, mentions, handoffs, shared context, and task state.

## MVP First

Build in this order:

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

## Stack

Frontend:
- Next.js
- Tailwind
- shadcn/ui
- React Flow
- Recharts

Backend:
- FastAPI
- Pydantic
- SQLModel or SQLAlchemy

Agents:
- Python Band SDK
- Lightweight LangGraph inside each agent only

Queue:
- Redis
- ARQ

Database:
- Supabase Postgres for deployed state
- SQLite fallback for local MVP

LLM:
- OpenAI primary if available
- Anthropic, AI/ML API, or OpenRouter fallback

Deployment:
- Vercel frontend
- Railway or Render backend
- Supabase Postgres
- Upstash Redis

## Development Rules

- Never commit secrets.
- Use .env locally and .env.example for documentation.
- Keep PRs small.
- Do not push directly to main once teammates are active.
- Prioritize working Band collaboration over UI polish.
- Prefer boring reliable code over impressive unstable architecture.
- If a feature does not help the demo, cut it.

## Main Demo

Incident WL-INC-001:
Suspicious PowerShell activity and possible data exfiltration on FIN-042.

Required visible flow:
Triage Agent -> Band room -> mentions Threat Intel and Forensics -> Compliance review -> Commander final decision.

## Validation

Before calling the MVP done:

- Backend starts.
- Frontend starts.
- Band credentials load safely.
- Triage Agent posts to Band.
- At least three agents visibly collaborate through Band.
- Final report is generated.
- Demo works three times in a row.
