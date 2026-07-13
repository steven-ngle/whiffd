import asyncio

from app.core.db import engine
from app.db import models  # noqa: F401
from app.db.base import Base


async def main() -> None:
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


asyncio.run(main())