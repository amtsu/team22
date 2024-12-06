from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import session_factory, SubscriptionRepository
from src_habr_com.text_data import HABR_LIST


async def habr_ikb(user_id):
    with session_factory() as session:
        user_tags = SubscriptionRepository(session).get_user_tags(user_id, 'habr')

        builder = InlineKeyboardBuilder()

        for tag in HABR_LIST:
            if tag in user_tags:
                builder.button(text=f'🏃 {tag}', callback_data=f'habr_{tag}')
            else:
                builder.button(text=f'{tag}', callback_data=f'habr_{tag}')

        builder.button(text='⏮ В главное меню', callback_data='main_menu')

        builder.adjust(2)
        return builder.as_markup()
