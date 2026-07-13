from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, String, UniqueConstraint
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

class Replay(Base):
    __tablename__ = "replays"

    id: Mapped[str] = mapped_column(String(40), primary_key=True)
    title: Mapped[str | None]
    map_name: Mapped[str | None]
    playlist: Mapped[str | None]
    duration: Mapped[int]
    played_at: Mapped[datetime] = mapped_column(DateTime(timezone=True))
    blue_goals: Mapped[int]
    orange_goals: Mapped[int]
    players: Mapped[list["PlayerStats"]] = relationship(back_populates="replay", cascade="all, delete-orphan")

class PlayerStats(Base):
    __tablename__ = "player_stats"
    __table_args__ = (UniqueConstraint("replay_id", "platform", "platform_id"),)

    id: Mapped[int] = mapped_column(primary_key=True)
    replay_id: Mapped[str] = mapped_column(ForeignKey("replays.id", ondelete="CASCADE"))
    name: Mapped[str]
    platform: Mapped[str | None]
    platform_id: Mapped[str | None]
    team: Mapped[str]
    score: Mapped[int]
    goals: Mapped[int]
    assists: Mapped[int]
    saves: Mapped[int]
    shots: Mapped[int]
    shooting_percentage: Mapped[float]

    replay: Mapped[Replay] = relationship(back_populates="players")