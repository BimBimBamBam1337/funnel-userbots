from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseStorage

from src.config import settings


def build_dispatcher(*, storage: BaseStorage) -> Dispatcher:
    dp = Dispatcher(storage=storage)
    return dp
