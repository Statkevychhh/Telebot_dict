import telebot
from telebot import types

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands='start')
def start(message):
    sent = bot.reply_to(message, 'Будь ласка, добавте сюди якийсь текст.')
    bot.register_next_step_handler(sent, review)
    
def review(message):
    message_to_save = f'{message.text}'
    with open('text65.txt', 'a') as txt:
        txt.write(message_to_save)
    
    
@bot.message_handler(commands='start2')
def keyboard2(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Кнопка 1')
    btn2 = types.KeyboardButton('Кнопка 2')
    btn3 = types.KeyboardButton('Кнопка 3')
    btn4 = types.KeyboardButton('Кнопка 4')
    kb.add(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Make a choose!', reply_markup=kb)
    
    
@bot.message_handler(commands='start3')
def keyboard3(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Кнопка 1')
    btn2 = types.KeyboardButton('Кнопка 2')
    btn3 = types.KeyboardButton('Кнопка 3')
    btn4 = types.KeyboardButton('Кнопка 4')
    kb.add(btn1, btn2)
    kb.add(btn3, btn4)
    bot.send_message(message.chat.id, 'Make a choose!' ,reply_markup=kb)
    

@bot.message_handler(commands='start4')
def keyboard4(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)  #max row_width = 12 btns
    btn1 = types.KeyboardButton('Кнопка 1')
    btn2 = types.KeyboardButton('Кнопка 2')
    btn3 = types.KeyboardButton('Кнопка 3')
    btn4 = types.KeyboardButton('Кнопка 4')
    kb.row(btn1, btn2, btn3, btn4)
    bot.send_message(message.chat.id, 'Make a choose!' ,reply_markup=kb)
    

@bot.message_handler(commands='start5')
def keyboard5(message):
    kb = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=3)
    btn1 = types.KeyboardButton('Кнопка 1', request_contact=True)
    btn2 = types.KeyboardButton('Кнопка 2', request_location=True)
    kb.add(btn1, btn2)
    bot.send_message(message.chat.id, 'Make a choose!', reply_markup=kb)
    
@bot.message_handler(content_types=['contact'])
def chedk_contact(message):
    if message.contact.user_id == message.from_user.id:
        bot.send_message(message.chat.id, f'Телефон вірний: {message.contact.phone_number}')
    else:
        bot.send_message(message.chat.id, 'Ви вказали не свій номер телефону!')


@bot.message_handler(content_types=['location'])
def check_location(message):
    bot.send_message(message.chat.id, message.location)


bot.polling()