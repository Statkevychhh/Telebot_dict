import telebot

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start'])
def start(message):
    with open('chatids.txt', 'a+') as chatids:
        print(message.chat.id, file=chatids)
    
@bot.message_handler(commands=['start2'])
def start2(message):
    readed = []
    if message.chat.id == 895617317:
        for i in open('chatids.txt', 'r').readlines():
            if not i in readed:
                bot.send_message(i, 'This is spam!')
                readed.append(i)
            else:
                pass


bot.polling()