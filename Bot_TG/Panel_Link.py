from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
itembtn1 = types.InlineKeyboardButton("IOS")
itembtn2 = types.InlineKeyboardButton("Android")
itembtn3 = types.InlineKeyboardButton("Вернуться в главное меню")
markup.row(itembtn1, itembtn2)
markup.row(itembtn3)