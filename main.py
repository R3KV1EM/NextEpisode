import telebot
from telebot import types

bot = telebot.TeleBot('6063475020:AAEXG8fi9UNnfHF6zUMEx_I8hH6oi87qP-g')

@bot.message_handler(commands=['start'])
def start(message):

    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("👋 Привет")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "👋 Привет! Я твой бот-помощник!", reply_markup=markup)

@bot.message_handler(content_types=['text'])
def get_text_messages(message):

    if message.text == '👋 Привет':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True) #создание новых кнопок
        btn1 = types.KeyboardButton('🏚️Адреса магазинов')
        btn2 = types.KeyboardButton('💨 ТОП 5 Одноразок')
        btn3 = types.KeyboardButton('💥Новинки')
        markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, '👨‍🎓 Я знаю все про вейпинг, давай помогу!', reply_markup=markup) #ответ бота




    elif message.text == '🏚️Адреса магазинов':

        # Create a reply keyboard with the list of shops

        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton('🏩пр. Ленина 52А(цоколь)')

        btn2 = types.KeyboardButton('🏠пр. Ленина 41(цоколь)')

        btn3 = types.KeyboardButton('🏙️ул. Дзержинского, 36')

        btn4 = types.KeyboardButton("🔙 Назад")


        markup.add(btn1, btn2, btn3, btn4)

        # Send a message with the list of shops and the reply keyboard

        bot.send_message(message.from_user.id, 'Выберите магазин:', reply_markup=markup)


    # Handle the user's choice of shop

    elif message.text == '🏩пр. Ленина 52А(цоколь)':

        # Send a message with the shop's address

        bot.send_message(message.from_user.id, 'Адрес: пр. Ленина, 52А (Цоколь) \n Время работы 10-22 \n Телефон '
                                               'магазина +79234158111 \nЛегко добраться с помощью \n🗺️Google Maps🗺️ '
                                               '\nhttps://goo.gl/maps/gfQUjK6xpxxYthon7')

        # Send a photo of the entrance for this shop

        with open('/home/archy/Документы/bot source/pochtaentr.png', 'rb') as photo:

            bot.send_photo(message.from_user.id, photo)


    elif message.text == '🏠пр. Ленина 41(цоколь)':

        # Send a message with the shop's address

        bot.send_message(message.from_user.id, 'Адрес: пр. Ленина, 41 (Цоколь) \n Время работы 10-22 \n Телефон магазина +79134158804 \nЛегко добраться с помощью \n🗺️Google Maps🗺️ \nhttps://goo.gl/maps/GEkcwstMCnCor5Yj8')

        # Send a photo of the entrance for this shop

        with open('/home/archy/Документы/bot source/cleverentr.png', 'rb') as photo:

            bot.send_photo(message.from_user.id, photo)


    elif message.text == '🏙️ул. Дзержинского, 36':

        # Send a message with the shop's address

        bot.send_message(message.from_user.id, 'Адрес: ул. Дзержинского, 36 \n Время работы 10-22 \n Телефон магазина +79234158008  \nЛегко добраться с помощью \n🗺️Google Maps🗺️ \nhttps://goo.gl/maps/69pfFs8t6LgrU8sr6')

        # Send a photo of the entrance for this shop

        with open('/home/archy/Документы/bot source/dz entr.png', 'rb') as photo:

            bot.send_photo(message.from_user.id, photo)

    elif message.text == "🔙 Назад":
        start(message)

    elif message.text == '💨 ТОП 5 Одноразок':
        bot.send_message(message.from_user.id, '1 место: 💘Lost Mary - 5000 puffs \n2 место: 💝Lost Mary - 4000 puffs\n3 место: 💖HQD - 1200 puffs \n4 место: 💗Elf Bar - 4000 puffs \n5 место: 💓Lost Mary & Elf Bar - 1500 puffs', parse_mode='Markdown')

    elif message.text == '💥Новинки':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton('🌬️Одноразки')

        btn2 = types.KeyboardButton('🧴Жидкости')

        btn3 = types.KeyboardButton('🧨Устройства')

        btn4 = types.KeyboardButton("🔙 Назад")
        markup.add(btn1, btn2, btn3, btn4)
        bot.send_message(message.from_user.id, '😃Я тебе расскажу про наши новинки', reply_markup=markup)

    elif message.text == '🌬️Одноразки':
        bot.send_message(message.from_user.id, '🤯 Husky 8000 puffs HARD - От производителей самой популярной '
                                               'жидкости в России')
        with open('/home/archy/Документы/bot source/husky8000.png', 'rb') as photo:

            bot.send_photo(message.from_user.id, photo)

        bot.send_message(message.from_user.id, "😋GTM Bar 4200 и 5000 20mg - Mesh испаритель 1.2 Ohm, огромное кол-во "
                                               "вкусов")
        with open('/home/archy/Документы/bot source/GTQ.png', 'rb') as foto:

            bot.send_photo(message.from_user.id, foto)

    elif message.text == '🧴Жидкости':
        bot.send_message(message.from_user.id, '👽Soak 30мл 20мг - Фирменные вкусы от знаменитых производителей '
                                               'одноразок ')
        with open('/home/archy/Документы/bot source/soak.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)
        bot.send_message(message.from_user.id, '🤠Rell Yellow 60мл 6мг(органика) 70/30 - Большая палитра вкусов для '
                                               '"Больших" устройств ')

        with open('/home/archy/Документы/bot source/rell.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)
        bot.send_message(message.from_user.id, '🙀Serial Chiller - Прохладная линейка на каждый день от маэcтро '
                                               'жижеварения, команды Candy Lab ')

        with open('/home/archy/Документы/bot source/serialchiller.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)
    elif message.text == '🧨Устройства':
        bot.send_message(message.from_user.id, '⭐Xros 3 \nАккумулятор - 1000mAh \nType-C \nКартридж 2мл \nКартриджи '
                                               '0.6 и 1 Ohm в комплекте')
        with open('/home/archy/Документы/bot source/xros3.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)

        bot.send_message(message.from_user.id, '⭐Xros 3 mini \nАккумулятор - 1000mAh \nType-C \nКартридж 2мл \nКартриджи '
                                               '0.6 в комплекте')
        with open('/home/archy/Документы/bot source/xros3mini.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)

        bot.send_message(message.from_user.id,
                         '⭐Pasito mini \nАккумулятор - 1100mAh \nType-C \nКартридж 3.5мл \nИспарители '
                         '0.6 и 1 Ohm в комплекте')
        with open('/home/archy/Документы/bot source/pasitomini.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)


bot.polling(none_stop=True, interval=0)
