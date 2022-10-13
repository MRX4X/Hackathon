import telebot
from telebot import types
token='5725301967:AAEq2MIY9NQVW5kCusWA4T75qvng7VpQjj4'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'Привет. Чтобы продолжить напишите команду /button')
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Руководитель группы перспективных технологий")
    markup.add(item1)
    item2 = types.KeyboardButton("Руководитель группы компьютерного зрения")
    markup.add(item2)
    bot.send_message(message.chat.id,'Выберите профессию',reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):

    #ДОЛЖНОСТЬ РУКОВОДИТЕЛЯ ГРУППЫ ПЕРСПЕКТИВНЫХ НАПРАВЛЕНИЙ
    if message.text=="Руководитель группы перспективных технологий":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("1. Программирование (Python и семейство С)")
        item2 = types.KeyboardButton("2. Математика (математический анализ)")
        item3 = types.KeyboardButton("3.Машинное обучение")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id,'Выберите название цифровой компетенции',reply_markup=markup)

    # 1.ПРОГРАММИРОВАНИЕ НА ПАЙТОН
    if message.text=="1. Программирование (Python и семейство С)":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("1.1.Знание основных структур данных, алгоритмов, принципов ООП, паттернов проектирования")
        item2 = types.KeyboardButton("1.2.Навык программирования на языке Python")
        item3 = types.KeyboardButton("1.3. Навык программирования на языке(ах) семейства C")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id,'Выберите индикаторы цифровых компетенций',reply_markup=markup)

    # 1.1 ООП
    if message.text=="1.1.Знание основных структур данных, алгоритмов, принципов ООП, паттернов проектирования":
        bot.send_message(message.chat.id,"https://www.youtube.com/playlist?list=PLmRNNqEA7JoPhVQCUisflWWhjdoKucDuf")
        bot.send_message(message.chat.id,"https://www.youtube.com/playlist?list=PLmRNNqEA7JoPhVQCUisflWWhjdoKucDuf")


    # 1.2 НАВЫК ПАЙТОНА
    if message.text=="1.2.Навык программирования на языке Python":
        bot.send_message(message.chat.id, "https://www.youtube.com/playlist?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu")
        bot.send_message(message.chat.id, "https://skillbox.ru/course/profession-python/?utm_source=yandex&utm_medium=cpc&utm_campaign=76_profession-python_yandex_cpc_master-campaign_course_ru_all_gizatullin_75085717&utm_content=adg_4935640604%7Cad_12338063830%7Cph_39262130527%7Ckey_---autotargeting%7Cdev_desktop%7Cpst_premium_1%7Crgnid_239_Сочи%7Cplacement_none%7Ccreative_%7Bcreative_name%7D&utm_term=---autotargeting&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3NTA4NTcxNzsxMjMzODA2MzgzMDt5YW5kZXgucnU6cHJlbWl1bQ&yclid=15061761636051451903")

    # 1.3 НАВЫК С
    if message.text=="1.3. Навык программирования на языке(ах) семейства C":
        bot.send_message(message.chat.id, "https://www.youtube.com/playlist?list=PL0lO_mIqDDFXNfqIL9PHQM7Wg_kOtDZsW")
        bot.send_message(message.chat.id, "https://skillfactory.ru/c-plus-plus-razrabotchik?utm_source=infopartners&utm_medium=cpa&utm_campaign=tutortop_cpc&utm_content=3b9f2bf4")
        bot.send_message(message.chat.id, "https://skillfactory.ru/c-sharp-razrabotchik")
        bot.send_message(message.chat.id, "https://www.youtube.com/playlist?list=PLIIXgDT0bKw6hIBb08OQgAAT81AzYnwZs")

    # 1.4 НАВЫК GIT, DOCKER
    if message.text=="1.4. Умение работать с базами данных, Git, Docker":
        bot.send_message(message.chat.id, "https://www.youtube.com/playlist?list=PLuY6eeDuleIOMB2R_Kky05ZfiAx2_pbAH")
        bot.send_message(message.chat.id, "https://githowto.com/ru")
        bot.send_message(message.chat.id, "https://www.youtube.com/playlist?list=PLD5U-C5KK50XMCBkY0U-NLzglcRHzOwAg")
        bot.send_message(message.chat.id, "https://habr.com/ru/post/310460/?ysclid=l979cu7hd5720677815")

    #2
    if message.text=="2. Математика (математический анализ)":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("2.1.Знание теории вероятностей, математической статистики и линейной алгебры")
        markup.add(item1)
        bot.send_message(message.chat.id,'Выберите индикаторы цифровых компетенций',reply_markup=markup)
    if message.text=="2.1.Знание теории вероятностей, математической статистики и линейной алгебры":
        bot.send_message(message.chat.id, "https://www.youtube.com/playlist?list=PLDrmKwRSNx7I3oNz_9RncOmuOj1Bny-Yw")
        bot.send_message(message.chat.id, "https://intuit.ru/studies/courses/637/493/info")
    if message.text=="Руководитель группы компьютерного зрения":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("1.IT-услуги(экономические)")
        item2 = types.KeyboardButton("2. Методики управления проектами")
        item3 = types.KeyboardButton("3.Программное обеспечение")
        item4 = types.KeyboardButton("4.Языки моделирования")
        item5 = types.KeyboardButton("5.Языки программирования и библиотеки")
        item6 = types.KeyboardButton("6.Машинное обучение(ML)")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        bot.send_message(message.chat.id,'Выберите что вам надо',reply_markup=markup)
bot.infinity_polling()