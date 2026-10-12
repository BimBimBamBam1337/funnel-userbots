from collections.abc import AsyncIterator
from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseStorage
from dishka import Provider, Scope, provide
from pydantic_settings.sources import ConfigFileSourceType
from sqlalchemy.ext.asyncio import AsyncSession

from src.bot.dispatcher import build_dispatcher
from src.bot.storage import build_redis, build_storage
from src.config import Config, settings
from src.db.session import AsyncSessionMaker


class AppProvider(Provider):
    scope = Scope.APP

    @provide
    def config(self, config: Config) -> Config:
        return settings


class BotProvider(Provider):
    scope = Scope.APP

    @provide
    async def storage(self, config: Config) -> AsyncIterator[BaseStorage]:
        redis = build_redis(config)
        try:
            yield build_storage(redis)
        finally:
            await redis.aclose()

    @provide
    async def dispatcher(self, storage: BaseStorage) -> Dispatcher:
        return build_dispatcher(storage=storage)


class RequestProvider(Provider):
    scope = Scope.REQUEST

    @provide
    async def session(seld) -> AsyncIterator[AsyncSession]:
        async with AsyncSessionMaker() as session:
            yield session
