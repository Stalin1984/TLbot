from Data import token
import telebot
from datetime import datetime
import random


while True:
    
    try:

        tk = token

        tb = telebot.TeleBot(tk)

        memes = [
            'https://vk.com/photo6630825_305221390',
            'https://vk.com/photo6630825_305221418',
            'https://vk.com/photo6630825_305221409',
            'https://vk.com/photo6630825_305221491',
            'https://vk.com/photo6630825_319710575',
            'https://vk.com/photo6630825_319710589'
        ]

        replies_time = ['скажи, а сколько времени?','скажи а сколько времени?',
                        'сколько времени?','скок времени?', 'который час?']

        @tb.message_handler(commands=['start','help','myid'])
        def comands(message):

            if message.text == '/start':
                tb.send_message(message.chat.id, 'Привет, '+ str(message.from_user.first_name) + " " + str(message.from_user.last_name) + "!")
            if message.text == '/myid':
                tb.send_message(message.chat.id, "Твой id: " + str(message.from_user.username))
            elif message.text == '/help':

                tb.send_message(message.chat.id,
                "В чем проблема, дружище?\n"
                "Вот список доступных команд:\n"
                "Чтобы узнать время:\n"
                "    Который час?\n"
                "    Cкок времени?\n"
                "    Cкажи, а сколько времени?\n"
                "    Cколько времени?\n"
                "Чтобы получить мемчик:\n"
                "    Cкинь прикол\n"
                "    Cкинь мемчик\n"
                "Чтобы сделать правильный выбор:\n"
                "    За кого мне голосовать?\n"
                "    Путин или обама?")
            else:
                pass

        @tb.message_handler(func=lambda m: True)
        def replies_to(message):

            if message.text[0] == '/':
                tb.send_message(message.chat.id, 'Вы ввели несуществующую команду.')

            elif message.text.lower() in replies_time:

                tm = datetime.now()
                current_time = tm.strftime("%H:%M:%S")
                tb.send_message(message.chat.id, str(current_time))

            elif message.text.lower() in ['за кого мне голосовать?', 'путин или обама?']:

                photo = 'https://ic.pics.livejournal.com/tipolog/9755416/989595/989595_original.jpg'
                tb.reply_to(message, 'Не знаю как вы, а я на выборы никогда не ходил, но в этот раз буду головать за Ивана.')
                tb.send_message(message.chat.id, 'Ивана в президенты!!!')
                tb.send_photo(message.chat.id, photo)

            elif message.text.lower() in ['скинь прикол', 'скинь мемчик']:

                mem = random.choice(memes)
                tb.send_photo(message.chat.id, mem)

            else:

                tb.send_message(message.chat.id,

                'Я вас не понял.'
                'Возможно вы допустили ошибку в слове,'
                'или такой команду еще не существет'

            )
                
        tb.polling(none_stop=True)
        
    except Exception as e:
        
        time.sleep(1)
        print(e)
