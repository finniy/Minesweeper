from app.bot_instance import dp, bot
from aiogram import types
from aiogram.filters import Command

@dp.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет! Добро пожаловать в бота-сапёра 🧨")

async def main():
    await dp.start_polling(bot)