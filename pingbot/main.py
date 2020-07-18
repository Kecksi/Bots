#!/usr/bin/env python3
import logging
import os
import telebot

with open(os.path.join(os.path.dirname(__file__), '.config'), 'r') as token_path:
    token = token_path.read().strip()

bot = telebot.TeleBot(token)
logger = telebot.logger
telebot.logger.setLevel(logging.INFO)


@bot.message_handler(commands=['test'])
def test(message):
    bot.reply_to(message, 'Zdarova')
    
bot.infinity_polling()
