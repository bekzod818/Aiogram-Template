import logging

from aiogram import Bot

from data.config import admins


async def on_startup_notify(bot: Bot):
    for admin in admins:
        try:
            bot_properties = await bot.me()
            message = ["Бот начал работу.",
                       f"<b>Bot id:</> {bot_properties.id}",
                       f"<b>Bot username:</> {bot_properties.username}"]
            await bot.send_message(admin, "\n".join(message))
        except Exception as err:
            logging.exception(err)
