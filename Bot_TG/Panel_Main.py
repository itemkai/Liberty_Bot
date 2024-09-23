from telebot import types

markup = types.ReplyKeyboardMarkup()
itembtn1 = types.InlineKeyboardButton(text="📱Ссылки для скачивания")
itembtn2 = types.InlineKeyboardButton(text="📃Отзывы")
itembtn3 = types.InlineKeyboardButton(text="❓Ответы на вопросы")
itembtn4 = types.InlineKeyboardButton(text="🧮Калькулятор стоимости")
itembtn5 = types.InlineKeyboardButton(text="📦Инфо по доставке")
itembtn6 = types.InlineKeyboardButton(text="🧩Как пользоваться приложениями")
itembtn7 = types.InlineKeyboardButton(text="💬Связаться с нами")

markup.row(itembtn7)
markup.row(itembtn2, itembtn4)
markup.row(itembtn1, itembtn6)
markup.row(itembtn3, itembtn5)