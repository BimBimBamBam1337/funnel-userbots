from sqlalchemy.ext.asyncio import AsyncSession

from src.core.types.dto import BaseDTO
from src.db.base import SAModel


class BaseRepository[MT: SAModel, CDT: BaseDTO, RDT: BaseDTO]:
    _model: type[MT]
    _create_dto: type[CDT]
    _read_dto: type[RDT]
    _session: AsyncSession

    def __init__(self, session: AsyncSession) -> None:
        self._session = session
