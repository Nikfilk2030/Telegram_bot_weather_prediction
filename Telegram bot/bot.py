import telebot
from telebot import types
import keys

token = keys.bot_token

bot = telebot.TeleBot(token)

# buttons description
button_text1 = 'Predict weather'
button_text2 = 'Get the Gosling meme'

# dictionary with simple command -> answer description
messages_and_answers = {button_text1: "Send your geolocation:",
                        "Tell me a joke": "When I see lovers' names carved in"
                                          " a tree, I don't think it's sweet. I"
                                          " just think it's surprising how many"
                                          " people bring a knife on a date."}


@bot.message_handler(commands=['start'])
def button_message(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1 = types.KeyboardButton(button_text1)
    item2 = types.KeyboardButton(button_text2)
    markup.add(item1, item2)

    bot.send_message(message.chat.id, 'Choose a button:', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text in messages_and_answers:
        bot.send_message(message.chat.id, messages_and_answers[message.text])
    elif message.text == button_text2:
        photo = open('Gosling.jpg', 'rb')
        bot.send_message(message.chat.id, 'Sending a photo:')
        bot.send_photo(message.chat.id, photo)
    else:
        bot.send_message(message.chat.id, "Sorry, i can't understand this command yet")


@bot.message_handler(content_types='location')
def message_reply(message):
    print(message)
    lng = message.location.longitude
    lat = message.location.latitude
    bot.send_message(message.chat.id, f'Your location: longitude {message.location.longitude},'
                                      f' latitude {message.location.latitude}')


bot.infinity_polling()
