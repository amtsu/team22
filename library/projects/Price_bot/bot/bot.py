import os
from dotenv import load_dotenv
from telegram import Update
from telegram.ext import (ApplicationBuilder,
                          CommandHandler,
                          MessageHandler,
                          ContextTypes,
                          filters,
                          ConversationHandler
                          )

from parse_admarginem import parse_price_admarginem
from base_parser import parse_prices
from crud_draft import save_user_link, get_user_links, del_user_links

load_dotenv()

TELEGRAM_TOKEN = os.getenv('BOT_TOKEN')

ASK_LINK = 1
ASK_LINK_ADM = 2

user_message = ""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        """Команды, которые принимает бот:
        /hello - поздороваться
        /parse - выводит информацию из парсеса цен
        /admarginem - находит цену на admarginem.ru
        /save_link - добавляет ссылку в парсер
        /del_links - удаляет все ваши сохраненные ссылки
        /cancel - завершить текущую операцию
        """
    )


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(f'Hello, {update.effective_user.first_name}')


async def handle_other_messages(update: Update, context: ContextTypes.DEFAULT_TYPE) -> str:
    # global user_message
    # user_message = update.message.text
    await update.message.reply_text(
        """Команды, которые принимает бот:
        /hello - поздороваться
        /parse - выводит информацию из парсеса цен
        /admarginem - находит цену на admarginem.ru
        /save_link - добавляет ссылку в парсер
        """
    )


async def parse(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Собираю цены"
    )
    result = parse_prices(update.effective_user.id)
    await update.message.reply_text(result)


async def del_links(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "Удаляю все ваши сохраненные ссылки"
    )
    result = del_user_links(update.effective_user.id)
    await update.message.reply_text(result)


async def admarginem_ask_for_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print('sdfsdfds')
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


async def ask_for_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text(
        "Пришлите мне ссылку, добавлю ее в список для парсинга"
        "\n\nотмена операции: /cancel"
    )
    return ASK_LINK


async def receive_and_save_link(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    user_link = update.message.text
    print(user_link)
    # await update.message.reply_text(f"Ссылка сохранена: {user_link}")
    await update.message.reply_text('Ссылка получена, сохраняю')
    all_links = save_user_link(update.effective_user.id, user_link)
    print(all_links)
    await update.message.reply_text("Ссылка сохранена")
    return ConversationHandler.END


async def cancel(update: Update, context: ContextTypes.DEFAULT_TYPE) -> int:
    await update.message.reply_text("Операция отменена.")
    return ConversationHandler.END


def main() -> None:
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

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
    application.add_handler(CommandHandler("hello", hello))
    application.add_handler(CommandHandler("parse", parse))
    application.add_handler(CommandHandler("del_links", del_links))

    application.add_handler(link_conv_handler)
    application.add_handler(admarginem_conv_handler)

    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_other_messages))

    application.run_polling()


if __name__ == '__main__':
    main()
