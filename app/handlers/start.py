from aiogram import types

from app.utils.keyboards import START_KEYBOARD
from app.logger import logger
from app.messages.text import WELCOME_MESSAGE
from app.database.players import PlayerDB

players_db = PlayerDB()


async def start_command(message: types.Message) -> None:
    """
    Отправляет пользователю приветственное сообщение при старте бота.
    Использует HTML для форматирования текста и отключает предпросмотр ссылок.
    Прикрепляет клавиатуру START_KEYBOARD для дальнейших действий.
    """
    user_id = message.from_user.id
    username = message.from_user.username or str(user_id)

    players_db.add_or_update_player(user_id=user_id, username=username)

    await message.answer(
        WELCOME_MESSAGE,
        reply_markup=START_KEYBOARD,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    logger.info(f'{username} запустил бота')
