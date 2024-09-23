from telebot import types

markup = types.InlineKeyboardMarkup()
link1 = types.InlineKeyboardButton("Ссылка на скачивание Poizon", url = 'https://apps.apple.com/ru/app/得物-得到运动x潮流x好物/id1012871328')
link2 = types.InlineKeyboardButton("Ссылка на скачивание TaoBao", url = 'https://apps.apple.com/ru/app/淘宝-春节不打烊/id387682726')
link3 = types.InlineKeyboardButton("Ссылка на скачивание 1688",   url = 'https://apps.apple.com/ru/app/阿里巴巴-1688-货源批发采购进货市场/id507097717')
markup.row(link1)
markup.row(link2)
markup.row(link3)