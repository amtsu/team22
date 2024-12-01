import asyncio
import logging
import sys
from os import getenv

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from handlers import main_router
from services import send_content
from src_overclockers_ru.handlers import overclockers_router
from src_sports_ru.handlers import sports_router
from src_trial_sport_ru.handlers import trial_sport_router

TOKEN = getenv("TELEBAN_TOKEN")

dp = Dispatcher(name=__name__)
dp.include_routers(
    main_router,
    sports_router,
    trial_sport_router,
    overclockers_router,
)


# @dp.message(CommandStart())
# async def command_start_handler(message: Message) -> None:
#     """
#     This handler receives messages with `/start` command
#     """
#     await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=await start_ikb())
#
#
# @dp.message(Command("help"))
# async def command_help_handler(message: Message) -> None:
#     """
#     Этот обработчик отвечает на сообщения с командой `/help`
#     """
#     help_text = HELP_MSG
#     await message.answer(help_text, parse_mode=ParseMode.HTML)
#
#
# @dp.message(Command("info"))
# async def command_info_handler(message: Message) -> None:
#     """
#     Этот обработчик отвечает на сообщения с командой `/info`
#     """
#     info_text = INFO_MSG
#     await message.answer(info_text, parse_mode=ParseMode.HTML)
#
#
# @dp.message(Command("subscriptions"))
# async def command_subscriptions_handler(message: Message) -> None:
#     """
#     Этот обработчик отвечает на сообщения с командой `/subscriptions`
#     """
#     subscriptions_text = SUBSCRIPTIONS_MSG.format(user_name=html.bold(message.from_user.full_name))
#     await message.answer(subscriptions_text, parse_mode=ParseMode.HTML)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.start()
    scheduler.add_job(send_content, 'interval', seconds=30, args=(bot,))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
