from aiogram import BaseMiddleware
from aiogram.types import TelegramObject
from typing import Any, Awaitable, Callable
from loguru import logger

from src.core.types.repository import BaseRepository


class DependencieMiddleware(BaseMiddleware):
    async def __call__(
        self,
        handler: Callable[[TelegramObject, dict[str, Any]], Awaitable[Any]],
        event: TelegramObject,
        data: dict[str, Any],
    ) -> Any:
        data["repo"] = BaseRepository()
        try:
            return await handler(event, data)
        except Exception as e:
            logger.error("Error: {}", e)
