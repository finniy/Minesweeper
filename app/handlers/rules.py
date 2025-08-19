from aiogram import types

from app.utils.keyboards import HOME_KEYBOARD_MENU
from app.messages.text import RULES_TEXT


async def handle_show_rules(callback: types.CallbackQuery) -> None:
    """
    Отправляет пользователю правила игры.
    Меняет текст текущего сообщения на правила и добавляет клавиатуру "Назад".
    """
    await callback.message.edit_text(
        RULES_TEXT,
        reply_markup=HOME_KEYBOARD_MENU,
        parse_mode="Markdown"
    )
    await callback.answer()
