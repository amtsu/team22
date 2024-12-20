import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums.parse_mode import ParseMode
from apscheduler.schedulers.asyncio import AsyncIOScheduler

from config import settings
from handlers import main_router
from services import send_content
from src_habr_com.handlers import habr_router
from src_igromania_ru.handlers import igromania_router
from src_overclockers_ru.handlers import overclockers_router
from src_rbc_ru.handlers import rbc_router
from src_smart_lab_ru.handlers import smart_lab_router
from src_sports_ru.handlers import sports_router

TOKEN = settings.TELEBAN_TOKEN

dp = Dispatcher(name=__name__)
dp.include_routers(
    main_router,
    sports_router,
    igromania_router,
    overclockers_router,
    rbc_router,
    habr_router,
    smart_lab_router,
)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    scheduler = AsyncIOScheduler(timezone='Europe/Moscow')
    scheduler.start()
    scheduler.add_job(send_content, 'interval', seconds=60, args=(bot,))
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
