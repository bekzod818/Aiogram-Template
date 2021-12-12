from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cat = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="💻 Kompyuter"),
            KeyboardButton(text="📱 Telefon"),
        ],
        [
            KeyboardButton(text="📺 Televizor"),
            KeyboardButton(text="🥶 Muzlatgich"),
        ],
    ],
    resize_keyboard=True,
)
