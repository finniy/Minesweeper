from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# Стартовая клавиатура
START_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🎮 Начать игру", callback_data="start_game")],
        [InlineKeyboardButton(text="📖 Правила", callback_data="show_rules")]
    ]
)

# Клавиатура с кнопкой "Домой"
HOME_KEYBOARD = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="🏠 Домой", callback_data="back_to_start")]
    ]
)
