import telebot

API_TOKEN = '5469376705:AAHCDzSgl4uWGTA56_l9JeprQRMBInS85Zs'

bot = telebot.TeleBot(API_TOKEN)


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


# Handle all other messages with content_type 'text' (content_types defaults to ['text'])
@bot.message_handler(func=lambda message: True)
def echo_message(message):
    if message.text == 'привет':
        bot.send_message(message.chat.id, 'пока')
    elif '+' in message.text:
        lst = message.text.split(' ')
        bot.send_message(message.chat.id, 'пока')
    else:
        bot.reply_to(message, message.text)

bot.polling()
