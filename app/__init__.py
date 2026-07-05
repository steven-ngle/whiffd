from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends
from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from app.core.config import settings
from app.core.db import engine
from app.services.ballchasing import BallchasingClient
from app.api.deps import get_ballchasing, get_db

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.ballchasing = BallchasingClient()
    try:
        yield
    finally:
        await app.state.ballchasing.close()
        await engine.dispose()

def create_app() -> FastAPI:
    app = FastAPI(
        title=settings.app_name,
        debug=settings.debug,
        lifespan=lifespan
    )

    @app.get("/health")
    async def health() -> dict[str, str]:
        return {"status": "ok"}
    
    @app.get("/ping-ballchasing")
    async def ping_ballchasing(client: BallchasingClient = Depends(get_ballchasing)) -> dict:
        return await client.ping()

    @app.get("/db-check")
    async def db_check(session: AsyncSession = Depends(get_db)) -> dict:
        result = await session.execute(text("SELECT version()"))
        return {"postgres": result.scalar_one()}
    
    return app
