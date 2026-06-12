from dataclasses import dataclass
from typing import Any

import httpx


class BandConfigurationError(RuntimeError):
    pass


@dataclass(frozen=True)
class BandDeliveryResult:
    delivered: bool
    detail: str
    status_code: int | None = None


class BandClient:
    def __init__(self, base_url: str, agent_api_key: str | None) -> None:
        self._base_url = base_url.rstrip("/")
        self._agent_api_key = agent_api_key

    @property
    def configured(self) -> bool:
        return bool(self._base_url and self._agent_api_key)

    def _headers(self) -> dict[str, str]:
        if not self._agent_api_key:
            raise BandConfigurationError("Band agent API key is not configured.")

        return {
            "X-API-Key": self._agent_api_key,
            "Content-Type": "application/json",
        }

    async def get_current_agent_profile(self) -> dict[str, Any]:
        async with httpx.AsyncClient(timeout=10) as client:
            response = await client.get(f"{self._base_url}/agent/me", headers=self._headers())
            response.raise_for_status()
            return response.json()

    async def send_text_message(self, chat_id: str, content: str) -> BandDeliveryResult:
        if not chat_id:
            raise BandConfigurationError("Band chat ID is not configured.")
        if not content.strip():
            raise ValueError("Band message content cannot be empty.")

        payload = {"content": content}
        async with httpx.AsyncClient(timeout=15) as client:
            response = await client.post(
                f"{self._base_url}/agent/chats/{chat_id}/messages",
                headers=self._headers(),
                json=payload,
            )

        if response.is_success:
            return BandDeliveryResult(
                delivered=True,
                detail="Message delivered to Band.",
                status_code=response.status_code,
            )

        return BandDeliveryResult(
            delivered=False,
            detail="Band rejected the message. Check chat ID, agent key, and mention format.",
            status_code=response.status_code,
        )

