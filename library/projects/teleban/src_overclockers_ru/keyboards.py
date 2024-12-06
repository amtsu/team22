from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import session_factory, SubscriptionRepository
from src_overclockers_ru.text_data import OVERCLOCKERS_SECTIONS


async def overclockers_ikb(user_id):
    with session_factory() as session:
        user_tags = SubscriptionRepository(session).get_user_tags(user_id, 'overclockers')

        builder = InlineKeyboardBuilder()

        for tag in OVERCLOCKERS_SECTIONS:
            if tag in user_tags:
                builder.button(text=f'💻 {tag}', callback_data=f'overclockers_{tag}')
            else:
                builder.button(text=f'{tag}', callback_data=f'overclockers_{tag}')

        builder.button(text='⏮ В главное меню', callback_data='main_menu')

        builder.adjust(2)
        return builder.as_markup()
