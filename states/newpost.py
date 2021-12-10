from aiogram.dispatcher.filters.state import StatesGroup, State

class NewPost(StatesGroup):
    title = State()
    desc = State()
    price = State()
    phone = State()
    address = State()
    image = State()
    confirm = State()
