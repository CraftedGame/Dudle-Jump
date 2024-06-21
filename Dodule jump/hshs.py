import telebot
from telebot.types import Message
from random import shuffle
cq = 0
bot = telebot.TeleBot('7376695289:AAHrph456LH8qq8s_Q1cHDd4UscYAC5mq8A')
coins = 100
questerions = [ 
    '123?',
    '12?',
    '1?',
]
answers = [
    ['1','12','123'],
    ['12','1','123'],
    ['123','12','1'],
]

@bot.message_handler(commands=['start'])
def process_start_command(message):
    bot.send_message(message.from_user.id, f'Это викторина!\n Ваше кол-во монет: {coins}')
    ac = answers[cq].copy()
    shuffle(ac)
    msg = questerions[cq] + '\n' + '\n'.join(ac)
    bot.send_message(message.from_user.id, 'Сейчас будет первый вопрос: ' + msg)

@bot.message_handler(content_types=['text'])
def process_messages(message: Message):
    global cq
    text = message.text.lower()
    if text == answers[cq][0]:
        coins += 50
        bot.send_message(message.from_user.id, f'Это правильный ответ!\n Ваше кол-во монет: {coins}')
    else:
        coins -= 25
        bot.send_message(message.from_user.id, f'Это неправильный ответ\n Ваше кол-во монет: {coins}')
    if cq == len(questerions):
        cq = 0
        msg = 'Викторина закончилась'
    else:
        cq += 1
        ac = answers[cq].copy()
        shuffle(ac)
        msg = questerions[cq] + '\n' + '\n'.join(ac)
    bot.send_message(message.from_user.id, msg)

bot.polling(none_stop=True, interval = 0)
