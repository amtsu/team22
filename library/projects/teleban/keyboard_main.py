from aiogram.utils.keyboard import InlineKeyboardBuilder


async def start_ikb():
    builder = InlineKeyboardBuilder()
    builder.button(text='Новости спорта | sports.ru', callback_data='sports')
    builder.button(text='Спортивный магазин | trial-sport.ru', callback_data='trial-sport')
    builder.button(text='Заглушка #2', callback_data='Заглушка #2')
    builder.button(text='Заглушка #3', callback_data='Заглушка #3')
    builder.button(text='Мои подписки', callback_data='Мои подписки')

    builder.adjust(1)  # количество кнопок в строке
    return builder.as_markup()
