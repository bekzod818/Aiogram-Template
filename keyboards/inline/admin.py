from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

confirmation_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[[
        InlineKeyboardButton(text="✅ Tasdiqlash", callback_data="admin_confirm"),
        InlineKeyboardButton(text="❌ Bekor qilish", callback_data="admin_cancel"),
    ]]
)
