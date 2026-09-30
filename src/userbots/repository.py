import uuid
from collections.abc import Sequence
from datetime import datetime

from sqlalchemy import func, select, update

from src.core.types.repository import BaseRepository
from src.userbots.models import UserBot
from src.userbots.dto import UserBotCreateDTO, UserBotReadDTO


class UserBotRepository(BaseRepository[UserBot, UserBotCreateDTO, UserBotReadDTO]):
    _model = UserBot
    _create_dto = UserBotCreateDTO
    _read_dto = UserBotReadDTO

    async def list_all(self) -> Sequence[UserBotReadDTO]:
        result = await self._session.execute(
            select(UserBot).order_by(UserBot.created_at)
        )
        return [UserBotReadDTO.model_validate(row) for row in result.scalars().all()]

    async def get_by_id(self, bot_id: int) -> UserBotReadDTO | None:
        result = await self._session.execute(
            select(UserBot).where(UserBot.bot_id == bot_id)
        )
        row = result.scalar_one_or_none()
        return UserBotReadDTO.model_validate(row) if row else None

    async def get_by_public_id(self, public_id: str) -> UserBotReadDTO | None:
        result = await self._session.execute(
            select(UserBot).where(UserBot.public_id == public_id)
        )
        row = result.scalar_one_or_none()
        return UserBotReadDTO.model_validate(row) if row else None

    async def get_by_username(self, username: str) -> UserBotReadDTO | None:
        result = await self._session.execute(
            select(UserBot).where(UserBot.username == username)
        )
        row = result.scalar_one_or_none()
        return UserBotReadDTO.model_validate(row) if row else None

    async def set_enable(self, bot_id: int, enabled: bool) -> None:
        await self._session.execute(
            update(UserBot)
            .where(UserBot.bot_id == bot_id)
            .values(enabled=enabled, update=func.now())
        )

    async def update_values(self, bot_id: int, values: dict[str, object]):
        await self._session.execute(
            update(UserBot)
            .where(UserBot.id == bot_id)
            .values(updated_at=func.now(), **values),
        )

    async def mark_status(
        self,
        bot_id: int,
        status: str,
        *,
        detail: str | None = None,
    ) -> None:
        values: dict[str, object] = {"status": status, "status_detail": detail}
        await self._session.execute(
            update(UserBot).where(UserBot.id == bot_id).values(**values)
        )
