from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="📑 E'lon berish"),
        ],
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)
