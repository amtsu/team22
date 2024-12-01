from aiogram import Router, html
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards import start_ikb
from text_data import HELP_MSG, INFO_MSG, SUBS_MSG, START_MSG

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    user_name = message.from_user.full_name or message.from_user.username
    start_text = START_MSG.format(user_name=user_name)
    await message.answer(text=start_text, parse_mode=ParseMode.HTML, reply_markup=await start_ikb())


@main_router.message(Command("help"))
async def command_help_handler(message: Message) -> None:
    """
    Этот обработчик отвечает на сообщения с командой `/help`
    """
    await message.answer(text=HELP_MSG, parse_mode=ParseMode.HTML)


@main_router.message(Command("info"))
async def command_info_handler(message: Message) -> None:
    """
    Этот обработчик отвечает на сообщения с командой `/info`
    """
    await message.answer(text=INFO_MSG, parse_mode=ParseMode.HTML)


@main_router.message(Command("subs"))
async def command_subscriptions_handler(message: Message) -> None:
    """
    Этот обработчик отвечает на сообщения с командой `/subscriptions`
    """
    user_name = message.from_user.full_name or message.from_user.username
    subscriptions_text = SUBS_MSG.format(user_name=user_name)
    await message.answer(text=subscriptions_text, parse_mode=ParseMode.HTML)
