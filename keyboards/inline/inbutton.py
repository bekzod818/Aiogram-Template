from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = []
first_row = []
second_row = []
third_row = []
for i in range(1, 6):
    first_row.append(InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))
for i in range(6, 11):
    second_row.append(InlineKeyboardButton(text=f"{i}", callback_data=f"{i}"))
third_row.append(InlineKeyboardButton(text=f"⬅️ Orqaga", callback_data="back"))
# third_row.append(InlineKeyboardButton(text=f"🎛 Bosh sahifa", callback_data="home"))
buttons = [first_row, second_row]

inline_menu = InlineKeyboardMarkup(inline_keyboard=buttons)

def make_button(link):
    product_menu = InlineKeyboardMarkup(inline_keyboard=[
            [
                InlineKeyboardButton(text="📌 Batafsil", url = link),
                InlineKeyboardButton(text="✉️ Ulashish", switch_inline_query="laptop")
            ]
        ])

    return product_menu
