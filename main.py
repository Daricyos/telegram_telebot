# -*- coding: utf-8 -*-
import telebot, config, kb, lg
from telebot import types
import sqlite3
from requests import get


bot = telebot.TeleBot(config.token)


class User:
    def __init__(self):
        connect = sqlite3.connect('users.db')
        cursor = connect.cursor()

        cursor.execute("""CREATE TABLE IF NOT EXISTS login_id(
            userid INTEGER
            city TEXT
        )""")

    connect.commit()


user_list = []


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, lg.st + message.from_user.first_name + lg.st2, reply_markup = kb.ikb)
    


@bot.message_handler(content_types = ['text'])
def keyboard(message):
    if message.text == lg.btn4:
        markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
        itembtn1 = types.KeyboardButton('Киев')
        itembtn2 = types.KeyboardButton('Главное меню⚡')
        markup.add(itembtn1, itembtn2)

        msg = bot.send_message(message.chat.id, '*Ваш город?*', reply_markup=markup, parse_mode="Markdown")
        bot.register_next_step_handler(msg, process_city_step)

def process_city_step(message):
    chat_id = message.chat.id



if __name__ == '__main__':
    bot.polling(none_stop = True)