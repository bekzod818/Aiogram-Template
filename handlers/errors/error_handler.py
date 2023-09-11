import logging
from typing import Any

from aiogram import Router
from aiogram.exceptions import (TelegramAPIError,
                                TelegramUnauthorizedError,
                                TelegramBadRequest,
                                TelegramNetworkError,
                                TelegramNotFound,
                                TelegramConflictError,
                                TelegramForbiddenError,
                                RestartingTelegram,
                                CallbackAnswerException,
                                TelegramEntityTooLarge,
                                TelegramRetryAfter,
                                TelegramMigrateToChat,
                                TelegramServerError)
from aiogram.handlers import ErrorHandler


router = Router()


@router.errors()
class MyErrorHandler(ErrorHandler):
    async def handle(self, ) -> Any:
        """
        Handler ошибок. Перехватывает почти все исключения, возникающих при работе бота.
        :param: None
        :return: stdout logging
        """
        if isinstance(self.exception_name, TelegramUnauthorizedError):
            """
            Возникает исключение, когда токен бота недействителен.
            """
            logging.info(f'Unauthorized: {self.exception_message}')
            return True
        
        if isinstance(self.exception_name, TelegramNetworkError):
            """
            Базовое исключение для всех сетевых ошибок Telegram.
            """
            logging.exception(f'NetworkError: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, TelegramNotFound):
            """
            Исключение возникает, когда чат, сообщение, пользователь и т. д. не найдены.
            """
            logging.exception(f'NotFound: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, TelegramConflictError):
            """
            Возникает исключение, когда токен бота уже используется другим приложением в режиме опроса.
            """
            logging.exception(f'ConflictError: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, TelegramForbiddenError):
            """
            Возникает исключение, когда бота выгоняют из чата и т. д.
            """
            logging.exception(f'ForbiddenError: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, CallbackAnswerException):
            """
            Исключение для обратного ответа.
            """
            logging.exception(f'CallbackAnswerException: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, TelegramMigrateToChat):
            """
            Возникает исключение, когда чат был перенесен в супергруппу.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, TelegramServerError):
            """
            Возникает исключение, когда сервер Telegram возвращает ошибку 5xx.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, TelegramAPIError):
            """
            Базовое исключение для всех ошибок Telegram API.
            """
            logging.exception(f'EntityTooLarge: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, TelegramRetryAfter):
            """
            Исключение возникает при превышении контроля за флудом.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, TelegramEntityTooLarge):
            """
            Возникает исключение, когда вы пытаетесь отправить слишком большой файл.
            """
            logging.exception(f'EntityTooLarge: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, TelegramBadRequest):
            """
            Возникает исключение, когда запрос имеет неверный формат.
            """
            logging.exception(f'BadRequest: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        if isinstance(self.exception_name, RestartingTelegram):
            """
            Возникает исключение при перезапуске сервера Telegram.

            Похоже, что эта ошибка больше не используется Telegram, но она все еще здесь для обратной совместимости.
            
            В настоящее время вы должны ожидать, что Telegram может вызывать RetryAfter (с тайм-аутом 5 секунд)
            ошибка вместо этой.
            """
            logging.exception(f'RestartingTelegram: {self.exception_message} \nUpdate: {self.update}')
            return True
        
        logging.exception(f'Update: {self.update} \n{self.exception_name}')
