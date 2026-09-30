import uuid
from datetime import datetime
from src.core.types.dto import BaseDTO


class UserBotCreateDTO(BaseDTO):
    public_id: str
    bot_id: int
    status: str
    api_id: int
    api_hash: str
    enabled: bool
    username: str
    created_at: datetime
    updated_at: datetime


class UserBotReadDTO(BaseDTO):
    id: uuid.UUID
    public_id: str
    bot_id: int
    status: str
    api_id: int
    api_hash: str
    enabled: bool
    username: str
    created_at: datetime
    updated_at: datetime
