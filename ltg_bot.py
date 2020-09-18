#!/bin/python3
import telebot

tg = telebot.TeleBot("1277500164:AAEkU8DbjZX0E6wRa3JDKUKumIjlOuSLsRM")
keyboard_main_menu = telebot.types.ReplyKeyboardMarkup(True)
keyboard_main_menu.row('Выгрузить таблицу', 'Закрыть')
remove_main_menu = telebot.types.ReplyKeyboardRemove()
keyboard_students_menu = telebot.types.ReplyKeyboardMarkup(True)
keyboard_students_menu.row('Присутствует', 'Отсутствует', 'Болеет', 'Отчислен/Переведён', 'Главное меню')
remove_students_menu = telebot.types.ReplyKeyboardRemove()
keyboard_rollCall = telebot.types.ReplyKeyboardMarkup(True)
keyboard_rollCall.row('Начать перекличку', 'Открыть Таблицу', 'Главное меню')
keyboard_link_sheet_menu = telebot.types.ReplyKeyboardMarkup(True)
keyboard_link_sheet_menu.row("гиперссылка", "Отмена")
tableupload = "Делаются запросы, делается структурка, вместо такого сообщения можно вывести список студентов и " \
              "подсчёт их пропусков "


@tg.message_handler(commands=['start'])
def sendFirstMessage(message):
    tg.send_message(message.chat.id, "Внимание!\nРаботать ТОЛЬКО последовательно по менюшкам, потому что пока что"
                                     " всё сделано сплошными условиями, т.е. хрень может получится,"
                                     " НЕ НАДО включать сейчас режим тестирование головного мозга"
                                     " (это шутка)", reply_markup=keyboard_main_menu)


@tg.message_handler(content_types=['text'])
def sendText(tmessage):
    if tmessage.text.lower() == "выгрузить таблицу":
        tg.send_message(tmessage.chat.id, tableupload,
                        reply_markup=keyboard_rollCall)
    elif tmessage.text == "Закрыть":
        tg.send_message(tmessage.chat.id, "Ну, видимо не сегодня", reply_markup=remove_main_menu)
    elif tmessage.text == 'Начать перекличку':
        tg.send_message(tmessage.chat.id, "Здесь каждый раз будет выводиться студент, его посещаемость и"
                                          " при нажатии на одну из кнопок, будет совершаться переход к"
                                          " следующему", reply_markup=keyboard_students_menu)
        tg.send_message(tmessage.chat.id, "Здесь мы уже отмечаем чувачков, при нажатии запросами всё будет "
                                          "отправляться в твою таблицу")
    elif tmessage.text == 'Присутствует':
        tg.send_message(tmessage.chat.id, "Ну тип присутствует и происходит переход к следующему по порядку студенту")
    elif tmessage.text == 'Отсутствует':
        tg.send_message(tmessage.chat.id, "Ну тип отсутствует и происходит переход к следующему по порядку студенту")
    elif tmessage.text == 'Болеет':
        tg.send_message(tmessage.chat.id, "Ну тип болеет и происходит переход к следующему по порядку студенту")
    elif tmessage.text == 'Отчислен/Переведён':
        tg.send_message(tmessage.chat.id, "Ну тип отчислен или переведён и происходит переход к следующему по порядку "
                                          "студенту")
    elif tmessage.text == 'Главное меню':
        sendFirstMessage(tmessage)
    elif tmessage.text == 'Открыть Таблицу':
        tg.send_message(tmessage.chat.id, "Ну тупа ссылка на таблицу думаю лишним не будет",
                        reply_markup=keyboard_link_sheet_menu)
    elif tmessage.text == 'Отмена':
        tg.send_message(tmessage.chat.id, tableupload, reply_markup=keyboard_rollCall)
    else:
        tg.send_message(tmessage.chat.id, "Я тебя не понимаю")


tg.polling()
