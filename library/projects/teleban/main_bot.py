import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from db_managers.content_manager import ContentDatabaseManager, TABLE_NAMES
from db_managers.subscription_manager import SubscriptionDatabaseManager
from keyboard_main import start_ikb
from src_sports_ru.handlers import sports_router
from src_trial_sport_ru.handlers import trial_sport_router
from src_kinopoisk_ru.handlers import kinopoisk_router
from text_content import HELP_MSG, INFO_MSG, SUBSCRIPTIONS_MSG

TOKEN = getenv("TELEBAN_TOKEN")

dp = Dispatcher(name=__name__)
dp.include_routers(
    sports_router,
    trial_sport_router,
    kinopoisk_router
)


async def send_content(table: str, bot: Bot) -> None:
    # проверка наличия нового контента
    with ContentDatabaseManager(table) as content_db:
        if not content_db.check_new_content():
            return None
        new_content = content_db.get_new_content()

    # перебор нового контента для рассылки
    anti_duplicating_list = []  # храним историю рассылки, чтобы исключить дублирование

    for title, link, source, tags in new_content:
        tags = tags.split(',')

        for tag in tags:
            with SubscriptionDatabaseManager() as db:
                if not db.check_exist_subscription(source, tag):  # проверка наличия подписчиков на тег
                    continue
                user_list = db.get_tag_users(source, tag)  # получение пользователей для рассылки

                # перебор пользователей и рассылка им новости
                for user_id in user_list:
                    if (user_id, link) in anti_duplicating_list:  # проверка, что новость ранее не высылалась
                        continue

                    # отправка сообщения
                    await bot.send_message(
                        chat_id=user_id,
                        text=f'<b>{title}</b>\n'
                             f'{link}'
                    )
                    anti_duplicating_list.append((user_id, link))  # добавляем в историю рассылки
                    await asyncio.sleep(1)

        with ContentDatabaseManager('content_sports_ru') as db:
            db.update_status(link)  # меняем статус на "Отправлено"


async def send_content_main(bot: Bot) -> None:
    for table in TABLE_NAMES:
        await send_content(table, bot)


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=await start_ikb())


@dp.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    Этот обработчик отвечает на сообщения с командой `/help`
    """
    help_text = HELP_MSG
    await message.answer(help_text, parse_mode=ParseMode.HTML)


@dp.message(Command("info"))
async def command_info_handler(message: Message) -> None:
    """
    Этот обработчик отвечает на сообщения с командой `/info`
    """
    info_text = INFO_MSG
    await message.answer(info_text, parse_mode=ParseMode.HTML)


@dp.message(Command("subscriptions"))
async def command_subscriptions_handler(message: Message) -> None:
    """
    Этот обработчик отвечает на сообщения с командой `/subscriptions`
    """
    subscriptions_text = SUBSCRIPTIONS_MSG.format(user_name=html.bold(message.from_user.full_name))
    await message.answer(subscriptions_text, parse_mode=ParseMode.HTML)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.start()
    scheduler.add_job(send_content_main, 'interval', seconds=30, args=(bot,))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
