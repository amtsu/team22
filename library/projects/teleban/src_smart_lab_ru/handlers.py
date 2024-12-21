from aiogram import F, Router
from aiogram.types import CallbackQuery

from data import session_factory, SubscriptionRepository
from src_smart_lab_ru.keyboards import smart_lab_ikb

smart_lab_router = Router()


@smart_lab_router.callback_query(F.data.startswith('smart_lab_'))
async def handle_subscription(callback: CallbackQuery):
    source = 'smart_lab'
    user_id = callback.from_user.id
    tag = callback.data.removeprefix(f'{source}_')

    with session_factory() as session:
        db = SubscriptionRepository(session)
        user_tags = db.get_user_tags(user_id, source)

        if tag in user_tags:
            db.remove_subscription(user_id, source, tag)
            await callback.answer(f'Вы отписались от {tag}')
            await callback.message.edit_reply_markup(reply_markup=await smart_lab_ikb(user_id))
        else:
            db.add_subscription(user_id, source, tag)
            await callback.answer(f'Вы подписались на {tag}')
            await callback.message.edit_reply_markup(reply_markup=await smart_lab_ikb(user_id))


@smart_lab_router.callback_query(F.data.startswith('smart_lab'))
async def trial_sports_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data

    match data:
        case 'smart_lab':
            await callback.answer(f'Вы выбрали новости компаний IMOEX | smart-lab.ru')
            await callback.message.edit_reply_markup(reply_markup=await smart_lab_ikb(user_id))
