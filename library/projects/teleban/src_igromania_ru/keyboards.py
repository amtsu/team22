from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import session_factory, SubscriptionRepository
from src_igromania_ru.text_data import IGROMANIA_RU_DICTIONARY


async def igromania_ikb(user_id):
    with session_factory() as session:
        user_tags = SubscriptionRepository(session).get_user_tags(user_id, 'igromania')

        builder = InlineKeyboardBuilder()

        for tag in IGROMANIA_RU_DICTIONARY:
            if tag in user_tags:
                builder.button(text=f'🎮 {tag}', callback_data=f'igromania_{tag}')
            else:
                builder.button(text=f'{tag}', callback_data=f'igromania_{tag}')

        builder.button(text='⏮ В главное меню', callback_data='main_menu')

        builder.adjust(2)
        return builder.as_markup()
