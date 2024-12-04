import asyncio
from typing import Sequence

from aiogram import Bot
from aiogram.exceptions import TelegramBadRequest

from data import session_factory, ContentRepository, ContentBase, SubscriptionRepository


async def send_content(bot: Bot) -> None:
    with session_factory() as session:
        db = ContentRepository(session)
        if not db.check_new_content():  # проверка наличия нового контента
            return None
        new_content: Sequence[ContentBase] = db.get_new_content()  # получение нового контента

    anti_duplicating_list = []  # храним историю рассылки, чтобы исключить дублирование

    # перебор нового контента для рассылки
    for instance in new_content:
        link = instance.link
        source = instance.source
        tags = instance.tags
        title = instance.title

        # перебор тегов в новости/статье
        for tag in tags:
            with session_factory() as session:
                db = SubscriptionRepository(session)
                if not db.check_exist_subscription(source, tag):  # проверка наличия подписок на тег
                    continue
                user_list = db.get_tag_users(source, tag)  # получаем список подписанных пользователей

            # перебор пользователей и рассылка им новости/статьи
            for user_id in user_list:
                if (user_id, link) in anti_duplicating_list:  # проверка, что новость ранее не высылалась
                    continue

                # отправка сообщения
                try:
                    await bot.send_message(
                        chat_id=user_id,
                        text=f'<b>{title}</b>\n'
                             f'{link}'
                    )
                except TelegramBadRequest as err:
                    print(f'user_id={user_id}', err)

                anti_duplicating_list.append((user_id, link))  # добавляем в историю рассылки
                # await asyncio.sleep(1)  # не забыть убрать в проде

        with session_factory() as session:
            ContentRepository(session).update_status(link)  # смена статуса на "отправлено"
