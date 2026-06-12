# Tool Usage Doctrine

## Core Principle

Band is the agent collaboration layer.

Every important agent-to-agent handoff must be visible through Band rooms, messages, mentions, shared context, or audit trail.

## Tool Roles

### Band

Use for:
- Agent rooms
- Agent messages
- @mentions
- Handoffs
- Shared context
- Audit trail
- Demo proof

Do not replace Band with a hidden backend orchestrator.

### FastAPI

Use for:
- Backend API
- Incident state
- Health checks
- Agent trigger endpoints
- Final report delivery

FastAPI supports the demo. It does not replace Band coordination.

### NativelyAI / Native.Builder

Use for:
- Adam's DevRel showcase layer
- Landing page
- Product explainer
- Monday interview artifact
- Builder-facing screenshots

Do not use Native.Builder as the core runtime for Band agents.

### Featherless

Use for:
- Optional OpenAI-compatible provider support
- One text-heavy agent, preferably Compliance or Commander
- Bonus sponsor integration

Do not make the core demo depend on Featherless.

### AI/ML API

Use for:
- Optional multi-model provider support
- Provider-router validation
- Fallback or comparison output

Do not make the core demo depend on AI/ML API.

### Redis / ARQ

Use only after the basic Band flow works.

Use for:
- Async jobs
- Retry handling
- Agent status queues

Do not build this before the Band test message.

### Supabase

Use for deployed state if time allows.

SQLite or in-memory state is acceptable for MVP.

## Secret Handling

Never commit:
- API keys
- Promo codes
- QR redemption links
- Sponsor credit links
- Private credentials

Use local .env only.

## Build Priority

1. Band room test message
2. Triage Agent posts alert
3. Triage Agent mentions Threat Intel and Forensics
4. At least three agents respond visibly through Band
5. Commander final report
6. Dashboard display
7. Sponsor integrations
8. NativelyAI showcase
