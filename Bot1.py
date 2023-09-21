import telebot

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)


@bot.message_handler(regexp=r'funny jpeg', func= lambda message: True)  #text
def sending(message):
    bot.send_message(message.chat.id, 'This is logic "AND" .')

@bot.message_handler(regexp=r'Sam')
@bot.message_handler(regexp=r'Jane')
def sending(message):
    bot.send_message(message.chat.id, 'This is logic "OR" .')



@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f"Hello {message.from_user.first_name}!")

@bot.message_handler(regexp=r'funny gp')
def sending(message):
    bot.send_message(message.chat.id, 'Yes, broo!')

@bot.message_handler(func = lambda message: True)
def replying(message):
    bot.reply_to(message, message.chat.id)
    
@bot.message_handler(chat_types=['private'])
def sending(message):
    bot.reply_to(message.chat.type, message.chat.id)
    
@bot.message_handler(content_types=['photo','video'])  #text
def sending(message):
    bot.send_message(message.chat.id, 'This is not text!')

bot.infinity_polling()