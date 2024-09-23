from telebot import types

markup = types.InlineKeyboardMarkup()
link1 = types.InlineKeyboardButton("Ссылка на скачивание Poizon", url = 'https://m.anxinapk.com/rj/12201303.html')
link2 = types.InlineKeyboardButton("Ссылка на скачивание TaoBao", url = 'https://play.google.com/store/apps/details?id=com.taobao.taobao')
link3 = types.InlineKeyboardButton("Ссылка на скачивание 1688",   url = 'https://www.anxinapk.com/rj/2904.html')
markup.row(link1)
markup.row(link2)
markup.row(link3)