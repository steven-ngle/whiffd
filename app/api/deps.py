from fastapi import Request
from collections.abc import AsyncIterator
from sqlalchemy.ext.asyncio import AsyncSession
from app.core.db import SessionFactory
from app.services.ballchasing import BallchasingClient

def get_ballchasing(request: Request) -> BallchasingClient:
    return request.app.state.ballchasing

async def get_db() -> AsyncIterator[AsyncSession]:
    async with SessionFactory() as session:
        yield session
        