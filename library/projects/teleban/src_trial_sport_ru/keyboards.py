from aiogram.utils.keyboard import InlineKeyboardBuilder

from db_managers.subscription_manager import SubscriptionDatabaseManager
from src_trial_sport_ru.text_data import TRIAL_SPORT_LIST

async def trial_sport_ikb(user_id):
    with SubscriptionDatabaseManager() as db:
        user_tags = db.get_user_tags(user_id, 'trial-sport')

        builder = InlineKeyboardBuilder()

        for tag in TRIAL_SPORT_LIST:
            if tag in user_tags:
                builder.button(text=f'🏃‍♀️ {tag}', callback_data=f'trial-sport{tag}')
            else:
                builder.button(text=f'{tag}', callback_data=f'trial-sport{tag}')

        builder.button(text='⏮ В главное меню', callback_data='sports_main_menu')

        builder.adjust(3)
        return builder.as_markup()