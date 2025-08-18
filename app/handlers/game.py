from aiogram import types

async def handle_start_game(callback: types.CallbackQuery):
    await callback.answer("Игра начинается!")