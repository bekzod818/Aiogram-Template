import time

from aiogram.dispatcher.middlewares.base import BaseMiddleware
from aiogram.types import Message


class ThrottlingMiddleware(BaseMiddleware):
    def __init__(self, slow_mode_delay=0.5):
        self.user_timeouts = {}
        self.slow_mode_delay = slow_mode_delay
        super(ThrottlingMiddleware, self).__init__()

    async def __call__(self, handler, event: Message, data):
        user_id = event.from_user.id
        current_time = time.time()
        
        # Проверяем, есть ли запись о последнем запросе от этого пользователя
        last_request_time = self.user_timeouts.get(user_id, 0)
        if current_time - last_request_time < self.slow_mode_delay:
            # Если запросы слишком частые, включаем медленный режим
            await event.reply('Слишком много запросов! Подождите немного.')
            return
        
        else:
            # Обновляем время последнего запроса
            self.user_timeouts[user_id] = current_time
            # Пропускаем event к handler
            return await handler(event, data)
        
        