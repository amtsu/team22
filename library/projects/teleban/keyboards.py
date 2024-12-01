from aiogram.utils.keyboard import InlineKeyboardBuilder


async def start_ikb():
    builder = InlineKeyboardBuilder()
    builder.button(text='НОВОСТИ СПОРТА | sports.ru', callback_data='sports')
    builder.button(text='ЦИФРОВЫЕ НОВОСТИ | overclockers.ru', callback_data='overclockers')
    builder.button(text='ТРИАЛ-СПОРТ | trial-sport.ru', callback_data='trial-sport')
    builder.button(text='Мои подписки', callback_data='Мои подписки')

    builder.adjust(1)  # количество кнопок в строке
    return builder.as_markup()
