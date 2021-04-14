# -*- coding: utf-8 -*-
import telebot, lg
from telebot import types


tikm = types.InlineKeyboardMarkup
tikb = types.InlineKeyboardButton
trkm = types.ReplyKeyboardMarkup
trkb = types.KeyboardButton

#Start button
ikb = trkm(one_time_keyboard=True, resize_keyboard=True, row_width=2)
ltn1 = trkb(lg.btn1)
ltn2 = trkb(lg.btn2)
ltn3 = trkb(lg.btn3)
ltn4 = trkb(lg.btn4)
ikb.add(ltn1, ltn2, ltn3, ltn4)