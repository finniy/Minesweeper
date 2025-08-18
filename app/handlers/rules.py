from aiogram import types

from app.keyboards import HOME_KEYBOARD

async def handle_show_rules(callback: types.CallbackQuery):
    # Меняем текст сообщения и ставим кнопку "Назад"
    await callback.message.edit_text('<Правила игры>', reply_markup=HOME_KEYBOARD)
    await callback.answer()
