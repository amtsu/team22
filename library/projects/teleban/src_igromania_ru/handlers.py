from aiogram import F, Router
from aiogram.types import CallbackQuery

from data import session_factory, SubscriptionRepository
from src_igromania_ru.keyboards import igromania_ikb

igromania_router = Router()


@igromania_router.callback_query(F.data.startswith('igromania_'))
async def handle_subscription(callback: CallbackQuery):
    source = 'igromania'
    user_id = callback.from_user.id
    tag = callback.data.removeprefix(f'{source}_')

    with session_factory() as session:
        db = SubscriptionRepository(session)
        user_tags = db.get_user_tags(user_id, source)

        if tag in user_tags:
            db.remove_subscription(user_id, source, tag)
            await callback.answer(f'Вы отписались от {tag}')
            await callback.message.edit_reply_markup(reply_markup=await igromania_ikb(user_id))
        else:
            db.add_subscription(user_id, source, tag)
            await callback.answer(f'Вы подписались на {tag}')
            await callback.message.edit_reply_markup(reply_markup=await igromania_ikb(user_id))


@igromania_router.callback_query(F.data.startswith('igromania'))
async def igromania_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data
    match data:
        case 'igromania':
            await callback.answer(f'Вы выбрали Игроманию | igromania.ru')
            await callback.message.edit_reply_markup(reply_markup=await igromania_ikb(user_id))
