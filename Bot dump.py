import telebot
from telebot import types
import random

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
        btn4 = types.KeyboardButton("🧂Навигатор salt жидкостей")
        btn5 = types.KeyboardButton("🔮Выбери мне жидкость")
        markup.add(btn1, btn2, btn3, btn4, btn5)
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
    elif message.text == '🧂Навигатор salt жидкостей':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton('🌬🥶Холодные')

        btn2 = types.KeyboardButton('🍩Десертные')

        btn3 = types.KeyboardButton('🍓Фрукты-Ягоды')

        btn4 = types.KeyboardButton('🥤Газировки-Жвачки')

        btn5 = types.KeyboardButton("🔙 Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5)
        bot.send_message(message.from_user.id, '🐸Давай посмотрим лучшие жидкости', reply_markup=markup)

    elif message.text == '🌬🥶Холодные':
        bot.send_message(message.from_user.id, "1) 🐺Husky Double Ice - Siberian Black \n2) 🐺Husky - Gum Wolf \n3) ⚗️Rell "
                                               "Orange - Peach Ice \n4) 🔋Glitch Sauce - Энергетик с клюквой \n5) 🍃Dual "
                                               "- Мятные леденцы с эвкалиптом \n6) 🫐Морс Мороз - Лесные ягоды \n7) "
                                               "🐺Husky White - Mint Wind \n8) 🌲Boshki - Добрые On Ice \n9) 🧸Мишка - "
                                               "Холодный ананас \n10) 🧃Serial Chiller - Сок с гранатом")

        with open('/home/archy/Документы/bot source/coldfruits.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)

    elif message.text == '🍩Десертные':
        bot.send_message(message.from_user.id, "1) 🍪ElectroJam - Milk coffee candy \n2) 🍿ElectroJam - Popcorn \n3) "
                                               "🍪ElectroJam - "
                                               "Salt caramel cookie \n4) 🫐JamMonster - Blueberry \n5) 👻 JamMonster "
                                               "- Blueberry\n6) ☕CoffeIN - Hot Chocolate \n7) "
                                               "🍩Rell Green - Пончик с клубникой \n8) 🪱Slurm - Cherry Worms \n9) 🧸Мишка - "
                                               "Булочка с корицей \n10) 🍪ElectroJam - Milk chocolate cookie")
        with open('/home/archy/Документы/bot source/dessert.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)

    elif message.text == '🍓Фрукты-Ягоды':
        bot.send_message(message.from_user.id, "1) 🍇Glitch Sauce No Mint - Виноградный сок (Grape King)  \n2) 🪀Toyz - "
                                               "Сумасшедшая малина  \n3)"
                                               "🐛Slurm  - "
                                               "Брусника, клюква \n4) 🌲Boshki - Малиновое варенье с хвоёй (сахарные) "
                                               "\n5) 🔥Hot Spot"
                                               "- Персик, маракуйя\n6) 👹Scandalist - Киви,  Малина (Ex's Heart) \n7) "
                                               "🫙Maxwell's - Дыня, Арбуз и Клубничный джем (Rich) \n8) 🥤Морс - "
                                               "Клубника, гранат \n9) 🍹Rell Green  -"
                                               "Киви, маракуйя, гуава \n10) 🍍Genetic Code - Ананас, клюква")

        with open('/home/archy/Документы/bot source/fruits.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)


    elif message.text == "🔙 Назад":
        start(message)

    elif message.text == '🥤Газировки-Жвачки':
        bot.send_message(message.from_user.id,
                         "1)🥤Taboo Cult - Лимонад с малиной (Pink Lemonade)  \n2) ⚡Sun Strike - "
                         "Энергетик с яблоком и киви (Shot of Adrenaline)  \n3)"
                         "👹Scandalist - "
                         "Жвачка с клубникой и малиной (Boy oh boy) \n4) 🌲Boshki On Ice - Клубничная кола с хвоёй (CS) "
                         "\n5) 🧑‍🚀Cosmonaut"
                         "- Коктейль с гранатом и голубикой (Minus 273.15)\n6) 🍓Glitch Sauce - Газировка с клубникой ("
                         "Rogue)\n7)"
                         "🐺Husky - Жвачка с манго (Chew Peak)\n8) 🐺Husky Double Ice - "
                         "Ледяная кола (Winter River) \n9) 🫙Maxwell's  -"
                         "Травянистая Cоветская кока-кола (Baikal) \n10) 🌵Raisin - Кактусовый Лимонад (Phobia)")

        with open('/home/archy/Документы/bot source/lemonade.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)

    elif message.text == "🔮Выбери мне жидкость":
        liquids = ["Glitch Sauce No Mint - Виноградный сок (Grape King)",
                   "Toyz - Сумасшедшая малина ", "Slurm - Брусника, клюква",
                   "Boshki - Малиновое варенье с хвоёй (сахарные)",
                   "Hot Spot - Персик, маракуйя",
                   "Scandalist - Киви,  Малина (Ex's Heart)", "Maxwell's - Дыня, Арбуз и Клубничный джем (Rich)",
                   "Морс - "
                   "Клубника, "
                   "гранат",
                   "Rell Green - Киви, маракуйя, гуава", "Husky - Gum Wolf", "Dual - Мятные леденцы с эвкалиптом",
                   "Boshki - "
                   "Добрые On Ice"]
        result = random.choice(liquids)
        bot.send_message(message.from_user.id, result)
        with open('/home/archy/Документы/bot source/randompepe.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)






bot.polling(none_stop=True, interval=0)
