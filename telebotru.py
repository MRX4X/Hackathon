import telebot
from telebot import types
token='5725301967:AAEq2MIY9NQVW5kCusWA4T75qvng7VpQjj4'
bot=telebot.TeleBot(token)
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id,'<b>Здравствуйте! Вы пришли на рекомендательный сервис системы дистанционного обучения. Выбирайте курс и приступайте к работе! Чтобы продолжить напишите команду /button</b>', parse_mode='html')
@bot.message_handler(commands=['button'])
def button_message(message):
    markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
    item1=types.KeyboardButton("Руководитель группы перспективных технологий")
    markup.add(item1)
    item2 = types.KeyboardButton("Руководитель группы компьютерного зрения")
    markup.add(item2)
    item3 = types.KeyboardButton("Руководитель группы обработки естественного языка")
    markup.add(item3)
    bot.send_message(message.chat.id,'<b>Выберите специальность на которой работайте</b>', parse_mode='html', reply_markup=markup)
@bot.message_handler(content_types='text')
def message_reply(message):

    #ДОЛЖНОСТЬ РУКОВОДИТЕЛЯ ГРУППЫ ПЕРСПЕКТИВНЫХ НАПРАВЛЕНИЙ
    if message.text=="Руководитель группы перспективных технологий":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("1. Программирование (Python и семейство С)")
        item2 = types.KeyboardButton("2. Математика (математический анализ)")
        markup.add(item1)
        markup.add(item2)
        bot.send_message(message.chat.id,'<b>Выберите название цифровой компетенции</b>', parse_mode='html', reply_markup=markup)

    # 1.ПРОГРАММИРОВАНИЕ НА ПАЙТОН
    if message.text=="1. Программирование (Python и семейство С)":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("1.1.Знание основных структур данных, алгоритмов, принципов ООП, паттернов проектирования")
        item2 = types.KeyboardButton("1.2.Навык программирования на языке Python")
        item3 = types.KeyboardButton("1.3. Навык программирования на языке(ах) семейства C")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id,'<b>Выберите индикаторы цифровых компетенций</b>', parse_mode='html', reply_markup=markup)

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

    #2 МАТ.АНАЛИЗ
    if message.text=="2. Математика (математический анализ)":
        bot.send_message(message.chat.id, '2.1.Знание теории вероятностей, математической статистики и линейной алгебры')
        bot.send_message(message.chat.id, "https://www.youtube.com/playlist?list=PLDrmKwRSNx7I3oNz_9RncOmuOj1Bny-Yw")
        bot.send_message(message.chat.id, "https://intuit.ru/studies/courses/637/493/info")


    #РУКОВОДИТЕЛЬ ГРУППЫ КОМПЬЮТЕРНОГО ЗРЕНИЯ
    if message.text=="Руководитель группы компьютерного зрения":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("1. Технологическая экспертиза")
        item2 = types.KeyboardButton("2. Методики управления проектами")
        item4 = types.KeyboardButton("3.Языки моделирования")
        item5 = types.KeyboardButton("4.Языки программирования и библиотеки")
        item6 = types.KeyboardButton("5.Машинное обучение(ML)")
        markup.add(item1)
        markup.add(item2)
        markup.add(item4)
        markup.add(item5)
        markup.add(item6)
        bot.send_message(message.chat.id, '<b>Выберите название цифровой компетенции</b>', parse_mode='html', reply_markup=markup)

    # 1. ТЕХНОЛОГИЧЕСКАЯ ЭКСПЕРТИЗА
    if message.text=="1. Технологическая экспертиза":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("1.1 Знания рынка IT-услуг")
        item2 = types.KeyboardButton("1.2.Знание основ рыночной экономики, конъюнктуры рынка программного обеспечения и IT – услуг")
        item3 = types.KeyboardButton("1.3.Знание методик управления проектами и опыт руководства проектами")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, '<b>Выберите индикаторы цифровых компетенций</b>', parse_mode='html', reply_markup=markup)

    # 1.1 Знания рынка IT-услуг
    if message.text=="1.1 Знания рынка IT-услуг":
        bot.send_message(message.chat.id,"https://www.youtube.com/playlist?list=PLm8qrmaJN2vvSsc9GRuL_FzVZ_07I_X7i")
        bot.send_message(message.chat.id,"https://career.habr.com/courses/skills/upravlenie-it-uslugami?ysclid=l97airxyql454758353")

    #1.2.Знание основ рыночной экономики, конъюнктуры рынка программного обеспечения и IT – услуг
    if message.text=="1.2.Знание основ рыночной экономики, конъюнктуры рынка программного обеспечения и IT – услуг":
        bot.send_message(message.chat.id,"https://www.youtube.com/watch?v=NAdhtJM7FaI")
        bot.send_message(message.chat.id,"https://www.klerk.ru/boss/articles/452803/")

    #1.3.Знание методик управления проектами и опыт руководства проектами
    if message.text=="1.3.Знание методик управления проектами и опыт руководства проектами":
        bot.send_message(message.chat.id,"https://www.youtube.com/watch?v=PKKAvWyxwhA")
        bot.send_message(message.chat.id,"https://gb.ru/geek_university/developer/project-manager?utm_source=yandex&utm_medium=cpc&utm_campaign=6236_gu-project-manager_yandex_cpc_poisk_faculty_ru_management_gizatullin_79056260&utm_content=adg_5045719267%7Cad_12862615486%7Cph_41427121364%7Ckey_управление%20проектами%20курсы%7Cdev_desktop%7Cpst_premium_1%7Crgnid_10995_Краснодарский%20край%7Cplacement_none%7Ccreative_%7Bcreative_name%7D&utm_term=управление%20проектами%20курсы&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3OTA1NjI2MDsxMjg2MjYxNTQ4Njt5YW5kZXgucnU6cHJlbWl1bQ&yclid=17469755342744453119")

    # 2. Методики управления проектами
    if message.text == "2. Методики управления проектами":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("2.1.Знание методик управления проектами (Agile, Devops, PMI или IPMA)")
        markup.add(item1)
        bot.send_message(message.chat.id, '<b>Выберите индикаторы цифровых компетенций</b>', parse_mode='html', reply_markup=markup)

    # 2.1.Знание методик управления проектами (Agile, Devops, PMI или IPMA)"
    if message.text == "2.1.Знание методик управления проектами (Agile, Devops, PMI или IPMA)":
        bot.send_message(message.chat.id, "https://www.youtube.com/playlist?list=PLGjRcOYH_YqFy3ODveTe6B5f8IcE_8Y1E")
        bot.send_message(message.chat.id, "https://www.youtube.com/c/pmi/videos")

    # 3.Языки моделирования
    if message.text == "3.Языки моделирования":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("3.1.Знание принципов описания процессов в различных нотациях (UML, IDEF, BPML и д.р.)")
        markup.add(item1)
        bot.send_message(message.chat.id, '<b>Выберите индикаторы цифровых компетенций</b>', parse_mode='html', reply_markup=markup)

    # 3.1.Знание принципов описания процессов в различных нотациях (UML, IDEF, BPML и д.р.)
    if message.text == "3.1.Знание принципов описания процессов в различных нотациях (UML, IDEF, BPML и д.р.)":
        bot.send_message(message.chat.id, "https://www.youtube.com/playlist?list=PLPPIc-4tm3YTw3FUu75jsW4QgrXopfXhX")
        bot.send_message(message.chat.id, "https://intuit.ru/studies/courses/1007/229/info?ysclid=l97bipqh8h624921431")

    # 4.Языки программирования и билиотеки
    if message.text == "4.Языки программирования и библиотеки":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("4.1 Знание языков программирования R/Python, Matlab/Octave")
        markup.add(item1)
        bot.send_message(message.chat.id, '<b>Выберите индикаторы цифровых компетенций</b>', parse_mode='html', reply_markup=markup)

    # 4.1 Знание языков программирования R/Python, Matlab/Octave
    if message.text == "4.1 Знание языков программирования R/Python, Matlab/Octave":
        bot.send_message(message.chat.id, "https://youtube.com/playlist?list=PLu5flfwrnSD7wxKXFgsiuxrMKLfFHm6CD")
        bot.send_message(message.chat.id, "https://youtube.com/playlist?list=PL0lO_mIqDDFXgfuxOEDTCwsWmKezOaDTu")

    # 5.Машинное обучение(ML)
    if message.text == "5.Машинное обучение(ML)":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item2 = types.KeyboardButton("5.1.Знание специальных библиотек machine learning (Tensorflow, Teano, Panda, Scikit-learn)")
        markup.add(item2)
        bot.send_message(message.chat.id, '<b>Выберите индикаторы цифровых компетенций</b>', parse_mode='html', reply_markup=markup)

    # 5.1.Знание специальных библиотек machine learning (Tensorflow, Teano, Panda, Scikit-learn)
    if message.text == "5.1.Знание специальных библиотек machine learning (Tensorflow, Teano, Panda, Scikit-learn)":
        bot.send_message(message.chat.id, "https://youtu.be/sNDW8d8eB1U")
        bot.send_message(message.chat.id, "https://youtu.be/vfyZf2Wj3pU")


    # РУКОВОДИТЕЛЬ ГРУППЫ ОБРАБОТКИ ЕСТЕСТВЕННОГО ЯЗЫКА
    if message.text == "Руководитель группы обработки естественного языка":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("1. Техническая экспертиза")
        item2 = types.KeyboardButton("2. Пользование компьютером")
        item5 = types.KeyboardButton("3. Моделирование")
        markup.add(item1)
        markup.add(item2)
        markup.add(item5)
        bot.send_message(message.chat.id, '<b>Выберите название цифровой компетенции</b>', parse_mode='html', reply_markup=markup)

    # 1. ТЕХНИЧЕСКАЯ ЭКСПЕРТИЗА
    if message.text=="1. Техническая экспертиза":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("1.1 Знания IT-услуг")
        item2 = types.KeyboardButton("1.2.Знание рыночной экономики, конъюнктуры рынка программного обеспечения и IT – услуг")
        item3 = types.KeyboardButton("1.3.Знание методик управления и опыт руководства проектами")
        markup.add(item1)
        markup.add(item2)
        markup.add(item3)
        bot.send_message(message.chat.id, '<b>Выберите индикаторы цифровых компетенций</b>', parse_mode='html', reply_markup=markup)

    # 1.1 Знания рынка IT-услуг
    if message.text=="1.1 Знания IT-услуг":
        bot.send_message(message.chat.id,"https://www.youtube.com/playlist?list=PLm8qrmaJN2vvSsc9GRuL_FzVZ_07I_X7i")
        bot.send_message(message.chat.id,"https://career.habr.com/courses/skills/upravlenie-it-uslugami?ysclid=l97airxyql454758353")

    #1.2.Знание основ рыночной экономики, конъюнктуры рынка программного обеспечения и IT – услуг
    if message.text=="1.2.Знание рыночной экономики, конъюнктуры рынка программного обеспечения и IT – услуг":
        bot.send_message(message.chat.id,"https://www.youtube.com/watch?v=NAdhtJM7FaI")
        bot.send_message(message.chat.id,"https://www.klerk.ru/boss/articles/452803/")

    #1.3.Знание методик управления проектами и опыт руководства проектами
    if message.text=="1.3.Знание методик управления и опыт руководства проектами":
        bot.send_message(message.chat.id,"https://www.youtube.com/watch?v=PKKAvWyxwhA")
        bot.send_message(message.chat.id,"https://gb.ru/geek_university/developer/project-manager?utm_source=yandex&utm_medium=cpc&utm_campaign=6236_gu-project-manager_yandex_cpc_poisk_faculty_ru_management_gizatullin_79056260&utm_content=adg_5045719267%7Cad_12862615486%7Cph_41427121364%7Ckey_управление%20проектами%20курсы%7Cdev_desktop%7Cpst_premium_1%7Crgnid_10995_Краснодарский%20край%7Cplacement_none%7Ccreative_%7Bcreative_name%7D&utm_term=управление%20проектами%20курсы&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3OTA1NjI2MDsxMjg2MjYxNTQ4Njt5YW5kZXgucnU6cHJlbWl1bQ&yclid=17469755342744453119")


    #2. ПОЛЬЗОВАНИЕ КОМПЬЮТЕРОМ
    if message.text=="2. Пользование компьютером":
        markup=types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1=types.KeyboardButton("2.1.Знание пакета офисных программ (MS Word, MS Excel, MS PowerPoint).")
        markup.add(item1)
        bot.send_message(message.chat.id, '<b>Выберите индикаторы цифровых компетенций</b>', parse_mode='html', reply_markup=markup)

    #2.1.Знание пакета офисных программ (MS Word, MS Excel, MS PowerPoint).
    if message.text=="2.1.Знание пакета офисных программ (MS Word, MS Excel, MS PowerPoint).":
        bot.send_message(message.chat.id,"https://www.youtube.com/watch?v=Q__XAwr9N00")
        bot.send_message(message.chat.id,"https://skillbox.ru/course/excel-gsheets/?utm_source=yandex&utm_medium=cpc&utm_campaign=144_excel-gsheets_yandex_cpc_poisk_course_all_management_skillbox_75100275&utm_content=adg_4935935428%7Cad_12258932214%7Cph_39270267828%7Ckey_курсы%20эксель%7Cdev_desktop%7Cpst_premium_1%7Crgnid_10995_Краснодарский%20край%7Cplacement_none%7Ccreative_%7Bcreative_name%7D&utm_term=курсы%20эксель&ad_sale&ad2021&_openstat=ZGlyZWN0LnlhbmRleC5ydTs3NTEwMDI3NTsxMjI1ODkzMjIxNDt5YW5kZXgucnU6cHJlbWl1bQ&yclid=1167892974130954239")

    # 4.Языки моделирования
    if message.text == "3. Моделирование":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        item1 = types.KeyboardButton("3.1.Знание принципов процессов в различных нотациях (UML, IDEF, BPML и д.р.)")
        markup.add(item1)
        bot.send_message(message.chat.id, '<b>Выберите индикаторы цифровых компетенций</b>', parse_mode='html', reply_markup=markup)

    # 4.1.Знание принципов описания процессов в различных нотациях (UML, IDEF, BPML и д.р.)
    if message.text == "3.1.Знание принципов процессов в различных нотациях (UML, IDEF, BPML и д.р.)":
        bot.send_message(message.chat.id, "https://www.youtube.com/playlist?list=PLPPIc-4tm3YTw3FUu75jsW4QgrXopfXhX")
        bot.send_message(message.chat.id, "https://intuit.ru/studies/courses/1007/229/info?ysclid=l97bipqh8h624921431")


bot.infinity_polling()