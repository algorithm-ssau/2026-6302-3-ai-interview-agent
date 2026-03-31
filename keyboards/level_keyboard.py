from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

def level_keyboard():
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text="Junior")],
            [KeyboardButton(text="Middle")],
            [KeyboardButton(text="Senior")]
        ],
        resize_keyboard=True
    )