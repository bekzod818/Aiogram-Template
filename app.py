import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.session.middlewares.request_logging import logger
from utils.db.postgres import Database


def setup_handlers(dispatcher: Dispatcher) -> None:
    """HANDLERS"""
    from handlers import setup_routers

    dispatcher.include_router(setup_routers())


def setup_middlewares(dispatcher: Dispatcher, bot: Bot) -> None:
    """MIDDLEWARE"""
    from middlewares.throttling import ThrottlingMiddleware

    # Классический внутренний Middleware для защита от спама. Базовые тайминги 0.5 секунд между запросами
    dispatcher.message.middleware(ThrottlingMiddleware(slow_mode_delay=0.5))


def setup_filters(dispatcher: Dispatcher) -> None:
    """FILTERS"""
    from filters import ChatPrivateFilter

    # Классический общий Filter для определения типа чата
    # Также фильтр можно ставить отдельно на каждый роутер в handlers/users/__init__
    dispatcher.message.filter(ChatPrivateFilter(chat_type=["private"]))


async def setup_aiogram(dispatcher: Dispatcher, bot: Bot) -> None:
    logger.info("Configuring aiogram")
    setup_handlers(dispatcher=dispatcher)
    setup_middlewares(dispatcher=dispatcher, bot=bot)
    setup_filters(dispatcher=dispatcher)
    logger.info("Configured aiogram")


async def database_connected():
    db = Database()

    # Ma'lumotlar bazasini yaratamiz:
    await db.create()
    # await db.drop_users()
    await db.create_table_users()


async def aiogram_on_startup_polling(dispatcher: Dispatcher, bot: Bot) -> None:
    from utils.set_bot_commands import set_default_commands
    from utils.notify_admins import on_startup_notify

    logger.info("Database connected")
    await database_connected()

    logger.info("Starting polling")
    await bot.delete_webhook(drop_pending_updates=True)
    await setup_aiogram(bot=bot, dispatcher=dispatcher)
    await on_startup_notify(bot=bot)
    await set_default_commands(bot=bot)


async def aiogram_on_shutdown_polling(dispatcher: Dispatcher, bot: Bot):
    logger.info("Stopping polling")
    await bot.session.close()
    await dispatcher.storage.close()


def main():
    """CONFIG"""
    from data.config import BOT_TOKEN
    from aiogram.enums import ParseMode
    from aiogram.fsm.storage.memory import MemoryStorage

    bot = Bot(token=BOT_TOKEN, parse_mode=ParseMode.HTML)
    storage = MemoryStorage()
    dispatcher = Dispatcher(storage=storage)

    dispatcher.startup.register(aiogram_on_startup_polling)
    dispatcher.shutdown.register(aiogram_on_shutdown_polling)
    asyncio.run(dispatcher.start_polling(bot,  # Экземпляр бота
                                            # список типов обновлений, которые бот будет получать ['message', 'chat_member']
                                            # при dp.resolve_used_update_types() aiogram пройдётся по роутерам и сам составит список
                                            allowed_updates=['message', 'chat_member'],
                                            # закрывать сеансы бота при выключении
                                            close_bot_session=True))


if __name__ == "__main__":
    main()
