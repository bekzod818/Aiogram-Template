from loader import dp, bot
from aiogram import types
from states.newpost import NewPost
from aiogram.dispatcher import FSMContext
from keyboards.inline.manage import confirmation_keyboard


@dp.message_handler(text_contains="E'lon berish", state=None)
async def new_post(message: types.Message):
    await message.answer("Mahsulot nomini kiriting")
    await NewPost.title.set()


@dp.message_handler(state=NewPost.title)
async def title(message: types.Message, state: FSMContext):
    title = message.text

    await state.update_data(
        {'title': title}
    )
    await message.answer("Mahsulot haqida to'liq ma'lumot kiriting")
    await NewPost.next()


@dp.message_handler(state=NewPost.desc)
async def title(message: types.Message, state: FSMContext):
    desc = message.text

    await state.update_data(
        {'desc': desc}
    )
    await message.answer("Mahsulot narxini kiriting")
    await NewPost.next()


@dp.message_handler(state=NewPost.price)
async def title(message: types.Message, state: FSMContext):
    price = message.text

    await state.update_data(
        {'price': price}
    )
    await message.answer("Telefon raqamingizni kiriting")
    await NewPost.next()


@dp.message_handler(state=NewPost.phone)
async def title(message: types.Message, state: FSMContext):
    phone = message.text

    await state.update_data(
        {'phone': phone}
    )
    await message.answer("Manzilingizni kiriting")
    await NewPost.next()


@dp.message_handler(state=NewPost.address)
async def title(message: types.Message, state: FSMContext):
    address = message.text

    await state.update_data(
        {'address': address}
    )
    await message.answer("Mahsulot rasmini yuboring")
    await NewPost.next()


@dp.message_handler(content_types=['photo'], state=NewPost.image)
async def title(message: types.Message, state: FSMContext):
    image = message.photo[-1].file_id

    await state.update_data(
        {'image': image}
    )
    # Ma'lumotlarni qayta o'qiymiz
    data = await state.get_data()
    title = data.get('title')
    desc = data.get('desc')
    price = data.get('price')
    phone = data.get('phone')
    address = data.get('address')
    image = data.get('image')

    msg = "📄 <b>Quyidagi ma'lumotlar qabul qilindi:</b>\n\n"
    msg += f"Nomi: {title}\n"
    msg += f"Batafsil: {desc}\n"
    msg += f"Narxi: {price}\n"
    msg += f"Tel raqam: {phone}\n"
    msg += f"Manzil: {address}\n"
    await message.answer_photo(image, caption=msg, reply_markup=confirmation_keyboard)
    await NewPost.next()
    # await state.finish()
