import telebot
import requests

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message('@hhhgggyyyttt', '1')
    
@bot.message_handler(commands=['start2'])
def start2(message):
    requests.get('https://api.telegram.org//')


bot.infinity_polling()