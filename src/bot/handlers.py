from aiogram import F, Router
from aiogram.filters import Command
from aiogram import types

from src.bot import text

router = Router()


@router.message(Command("start"))
async def start_router(message: types.Message):
    await message.answer(text.start_text)


@router.message(Command("add_userbot"))
async def add_userbot_router(message: types.Message):
    await message.answer(text.add_userbot_text)
