from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import session_factory, SubscriptionRepository


async def start_ikb():
    builder = InlineKeyboardBuilder()
    builder.button(text='НОВОСТИ СТРАНЫ И МИРА | rbc.ru', callback_data='rbc')
    builder.button(text='НОВОСТИ СПОРТА | sports.ru', callback_data='sports')
    builder.button(text='ЦИФРОВЫЕ НОВОСТИ | overclockers.ru', callback_data='overclockers')
    builder.button(text='ХАБР | habr.com', callback_data='habr')
    builder.button(text='ТРИАЛ-СПОРТ | trial-sport.ru', callback_data='trial-sport')

    builder.adjust(1)  # количество кнопок в строке
    return builder.as_markup()


async def subscriptions_ikb(user_id):
    builder = InlineKeyboardBuilder()

    with session_factory() as session:
        subscriptions = SubscriptionRepository(session).get_user_subscriptions(user_id) or None

    pass