from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart
from filters import IsPrivate
from loader import dp, bot
from data.config import CHANNELS
from keyboards.inline.subscription import check_button


@dp.message_handler(IsPrivate(), CommandStart())
async def bot_start(message: types.Message):
    # await message.answer(f"Salom, {message.from_user.full_name}!\nYangi e'lon berishni hohlaysizmi?", reply_markup=menu)
    channels_format = str()
    for channel in CHANNELS:
        chat = await bot.get_chat(channel)
        invite_link = await chat.export_invite_link()
        # logging.info(invite_link)
        channels_format += f"➡️ <a href='{invite_link}'><b>{chat.title}</b></a>\n"

    await message.answer(f"Quyidagi kanallarga obuna bo'ling: \n\n"
                         f"{channels_format}",
                         reply_markup=check_button,
                         disable_web_page_preview=True)