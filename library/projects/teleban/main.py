import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import TOKEN
from keyboard_main import start_ikb
from db_managers.subscription_manager import SubscriptionDatabaseManager

from src_sports_ru.handlers import sports_router
from db_managers.content_manager import SportsDatabaseManager
from src_sports_ru.text_data import NBA_TAGS_LIST

dp = Dispatcher(name=__name__)
dp.include_routers(sports_router)


async def send_out_content(bot: Bot):
    new_content = None
    with SportsDatabaseManager() as db:
        if db.check_new_content():
            new_content = db.get_new_content()
        else:
            return None

    for title, link, tags in new_content:
        tags = tags.split(',')
        anti_duplicating_list = []

        for tag in tags:
            if tag not in NBA_TAGS_LIST:
                continue
            with SubscriptionDatabaseManager() as db:
                if not db.check_exist_subscription('sports', tag):
                    continue
                else:
                    user_list = db.get_tag_users('sports', tag)

            for user_id in user_list:
                if (user_id, link) in anti_duplicating_list:
                    continue

                await bot.send_message(
                    chat_id=user_id,
                    text=f'<b>{title}</b>\n'
                         f'{link}'
                )
                anti_duplicating_list.append((user_id, link))

        with SportsDatabaseManager() as db:
            db.update_status(link)


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
