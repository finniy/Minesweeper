from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from app.utils.game_logic import Game


def create_board(game: Game, game_key: str, win: bool = False) -> InlineKeyboardMarkup:
    """
    Преобразует игровое поле Сапера в InlineKeyboardMarkup для Telegram.
    Каждая клетка представлена кнопкой:
    💥 — мина, число — количество мин вокруг, ⬜ — закрытая клетка.
    При победе все клетки открываются.
    """
    keyboard = []
    for row in range(game.rows):
        row_buttons = []
        for col in range(game.cols):
            cell = game.board[row][col]
            if cell.opened or win:
                if cell.mine:
                    text = "💥"
                elif cell.neighbours > 0:
                    text = str(cell.neighbours)
                else:
                    text = "0"
            else:
                text = "⬜"  # закрытая клетка
            row_buttons.append(
                InlineKeyboardButton(
                    text=text,
                    callback_data=f"open_{game_key}_{row}_{col}"
                )
            )
        keyboard.append(row_buttons)

    return InlineKeyboardMarkup(inline_keyboard=keyboard)
