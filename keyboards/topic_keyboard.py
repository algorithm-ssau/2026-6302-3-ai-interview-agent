from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def topic_keyboard():
    """Клавиатура выбора темы"""
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="🐍 Python")],
            [KeyboardButton(text="☕ Java")],
            [KeyboardButton(text="🗄 SQL")],
            [KeyboardButton(text="📦 Git")]
        ],
        resize_keyboard=True
    )