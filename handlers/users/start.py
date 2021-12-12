from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from keyboards.default.categorymenu import cat
from states.shop import Shop
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f"Salom, {message.from_user.full_name}!\nBo'limlardan birini tanlang 🔽", reply_markup=cat)
    await Shop.category.set()
