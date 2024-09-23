from telebot import types

markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
itembtn1 = types.InlineKeyboardButton("Добавить еще один товар в заказ")
itembtn2 = types.InlineKeyboardButton("Закончить и связаться с админом")

markup.row(itembtn1)
markup.row(itembtn2)