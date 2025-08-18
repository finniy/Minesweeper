from aiogram.types import CallbackQuery

from app.keyboards import START_KEYBOARD

async def home_handler(callback: CallbackQuery) -> None:
    """
    Обработчик нажатия кнопки "🏠 Домой".
    """
    await callback.message.edit_text(
        "<Команда /start>",
        reply_markup=START_KEYBOARD
    )
    await callback.answer()
