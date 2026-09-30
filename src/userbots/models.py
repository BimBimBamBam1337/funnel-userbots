import uuid

from datetime import datetime
from sqlalchemy import BigInteger, Boolean, Integer, String, func
from sqlalchemy.orm import Mapped, mapped_column
from src.db.base import SAModel, uuid_pk

USER_BOT_STATUS_DISABLED = "disabled"
USER_BOT_STATUS_ACTIVE = "active"
USER_BOT_STATUS_ERROR = "error"


class UserBot(SAModel):
    __tablename__ = "userbots"
    id: Mapped[uuid.UUID] = uuid_pk()
    public_id: Mapped[str] = mapped_column(String(32), unique=True)
    bot_id: Mapped[int] = mapped_column(BigInteger)
    api_id: Mapped[int] = mapped_column(Integer)
    status: Mapped[str] = mapped_column(String(16), default=USER_BOT_STATUS_DISABLED)
    status_detail: Mapped[str] = mapped_column(String(255), nullable=True)
    enabled: Mapped[bool] = mapped_column(Boolean, default=False)
    api_hash: Mapped[str] = mapped_column(String(32))
    username: Mapped[str] = mapped_column(String(60))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(server_default=func.now())
