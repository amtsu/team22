@sports_router.callback_query(F.data.startswith('trial-sport'))
async def handle_subscription(callback: CallbackQuery, source: str, keyboard_func):
    user_id = callback.from_user.id
    tag = callback.data.removeprefix(f'{source}_')

    with SubscriptionDatabaseManager() as db:

        user_tags = db.get_user_tags(user_id, source)

        if tag in user_tags:
            db.remove_subscription(user_id, source, tag)
            await callback.answer(f'Вы отписались от {tag}')
            await callback.message.edit_reply_markup(reply_markup=await trial_sport_ikb(user_id))
        else:
            db.add_subscription(user_id, source, tag)
            await callback.answer(f'Вы подписались на {tag})')
            await callback.message.edit_reply_markup(reply_markup=await trial_sport_ikb(user_id))

@sports_router.callback_query(F.data.startswith('trial-sport'))
async def sports_callback(callback: CallbackQuery):
    user_id = callback.from_user.id
    data = callback.data
    match data:
        case 'trial-sport':
            await callback.answer(f'Вы выбрали спортивный магазин | trial-sport.ru')
            await callback.message.edit_reply_markup(reply_markup=await trial_sport_ikb(user_id))
