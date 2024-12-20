from aiogram import F, Router
from aiogram.types import CallbackQuery

from data import session_factory, SubscriptionRepository
from src_sports_ru.keyboards import sports_sections_ikb, sports_nba_ikb, sports_nfl_ikb, sports_nhl_ikb

sports_router = Router()
sports_data = {
    'sports_nba': sports_nba_ikb,
    'sports_nfl': sports_nfl_ikb,
    'sports_nhl': sports_nhl_ikb,
}


async def handle_subscription(callback: CallbackQuery, source: str, keyboard_func):
    user_id = callback.from_user.id
    tag = callback.data.removeprefix(f'{source}_')

    with session_factory() as session:
        db = SubscriptionRepository(session)
        user_tags = db.get_user_tags(user_id, source)

        if tag in user_tags:
            db.remove_subscription(user_id, source, tag)
            await callback.answer(f'Вы отписались от {tag}')
        else:
            db.add_subscription(user_id, source, tag)
            await callback.answer(f'Вы подписались на {tag}')

        # Обновляем клавиатуру с учётом подписок пользователя
        await callback.message.edit_reply_markup(reply_markup=await keyboard_func(user_id))


@sports_router.callback_query(F.data.startswith(tuple(sports_data.keys())))
async def sports_callback(callback: CallbackQuery):
    # Определяем нужный источник и клавиатуру на основе данных callback
    for source, keyboard_func in sports_data.items():
        if callback.data.startswith(source):
            await handle_subscription(callback, source, keyboard_func)


@sports_router.callback_query(F.data.startswith('sports'))
async def sports_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data

    match data:
        case 'sports':
            await callback.answer(f'Вы выбрали новости спорта | sports.ru')
            await callback.message.edit_reply_markup(reply_markup=await sports_sections_ikb())
        case 'sports_nba':
            await callback.answer(f'Вы выбрали NBA')
            await callback.message.edit_reply_markup(reply_markup=await sports_nba_ikb(user_id))
        case 'sports_nfl':
            await callback.answer(f'Вы выбрали NFL')
            await callback.message.edit_reply_markup(reply_markup=await sports_nfl_ikb(user_id))
        case 'sports_nhl':
            await callback.answer(f'Вы выбрали NHL')
            await callback.message.edit_reply_markup(reply_markup=await sports_nhl_ikb(user_id))
