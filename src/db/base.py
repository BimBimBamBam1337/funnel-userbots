import uuid
from datetime import datetime
from typing import Any, ClassVar

from sqlalchemy import UUID, DateTime, MetaData, func
from sqlalchemy.orm import DeclarativeBase, mapped_column
from sqlalchemy.orm.properties import MappedColumn

POSTGRES_NAMING_CONVENTION = {
    "ix": "%(table_name)s_%(column_0_N_name)s_idx",
    "uq": "%(table_name)s_%(column_0_N_name)s_key",
    "ck": "%(table_name)s_%(constraint_name)s_check",
    "fk": "%(table_name)s_%(column_0_name)s_fkey",
    "pk": "%(table_name)s_pkey",
}


class SAModel(DeclarativeBase):
    __tablename__: str
    metadata = MetaData(naming_convention=POSTGRES_NAMING_CONVENTION)
    # No ``default=uuid.uuid4`` in the type map — it silently leaks onto FK /
    # nullable UUID columns and invents random references when callers forget
    # to pass a value. Primary keys set ``default=uuid.uuid4`` explicitly.
    type_annotation_map: ClassVar[dict[type, Any]] = {
        datetime: DateTime(timezone=True),
        uuid.UUID: UUID,
    }


def uuid_pk() -> MappedColumn[uuid.UUID]:
    """Primary-key ``uuid.UUID`` column with both ORM + DB defaults.

    * ``default=uuid.uuid4`` keeps ORM inserts working without round trips.
    * ``server_default=func.gen_random_uuid()`` lets raw SQL inserts
      (migrations, admin scripts) omit the ``id`` column.
    """
    return mapped_column(
        UUID,
        primary_key=True,
        default=uuid.uuid4,
        server_default=func.gen_random_uuid(),
    )
