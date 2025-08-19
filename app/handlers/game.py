from aiogram import types

from app.game_logic import Game
from app.bot_instance import active_games
from app.keyboards import HOME_KEYBOARD
from app.utils.board import create_board
from app.utils.key import generate_game_key


async def handle_start_game(callback: types.CallbackQuery):
    user_id = callback.from_user.id
    username = callback.from_user.username
    game = Game(mines=10)
    game_key = generate_game_key()

    if any(user_id == val[0] for val in active_games.values()):
        await callback.answer("Вы уже создали игру")
        return

    active_games[game_key] = {
        "user_id": user_id,
        "username": username,
        "game": game
    }

    await callback.message.edit_text(
        "Игра началась! 🎮",
        reply_markup=create_board(game, game_key)
    )
    await callback.answer()


async def handle_open_cell(callback: types.CallbackQuery):
    _, game_key, row, col = callback.data.split('_')
    row, col = int(row), int(col)

    game_data = active_games.get(game_key)
    if not game_data:
        await callback.answer("Игра окончена или не найдена")
        return

    game = game_data["game"]
    user_id = game_data["user_id"]
    username = game_data["username"]

    result = game.open_clear_cell(row, col)

    if result == 'blow':
        await callback.message.edit_text(
            "Игра окончена 🎮",
            reply_markup=create_board(game, game_key)
        )

        await callback.message.answer(
            "💥 Бум! Ты подорвался на мине",
            reply_markup=HOME_KEYBOARD
        )
        del active_games[game_key]
        return

    if result == 'opened':  # клетка уже открыта
        await callback.answer("Эта клетка уже открыта")
        return

    # обычный ход — обновляем сообщение с текущей доской
    await callback.message.edit_text(
        "Игра продолжается 🎮",
        reply_markup=create_board(game, game_key)
    )

    await callback.answer()

    if game.check_victory():
        await callback.message.edit_text(
            "Игра окончена 🎮",
            reply_markup=create_board(game, game_key, True)
        )

        await callback.message.answer(
            "🎉 Поздравляем, вы выиграли!",
            reply_markup=HOME_KEYBOARD
        )
        del active_games[game_key]
