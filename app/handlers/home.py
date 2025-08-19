from aiogram.types import CallbackQuery

from app.utils.keyboards import START_KEYBOARD
from app.messages.text import WELCOME_MESSAGE


async def home_handler(callback: CallbackQuery) -> None:
    """
    Обработчик нажатия кнопки "Домой".
    """
    await callback.message.edit_text(
        WELCOME_MESSAGE,
        reply_markup=START_KEYBOARD,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    await callback.answer()
