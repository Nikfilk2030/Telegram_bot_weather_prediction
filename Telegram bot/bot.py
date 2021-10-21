import telebot
from telebot import types
from time import sleep

token = '2065553085:AAEbFGvC6uxJxfO2j7bqKVNG_WyCwUGKRsM'

bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton("Предсказать погоду")
    item2 = types.KeyboardButton('Получить мем с кошечкой')
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Выберите что вам надо', reply_markup=markup)


# @bot.message_handler(content_types='text')
# def message_reply(message):
#     bot.send_message(message.chat.id, 'Пришлите свою геопозицию')


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text == 'Предсказать погоду':
        bot.send_message(message.chat.id, 'Пришлите свою геопозицию:')
    else:
        photo = open('Gosling.jpg', 'rb')
        bot.send_message(message.chat.id, 'Присылаю фото:')
        bot.send_photo(message.chat.id, photo)


@bot.message_handler(content_types='location')
def message_reply(message):
    print(message)
    print('longitude', message.location.longitude)
    print('latitude', message.location.latitude)
    bot.send_message(message.chat.id, f'Ваша локация: longitude {message.location.longitude},'
                                      f' latitude {message.location.latitude}')


bot.infinity_polling()
