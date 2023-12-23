import telebot


token = '6761072442:AAHxV96Ryj7DYckZKbjSyRjctXshlYQjwTY'

bot=telebot.TeleBot(token)

def say_goodbye(message):
    passwords = ['пока', 'прощай', 'до свидания', 'до скорых встреч']
    text_mes = message.text.lower()
    for i in passwords:
        if i in text_mes:
            return True

@bot.message_handler(content_types=['text'], func = say_goodbye)
def say_hello(message):
    bot.send_message(message.chat.id, f"Прощайте, <b>{message.from_user.first_name}</b>.", parse_mode='html')

@bot.message_handler(commands=['start'])
def start(message):
    hello_mess = (f'Приветcтвую, <b>{message.from_user.first_name}</b>.\n'
                  f'Чтобы узнать о моих возможностях нажмите /help')
    bot.send_message(message.chat.id, hello_mess, parse_mode='html')


@bot.message_handler(commands=['help'])
def help(message):
    help_mess = ('Я <b>Шерлок Бот</b> и вот мои функции:\n'
                 '- Я могу здароваться по команде /start.\n'
                 '- Я могу прощаться.\n'
                 '- Я могу отвечать на текст, фото, аудио.\n'
                 '- /description - по команде получите моё описание.')
    bot.send_message(message.chat.id, help_mess, parse_mode='html')

@bot.message_handler(commands=['description'])
def description(message):
    bot.send_message(message.chat.id, 'Имя: <b>Шерлок</b>\n'
                                      'Возраст: <b>30 лет</b>\n'
                                      'Профессия: <b>Детектив-консультант</b>\n'
                                      
                                      'Описание: <b>Я спортивен, является хорошим боксёром, отличное владею револьвером, шпагой и даже хлыстом. '
                                      'Я хорошо играю на скрипке, обладаю достаточно глубокими знаниями из разных научных областей. '
                                      'У меня превосходная память, я крайне наблюдателен и большинство преступлений я расследую при помощи логических размышлений и метода дедукции.</b>', parse_mode='html')


@bot.message_handler(content_types=['photo'])
def answer_photo(message):
    bot.send_message(message.chat.id, 'Интересное фото... Сделано мастером своего дела.')

@bot.message_handler(content_types=['voice'])
def answer_audio(message):
    bot.send_message(message.chat.id, 'Ваш голос прелестен...')

@bot.message_handler(commands=['photo']) # немного не понял как реализовать отправку фото через инет
def photo(message):
    photo = open('https://disk.yandex.ru/i/vt_tziBA1slS-Q')
    bot.send_photo(message.chat.id, photo)




@bot.message_handler()
def if_random_text(message):
    bot.send_message(message.chat.id, 'Мне с вами скучно')

bot.polling(non_stop=True)