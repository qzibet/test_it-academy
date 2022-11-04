import random
import telebot


TOKEN = '5661004235:AAF6GcTkjtSR5NRpGPQxtyZ-D72Dtz7XSjA'

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, 'Привет мир!')


@bot.message_handler(func=lambda message: True)
def echo(message):

    if message.text:
        bot.send_message(message.chat.id, f'Ответ: {eval(message.text)}')
    else:
        bot.reply_to(message, message.text)


bot.polling()






# @bot.message_handler(func=lambda message: True)
# def game(message):
#     ...

