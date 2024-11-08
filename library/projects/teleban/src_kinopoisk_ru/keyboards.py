from aiogram.utils.keyboard import InlineKeyboardBuilder

from db_managers.subscription_manager import SubscriptionDatabaseManager
from src_kinopoisk_ru.text_data import KINOPOISK_RU_DICTIONARY

async def kinopoisk_ikb(user_id):
    with SubscriptionDatabaseManager() as db:
        user_tags = db.get_user_tags(user_id, 'kinopoisk')

        builder = InlineKeyboardBuilder()

        for tag in KINOPOISK_RU_DICTIONARY.keys():
            if tag in user_tags:
                builder.button(text=f'🎬 {tag}', callback_data=f'kinopoisk_{tag}')
            else:
                builder.button(text=f'{tag}', callback_data=f'kinopoisk_{tag}')

        builder.button(text='⏮ В главное меню', callback_data='sports_main_menu')

        builder.adjust(3)
        return builder.as_markup()
