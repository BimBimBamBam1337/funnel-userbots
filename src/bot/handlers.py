from aiogram import F, Router, types
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext


from src.bot import text


async def start_router(message: types.Message):
    await message.answer(text.start_text)


async def add_userbot_router(message: types.Message):
    await message.answer(text.add_userbot_text)


async def func():
    pass
