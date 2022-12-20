#!/usr/local/bin/python
# coding: utf-8
"""
ДОБАВИТЬ КОММЕНТАРИЙ
это модуль с тестом бота для телеги
мануал взял вот тут:
https://otus.ru/journal/bot-v-telegram-na-pitone-ot-a-do-ya/
описание модуля тут
https://pypi.org/project/pyTelegramBotAPI
"""
from datetime import datetime
import telebot

# from telebot import types
import superhomosecret

# from functions import message_handler
# =========================================================================
# так можно
bot = telebot.TeleBot(superhomosecret.SUPERHOMOSECRET)
# ========================================================================
@bot.message_handler(content_types=["text"])
def get_text_messages(message: telebot.types.Message) -> None:
    """
    функция, обрабатывающая сообщения, принимаемые ботом
    """
    # message_handler(message)
    if message.chat.type == "private":
        with open("bot.log", "a", encoding="utf-8") as fout:
            print(
                f"{datetime.now()}: FROM {message.from_user.id} comes text: {message.text}",
                file=fout,
            )
        print(f"message from {message.from_user.id} comes.")

        if message.text.lower() == "привет":
            # bot.send_message(message.from_user.id, "Привет пидор.")
            bot.reply_to(message, "Привет пидор.")
    elif message.chat.type in ("group", "supergroup"):
        # print("group chat message")
        with open("bot.log", "a", encoding="utf-8") as fout:
            print(
                f"{datetime.now()}: FROM {message.from_user.id} in"
                / "{message.chat.id} comes text: {message.text}",
                file=fout,
            )
        if message.text.lower() == "привет":
            bot.reply_to(message, "Привет пидор.")
        print(f"group message in {message.chat.id}")
    else:
        print("unknown message")


# ========================================================================


def main():
    """
    запускаем бота!
    """
    bot.send_message(102739674, "Бот запущен!")
    bot.send_message(-1001418430207, "Эй, группа, бот запущен!")
    bot.polling(none_stop=True, interval=5)


# =========================================================================


if __name__ == "__main__":
    main()
