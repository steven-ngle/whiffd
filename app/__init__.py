from contextlib import asynccontextmanager
from fastapi import FastAPI, Depends

from app.core.config import settings
from app.services.ballchasing import BallchasingClient
from app.api.deps import get_ballchasing

@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.ballchasing = BallchasingClient()
    try:
        yield
    finally:
        await app.state.ballchasing.close()

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

    return app
