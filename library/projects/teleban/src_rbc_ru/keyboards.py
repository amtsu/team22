from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import SubscriptionRepository, session_factory
from src_rbc_ru.text_data import RBC_DICT


async def rbc_ikb(user_id):
    with session_factory() as session:
        user_tags = SubscriptionRepository(session).get_user_tags(user_id, 'rbc')

        builder = InlineKeyboardBuilder()

        for tag in RBC_DICT:
            if tag in user_tags:
                builder.button(text=f'💼 {tag}', callback_data=f'rbc_{tag}')
            else:
                builder.button(text=f'{tag}', callback_data=f'rbc_{tag}')

        builder.button(text='⏮ В главное меню', callback_data='sports_main_menu')

        builder.adjust(2)
        return builder.as_markup()
