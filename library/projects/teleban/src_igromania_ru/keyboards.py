from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import session_factory, SubscriptionRepository
from src_igromania_ru.text_data import IGROMANIA_SECTIONS


async def igromania_ikb(user_id):
    source = 'igromania'

    with session_factory() as session:
        user_tags = SubscriptionRepository(session).get_user_tags(user_id, source)

        builder = InlineKeyboardBuilder()

        for tag in IGROMANIA_SECTIONS:
            if tag in user_tags:
                builder.button(text=f'🎮 {tag}', callback_data=f'{source}_{tag}')
            else:
                builder.button(text=f'{tag}', callback_data=f'{source}_{tag}')

        builder.button(text='⏮ В главное меню', callback_data='main_menu')

        builder.adjust(2)
        return builder.as_markup()
