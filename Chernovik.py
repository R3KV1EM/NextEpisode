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
        btn6 = types.KeyboardButton("📚Новичку")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
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
        with open('/home/archy/Документы/bot source/odnorazki.png', 'rb') as photo:

            bot.send_photo(message.from_user.id, photo)

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
        bot.send_message(message.from_user.id, '🐸Мы собрали для тебя топ 10 (место в рейтинге не является приортитетом)', reply_markup=markup)

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

    elif message.text == "📚Новичку":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

        btn1 = types.KeyboardButton('🧪PG/VG')

        btn2 = types.KeyboardButton('🚬Salt vs Organic')

        btn3 = types.KeyboardButton('ΩСопротивление')

        btn4 = types.KeyboardButton('🔋Советы по зарядке')

        btn5 = types.KeyboardButton('💡Продление жизни испарителю/картриджу')

        btn6 = types.KeyboardButton("🔙 Назад")
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        bot.send_message(message.from_user.id, '🧑‍🎓 Полезный туториал для новичка', reply_markup=markup)

    elif message.text == "🧪PG/VG":
        bot.send_message(message.from_user.id, "PG/VG - это соотнешение Пропиленгликоля(PG) к Глицерину(VG), что это "
                                               "дает и о чем это нам говорит? \nPG-VG - это основа каждой Vape "
                                               "жидкости, при изготовлении сперва смешиваются эти компоненты а уже "
                                               "после этого добавляются ароматизаторы которые и придают определенный "
                                               "вкус жидкости. \nЗачем нам знать соотношение? Ответ прост - для того "
                                               "что-бы понимать густоту жидкости и для каких устройств она "
                                               "предназначена. \n PG/VG 30/70 - говорит нам о том что жидкость "
                                               "достаточно густая и предназначена для мощных устройств > 40 Ватт. \n "
                                               "PG/VG 50/50 - говорит нам о том что жидкость менее густая и "
                                               "предназначена для маломощных устройств < 40 Ватт. \n Предоставленная "
                                               "информация не является аксиомой и все может варьироваться в "
                                               "зависимости от типа устройства и его нагревателей (картриджей, "
                                               "испарителей) но основа именно такая")

        with open('/home/archy/Документы/bot source/pgvg.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)

    elif message.text == "🚬Salt vs Organic":
        bot.send_message(message.from_user.id, "Что значит солевой никотин, что такое солевая жидкость? \nСолевой "
                                               "никотин это разновидность никотина, чей PH-баланс смещен в сторону "
                                               "кислоты, относительно обычного щелочного никотина. В табаке "
                                               "представлен как солевой никотин, так и щелочной, причем солевого "
                                               "больше – поэтому сигареты быстро утоляют никотиновый голод, "
                                               "а классический вейпинг медленно. \nНужно отметить, что под “обычным "
                                               "никотином” в вейпинге понимается щелочной никотин, тогда как “обычный "
                                               "никотин” в природе и табаке, это наоборот солевой. Солевой никотин "
                                               "имеет PH-баланс приближенный к тканям человеческого тела, "
                                               "отчего меньше реагирует со слизистой (меньше удар по горлу - TX) и "
                                               "быстрее усваивается \n\nИз вышеуказанной информации можно сделать "
                                               "вывод \n\n1)Органика(Щелочь) в жидкостях больше предназначена для "
                                               "длительного перепара и для получения никотиного эффекта потребуется "
                                               "~10-20 минут парения, крепость никотина ощущается более явно в "
                                               "процессе парения \n\n2)Солевой никотин больше предназначен для"
                                               "быстрого получения никотинового эффекта и коротких перекуров ~3-5 "
                                               "мин. крепость никотина ощущается гораздо мягче в сравнении с щелочью")
        with open('/home/archy/Документы/bot source/nictonie.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)
    elif message.text == "ΩСопротивление":
        bot.send_message(message.from_user.id, "Если говорить очень кратко то обычно на выбор в вашем устройстве есть "
                                               "несколько вариантов испарителей(картриджей) с разным сопротивлением. "
                                               "\nРассмотрим на примере Jellybox Nano, у этого устройства имеется два "
                                               "вида испарителей 1)0.5 Ohm 2)1 Ohm \n\nИспаритель на 0.5 Ohm - "
                                               "предназначен на большую мощность и имеет более свободную затяжку, "
                                               "генерирует больше пара. \n\nИспаритель на 1 Ohm - имеет более тугую "
                                               "затяжку, предназначен для меньшей мощности, генерирует меньше пара "
                                               "чем испаритель на 0.5 Ohm \n\nЗаключение: Чем НИЖЕ сопротивление, тем больше пара, вкуса и более свободная затяжка. Соответственно чем ВЫШЕ сопротивление, тем меньше мощности необходимо, меньше пара, затяжка более тугая.")
        with open('/home/archy/Документы/bot source/resistance.png', 'rb') as fotq:

            bot.send_photo(message.from_user.id, fotq)
    elif message.text == "🔋Советы по зарядке":
        bot.send_message(message.from_user.id, "1)Желательно заряжать устройство током не больше 1А(От компьютера или "
                                               "Powerbank) \n\n2)Желательно снимать картридж при зарядке - в процессе "
                                               "заряда, устройство начинает нагреваться(особенно если ток более 1А) "
                                               "тепло от устройства передается на картридж и делает жидкость менее "
                                               "густой что может стать причиной протечек.")
        with open('/home/archy/Документы/bot source/charging.png', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo)


    elif message.text == "💡Продление жизни испарителю/картриджу":
        bot.send_message(message.from_user.id, "1) Перед использованием нового картриджа/испарителя нужно заправить "
                                               "бак и подождать ~15мин. до полной пропитки \n2) Не использовать "
                                               "устройство на холоде (при воздействии отрицательных температур "
                                               "жидкость густет и начинает плохо пропитывать нагревательный элемент "
                                               "\n3) Заправлять подходящую по густоте жидкость(PG/VG) \n4) Не "
                                               "смешивать жидкости в картридже (1 Картридж - 1 Жидкость) \n5) "
                                               "Десертные вкусы как правило быстрее портят картридж чем нейтральные "
                                               "фрукты или ягоды")
        with open('/home/archy/Документы/bot source/cartridge.png', 'rb') as photo:
            bot.send_photo(message.from_user.id, photo)

bot.polling(none_stop=True, interval=0)
