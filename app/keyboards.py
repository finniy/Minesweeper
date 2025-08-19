from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Стартовая клавиатура
START_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Начать игру", callback_data="start_game")],
        [InlineKeyboardButton(text="📖 Правила", callback_data="show_rules")]
    ]
)

# Клавиатура с кнопкой "Домой" для меню
HOME_KEYBOARD_MENU = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Начать игру", callback_data="start_game")],
        [InlineKeyboardButton(text="🏠 Домой", callback_data="back_to_start")]
    ]
)

# Клавиатура с кнопкой "Домой" для игры
HOME_KEYBOARD_GAME = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🔄 Сыграть снова", callback_data="start_game")],
        [InlineKeyboardButton(text="🏠 Домой", callback_data="back_to_start")]
    ]
)
