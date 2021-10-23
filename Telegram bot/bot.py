import telebot
from telebot import types
import keys
import pandas as pd

# taken bot token from keys.py
token = keys.bot_token

# init bot
bot = telebot.TeleBot(token)

# buttons description
button_text1 = 'Predict weather'
button_text2 = 'Get a dog meme'
button_text3 = 'Reboot bot'

# dictionary with simple command -> answer description
messages_and_answers = {"Tell me a joke": "When I see lovers' names carved in"
                                          " a tree, I don't think it's sweet. I"
                                          " just think it's surprising how many"
                                          " people bring a knife on a date.",
                        "Hello": "Hello",
                        "What can you do?": "How much are you ready to pay?"}


@bot.message_handler(commands=['start'])
def button_maker(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(button_text1)
    button2 = types.KeyboardButton(button_text2)
    button3 = types.KeyboardButton(button_text3)
    markup.add(button3, button2)
    markup.add(button1)
    # Starting words:
    bot.send_message(message.chat.id, 'Hello! Choose a button', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    if message.text in messages_and_answers:  # answering on simple things
        bot.send_message(message.chat.id, messages_and_answers[message.text])

    elif message.text == button_text1:
        bot.send_message(message.chat.id, "Send your geolocation, you have to use this button:")
        geoposition_instruction_photo = open('geoposition.jpg', 'rb')
        bot.send_photo(message.chat.id, geoposition_instruction_photo)

    elif message.text == button_text2:
        dog_meme_photo = open('dog_meme.jpg', 'rb')
        bot.send_message(message.chat.id, 'Sending a photo...')
        bot.send_photo(message.chat.id, dog_meme_photo)

    elif message.text == button_text3:
        button_maker(message)

    else:
        bot.send_message(message.chat.id, "Sorry, i can't understand this command yet")


@bot.message_handler(content_types='location')
def geolocation_reply(message):
    lng, lat = message.location.longitude, message.location.latitude

    bot.send_message(message.chat.id, f'Your location:\n'
                                      f'longitude {lng}\n'
                                      f'latitude {lat}')


bot.infinity_polling()
