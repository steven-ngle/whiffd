import httpx

from app.core.config import settings


class BallchasingClient:
    def __init__(self) -> None:
        self._client = httpx.AsyncClient(
            base_url=settings.ballchasing_base_url,
            headers={"Authorization": settings.ballchasing_api_key},
            timeout=10.0,
        )

    async def close(self) -> None:
        await self._client.aclose()

    async def ping(self) -> dict:
        response = await self._client.get("/")
        response.raise_for_status()
        return response.json()