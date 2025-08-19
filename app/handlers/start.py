from aiogram import types

from app.keyboards import START_KEYBOARD
from app.messages.text import WELCOME_MESSAGE


async def start_command(message: types.Message) -> None:
    """
    Отправляет пользователю приветственное сообщение при старте бота.
    Использует HTML для форматирования текста и отключает предпросмотр ссылок.
    Прикрепляет клавиатуру START_KEYBOARD для дальнейших действий.
    """
    await message.answer(
        WELCOME_MESSAGE,
        reply_markup=START_KEYBOARD,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
