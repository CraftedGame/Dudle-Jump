import telebot
from telebot.types import Message
bot = telebot.TeleBot('7376695289:AAHrph456LH8qq8s_Q1cHDd4UscYAC5mq8A')
words = ['кошка',
'собака',
'свинья',
'корова',
'хомяк',
'кролик',
'крокодил',
'лев',
'баран']
clue = []
sw = None
lives = 9
bot.polling(none_stop=True, interval = 0)