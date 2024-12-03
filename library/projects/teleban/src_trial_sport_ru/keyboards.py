from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import session_factory, SubscriptionRepository
from src_trial_sport_ru.text_data import TRIAL_SPORT_LIST


async def trial_sport_ikb(user_id):
    with session_factory() as session:
        user_tags = SubscriptionRepository(session).get_user_tags(user_id, 'trial-sport')

        builder = InlineKeyboardBuilder()

        for tag in TRIAL_SPORT_LIST:
            if tag in user_tags:
                builder.button(text=f'🏃 {tag}', callback_data=f'trial-sport_{tag}')
            else:
                builder.button(text=f'{tag}', callback_data=f'trial-sport_{tag}')

        builder.button(text='⏮ В главное меню', callback_data='sports_main_menu')

        builder.adjust(2)
        return builder.as_markup()
