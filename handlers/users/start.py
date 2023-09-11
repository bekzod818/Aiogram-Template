from typing import Any

from aiogram import Router
from aiogram.filters import Command
from aiogram.handlers import MessageHandler
from aiogram.methods import SendMessage

router = Router()


@router.message(Command(commands=['start']))
class MyHandler(MessageHandler):

    # название функции всегда handle, потому что это перезапись метода
    async def handle(self) -> Any:
        return SendMessage(chat_id=self.chat.id, text=f"Hello, {self.from_user.username}")
