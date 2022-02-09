# Создаём телеграмм ботов:
# 1. Эхо бот
import telebot
bot = telebot.TeleBot("5118172810:AAFohxL0hOr-MqOmvhIGpsNmB4mllXBXGtQ") # Создаем экземпляр бота
@bot.message_handler(commands=["start"]) # Функция, обрабатывающая команду /start
def start(m, res=False):
    bot.send_message(m.chat.id, 'привет серый)')
@bot.message_handler(content_types=["text"]) # Получение сообщений от юзера
def handle_text(message):
    bot.send_message(message.chat.id, 'Вы написали: ' + message.text)
bot.polling(none_stop=True, interval=0) # Запускаем бота.