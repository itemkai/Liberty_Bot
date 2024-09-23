from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
itembtn1 = types.InlineKeyboardButton("Poizon")
itembtn2 = types.InlineKeyboardButton("TaoBao")
itembtn3 = types.InlineKeyboardButton("Вернуться в главное меню")
markup.add(itembtn1, itembtn2)
markup.add(itembtn3)