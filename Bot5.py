import telebot
from telebot import util

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands='split')
def split(message):
    text = open('text65.txt', encoding='utf8')
    for x in util.split_string(text, 200):
        bot.send_message(message.chat.id, x)
    
    
@bot.message_handler(commands='split2')
def split2(message):
    text = open('text65.txt', encoding='utf8')
    for y in util.smart_split(text, 200):
        bot.send_message(message.chat.id, y)
        
bot.infinity_polling()