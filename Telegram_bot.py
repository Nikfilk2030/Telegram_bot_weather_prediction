import telebot
from telebot import types
import keys
import pandas as pd
import datetime
from Weather_getter import Get_weather
import time

# Creating ID - coordinates connection
id_to_coordinates = {}

# Taken bot token from keys.py
token = keys.bot_token

# Init bot
bot = telebot.TeleBot(token)

# Buttons description
button_text1 = 'Predict weather'
button_text2 = 'Get a dog meme'
button_text3 = 'Reboot bot'
button_text4 = 'Now'
button_text5 = 'In the next hour'
button_text6 = 'Tomorrow'

# Dictionary with simple command -> answer description
messages_and_answers = {"Tell me a joke": "When I see lovers' names carved in"
                                          " a tree, I don't think it's sweet. I"
                                          " just think it's surprising how many"
                                          " people bring a knife on a date.",
                        "Hello": "Hello",
                        "What can you do?": "How much are you ready to pay?"}


@bot.message_handler(commands=['start'])
def greetings(message):
    bot.send_message(message.chat.id, "Hello! Thanks for using me!")
    button_maker(message)


def button_maker(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton(button_text1)
    button2 = types.KeyboardButton(button_text2)
    button3 = types.KeyboardButton(button_text3)
    markup.add(button3, button2)
    markup.add(button1)
    # Starting words:
    bot.send_message(message.chat.id, 'Please, choose a button', reply_markup=markup)


def second_button_keyboard(message):  # To change main menu to "hours" menu
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button3 = types.KeyboardButton(button_text3)
    button4 = types.KeyboardButton(button_text4)
    button5 = types.KeyboardButton(button_text5)
    button6 = types.KeyboardButton(button_text6)
    markup.add(button3, button4)
    markup.add(button5, button6)
    bot.send_message(message.chat.id, 'Please, choose time:', reply_markup=markup)


@bot.message_handler(content_types='text')
def message_reply(message):
    global id_to_coordinates

    if message.text in messages_and_answers:  # Answering on simple things
        bot.send_message(message.chat.id, messages_and_answers[message.text])

    elif message.text == button_text1:  # Predict weather
        bot.send_message(message.chat.id, "Send your geolocation, you have to use this button:")
        geoposition_instruction_photo = open('Bot_pictures/geoposition.jpg', 'rb')
        bot.send_photo(message.chat.id, geoposition_instruction_photo)

    elif message.text == button_text2:  # Get a meme
        dog_meme_photo = open('Bot_pictures/dog_meme.jpg', 'rb')
        bot.send_message(message.chat.id, 'Sending a photo...')
        bot.send_photo(message.chat.id, dog_meme_photo)

    elif message.text == button_text3:  # Reboots bot
        button_maker(message)

    elif message.text == button_text4:  # Weather now
        bot.send_message(message.chat.id, 'Sending the current weather...')
        lat, lng = id_to_coordinates[message.chat.id][1], id_to_coordinates[message.chat.id][0]
        unpacked_dataframe = Get_weather.unpack_df(Get_weather.get_current_weather(lat, lng), 0)
        for criteria in unpacked_dataframe:
            bot.send_message(message.chat.id, f'{criteria[0]}: {criteria[1]}')

    elif message.text == button_text5:  # Weather in 1 hour
        bot.send_message(message.chat.id, f"Sending the weather\n"
                                          f"at {(datetime.datetime.now() + datetime.timedelta(hours=1)).hour}"
                                          f" O'Clock...")
        lat, lng = id_to_coordinates[message.chat.id][1], id_to_coordinates[message.chat.id][0]
        unpacked_dataframe = Get_weather.unpack_df(Get_weather.get_three_days_weather(lat, lng), 1)
        for criteria in unpacked_dataframe:
            bot.send_message(message.chat.id, f'{criteria[0]}: {criteria[1]}')

    elif message.text == button_text6:  # Weather tomorrow at the same time
        bot.send_message(message.chat.id, f"Sending the weather\n"
                                          f"{(datetime.datetime.now() + datetime.timedelta(days=1)).date()} at\n"
                                          f"{(datetime.datetime.now() + datetime.timedelta(days=1)).hour} O'Clock...")
        lat, lng = id_to_coordinates[message.chat.id][1], id_to_coordinates[message.chat.id][0]
        unpacked_dataframe = Get_weather.unpack_df(Get_weather.get_three_days_weather(lat, lng), 24)
        for criteria in unpacked_dataframe:
            bot.send_message(message.chat.id, f'{criteria[0]}: {criteria[1]}')

    else:
        bot.send_message(message.chat.id, "Sorry, i can't understand this command yet")


@bot.message_handler(content_types='location')
def geolocation_reply(message):
    global id_to_coordinates
    lng, lat = message.location.longitude, message.location.latitude
    id_to_coordinates[message.chat.id] = [lng, lat]
    print(id_to_coordinates)

    bot.send_message(message.chat.id, f'Your location:is: {Get_weather.get_location(lat, lng)}')

    second_button_keyboard(message)  # Creating new keyboard


bot.infinity_polling()
