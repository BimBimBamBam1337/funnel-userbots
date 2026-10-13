from aiogram import Dispatcher
from aiogram.fsm.storage.base import BaseStorage


def build_dispatcher(*, storage: BaseStorage) -> Dispatcher:
    dp = Dispatcher(storage=storage)
    return dp
