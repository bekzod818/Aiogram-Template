from aiogram.dispatcher.filters.state import StatesGroup, State

class Shop(StatesGroup):
    category = State()
    sub_category = State()
    product = State()
