import telebot

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands='start')
def start(message):
    photo = bot.get_user_profile_photos(message.chat.id)
    bot.send_photo(message.chat.id, photo.photos[0][0].file_id)


@bot.message_handler(content_types=['sticker', 'photo'])
def start2(message):
    bot.forward_message(chat_id='',
                        from_chat_id=message.chat.id,
                        message_id=message.id)


@bot.message_handler(commands='start3')
def start3(message):
    bot.copy_message(chat_id='',
                        from_chat_id=message.chat.id,
                        message_id=message.id)


bot.polling()