from aiogram.types import ReplyKeyboardMarkup

markup1 = ReplyKeyboardMarkup(resize_keyboard=True)
markup1.row('ACER', 'APPLE')
markup1.row('DELL', 'ASUS')
markup1.row('LENOVO', '🔙 ORQAGA')


markup2 = ReplyKeyboardMarkup(resize_keyboard=True)
markup2.row('XIAOMI', 'APPLE')
markup2.row('SAMSUNG', 'VIVO')
markup2.row('HUAWEI', '🔙 ORQAGA')


markup3 = ReplyKeyboardMarkup(resize_keyboard=True)
markup3.row('LG', 'SAMSUNG')
markup3.row('SHIVAKI', 'ARTEL')
markup3.row('SONY', '🔙 ORQAGA')


markup4 = ReplyKeyboardMarkup(resize_keyboard=True)
markup4.row('HOFFMAN', 'BOSCH')
markup4.row('SAMSUNG', 'ARTEL')
markup4.row('GOODWELL', '🔙 ORQAGA')

numbers = ReplyKeyboardMarkup(resize_keyboard=True)
numbers.row('1️⃣', '2️⃣', "3️⃣")
numbers.row('4️⃣', '5️⃣', "6️⃣")
numbers.row('7️⃣', "8️⃣", "9️⃣")
numbers.row('🔟', 'ORQAGA', "BOSH MENU")
