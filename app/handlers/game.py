from aiogram import types

from app.bot_instance import active_games
from app.utils.game_logic import Game
from app.logger import logger
from app.utils.board import create_board
from app.utils.key import generate_game_key
from app.utils.keyboards import HOME_KEYBOARD_GAME
from app.database.players import PlayerDB
from app.messages.text import START_GAME_TEXT, GAME_OVER_TEXT, BLOW_TEXT, ALREADY_OPENED_TEXT, VICTORY_TEXT, \
    ALREADY_CREATED_GAME_TEXT, GAME_NOT_FOUND_TEXT

players_db = PlayerDB()


async def handle_start_game(callback: types.CallbackQuery) -> None:
    """
    Создаёт новую игру для пользователя.
    Проверяет, есть ли уже активная игра.
    Инициализирует объект Game и сохраняет его в active_games.
    Отправляет сообщение с пустой доской.
    """
    user_id = callback.from_user.id
    username = callback.from_user.username or user_id
    game = Game(mines=10)
    game_key = generate_game_key()

    if any(user_id == val[0] for val in active_games.values()):
        await callback.answer(ALREADY_CREATED_GAME_TEXT)
        return

    active_games[game_key] = {
        "user_id": user_id,
        "username": username,
        "game": game
    }

    await callback.message.edit_text(
        START_GAME_TEXT,
        reply_markup=create_board(game, game_key)
    )
    await callback.answer()

    logger.info(f'Игра {game_key} запущена пользователем {username}')


async def handle_open_cell(callback: types.CallbackQuery) -> None:
    """
    Обрабатывает клик по клетке.
    Открывает клетку и проверяет результат (мину, уже открытую или обычный ход).
    Обновляет доску и проверяет победу.
    Завершает игру при поражении или победе.
    """
    _, game_key, row, col = callback.data.split('_')
    row, col = int(row), int(col)

    game_data = active_games.get(game_key)
    if not game_data:
        await callback.answer(GAME_NOT_FOUND_TEXT)
        return

    game = game_data["game"]
    user_id = game_data["user_id"]

    result = game.open_clear_cell(row, col)

    if result == 'blow':  # Взрыв
        await callback.message.edit_text(
            GAME_OVER_TEXT,
            reply_markup=create_board(game, game_key)
        )

        await callback.message.answer(
            BLOW_TEXT,
            reply_markup=HOME_KEYBOARD_GAME
        )
        del active_games[game_key]

        players_db.update_after_game(user_id, game.opened_cells_count, victory=False)

        logger.info(f'Игра {game_key} окончена')
        return

    if result == 'opened':  # клетка уже открыта
        await callback.answer(ALREADY_OPENED_TEXT)
        return

    # обычный ход — обновляем сообщение с текущей доской
    await callback.message.edit_text(
        START_GAME_TEXT,
        reply_markup=create_board(game, game_key)
    )
    await callback.answer()

    if game.check_victory():
        await callback.message.edit_text(
            GAME_OVER_TEXT,
            reply_markup=create_board(game, game_key, True)
        )

        await callback.message.answer(
            VICTORY_TEXT,
            reply_markup=HOME_KEYBOARD_GAME
        )

        players_db.update_after_game(user_id, game.opened_cells_count, victory=True)

        del active_games[game_key]

        logger.info(f'Игра {game_key} окончена')
