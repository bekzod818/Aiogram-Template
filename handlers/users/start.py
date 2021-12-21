import asyncpg
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.start_keyboard import menu
from loader import dp, db, bot
from data.config import ADMINS


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    name = message.from_user.username
    try:
        user = await db.add_user(
            telegram_id=message.from_user.id,
            full_name=message.from_user.full_name,
            username=message.from_user.username,
        )

        # ADMINGA xabar beramiz
        count = await db.count_users()
        msg = f"@{user[2]} bazaga qo'shildi.\nBazada {count} ta foydalanuvchi bor."
        await bot.send_message(chat_id=ADMINS[0], text=msg)
    except asyncpg.exceptions.UniqueViolationError:
        # user = await db.select_user(telegram_id=message.from_user.id)
        await bot.send_message(chat_id=ADMINS[0], text=f"@{name} bazaga oldin qo'shilgan")

    await message.answer(f"Xush kelibsiz! @{name}\nKurslar ro'yhati bilan tanishasizmi?", reply_markup=menu)
