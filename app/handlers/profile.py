from aiogram.types import CallbackQuery

from app.database.players import PlayerDB
from app.utils.keyboards import HOME_KEYBOARD_MENU
from app.messages.text import NO_STATS, STATS_TEXT

players_db = PlayerDB()


async def profile_handler(callback: CallbackQuery) -> None:
    """
    Отправляет статистику игрока по ID.
    Если статистики нет — сообщает об этом.
    """
    user_id = callback.from_user.id
    stats = players_db.get_player_profile(user_id)

    if stats is None:
        await callback.answer(NO_STATS)
        return

    response = STATS_TEXT.format(
        games_played=stats["games_played"],
        wins=stats["wins"],
        losses=stats["losses"],
        elo_rating=stats["rating"]
    )

    await callback.message.edit_text(
        response,
        reply_markup=HOME_KEYBOARD_MENU,
        parse_mode="HTML",
    )
    await callback.answer()
