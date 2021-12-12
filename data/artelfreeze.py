import requests
from bs4 import BeautifulSoup
from uuid import uuid4
from aiogram import types
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

def get_data(num):
    url = "https://glotr.uz/holodilniki-v-taskente/proizvoditel-artel/"

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


freezes = []
for i in range(4, 14):
    freezes.append(get_data(i))
