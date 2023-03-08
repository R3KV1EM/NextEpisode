import telebot, time, datetime, threading
import schedule
from telebot import types
bot = telebot.TeleBot('6216160010:AAFzelElNZL5nKebCvZ65d58wAMQO86zCbI')
your_chat_id = '@keauxs'


@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🙋‍♂️Начать рабочий день")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋Хорошего дня! Не забудь отметить открытие магазина", reply_markup=markup)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '🙋‍♂️Начать рабочий день':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('🏚️Открыть магазин')
        btn2 = types.KeyboardButton('RESERVED1')
        btn3 = types.KeyboardButton('RESERVED2')
        btn4 = types.KeyboardButton("RESERVED3")
        btn5 = types.KeyboardButton("RESERVED4")
        btn6 = types.KeyboardButton("RESERVED5")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '👑Добро пожаловать в рабочую панель 0.1.0', reply_markup=markup)


    elif message.text == '🏚️Открыть магазин':

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton('🏩пр. Ленина 52А(цоколь)')

        btn2 = types.KeyboardButton('🏠пр. Ленина 41(цоколь)')

        btn3 = types.KeyboardButton('🏙️ул. Дзержинского, 36')

        btn4 = types.KeyboardButton("🔙 Назад")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, 'Выберите магазин:', reply_markup=markup)

    if message.text == '🏩пр. Ленина 52А(цоколь)':
        bot.send_message(message.from_user.id, f"🔑Открытие магазина зарегистрировано в {time.asctime()}")
        opening_times['🏩пр. Ленина 52А(цоколь)'] = datetime.datetime.now()

    if message.text == '🏠пр. Ленина 41(цоколь)':
        bot.send_message(message.from_user.id, f"🔑Открытие магазина зарегистрировано в {time.asctime()}")
        opening_times['🏠пр. Ленина 41(цоколь)'] = datetime.datetime.now()

    if message.text == '🏙️ул. Дзержинского, 36':
        bot.send_message(message.from_user.id, f"🔑Открытие магазина зарегистрировано в {time.asctime()}")
        opening_times['🏙️ул. Дзержинского, 36'] = datetime.datetime.now()

# dictionary to store opening time for each shop
# dictionary to store opening time for each shop
opening_times = {
    '🏩пр. Ленина 52А(цоколь)': None,
    '🏠пр. Ленина 41(цоколь)': None,
    '🏙️ул. Дзержинского, 36': None,
}

# set the opening times for each shop
for shop, opening_time in opening_times.items():
    opening_times[shop] = datetime.datetime.combine(datetime.date.today(), datetime.time(hour=10, minute=0))

def check_opening_times():
    open_shops = []
    closed_shops = []
    now = datetime.datetime.now()
    for shop, opening_time in opening_times.items():
        if opening_time <= now <= opening_time + datetime.timedelta(hours=11):
            open_shops.append(shop)
        else:
            closed_shops.append(shop)
    message = f"Открыты: {', '.join(open_shops)}\nЗакрыты: {', '.join(closed_shops)}"
    bot.send_message(your_chat_id, message)

# set the time to run the report
report_time = datetime.time(hour=2, minute=30)
# set the time to clear the opening times dictionary
clear_time = datetime.time(hour=9, minute=0)

def bot_loop():
    bot.polling(none_stop=True, interval=0)

def check_loop():
    while True:
        now = datetime.datetime.now().time()
        if now >= report_time:
            check_opening_times()
            time.sleep(45)  # sleep for a minute to prevent sending multiple reports
        elif now >= clear_time:
            opening_times.clear()  # clear the opening_times dictionary
        time.sleep(30)  # sleep for 30 seconds before checking again

# start the bot loop thread
bot_thread = threading.Thread(target=bot_loop)
bot_thread.start()

# start the check loop thread
check_thread = threading.Thread(target=check_loop)
check_thread.start()

# wait for both threads to finish (which they never will, so this is just to keep the main thread from exiting)
bot_thread.join()
check_thread.join()
