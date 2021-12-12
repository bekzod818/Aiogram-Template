from loader import dp
from aiogram import types
from aiogram.dispatcher.filters import Text
from states.shop import Shop
from aiogram.dispatcher import FSMContext
from data.acerlaptop import laptops
from data.arteltv import tvs
from data.artelfreeze import freezes
from keyboards.default.categorymenu import cat
from keyboards.inline.inbutton import inline_menu, make_button
from keyboards.default.submenu import numbers
from aiogram.types import CallbackQuery


@dp.message_handler(Text(equals=["ACER"]), state=Shop.sub_category)
async def sub_cat(message: types.Message, state: FSMContext):
    sub_category = message.text
    await state.update_data(
        {"sub_category": sub_category}
    )
    msg = ""
    for i in range(len(laptops)):
        msg += f"<b><u>{i + 1}-NOUTBUK</u></b>: {laptops[i]['name']}<b><u>NARX:</u></b> ({laptops[i]['price']}) \n"
    await message.answer(msg, parse_mode="html", reply_markup=inline_menu)
    await Shop.product.set()

@dp.message_handler(Text(equals=["ARTEL"]), state=Shop.sub_category)
async def duplicate(message: types.Message, state: FSMContext):
    sub_category = message.text
    await state.update_data(
        {"sub_category": sub_category}
    )
    data = await state.get_data()
    category = data.get('category')
    if category == "📺 Televizor":
        for tv in tvs:
            msg = f"<b>NOMI</b>: {tv['name']}<b>NARX:</b> {tv['price']}\n"
            img = tv['link']
            menu = make_button(tv['about'])
            await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.sub_category.set()
    elif category == "🥶 Muzlatgich":
        # await message.answer("Artel Muzlatgizlari")
        msg = ""
        for i in range(len(freezes)):
            msg += f"<b><u>{i + 1}-MUZLATGICH</u></b>: {freezes[i]['name']}<b><u>NARX:</u></b> ({freezes[i]['price']}) \n"
        await message.answer(msg, parse_mode="html", reply_markup=numbers)
        await Shop.product.set()

@dp.callback_query_handler(text="1", state=Shop.product)
async def call_laptop(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "💻 Kompyuter" and sub_category == "ACER":
        msg = f"<b>NOMI</b>: {laptops[0]['name']}<b>NARX:</b> {laptops[0]['price']}\n"
        msg += laptops[0]['link']
        menu = make_button(laptops[0]['about'])
        await call.message.delete()
        await call.message.answer(msg, reply_markup=menu)
        # await call.message.answer_photo(photo=img, caption=msg, reply_markup=cat)
        await Shop.sub_category.set()

@dp.callback_query_handler(text="2", state=Shop.product)
async def call_laptop(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "💻 Kompyuter" and sub_category == "ACER":
        msg = f"<b>NOMI</b>: {laptops[1]['name']}<b>NARX:</b> {laptops[1]['price']}\n"
        img = laptops[1]['link']
        menu = make_button(laptops[1]['about'])
        await call.message.delete()
        await call.message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.sub_category.set()

@dp.callback_query_handler(text="3", state=Shop.product)
async def call_laptop(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "💻 Kompyuter" and sub_category == "ACER":
        msg = f"<b>NOMI</b>: {laptops[2]['name']}<b>NARX:</b> {laptops[2]['price']}\n"
        img = laptops[2]['link']
        menu = make_button(laptops[2]['about'])
        await call.message.delete()
        await call.message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.sub_category.set()

@dp.callback_query_handler(text="4", state=Shop.product)
async def call_laptop(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "💻 Kompyuter" and sub_category == "ACER":
        msg = f"<b>NOMI</b>: {laptops[3]['name']}<b>NARX:</b> {laptops[3]['price']}\n"
        img = laptops[3]['link']
        menu = make_button(laptops[3]['about'])
        await call.message.delete()
        await call.message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.sub_category.set()

@dp.callback_query_handler(text="5", state=Shop.product)
async def call_laptop(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "💻 Kompyuter" and sub_category == "ACER":
        msg = f"<b>NOMI</b>: {laptops[4]['name']}<b>NARX:</b> {laptops[4]['price']}\n"
        img = laptops[4]['link']
        menu = make_button(laptops[4]['about'])
        await call.message.delete()
        await call.message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.sub_category.set()

@dp.callback_query_handler(text="6", state=Shop.product)
async def call_laptop(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "💻 Kompyuter" and sub_category == "ACER":
        msg = f"<b>NOMI</b>: {laptops[5]['name']}<b>NARX:</b> {laptops[5]['price']}\n"
        img = laptops[5]['link']
        menu = make_button(laptops[5]['about'])
        await call.message.delete()
        await call.message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.sub_category.set()

@dp.callback_query_handler(text="7", state=Shop.product)
async def call_laptop(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "💻 Kompyuter" and sub_category == "ACER":
        msg = f"<b>NOMI</b>: {laptops[6]['name']}<b>NARX:</b> {laptops[6]['price']}\n"
        img = laptops[6]['link']
        menu = make_button(laptops[6]['about'])
        await call.message.delete()
        await call.message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.sub_category.set()

@dp.callback_query_handler(text="8", state=Shop.product)
async def call_laptop(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "💻 Kompyuter" and sub_category == "ACER":
        msg = f"<b>NOMI</b>: {laptops[7]['name']}<b>NARX:</b> {laptops[7]['price']}\n"
        img = laptops[7]['link']
        menu = make_button(laptops[7]['about'])
        await call.message.delete()
        await call.message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.sub_category.set()

@dp.callback_query_handler(text="9", state=Shop.product)
async def call_laptop(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "💻 Kompyuter" and sub_category == "ACER":
        msg = f"<b>NOMI</b>: {laptops[8]['name']}<b>NARX:</b> {laptops[8]['price']}\n"
        img = laptops[8]['link']
        menu = make_button(laptops[8]['about'])
        await call.message.delete()
        await call.message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.sub_category.set()

@dp.callback_query_handler(text="10", state=Shop.product)
async def call_laptop(call: CallbackQuery, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "💻 Kompyuter" and sub_category == "ACER":
        msg = f"<b>NOMI</b>: {laptops[9]['name']}<b>NARX:</b> {laptops[9]['price']}\n"
        img = laptops[9]['link']
        menu = make_button(laptops[9]['about'])
        await call.message.delete()
        await call.message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.sub_category.set()
