import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from db_managers.content_manager import ContentDatabaseManager
from db_managers.subscription_manager import SubscriptionDatabaseManager
from keyboard_main import start_ikb
from src_sports_ru.handlers import sports_router
from src_sports_ru.text_data import NBA_TAGS_LIST

TOKEN = getenv("TELEBAN_TOKEN")

dp = Dispatcher(name=__name__)
dp.include_routers(sports_router)


async def send_out_content(bot: Bot):
    """
    Функция рассылки нового контента пользователям (пока только спортс.ру).
    """
    # проверка наличия нового контента
    with ContentDatabaseManager('content_sports_ru') as db:
        if db.check_new_content():
            new_content = db.get_new_content()
        else:
            return None

    # перебор нового контента для рассылки
    for title, link, tags in new_content:
        tags = tags.split(',')
        anti_duplicating_list = []  # храним историю рассылки, чтобы исключить дублирование

        # перебор тегов новости
        for tag in tags:
            if tag not in NBA_TAGS_LIST:  # проверка, есть ли тег в предложенных для пользователя
                continue

            with SubscriptionDatabaseManager() as db:
                if not db.check_exist_subscription('sports', tag):  # проверка наличия подписчиков на тег
                    continue
                else:
                    user_list = db.get_tag_users('sports', tag)  # получение пользователей для рассылки

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

        with ContentDatabaseManager('content_sports_ru') as db:
            db.update_status(link)  # меняем статус на "Отправлено"


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=await start_ikb())


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.start()
    scheduler.add_job(send_out_content, 'interval', seconds=20, args=(bot,))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
