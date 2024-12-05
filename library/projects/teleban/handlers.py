from aiogram import Router, Bot
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from keyboards import start_ikb
from text_data import HELP_MSG, INFO_MSG, SUBS_MSG, START_MSG, FB_MSG

main_router = Router()


@main_router.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    user = message.from_user
    user_name = user.full_name or user.username or user.id
    text = START_MSG.format(user_name=user_name)
    await message.answer(text=text, parse_mode=ParseMode.HTML, reply_markup=await start_ikb())


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
    Этот обработчик отвечает на сообщения с командой `/subs`
    """
    user = message.from_user
    user_name = user.full_name or user.username or user.id
    text = SUBS_MSG.format(user_name=user_name)
    await message.answer(text=text, reply_markup=await start_ikb())

    # user_id = message.from_user.id
    # user_name = message.from_user.full_name or message.from_user.username
    # subscriptions_text = SUBS_MSG.format(user_name=user_name)
    # await message.answer(text=subscriptions_text, parse_mode=ParseMode.HTML)
    #
    # with session_factory() as session:
    #     subscriptions = SubscriptionRepository(session).get_user_subscriptions(user_id)
    # result = []
    # for source, tag in subscriptions:
    #     result.append(f'{source} {tag}')
    # result = '\n'.join(result)
    #
    # await message.answer(text=result)


@main_router.message()
async def feedback_handler(message: Message, bot: Bot) -> None:
    """
    Этот обработчик переправляет обратную связь пользователей разработчикам.
    """
    admin_id = 297338735
    user = message.from_user.username or message.from_user.id
    text = f'Пользователь {user} написал:\n{message.text}'

    try:
        await bot.send_message(chat_id=admin_id, text=text)
    except Exception as err:
        print(f'Не удалось отправить сообщение admin_id={admin_id}', err)
    finally:
        try:
            await message.answer(FB_MSG)
        except Exception as err:
            print(f'Не удалось отправить сообщение user={user}', err)
