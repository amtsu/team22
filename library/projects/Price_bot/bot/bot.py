import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

from team22.library.projects.Price_bot.parser.parse_admarginem import (
    parse_price_admarginem,
)

# from parser import parse_prices
from team22.library.projects.Price_bot.parser.parser_for_bot import main_parser_engin
from team22.library.projects.Price_bot.sql import sql_connection
from team22.library.projects.Price_bot.start_manager import general_interface

load_dotenv()

TELEGRAM_TOKEN = os.getenv("BOT_TOKEN")

user_message = ""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        """Команды, которые принимает бот:
        /hello - поздороваться
        /parse - выводит информацию из парсеса цен
        /admarginem - находит цену на admarginem.ru
        """
    )


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f"Hello, {update.effective_user.first_name}")


async def admarginem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Пришли мне ссылку на кингу на admarginem.ru, и я узнаю цену"
    )


async def parse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Собираю цены")
    interface = general_interface.GeneralInterface()
    # engine = main_parser_engin()
    engine = interface.parse()
    for key, value in engine.items():
        await update.message.reply_text(f"{key} - {value}руб")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик ссылок с admarginem"""
    global user_message
    user_message = update.message.text
    if "admarginem.ru" not in user_message:
        await update.message.reply_text(
            "Пока я принимаю только ссылки с admarginem.ru, и команды: см /start"
        )
    else:
        interface = general_interface.GeneralInterface()
        # price = parse_price_admarginem(user_message)
        price = interface.parse_price_admarginem(user_message, update.effective_user.id)
        await update.message.reply_text(f"Цена книги: {price}")


def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("hello", hello))
    application.add_handler(CommandHandler("parse", parse))
    application.add_handler(CommandHandler("admarginem", admarginem))

    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)
    )

    application.run_polling()


if __name__ == "__main__":
    main()
