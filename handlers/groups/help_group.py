from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp
from filters import IsGroup
from loader import dp


@dp.message_handler(IsGroup(), CommandHelp())
async def bot_help(message: types.Message):
    text = ("Guruhdagi Buyruqlar: ",
            "/start - Botni ishga tushirish",
            "/help - Yordam so'rash")

    await message.answer("\n".join(text))
