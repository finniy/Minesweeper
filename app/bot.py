from aiogram import filters
from aiogram import Dispatcher

from app.bot_instance import dp, bot
from app.handlers.start import start_command
from app.handlers.game import handle_start_game, handle_open_cell
from app.handlers.rules import handle_show_rules
from app.handlers.home import home_handler
from app.handlers.rating import rating_handler


def register_handlers(dp: Dispatcher) -> None:
    """
    Регистрирует все хендлеры бота.
    """
    # Хендлер на команду /start
    dp.message.register(start_command, filters.Command(commands=["start"]))

    # Хендлеры на callback_data
    dp.callback_query.register(handle_start_game, lambda c: c.data == "start_game")
    dp.callback_query.register(handle_open_cell, lambda c: c.data.startswith("open_"))
    dp.callback_query.register(handle_show_rules, lambda c: c.data == "show_rules")
    dp.callback_query.register(home_handler, lambda c: c.data == "back_to_start")
    dp.callback_query.register(rating_handler, lambda c: c.data == "rating")


register_handlers(dp)


async def main() -> None:
    """
    Запускает бота и начинает опрос Telegram API.
    """
    await dp.start_polling(bot)
