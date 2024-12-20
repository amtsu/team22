from aiogram.utils.keyboard import InlineKeyboardBuilder

from data import session_factory, SubscriptionRepository


async def start_ikb():
    builder = InlineKeyboardBuilder()
    builder.button(text='НОВОСТИ СТРАНЫ И МИРА | rbc.ru', callback_data='rbc')
    builder.button(text='НОВОСТИ СПОРТА | sports.ru', callback_data='sports')
    builder.button(text='ЦИФРОВЫЕ НОВОСТИ | overclockers.ru', callback_data='overclockers')
    builder.button(text='ИГРОВЫЕ НОВОСТИ | igromania.ru', callback_data='igromania')
    builder.button(text='КОМПАНИИ IMOEX | smart-lab.ru', callback_data='smart_lab')
    builder.button(text='ХАБР (в разработке) | habr.com', callback_data='habr')

    builder.adjust(1)  # количество кнопок в строке
    return builder.as_markup()
