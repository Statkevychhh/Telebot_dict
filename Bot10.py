import telebot
from telebot import types

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_location(message.chat.id, 49.229298, 28.420358)
    

@bot.message_handler(commands=['start2'])
def start2(message):
    bot.send_contact(message.chat.id, phone_number=380686227495, first_name='Artur', last_name='Statkevych')


@bot.message_handler(commands=['start3'])
def start3(message):
    bot.send_poll(message.chat.id, question='Do you like me?',
                  options=['yes', 'No', 'Maybe'],
                  allows_multiple_answers=False,
                  is_anonymous=False)


bot.infinity_polling()