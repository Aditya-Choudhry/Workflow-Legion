# Workflow Legion Stack

## Priority

Band is the collaboration layer.

## Frontend

Next.js + Tailwind + shadcn/ui + React Flow + Recharts

## Backend

FastAPI + Pydantic + SQLModel/SQLAlchemy

## Agents

Python Band SDK + lightweight LangGraph per agent

## Queue

Redis + ARQ

## Database

Supabase Postgres for deployed state.
SQLite fallback for local MVP.

## LLM Providers

Primary:
- OpenAI

Fallback:
- Anthropic
- AI/ML API
- OpenRouter

## Deployment

Frontend:
- Vercel

Backend:
- Railway or Render

Database:
- Supabase Postgres

Redis:
- Upstash Redis
