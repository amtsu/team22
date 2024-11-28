from aiogram import F, Router
from aiogram.types import CallbackQuery

from db_managers.subscription_manager import SubscriptionDatabaseManager
from src_kinopoisk_ru.keyboards import kinopoisk_ikb

kinopoisk_router = Router()


@kinopoisk_router.callback_query(F.data.startswith('kinopoisk_'))
async def handle_subscription(callback: CallbackQuery):
    source = 'kinopoisk'
    user_id = callback.from_user.id
    tag = callback.data.removeprefix(f'{source}_')

    with SubscriptionDatabaseManager() as db:
        user_tags = db.get_user_tags(user_id, source)

        if tag in user_tags:
            db.remove_subscription(user_id, source, tag)
            await callback.answer(f'Вы отписались от {tag}')
            await callback.message.edit_reply_markup(reply_markup=await kinopoisk_ikb(user_id))
        else:
            db.add_subscription(user_id, source, tag)
            await callback.answer(f'Вы подписались на {tag})')
            await callback.message.edit_reply_markup(reply_markup=await kinopoisk_ikb(user_id))


@kinopoisk_router.callback_query(F.data.startswith('kinopoisk'))
async def kinopoisk_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data
    match data:
        case 'kinopoisk':
            await callback.answer(f'Вы выбрали новости кинопоиска | kinopoisk.ru/media/')
            await callback.message.edit_reply_markup(reply_markup=await kinopoisk_ikb(user_id))