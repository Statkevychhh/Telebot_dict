import telebot
from telebot import types

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    button1 = types.KeyboardButton(text='Кнопка1')
    button2 = types.KeyboardButton(text='Кнопка2')
    kb.add(button1, button2)
    bot.send_message(message.chat.id, 'Click, please',
                     reply_markup=kb)
 
    
@bot.message_handler(content_types=['text'])
def get_text(message):
    if message.text == 'Кнопка1':
        bot.send_message(message.chat.id, '11111')
    elif message.text == 'Кнопка2':
        bot.send_message(message.chat.id, '22222')



bot.polling()