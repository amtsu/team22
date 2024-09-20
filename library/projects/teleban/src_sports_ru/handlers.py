from aiogram import F, Router
from aiogram.types import CallbackQuery


from keyboard_main import start_ikb
from db_managers.subscription_manager import SubscriptionDatabaseManager
from src_sports_ru.keyboards import sports_sections_ikb, sports_nba_ikb

sports_router = Router()


# @sports_router.callback_query(F.data == 'sports')
# async def subscribe_cmd(callback: CallbackQuery):
#     user = callback.from_user
#     main_choice = callback.data
#     await callback.answer(f'Пользователь {user.full_name} подписался на {main_choice}')
#     await callback.message.edit_reply_markup(reply_markup=await sports_sections_ikb())
#
#
# @sports_router.callback_query(F.data == 'sports_nba')
# async def subscribe_cmd(callback: CallbackQuery):
#     user = callback.from_user
#     main_choice = callback.data
#     await callback.answer(f'Пользователь {user.full_name} подписался на {main_choice}')
#     await callback.message.edit_reply_markup(reply_markup=await sports_nba_ikb())


@sports_router.callback_query(F.data.startswith('sports_nba_'))
async def sports_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    source = 'sports'
    tag = callback.data[11:]

    with SubscriptionDatabaseManager() as db:

        user_tags = db.get_user_tags(user_id, source)

        if tag in user_tags:
            db.remove_subscription(user_id, source, tag)
            await callback.answer(f'Вы отписались от {tag}')
            await callback.message.edit_reply_markup(reply_markup=await sports_nba_ikb(user_id))
        else:
            db.add_subscription(user_id, source, tag)
            await callback.answer(f'Вы подписались на {tag})')
            await callback.message.edit_reply_markup(reply_markup=await sports_nba_ikb(user_id))


@sports_router.callback_query(F.data.startswith('sports'))
async def sports_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data
    match data:
        case 'sports':
            await callback.answer(f'Вы выбрали новости спорта | sports.ru')
            await callback.message.edit_reply_markup(reply_markup=await sports_sections_ikb())
        case 'sports_nba':
            await callback.answer(f'Вы выбрали NBA (National Basketball Association)')
            await callback.message.edit_reply_markup(reply_markup=await sports_nba_ikb(user_id))
        case _:
            await callback.answer(f'Возвращаемся в главное меню...')
            await callback.message.edit_reply_markup(reply_markup=await start_ikb())
