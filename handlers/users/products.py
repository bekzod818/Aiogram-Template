from aiogram import types
from aiogram.dispatcher.filters import Text
from loader import dp
from keyboards.default.categorymenu import cat
from states.shop import Shop
from aiogram.dispatcher import FSMContext
from data.artelfreeze import freezes
from keyboards.inline.inbutton import make_button


@dp.message_handler(Text(equals=["1️⃣"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[0]['name']}<b>NARX:</b> {freezes[0]['price']}\n"
        img = freezes[0]['link']
        menu = make_button(freezes[0]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()


@dp.message_handler(Text(equals=["2️⃣"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[1]['name']}<b>NARX:</b> {freezes[1]['price']}\n"
        img = freezes[1]['link']
        menu = make_button(freezes[1]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()


@dp.message_handler(Text(equals=["3️⃣"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[2]['name']}<b>NARX:</b> {freezes[2]['price']}\n"
        img = freezes[2]['link']
        menu = make_button(freezes[2]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()


@dp.message_handler(Text(equals=["4️⃣"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[3]['name']}<b>NARX:</b> {freezes[3]['price']}\n"
        img = freezes[3]['link']
        menu = make_button(freezes[3]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()


@dp.message_handler(Text(equals=["5️⃣"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[4]['name']}<b>NARX:</b> {freezes[4]['price']}\n"
        img = freezes[4]['link']
        menu = make_button(freezes[4]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()


@dp.message_handler(Text(equals=["5️⃣"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[4]['name']}<b>NARX:</b> {freezes[4]['price']}\n"
        img = freezes[4]['link']
        menu = make_button(freezes[4]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()


@dp.message_handler(Text(equals=["6️⃣"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[5]['name']}<b>NARX:</b> {freezes[5]['price']}\n"
        img = freezes[5]['link']
        menu = make_button(freezes[5]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()


@dp.message_handler(Text(equals=["7️⃣"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[6]['name']}<b>NARX:</b> {freezes[6]['price']}\n"
        img = freezes[6]['link']
        menu = make_button(freezes[6]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()


@dp.message_handler(Text(equals=["8️⃣"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[7]['name']}<b>NARX:</b> {freezes[7]['price']}\n"
        img = freezes[7]['link']
        menu = make_button(freezes[7]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()


@dp.message_handler(Text(equals=["9️⃣"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[8]['name']}<b>NARX:</b> {freezes[8]['price']}\n"
        img = freezes[8]['link']
        menu = make_button(freezes[8]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()


@dp.message_handler(Text(equals=["🔟"]), state=Shop.product)
async def freeze(message: types.Message, state: FSMContext):
    data = await state.get_data()
    category = data.get('category')
    sub_category = data.get('sub_category')
    if category == "🥶 Muzlatgich" and sub_category == "ARTEL":
        msg = f"<b>NOMI</b>: {freezes[9]['name']}<b>NARX:</b> {freezes[9]['price']}\n"
        img = freezes[9]['link']
        menu = make_button(freezes[9]['about'])
        await message.answer_photo(photo=img, caption=msg, reply_markup=menu)
        await Shop.product.set()
