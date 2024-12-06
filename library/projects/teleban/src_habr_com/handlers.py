from aiogram import F, Router
from aiogram.types import CallbackQuery

from data import session_factory, SubscriptionRepository
from src_habr_com.keyboards import habr_ikb

habr_router = Router()


@habr_router.callback_query(F.data.startswith('habr_'))
async def handle_subscription(callback: CallbackQuery):
    source = 'habr'
    user_id = callback.from_user.id
    tag = callback.data.removeprefix(f'{source}_')

    with session_factory() as session:
        db = SubscriptionRepository(session)
        user_tags = db.get_user_tags(user_id, source)

        if tag in user_tags:
            db.remove_subscription(user_id, source, tag)
            await callback.answer(f'Вы отписались от {tag}')
            await callback.message.edit_reply_markup(reply_markup=await habr_ikb(user_id))
        else:
            db.add_subscription(user_id, source, tag)
            await callback.answer(f'Вы подписались на {tag}')
            await callback.message.edit_reply_markup(reply_markup=await habr_ikb(user_id))


@habr_router.callback_query(F.data.startswith('habr'))
async def habr_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data
    match data:
        case 'habr':
            await callback.answer(f'Вы выбрали Хабр | habr.com')
            await callback.message.edit_reply_markup(reply_markup=await habr_ikb(user_id))
