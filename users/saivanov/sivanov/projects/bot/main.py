#!/usr/local/bin/python
# coding: utf-8
"""
here is the bot
and у меня больше нет проблемм с русским языком

это про обсудить https://github.com/search?p=99&q=telebot.TeleBot&type=Code
"""
from datetime import datetime
import telebot  # type: ignore

# from telebot import types
import superhomosecret

# from functions import message_handler
# =========================================================================
# allowed
bot = telebot.TeleBot(superhomosecret.SUPERHOMOSECRET)
# ========================================================================
def alert_message(message: str) -> None:
    """
    функция, рассылающая сообщения по списку ALARMADDRESSEE
    """
    for addressee in superhomosecret.ALARMADDRESSEE:
        bot.send_message(
            addressee,
            message,
        )


# ========================================================================
@bot.message_handler(content_types=["text"])
def get_text_messages(message: telebot.types.Message) -> None:
    """
    here is the text message handler
    """
    # message_handler(message)
    # --------------------------------------------------------------------------------------
    # сообщения из facility
    if (message.chat.type in ("group", "supergroup")) and (
        message.chat.id in superhomosecret.FACILITY
    ):
        # ----------------------------------------------------------------------------------
        # тут нужно добавить лог чата
        with open(superhomosecret.FACILITYLOGFILEPATH, "a", encoding="utf-8") as fout:
            print(
                f"{datetime.now()}: FROM {message.from_user.id} comes text: {message.text}",
                file=fout,
            )
        # ---------------------------------------------------------------------------------
        if message.from_user.id > superhomosecret.NEWCOMERS:  # fresh meat
            alert_message(
                f"ALARM! User {message.from_user.first_name}"
                f" ({message.from_user.id}) texted: {message.text}"
                f" ({superhomosecret.CHATHYPERLINK}{message.id})",
            )
        # ---------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------
        if (
            (message.text.lower().find("#куплю") < 0)
            and (message.text.lower().find("#продам") < 0)
            and (message.text.lower().find("#обмен") < 0)
        ):  # no #куплю #продам #обмен

            alert_message(
                f"ALARM: no #куплю#продам#обмен! User {message.from_user.first_name}"
                f" ({message.from_user.id}) texted: {message.text}"
                f" ({superhomosecret.CHATHYPERLINK}{message.id})",
            )
        elif message.text.lower().find("#видео") < 0:  # no #видео
            alert_message(
                f"ALARM: no #видео! User {message.from_user.first_name}"
                f" ({message.from_user.id}) texted: {message.text}"
                f" ({superhomosecret.CHATHYPERLINK}{message.id})",
            )

    # --------------------------------------------------------------------------------------
    # тестовая часть, про пидоров

    if message.chat.type == "private":
        with open(superhomosecret.TESTBENCHLOGFILEPATH, "a", encoding="utf-8") as fout:
            print(
                f"{datetime.now()}: FROM {message.from_user.id} comes text: {message.text}",
                file=fout,
            )
        print(f"message from {message.from_user.id} comes.")

        if message.text.lower() in ("privet", "привет"):
            # bot.send_message(message.from_user.id,"")
            bot.reply_to(message, f"Привет {message.from_user.first_name}, ты пидор")
        if message.from_user.id in superhomosecret.COMMANDERS:
            if message.text.lower() == "log":
                with open(
                    superhomosecret.TESTBENCHLOGFILEPATH, "r", encoding="utf-8"
                ) as fin:
                    file_contents = fin.read()
                    bot.reply_to(message, file_contents[-4000:])
    elif (
        message.chat.type in ("group", "supergroup")
        and message.chat.id not in superhomosecret.FACILITY
    ):
        # print("group chat message")
        print(message.id)
        with open(superhomosecret.TESTBENCHLOGFILEPATH, "a", encoding="utf-8") as fout:
            print(
                f"{datetime.now()}: FROM {message.from_user.id} in"
                f" {message.chat.id} comes text: {message.text}",
                file=fout,
            )
        if message.text.lower() in ("privet", "привет"):
            bot.reply_to(message, f"Привет {message.from_user.first_name}, ты пидор!")
        print(f"group message in {message.chat.id}")
    else:
        print("unknown message")


# ========================================================================
@bot.message_handler(content_types=["photo", "document"])
def get_pic_and_doc_messages(message: telebot.types.Message) -> None:
    """
    тут для маркета будем ловить сообщения с картинками
    """
    # message_handler(message)
    # --------------------------------------------------------------------------------------
    # сообщения из facility
    if (message.chat.type in ("group", "supergroup")) and (
        message.chat.id in superhomosecret.FACILITY and message.caption is not None
    ):
        # ----------------------------------------------------------------------------------
        # тут нужно добавить лог чата
        with open(superhomosecret.FACILITYLOGFILEPATH, "a", encoding="utf-8") as fout:
            # print(f"{message.caption}")
            print(
                f"{datetime.now()}: FROM {message.from_user.id} comes pictures"
                f" with caption: {message.caption}",
                file=fout,
            )
        # ---------------------------------------------------------------------------------
        if message.from_user.id > superhomosecret.NEWCOMERS:  # fresh meat
            alert_message(
                f"ALARM! User {message.from_user.first_name}"
                f" ({message.from_user.id}) pictured: {message.caption}",
            )
        # --------------------------------------------------------------------------------------
        # ----------------------------------------------------------------------------------
        if (
            (message.caption.lower().find("#куплю") < 0)
            and (message.caption.lower().find("#продам") < 0)
            and (message.caption.lower().find("#обмен") < 0)
        ):  # no #куплю #продам #обмен
            alert_message(
                f"ALARM: no #куплю#продам#обмен! User {message.from_user.first_name}"
                f" ({message.from_user.id}) texted: {message.caption}"
                f" ({superhomosecret.CHATHYPERLINK}{message.id})",
            )
        elif message.caption.lower().find("#видео") < 0:  # no #видео
            alert_message(
                f"ALARM: no #видео! User {message.from_user.first_name}"
                f" ({message.from_user.id}) texted: {message.caption}"
                f" ({superhomosecret.CHATHYPERLINK}{message.id})",
            )


# =========================================================================
def main():
    """
    bot operation
    """
    for address in superhomosecret.GENERALINFOADDRESSEE:
        bot.send_message(address, "bot started")
    bot.polling(none_stop=True, interval=5)


# =========================================================================
if __name__ == "__main__":
    main()
# privet
