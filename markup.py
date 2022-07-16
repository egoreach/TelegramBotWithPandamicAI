from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

btn_main = KeyboardButton('Назад')

# --Main menu--
btn1 = KeyboardButton('Информация о COVID-19')
btn2 = KeyboardButton('Интересное о COVID-19')
mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn1, btn2)

# --Other Menu(btn1)
btn_prod = KeyboardButton('Узнать прогноз')
btn_kol = KeyboardButton('Сколько зараженных на данный момент')# --можно убрать--
otherMenu2 = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_prod, btn_kol, btn_main)

# --Other Menu(btn2)
btn_fact = KeyboardButton('Факты о COVID-19')
btn_zar = KeyboardButton('Профилактика COVID-19')
otherMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_fact, btn_zar, btn_main)

# --Prevention Menu
btn_cip = KeyboardButton('Симптомы')
btn_pren = KeyboardButton('Профилактика')
preventionMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btn_cip, btn_pren, btn_main)