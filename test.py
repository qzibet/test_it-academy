import telebot

from parser_mashin import parse_mashina


TOKEN = '5708136884:AAGSapOgop0XW_nqfztiTN9CCOofzjSgrg8'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def bot_starting(message):
    bot.reply_to(message, 'Привет мир!😊')
    bot.send_message(message.chat.id, 'Введите логин от инсты(пример: login = q_zi_bet)')

@bot.message_handler(content_types=['text'])
def check_message(message):
    user = message.from_user
    print(f'Пользователь {user.first_name} id:{user.id}')
    print(f'Сообщение: {message.text}')
    if message.text == 'хочу машину':
        cars = parse_mashina()
        for car in cars:
            text = f'{car.get("car_name")} \n{car.get("car_price")} \n{car.get("car_views")}'
            bot.send_message(message.chat.id, text)

bot.infinity_polling()
