from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.game_logic import Game


def create_board(game: Game):
    """Превращает поле в inline-кнопки."""

    keyboard = []
    for row in range(game.rows):
        row_buttons = []
        for col in range(game.cols):
            cell = game.board[row][col]
            if cell.opened:
                if cell.mine:
                    text = "💥"
                elif cell.neighbours > 0:
                    text = str(cell.neighbours)
                else:
                    text = "0"
            else:
                text = "⬜"  # закрытая клетка
            row_buttons.append(
                InlineKeyboardButton(text=text, callback_data=f"open_{row}_{col}")
            )
        keyboard.append(row_buttons)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
