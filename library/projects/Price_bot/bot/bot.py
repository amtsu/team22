import os
import asyncio
from dotenv import load_dotenv
from telegram import Update
import random
from telegram.ext import (ApplicationBuilder,
                          CommandHandler,
                          MessageHandler,
                          ContextTypes,
                          filters,
                          JobQueue
                          )

from parse_admarginem import parse_price_admarginem
# from parser import parse_prices
# from parser_for_bot import main_parser_engin
from parser_for_bot_async import main_parser_engin


load_dotenv()

TELEGRAM_TOKEN = os.getenv('BOT_TOKEN')

user_message = ""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        """Команды, которые принимает бот:
        /hello - поздороваться
        /parse - запускает мониторинг цены
        /stop_parsing - выключает мониторинг цен
        /admarginem - находит цену на admarginem.ru
        """
    )


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}')


async def admarginem(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Пришли мне ссылку на кингу на admarginem.ru, и я узнаю цену"
    )


async def parse_and_send_prices(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    # engine = main_parser_engin()
    engine = await main_parser_engin()
    for key, value in engine.items():
        await context.bot.send_message(chat_id=chat_id, text=f'{key} - {value}руб')
    # delay = random.uniform(3, 10)
    # await asyncio.sleep(delay)


async def parse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Собираю цены")

    if not context.job_queue.get_jobs_by_name(str(update.effective_chat.id)):
        context.job_queue.run_repeating(
            parse_and_send_prices,
            interval=120,
            first=2,
            name=str(update.effective_chat.id),
            chat_id=update.effective_chat.id
        )
        await update.message.reply_text("Парсинг запущен и будет обновляться каждые 2 минуты.")
    else:
        await update.message.reply_text("Парсинг уже запущен.")

    # engine = main_parser_engin()
    # for key, value in engine.items():
    #     await update.message.reply_text(f'{key} - {value}руб')


async def stop_parsing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    jobs = context.job_queue.get_jobs_by_name(str(update.effective_chat.id))
    if not jobs:
        await update.message.reply_text("Нет запущенных задач для остановки.")
        return

    for job in jobs:
        job.schedule_removal()

    await update.message.reply_text("Парсинг остановлен.")


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Обработчик ссылок с admarginem"""
    global user_message
    user_message = update.message.text

    if "admarginem.ru" not in user_message:
        await update.message.reply_text(
            'Пока я принимаю только ссылки с admarginem.ru, и команды: см /start')
    else:
        price = parse_price_admarginem(user_message)
        await update.message.reply_text(f'Цена книги: {price}')


def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    job_queue = JobQueue()
    job_queue.set_application(application)

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("hello", hello))
    application.add_handler(CommandHandler("parse", parse))
    application.add_handler(CommandHandler("stop_parsing", stop_parsing))
    application.add_handler(CommandHandler("admarginem", admarginem))

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    application.run_polling()


if __name__ == '__main__':
    main()
