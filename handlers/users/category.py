from aiogram import types
from aiogram.dispatcher.filters import Text
from keyboards.default.submenu import markup1, markup2, markup3, markup4
from loader import dp
from keyboards.default.categorymenu import cat
from states.shop import Shop
from aiogram.dispatcher import FSMContext


@dp.message_handler(Text(equals=["💻 Kompyuter"]), state=Shop.category)
async def laptop(message: types.Message, state: FSMContext):
    category = message.text
    await state.update_data(
        {"category": category}
    )
    await message.answer(f"Kompyuter turlaridan birini tanlang 🔽", reply_markup=markup1)
    await Shop.next()

@dp.message_handler(Text(equals=["📱 Telefon"]), state=Shop.category)
async def phone(message: types.Message, state: FSMContext):
    category = message.text
    await state.update_data(
        {"category": category}
    )
    await message.answer(f"Telefon turlaridan birini tanlang 🔽", reply_markup=markup2)
    await Shop.next()

@dp.message_handler(Text(equals=["📺 Televizor"]), state=Shop.category)
async def tv(message: types.Message, state: FSMContext):
    category = message.text
    await state.update_data(
        {"category": category}
    )
    await message.answer(f"Televizor turlaridan birini tanlang 🔽", reply_markup=markup3)
    await Shop.next()

@dp.message_handler(Text(equals=["🥶 Muzlatgich"]), state=Shop.category)
async def freeze(message: types.Message, state: FSMContext):
    category = message.text
    await state.update_data(
        {"category": category}
    )
    await message.answer(f"Muzlatkich turlaridan birini tanlang 🔽", reply_markup=markup4)
    await Shop.next()

@dp.message_handler(Text(equals=["🔙 ORQAGA"]), state=Shop.sub_category)
async def laptop(message: types.Message, state: FSMContext):
    await message.answer(f"Bo'limlardan birini tanlang 🔽", reply_markup=cat)
    await Shop.category.set()


@dp.message_handler(Text(equals=["ORQAGA"]), state=Shop.product)
async def laptop(message: types.Message, state: FSMContext):
    await message.answer(f"Muzlatkich turlaridan birini tanlang 🔽", reply_markup=markup4)
    await Shop.sub_category.set()


@dp.message_handler(Text(equals=["BOSH MENU"]), state=Shop.product)
async def laptop(message: types.Message, state: FSMContext):
    await message.answer(f"Bo'limlardan birini tanlang 🔽", reply_markup=cat)
    await Shop.category.set()
