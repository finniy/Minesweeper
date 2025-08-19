from aiogram.types import CallbackQuery

from app.database.players import PlayerDB
from app.utils.keyboards import HOME_KEYBOARD_MENU
from app.messages.text import PLAYERS_EMPTY, RATING_LINE, RATING_HEADER

players_db = PlayerDB()


async def rating_handler(callback: CallbackQuery) -> None:
    """
    Обрабатывает нажатие кнопки 'Рейтинг'.

    Получает топ-10 игроков из базы данных и формирует текст с их статистикой.
    Если игроков нет, отправляет уведомление.

    """
    top_players = players_db.get_top_players(10)

    if not top_players:
        await callback.answer(PLAYERS_EMPTY)
        return

    response = RATING_HEADER
    for i, player in enumerate(top_players, start=1):
        user_id, username, games_played, wins, losses, rating = player
        response += RATING_LINE.format(
            pos=i,
            username=username,
            elo=rating,
            wins=wins,
            losses=losses
        )

    await callback.message.edit_text(
        response,
        reply_markup=HOME_KEYBOARD_MENU,
        parse_mode="HTML",
        disable_web_page_preview=True
    )
    await callback.answer()
