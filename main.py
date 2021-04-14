# -*- coding: utf-8 -*-
import telebot, config, kb, lg
from telebot import types
from requests import get


bot = telebot.TeleBot(config.token)

@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, lg.st + message.from_user.first_name + lg.st2, reply_markup = kb.ikb)





if __name__ == '__main__':
    bot.polling(none_stop = True)