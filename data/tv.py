import requests
from bs4 import BeautifulSoup
from uuid import uuid4
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_data(num):
    url = "https://glotr.uz/televizory-v-taskente/proizvoditel-samsung-lg-shivaki-artel/"

    html = requests.get(url).text

    soup = BeautifulSoup(html, "html.parser")

    div = soup.findAll("div", attrs={"class":"proposals-item-content"})[num]
    name = div.find('a', attrs={'class': ['proposal-img', 'lazyload']})
    link = name.attrs['data-src']
    about = "https://glotr.uz" + name.attrs['href']

    div_info = soup.findAll("div", attrs={"class": "proposal-main-info-wrap"})[num]
    name_href = div.find("a", attrs={"class": "proposal-item-link"})
    span = name_href.select("span")
    name = span[0].text

    div_price = soup.findAll("div", attrs={"class": ["proposal-price_wrap", "text-overflow"]})[num]
    href = div_price.find("div", attrs={"proposal-main-price"})
    price = href.select("span.proposal-price-value")[0].text
    valyuta = href.select("span.proposal-price-currency")[0].text

    data = {
        "name": name,
        "link": link,
        "price": price + " " + valyuta,
        "about": about
    }

    return data


tvs = []
for i in range(4, 15):
    tvs.append(get_data(i))

data_tvs = []
for tv in tvs:
    menu = InlineKeyboardMarkup(inline_keyboard=[
        [
            InlineKeyboardButton(text="📌 Batafsil", url = tv["about"]),
            InlineKeyboardButton(text="✉️ Ulashish", switch_inline_query="tv")
        ]
    ])
    data_tvs.append(
        types.InlineQueryResultArticle(
            id = str(uuid4()),
            thumb_url = tv['link'],
            title = tv['name'],
            input_message_content=types.InputTextMessageContent(
                message_text=f"{tv['name']}\nNarxi: {tv['price']}",
            ),
            description = f"{tv['price']} {tv['about']}",
            reply_markup = menu
        ),
    )
