from types import TracebackType

from loguru import logger
from sqlalchemy.ext.asyncio import (
    AsyncEngine,
    AsyncSession,
    async_sessionmaker,
    create_async_engine,
)

from src.config import settings


class AsyncSessionMaker:
    _engine: AsyncEngine | None = None
    _sessionmaker: async_sessionmaker[AsyncSession] | None = None

    @classmethod
    async def _get_sessionmaker(cls) -> async_sessionmaker[AsyncSession]:
        if cls._sessionmaker is None:
            cls._engine = create_async_engine(
                url=settings.db.get_url().get_secret_value(),
                future=True,
                pool_pre_ping=True,
                pool_size=8,
                max_overflow=4,
                pool_timeout=10,
                pool_recycle=300,
            )
            cls._sessionmaker = async_sessionmaker(
                bind=cls._engine,
                autoflush=True,
                autocommit=False,
                expire_on_commit=False,
            )
        return cls._sessionmaker

    def __init__(self) -> None:
        self._session = self._get_sessionmaker()()

    async def __aenter__(self) -> AsyncSession:
        logger.debug("open db session")
        return await self._session.__aenter__()

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc_value: BaseException | None,
        traceback: TracebackType | None,
    ) -> None:
        logger.debug("close db session")
        return await self._session.__aexit__(exc_type, exc_value, traceback)
