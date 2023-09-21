import time
import telebot
from telebot import types


token = '5948101084:AAED3bBraGn07ssANxtZ7TIaeBVGCHQ_H2Y'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
    kb = types.ReplyKeyboardMarkup(row_width=3)
    button1 = types.KeyboardButton(text='💖')
    button2 = types.KeyboardButton(text='💕')
    button3 = types.KeyboardButton(text='💗')
    button4 = types.KeyboardButton(text='💙')
    button5 = types.KeyboardButton(text='💛')
    button6 = types.KeyboardButton(text='🤍')
    button7 = types.KeyboardButton(text='💘')
    button8 = types.KeyboardButton(text='❣️')
    button9 = types.KeyboardButton(text='❤‍🔥')
    button10 = types.KeyboardButton(text='❤‍🩹')
    kb.add(button1, button2, button3, button4, button5, button6, button7, button8, button9, button10)
    bot.send_message(message.chat.id, 'Привіт, Заюшка😘. Проклацай по порядку всі кнопочки нижче!', reply_markup=kb)

@bot.message_handler(regexp='💖')
def reply1(message):
    file = open('photo_love.jpg', 'rb')
    bot.send_photo(message.chat.id, file, 'Наше перше фото разом)) ')
    file.close()
    time.sleep(1)
    bot.send_message(message.chat.id, 'Так тоді стіснявся☺❤   Ще пам\'ятаю як приобняв тебе за талію, коли ми фоткались, а ти сказала :"Ого" і дуже здивувалась. Як мені тоді ніяково стало. Дуже тоді переймався тим, що ти подумаєш про мене🥺🥺🥺.  Но саме в той момент я зрозумів що люблю тебе і почав діяти, і не пожалів бо почав відносини з найкращою дівчиною в моєму житті)😉😘 ') 

@bot.message_handler(regexp='💕')
def reply2(message):
    file = open('photo_love2.jpg', 'rb')
    bot.send_photo(message.chat.id, file, 'Наше перше фото з цьомчиком😍👄.')
    file.close()
    time.sleep(3)
    bot.send_message(message.chat.id, '''Звичайно він не такий, як перший на цьомчик, зате дуже милий☺🥰. Доречі за перший, пам'ятаю як ми тоді стояли холодні на вулиці, а ти почала за зірки💫, блін як я тоді занєрвнічав, думаю йолки-палки, це ж вона хоче шоб я її поцілував, а я не вмію😂. І я такий рішаюсь вже, думаюладно, треба діяти. Тільки зібрався, підходю а тут ти крутишся в сторони😂. Я думаю, йолки-палки, то хоче вона, чи не хоче🤨. Но потім все-таки ти обернулась, теж рішилась і все склалось😻🥰. 
Я тоді на другий день дуже переживав чи сподобаються тобі рози, і не прогадав😎. 
Помню ще наш другий цьомчик🤩, то було щось з чимось, канєшно не такий як перший, но теж непогано. Ми тоді вже не так встидались один одного( і помню навіть цілував вже тебе тоді на стадіоні в твою ніжну щічку🤗). В нас тоді не зовсім вийшло, але я такий кажу : "Фігня. Давай ще раз? ", а ти така: "Давай!"  І я тоді розцвів😊😊, поняв що ти готова зі мною на все, бо так зразу согласитись на ще один цьом - це важко(Ps: в нас тоді вийшло покраще). Я ще тоді бачу що ти вроді цілується норм, а я не особо, і такий трошки запереживав😕, думаю блін треба шось думати, вдруг їй не сподобається. І такий кажу : "Опиту маловато, треба вчитись", а ти така: "Ну навчимось разом". Тоді я по настоящому зрадів, зрадів так, як ніколи не радів! 🥰''')
   

@bot.message_handler(regexp='💗')
def reply3(message):
    file = open('video_love.mp4', 'rb')
    bot.send_photo(message.chat.id, file, 'Снайперка моя маленька☺☺😘💕')
    file.close()
    
@bot.message_handler(regexp='💙')
def reply4(message):
    with open('photo_love61.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love62.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(1)
    bot.send_message(message.chat.id, 'Навіть в дитинстві була дуже мила😻😻🥰!!!  Люблю тебе💘!')
    
@bot.message_handler(regexp='💛')
def reply5(message):
    file = open('photo_love1.jpg', 'rb')
    bot.send_photo(message.chat.id, file, 'Дві сплюшки😜.  Зато які класнючі☺😺.')
    file.close()

@bot.message_handler(regexp='🤍')
def reply6(message):
    with open('photo_love34.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love33.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love32.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love31.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(1)
    bot.send_message(message.chat.id, 'Так тоді не хотів фоткатись😁, але фоткався😉. Все заради тебе😽. Доречі фото вийшли прикольні😻')

@bot.message_handler(regexp='💘')
def reply7(message):
    with open('photo_love5.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love52.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love53.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file, 'Охрана - Отмєна!😎')
        time.sleep(1)
    bot.send_message(message.chat.id, 'Тоді теж не дуже хотів фоткатись)) Але й ці фотки вийшли прикольні(як і всі фотки де ми разом🤗). Чіпси доречі були смачні, нам обом понравились.')
    
@bot.message_handler(regexp='❣️')
def reply8(message):
    with open('video_love2.mp4', 'rb') as file:
        bot.send_video(message.chat.id, file)
        time.sleep(0.5)
        bot.send_message(message.chat.id, 'Помню ще як тікав колись від тебе, щоб бабуся не побачила).Помню вже 5 ранку, бабуся з дідом має вставати, а ти всеодно мене не пускаєш🥰. Так і до ранку засижувались і нас майже ніколи не ловили☺. Помню ще колись в тісному жигулі разом лежали в обнімку, і слухали музичку. Навіть якогось разу було так, що тато твій спав в гаражі, а жигуль бу біля гаража, і ми собі тихенько в ньому лежали(я ще тоді дверима як гупну😂! Незнаю як твій тато не почув). Та й зараз би це повторив( і при нагоді повторю😉)!')

@bot.message_handler(regexp='❤‍🔥')
def reply9(message):
    with open('photo_love70.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love71.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love72.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love73.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love74.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love75.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love76.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(0.3)
    with open('photo_love77.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file)
        time.sleep(1)
    bot.send_message(message.chat.id, 'Пам\'ятаєш як ми їздили на арку і як ми доказували, один одному свою любов? 🥲(Ти ще тоді кульчик загубила😺). Це було місце яке завжди роздувало наші емоції. 💓💗❤‍🔥')

@bot.message_handler(regexp='❤‍🩹')
def reply10(message):
    with open('photo_love4.jpg', 'rb') as file:
        bot.send_photo(message.chat.id, file, ' Наше найкраще фото🥰🥰😍😍!')
        time.sleep(1)
        bot.send_message(message.chat.id, 'Люблю тебе дуже дуже-предуже сильно!❣️❣️❣️ Просто вибач мене за все погане і повір мені.😔😔  Прошу лиш про одне, хоч це для тебе і важко, но дай мені останній шанс 🥺🥺🙏')
        time.sleep(5)
        bot.send_message(message.chat.id, 'Лиш з тобою я зрозумів що таке по-настоящому любити. До цього я не дуже вірив в любов, але повірив, ти заставила мене повірити. Застав й мене зараз повірити, що одне кохання на все життя існує і це не вигадки. Давай разом докажемо це світу?')
        time.sleep(7.5)
        bot.send_message(message.chat.id, 'Бiгом цілуй поки я відвернувся😝😏!!!')


bot.polling()