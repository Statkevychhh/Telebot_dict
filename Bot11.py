import telebot
import requests
import json

token = '6665487964:AAGISSVQs66PJOBKM-2XliL_ZhzB__f7QAY'
bot = telebot.TeleBot(token)

answer = requests.get('http://numbersapi.com/#100')

print(answer.status_code)
print(answer.url)
print(answer.text)


@bot.message_handler(regexp='[0-9]+')
def start(message):
    answer = requests.get(f'http://numbersapi.com/{message.text}?json')
    bot.send_message(message.chat.id, json.loads(answer.text)['text'])


bot.polling()