# БОТ, ВЕДУЩИЙ TELEGRAM-КАНАЛ С АНЕКДОТАМИ
import telebot
import time
bot = telebot.TeleBot('5118172810:AAFohxL0hOr-MqOmvhIGpsNmB4mllXBXGtQ')
# Адрес телеграм-канала, начинается с @
CHANNEL_NAME = '@kanaldlaybota'
# Загружаем список шуток
f = open('data/fun.txt', 'r', encoding='UTF-8')
jokes = f.read().split('\n')
f.close()
# Пока не закончатся шутки, посылаем их в канал
for joke in jokes:
    bot.send_message(CHANNEL_NAME, joke)
    # Делаем паузу в один час
    time.sleep(1)
bot.send_message(CHANNEL_NAME, "Анекдоты закончились :-(")
