import os
import asyncio
import requests
from dotenv import load_dotenv
from telegram import Update
import random
from http import HTTPStatus
from telegram.ext import (ApplicationBuilder,
                          CommandHandler,
                          MessageHandler,
                          ContextTypes,
                          filters,
                          ConversationHandler,
                          JobQueue
                          )

from parse_admarginem import parse_price_admarginem
# from parser import parse_prices
# from parser_for_bot import main_parser_engin
from parser_for_bot_async import main_parser_engin, Parser
# from crud_draft import save_user_link, get_user_links, del_user_links
from crud_db import save_user_link, get_user_links, del_user_links

load_dotenv()

TELEGRAM_TOKEN = os.getenv('BOT_TOKEN')

ASK_LINK = 1
ASK_LINK_ADM = 2

user_message = ""

START_MESSAGE = """Привет! я помогаю мониторить цены.
    /commands - команды управления ботом
    """

COMMANDS = """Команды, которые принимает бот:

    /hello - поздороваться
    /admarginem - находит цену на admarginem.ru

    /save_link - добавляет ссылку в парсер
    /start_parsing - выводит информацию из парсеса цен
    /stop_parsing - выводит информацию из парсеса цен
    /show_links - показывает сохраенные ссылки
    /del_links - удаляет все ваши сохраненные ссылки

    /cancel - завершить текущую операцию
    """


# базовые команды 
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(START_MESSAGE)


async def commands(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(COMMANDS)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}')


async def handle_other_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # global user_message
    # user_message = update.message.text
    await update.message.reply_text(COMMANDS)


# управление парсером: старт, стоп, parse_and_send_prices
async def parse_and_send_prices(context: ContextTypes.DEFAULT_TYPE):
    chat_id = context.job.chat_id
    # links = get_user_links(chat_id)
    engine = await main_parser_engin(chat_id)
    for key, value in engine.items():
        await context.bot.send_message(chat_id=chat_id, text=f'{key} - {value}руб')
    # delay = random.uniform(3, 10)
    # await asyncio.sleep(delay)


async def start_parsing(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Собираю цены"
    )
    # links = get_user_links(update.effective_user.id)
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


# операции с линками эдмаргинем: ask, receive_and_parse
async def admarginem_ask_for_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Пришли мне ссылку на кингу на admarginem.ru, и я узнаю цену"
        "\n\nотмена операции: /cancel"
    )
    return ASK_LINK_ADM


async def receive_and_parse_admarginem_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    """Обработчик ссылок с admarginem"""
    # global user_message
    user_message = update.message.text

    if "admarginem.ru" not in user_message:
        await update.message.reply_text(
            'Пока я принимаю только ссылки с admarginem.ru, и команды: см /start')
    else:
        price = parse_price_admarginem(user_message)
        await update.message.reply_text('Ссылка получена, ищу цену')
        await update.message.reply_text(f'Цена книги: {price}')
    return ConversationHandler.END


# операции с линками: ask, save, show, del
async def ask_for_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Пришлите мне ссылку, на продукт из vkusvill.ru"
        "\nДобавлю ее в список для парсинга"
        "\n\nотмена операции: /cancel"
    )
    return ASK_LINK


async def receive_and_save_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_link = update.message.text
    if "vkusvill.ru/goods/" not in user_link:
        await update.message.reply_text(
            "Неверная ссылка, пока принимаю только продукты из vkusvill.ru")
        return ASK_LINK  # чек, работает ли

    # проверка, что передана рабочая ссылка
    # parser = Parser(user_link)
    try:
        requests.get(user_link)
        # html = await parser.open_html()
    except Exception as e:
        print(e)
        await update.message.reply_text(
            "Неверный формат или нерабочая ссылка.")
        return ASK_LINK   # снова показать инструкцию

    # # проверка, что по ссылке есть цена товара
    # price = parser.main_price_parser(html)
    # if price == "Цена не найдена":
    #     await update.message.reply_text(price)
    #     return ASK_LINK

    await update.message.reply_text('Ссылка получена, сохраняю')
    all_links = save_user_link(update.effective_user.id, user_link)
    # print(all_links)
    await update.message.reply_text(f"Ссылка сохранена: {user_link}")
    return ConversationHandler.END


async def del_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Удаляю все ваши сохраненные ссылки"
    )
    result = del_user_links(update.effective_user.id)
    await update.message.reply_text(result)


async def show_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Собираю ваши линки"
    )
    result = get_user_links(update.effective_user.id)  # ?поменять на update.effective_chat.id
    await update.message.reply_text(result)


# остановка сценариев
async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Операция отменена.")
    return ConversationHandler.END


def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    job_queue = JobQueue()
    job_queue.set_application(application)

    link_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("save_link", ask_for_link)],
        states={
            ASK_LINK: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_and_save_link)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    admarginem_conv_handler = ConversationHandler(
        entry_points=[CommandHandler("admarginem", admarginem_ask_for_link)],
        states={
            ASK_LINK_ADM: [MessageHandler(filters.TEXT & ~filters.COMMAND, receive_and_parse_admarginem_link)],
        },
        fallbacks=[CommandHandler("cancel", cancel)]
    )

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("commands", commands))
    application.add_handler(CommandHandler("hello", hello))
    application.add_handler(CommandHandler("start_parsing", start_parsing))
    application.add_handler(CommandHandler("stop_parsing", stop_parsing))
    application.add_handler(CommandHandler("show_links", show_links))
    application.add_handler(CommandHandler("del_links", del_links))

    application.add_handler(link_conv_handler)
    application.add_handler(admarginem_conv_handler)

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_other_messages))

    application.run_polling()


if __name__ == '__main__':
    main()
