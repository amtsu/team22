from datetime import datetime, timedelta
from typing import Sequence

from sqlalchemy import select, exists, update, delete
from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import Session

from data.models import SubscriptionBase, ContentBase


class SubscriptionRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_subscription(self, user_id: int, source: str, tag: str) -> SubscriptionBase:
        """Добавляет новую запись."""
        instance = SubscriptionBase(user_id=user_id, source=source, tag=tag)
        self.session.add(instance)
        self.session.commit()
        return instance

    def remove_subscription(self, user_id: int, source: str, tag: str) -> bool:
        """Удаляет запись из базы данных по user_id, source и tag."""
        instance = self._get_subscription(user_id, source, tag)
        self.session.delete(instance)
        self.session.commit()
        return True

    def check_exist_subscription(self, source: str, tag: str) -> bool:
        """Проверяет наличие подписок на tag и source."""
        return self.session.execute(
            select(exists().where(SubscriptionBase.source == source, SubscriptionBase.tag == tag))
        ).scalar()

    def get_user_tags(self, user_id: int, source: str) -> Sequence[str]:
        """Возвращает все теги пользователя по user_id и source."""
        return self.session.execute(
            select(SubscriptionBase.tag).where(
                SubscriptionBase.user_id == user_id, SubscriptionBase.source == source
            )
        ).scalars().all()

    def get_tag_users(self, source: str, tag: str) -> Sequence[int]:
        """Возвращает всех пользователей, подписанных на определенный тег и источник."""
        return self.session.execute(
            select(SubscriptionBase.user_id).where(
                SubscriptionBase.source == source, SubscriptionBase.tag == tag
            )
        ).scalars().all()

    def _get_subscription(self, user_id: int, source: str, tag: str) -> SubscriptionBase:
        """Возвращает запись подписки по user_id, source и tag, или вызывает исключение, если запись не найдена."""
        instance = self.session.execute(
            select(SubscriptionBase).where(
                SubscriptionBase.user_id == user_id,
                SubscriptionBase.source == source,
                SubscriptionBase.tag == tag
            )
        ).scalar_one_or_none()

        if instance is None:
            raise NoResultFound(f"Запись с user_id={user_id}, source='{source}' и tag='{tag}' не найдена.")

        return instance


class ContentRepository:
    def __init__(self, session: Session):
        self.session = session

    def add_content(self, title: str, link: str, source: str, tags: list[str]) -> ContentBase:
        """Добавляет новую запись в таблицу content."""
        instance = ContentBase(
            title=title,
            link=link,
            source=source,
            tags=tags,
            date_time=datetime.now(),
            status=False
        )
        self.session.add(instance)
        self.session.commit()
        return instance

    def add_all_content(self, instances: list[ContentBase]) -> bool:
        """Добавляет список контента в таблицу content."""
        # self.session.add_all(instances)

        for instance in instances:
            if self.exists_by_link(instance.link):
                continue

            self.session.add(instance)

        self.session.commit()
        return True

    def remove_content(self, link: str) -> bool:
        """Удаляет запись из таблицы content по ссылке."""
        instance = self._get_content_by_link(link)
        self.session.delete(instance)
        self.session.commit()
        return True

    def update_status(self, link: str) -> bool:
        """Обновляет статус записи по ссылке."""
        if not self.exists_by_link(link):
            raise NoResultFound(f"Запись с link='{link}' не найдена.")

        # Обновление статуса
        self.session.execute(
            update(ContentBase).where(ContentBase.link == link).values(status=True)
        )
        self.session.commit()
        return True

    def check_new_content(self) -> bool:
        """Проверяет наличие новых записей со статусом False."""
        return self.session.execute(
            select(exists().where(ContentBase.status.is_(False)))
        ).scalar()

    def get_new_content(self) -> Sequence[ContentBase]:
        """Возвращает все новые записи в виде списка объектов ContentBase."""
        return self.session.execute(
            select(ContentBase).where(ContentBase.status.is_(False))
        ).scalars().all()

    def exists_by_link(self, link: str) -> bool:
        """Проверяет наличие записи по ссылке."""
        return self.session.execute(
            select(exists().where(ContentBase.link == link))
        ).scalar()

    def add_tag(self, link: str, new_tag: str) -> bool:
        """Добавляет новый тег в список tags, если его еще нет."""
        instance = self._get_content_by_link(link)

        if new_tag not in instance.tags:
            instance.tags.append(new_tag)
            self.session.commit()
            return True

        return False

    def _get_content_by_link(self, link: str) -> ContentBase:
        """Возвращает запись контента по ссылке или вызывает исключение, если запись не найдена."""
        instance = self.session.execute(
            select(ContentBase).where(ContentBase.link == link)
        ).scalar_one_or_none()

        if instance is None:
            raise NoResultFound(f"Запись с link='{link}' не найдена.")

        return instance

    def remove_old_content(self) -> None:
        """
        Удаляет записи, которые старше 14 дней и у которых статус True.
        """
        required_time = datetime.now() - timedelta(days=14)

        self.session.execute(
            delete(ContentBase)
            .where(ContentBase.status is True)
            .where(ContentBase.date_time < required_time)
        )

        self.session.commit()
