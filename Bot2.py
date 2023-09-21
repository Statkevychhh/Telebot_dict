import telebot

token = '6509403956:AAFDgQss1pWb6F-PTv6a_M3eZiqzDp5nKzE'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Hi. I am your new TG-bot.')


@bot.message_handler(commands=['photo', 'photos'])
def send_photo(message):
    file = open('photo234.jpg', 'rb')
    bot.send_photo(message.chat.id, file, 'This is my photo!')
    file.close()
    
@bot.message_handler(commands=['video', 'videos'])
def send_video(message):
    file2 = open('video232.3gp', 'rb')
    bot.send_video(message.chat.id, file2)
    file2.close()

@bot.message_handler(commands=['link'])
def send_link_photo(message):
    bot.send_photo(message.chat.id, r'link')
    
    
@bot.message_handler(commands=['HTML', 'html'])
def HTML(message):
    bot.send_message(message.chat.id, r'Hi. <b>I am your new</b>  <b><i>TG-bot</i></b>.', parse_mode='HTML')

@bot.message_handler(commands=['HTML2', 'html2'])
def Markdown(message):
    bot.send_message(message.chat.id, r'*Hi.* I am your new *_TG-bot_.*', parse_mode='Markdown')


@bot.message_handler(commands='delete')
def delete(message):
    message1 = bot.send_message(message.chat.id, message.id)
    bot.delete_message(message.chat.id, message.id)
    
@bot.message_handler(commands='delete2')
def delete2(message):
    bot.delete_message(message.chat.id, message.id)


@bot.message_handler(commands='edit')
def edit(message):
    message1 = bot.send_message(message.chat.id, '1')
    bot.edit_message_text(chat_id=message.chat.id, message_id=message1, text = '2')


bot.infinity_polling()