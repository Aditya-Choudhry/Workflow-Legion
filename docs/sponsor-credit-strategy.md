# Sponsor Credit Strategy

## Purpose

Use available sponsor credits without making the core demo fragile.

## Core Rule

Band remains the agent collaboration layer.

Sponsor tools are used as support layers, provider integrations, or productization layers.

## Sponsor Usage

### Band

Primary runtime collaboration layer.

Required for the hackathon demo:
- Room-based agent collaboration
- Agent handoffs
- Mentions
- Shared context
- Audit trail

### NativelyAI / Native.Builder

Use as Adam's DevRel showcase layer.

Deliverables:
- Landing page or showcase page
- Builder-facing explanation of Workflow Legion
- Screenshots for Monday follow-up
- Short writeup: what Native.Builder helped accelerate

Do not use Native.Builder to replace the Band/FastAPI/agent runtime.

### Featherless

Use as an OpenAI-compatible LLM provider option.

Best demo use:
- Run one agent through Featherless, ideally Compliance or Commander
- Show provider flexibility
- Mention sponsor integration in README/demo notes

### AI/ML API

Use as an OpenAI-compatible multi-model provider option.

Best demo use:
- Add provider router support
- Use it for one comparison, fallback, or summarization agent
- Keep optional so the demo does not depend on credit availability

## Secret Handling

Never commit:
- Promo codes
- API keys
- QR redemption links
- Sponsor dashboard screenshots with secrets

Use:
- Local .env
- Password manager
- Private notes

## Bonus Prize Strategy

The project can credibly claim:
- Best use of Band: core collaboration layer
- Best use of Featherless: open-model agent/provider fallback
- Best use of AI/ML API: multi-provider model routing
- NativelyAI showcase: live DevRel artifact for Monday
