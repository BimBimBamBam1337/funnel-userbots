from aiogram import F, Router, types
from aiogram.filters import Command, CommandStart
from aiogram.fsm.context import FSMContext


from src.bot import text


async def start_router(message: types.Message):
    await message.answer(text.start_text)


async def add_userbot_router(message: types.Message):
    await message.answer(text.add_userbot_text)


async def func():
    pass


async def build_handler() -> Router:
    router = Router()
    router.message.register(start_router, CommandStart)
    router.message.register(add_userbot_router, Command("add_userbot"))
    return router
