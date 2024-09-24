"""
Общий интерфейс для работы всех модулей проекта
"""
from telegram.ext import ApplicationBuilder, CommandHandler

from team22.library.projects.Price_bot.bot import bot
from team22.library.projects.Price_bot.bot.bot import TELEGRAM_TOKEN
from team22.library.projects.Price_bot.parser.parser_for_bot import main_parser_engin
from team22.library.projects.Price_bot.sql import sql_connection
from team22.library.projects.Price_bot.start_manager.singleton import singleton


@singleton
class GeneralInterface:
    """
    Общий класс - интерфейс для взаимодействия модулей бота, парсера и БД
    (Класс сделан на будущее, пока в нем смысла нет)
    """
    def __init__(self):
        pass

    # self.start()

    # def start(self):
    #     application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
    #
    #     application.add_handler(CommandHandler("start", bot.start))

    def parse(self):
        application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()
        application.add_handler(CommandHandler("parse", bot.parse))
        parsed_data: dict = main_parser_engin()
        bd_connection = sql_connection.SQLConnection()
        bd_connection.add_to_db(parsed_data)
        return parsed_data

    def parse_price_admarginem(self, user_message, user_id):
        # price = parse_price_admarginem(user_message) ЗАКОММЕНЧЕНО, ПОТОМУ ЧТО НЕ РАБОТАЕТ
        price = 12345678
        bd_connection = sql_connection.SQLConnection()
        bd_connection.add_to_db(price, user_message, user_id)
        return price
