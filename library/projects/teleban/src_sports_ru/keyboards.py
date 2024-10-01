from aiogram.utils.keyboard import InlineKeyboardBuilder

from db_managers.subscription_manager import SubscriptionDatabaseManager
from src_sports_ru.text_data import NBA_TAGS_LIST


async def sports_sections_ikb():
    builder = InlineKeyboardBuilder()
    builder.button(text='NBA (National Basketball Association)', callback_data='sports_nba')
    builder.button(text='⏮ В главное меню', callback_data='sports_main_menu')

    builder.adjust(1)
    return builder.as_markup()


async def sports_nba_ikb(user_id):
    with SubscriptionDatabaseManager() as db:
        user_tags = db.get_user_tags(user_id, 'sports')

    builder = InlineKeyboardBuilder()

    for tag in NBA_TAGS_LIST:
        if tag in user_tags:
            builder.button(text=f'🏀 {tag}', callback_data=f'sports_nba_{tag}')
        else:
            builder.button(text=f'{tag}', callback_data=f'sports_nba_{tag}')

    builder.button(text='⏮ В главное меню', callback_data='sports_main_menu')

    builder.adjust(3)
    return builder.as_markup()
