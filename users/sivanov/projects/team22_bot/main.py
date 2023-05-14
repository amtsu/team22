#!/usr/local/bin/python
# coding: utf-8
"""
here is the bot
team_22 бот выполняет простые sql запросы к тестовой базе
"""
from datetime import datetime
import sqlite3

# import asyncio
import logging
from aiogram import Bot, Dispatcher, executor, types  # type: ignore
import superhomosecret

# =========================================================================
# allowed
logging.basicConfig(level=logging.INFO)
bot = Bot(token=superhomosecret.SUPERHOMOSECRET)
bot_disp = Dispatcher(bot)
# ========================================================================
@bot_disp.message_handler(commands=["start", "help"])
async def start_message_handler(message: types.Message) -> None:
    """
    Обработка реакции на команды start или help
    """
    # log message
    with open(superhomosecret.LOGFILEPATH, "a", encoding="utf-8") as fout:
        print(
            f"{datetime.now()}: #command {message.text}",
            file=fout,
        )
    # process message
    await message.reply(f"Привет, получил '{message.text}', работаем!")
    await message.reply("Можно выполнять sql запросы к тестовой бд, запросы должны" \
                        " начинаться с команды /sql")


# DBFILEPATH
# =========================================================================
@bot_disp.message_handler(commands=["sql"])
async def sql_message_handler(message: types.Message) -> None:
    """
    работа с базой данных для всех желающих
    """
    # log message
    with open(superhomosecret.LOGFILEPATH, "a", encoding="utf-8") as fout:
        print(
            f"{datetime.now()}: #sql {message.text}",
            file=fout,
        )
    request = message.text
    request = request.replace("/sql", "")
    request = request.strip()
    request = request.lower()
    if (
        (request != "")
        and ("drop" not in request)
        and ("alter" not in request)
        and ("delete" not in request)
    ):
        # process message
        logging.info(f"trying to connect to {superhomosecret.DBFILEPATH}")
        with sqlite3.connect(superhomosecret.DBFILEPATH) as connection:
            cursor = connection.cursor()
            try:
                cursor.execute(request)
                request_result = "\n".join(str(field) for field in cursor.fetchall())
            except sqlite3.DatabaseError as db_err:
                request_result = f"bad request: {db_err.args}"
    else:
        request_result = "drop or alter is not allowed"
    await message.reply(request_result[-4000:])


# =========================================================================
@bot_disp.message_handler()
async def all_messages_handler(message: types.Message) -> None:
    """7
    Обработка реакции на все сообщения без исключения
    """
    # log message
    with open(superhomosecret.LOGFILEPATH, "a", encoding="utf-8") as fout:
        print(
            f"{datetime.now()}: #text {message.text}",
            file=fout,
        )
    # process message
    await message.answer(f"received: {message.text}")


# =========================================================================
async def on_bot_start(_dispatcher):
    """
    Надеюсь что это будет выполняться перед стартом бота
    bot operation
    """
    for address in superhomosecret.GENERALINFOADDRESSEE:
        # асинхронные штуки без await не будут работать
        await bot.send_message(address, "bot started")


# =========================================================================


def main():
    """
    bot operation
    """
    executor.start_polling(bot_disp, skip_updates=True, on_startup=on_bot_start)


# =========================================================================
if __name__ == "__main__":
    main()  # асинхронность повсюду
