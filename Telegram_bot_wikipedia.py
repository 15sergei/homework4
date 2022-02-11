# # 2. Wikipedia бот
import telebot
import wikipedia,re
from telebot import TeleBot
bot = telebot.TeleBot('5118172810:AAFohxL0hOr-MqOmvhIGpsNmB4mllXBXGtQ') # Создаем экземпляр бота
wikipedia.set_lang("ru") # Устанавливаем русский язык в Wikipedia
def getwiki(s): # Чистим текст статьи в Wikipedia и ограничиваем его тысячей символов
    try:
        ny = wikipedia.page(s)
        wikitext = ny.content[:1000]    # Получаем первую тысячу символов
        wikimas = wikitext.split('.')   # Разделяем по точкам
        wikimas = wikimas[:-1]  # Отбрасываем всЕ после последней точки
        wikitext2 = ''  # Создаем пустую переменную для текста
        for x in wikimas: # Проходимся по строкам, где нет знаков «равно» # (то есть все, кроме заголовков)
            if not ('==' in x):
                if (len((x.strip())) > 3):
                    wikitext2 = wikitext2 + x + '.'
            else:
                break
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\([^()]*\)', '', wikitext2)
        wikitext2 = re.sub('\{[^\{\}]*\}', '', wikitext2)
        return wikitext2
    except Exception as e:
        return 'В энциклопедии нет информации об этом'

@bot.message_handler(commands=["start"])
def start(m, res=False):
    bot.send_message(m.chat.id, 'Отправьте мне любое слово, и я найду его значение на Wikipedia')
    @bot.message_handler(content_types=["text"])
    def handle_text(message):
        bot.send_message(message.chat.id, getwiki(message.text))
bot.polling(none_stop=True, interval=0)
