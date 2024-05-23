"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите
  бота отвечать, в каком созвездии сегодня находится планета.

"""
from datetime import date
import ephem
import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

planets_and_moons = ['Mercury', 'Venus', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune', 'Pluto']

logging.basicConfig(format='%(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO,
                    filename='bot.log')


def greet_user(update, context) -> None:
    text = 'Вызван /start'
    print(text)
    update.message.reply_text(text)


def loc_of_pl(update, context) -> None:
    user_text = update.message.text
    try:
        planet_name = user_text.split()[1]
    except IndexError:
        update.message.reply_text("Не указано название планеты")
        return
    date_today = str(date.today())
    date_today = date_today.replace('-', '/')
    planet_name = planet_name.lower().capitalize()
    temp = ""
    if planet_name in planets_and_moons:
        if planet_name == 'Mercury':
            temp = ephem.Mercury(date_today)
        elif planet_name == 'Venus':
            temp = ephem.Venus(date_today)
        elif planet_name == 'Mars':
            temp = ephem.Mars(date_today)
        elif planet_name == 'Jupiter':
            temp = ephem.Jupiter(date_today)
        elif planet_name == 'Saturn':
            temp = ephem.Saturn(date_today)
        elif planet_name == 'Uranus':
            temp = ephem.Uranus(date_today)
        elif planet_name == 'Neptune':
            temp = ephem.Neptune(date_today)
        elif planet_name == 'Pluto':
            temp = ephem.Pluto(date_today)
        update.message.reply_text(ephem.constellation(temp))
    else:
        print("Введено неверное название")
        return

def talk_to_me(update, context) -> None:
    user_text = update.message.text
    print(user_text)
    update.message.reply_text(user_text)


def main() -> None:
    mybot = Updater("6576223151:AAEolKJ9e9efO1vPSZdFiOw3vTPUOKrZ9rQ", use_context=True)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(CommandHandler("planet", loc_of_pl))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    mybot.start_polling()
    mybot.idle()


if __name__ == "__main__":
    main()
