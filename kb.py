# -*- coding: utf-8 -*-
import telebot, lg
from telebot import types


tikm = types.InlineKeyboardMarkup
trkm = types.ReplyKeyboardMarkup
tikb = types.InlineKeyboardButton

#Start button
ikb = tikm()
ltn1 = tikb(text = 'Заказать воду', callback_data= 'voda')
ltn2 = tikb(text = 'О нас', callback_data= 'kompany')
ltn3 = tikb(text = 'Акции', callback_data= 'promotions')
ltn4 = tikb(text = 'Контакты', callback_data = 'contacts')
ikb.add(ltn1, ltn2, ltn3, ltn4)