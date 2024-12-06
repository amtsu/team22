from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import SubscriptionRepository, session_factory
from src_rbc_ru.text_data import AUTO_DICT


async def auto_ikb(user_id):
    with session_factory() as session:
        user_tags = SubscriptionRepository(session).get_user_tags(user_id, 'auto')

        builder = InlineKeyboardBuilder()

        for tag in AUTO_DICT:
            if tag in user_tags:
                builder.button(text=f'💼 {tag}', callback_data=f'auto_{tag}')
            else:
                builder.button(text=f'{tag}', callback_data=f'auto_{tag}')

        builder.button(text='⏮ В главное меню', callback_data='main_menu')

        builder.adjust(1)
        return builder.as_markup()
