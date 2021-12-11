from loader import dp
from aiogram import types
from data.laptops import data_laptops
from data.phones import data_phones
from data.tv import data_tvs

@dp.inline_handler(text="laptop")
async def laptops_query(query: types.InlineQuery):
    await query.answer(data_laptops)


@dp.inline_handler(text="phone")
async def phones_query(query: types.InlineQuery):
    await query.answer(data_phones)


@dp.inline_handler(text="tv")
async def laptops_query(query: types.InlineQuery):
    await query.answer(data_tvs)
