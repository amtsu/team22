from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import session_factory, SubscriptionRepository
from src_smart_lab_ru.text_data import COMPANY_DICT


async def smart_lab_ikb(user_id):
    source = 'smart_lab'

    with (session_factory() as session):
        user_tags = SubscriptionRepository(session).get_user_tags(user_id, source)

        builder = InlineKeyboardBuilder()

        for title, tag in COMPANY_DICT.items():
            if tag in user_tags:
                builder.button(text=f'💹 {title}', callback_data=f'{source}_{tag}')
            else:
                builder.button(text=f'{title}', callback_data=f'{source}_{tag}')

        builder.button(text='⏮ В главное меню', callback_data='main_menu')

        builder.adjust(3)
        return builder.as_markup()
