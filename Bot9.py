import telebot

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)

@bot.edited_message_handler(func=lambda message: True)
def send_message(message):
    bot.send_message(message.chat.id, 'Hello!')



@bot.message_handler(commands=['start'])
def start(message):
    bot.send_dice(message.chat.id, 1)


bot.polling()