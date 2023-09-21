import telebot
from telebot import types

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands='start')
def start(message):
    kb = types.InlineKeyboardMarkup(row_width=1)  #max row_width = 9 btns
    btn1 = types.InlineKeyboardButton(text='Кнопка1', url='https://www.youtube.com')
    btn2 = types.InlineKeyboardButton(text='Кнопка2', url='https://www.youtube.com')
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, '1', reply_markup=kb)
    

@bot.message_handler(commands='start2')
def start2(message):
    markup = types.InlineKeyboardMarkup()
    switch1 = types.InlineKeyboardButton(text='Чат1', switch_inline_query='This is Chat1 !')
    markup.add(switch1)
    bot.send_message(message.chat.id, '1', reply_markup=markup)
    

@bot.message_handler(commands='start3')
def start3(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    clbk1 = types.InlineKeyboardButton(text='Кнопка1', callback_data='btn1')
    clbk2 = types.InlineKeyboardButton(text='Кнопка2', callback_data='btn2')
    kb.add(clbk1, clbk2)
    bot.send_message(message.chat.id, '1', reply_markup=kb)

@bot.callback_query_handler(func=lambda callback: callback.data)
def check_callback_data(callback):
    if callback.data == 'btn1':
        bot.send_message(callback.message.chat.id, 'Ви нажали на першу кнопку!')
    elif callback.data == 'btn2':
        bot.send_message(callback.message.chat.id, 'Ви нажали на другу кнопку!')


@bot.message_handler(commands='start4')
def start4(message):
    kb = types.InlineKeyboardMarkup(row_width=1)
    url = types.InlineKeyboardButton(text='Url', url='https://www.youtube.com')
    switch = types.InlineKeyboardButton(text='Switch', switch_inline_query='Swich')
    callback = types.InlineKeyboardButton(text='Callback', callback_data='Button7')
    kb.add(url, switch, callback)
    bot.send_message(message.chat.id, 'Вибери кнопку!', reply_markup=kb)


bot.infinity_polling()