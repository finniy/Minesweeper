from aiogram import types
from app.keyboards import START_KEYBOARD

async def start_command(message: types.Message):
    await message.answer(
        "<Команда /start>",
        reply_markup=START_KEYBOARD
    )