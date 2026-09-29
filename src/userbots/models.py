import uuid

from datetime import datetime
from sqlalchemy import BigInteger, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base import SAModel, uuid_pk


class UserBot(SAModel):
    __tablename__ = "userbots"
    id: Mapped[uuid.UUID] = uuid_pk()
    public_id: Mapped[int] = mapped_column(BigInteger)
    api_id: Mapped[int] = mapped_column(Integer)
    api_hash: Mapped[str] = mapped_column(String(32))
    username: Mapped[str] = mapped_column(String(60))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now())
