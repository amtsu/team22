from datetime import datetime
from typing import Optional

from sqlalchemy import Integer, String, ARRAY, DateTime, Boolean, Text, UniqueConstraint
from sqlalchemy.ext.mutable import MutableList
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


# Базовый класс для декларативных моделей с привязкой к метаданным
class Base(DeclarativeBase):
    pass


# Декларативный класс для таблицы Subscription
class SubscriptionBase(Base):
    __tablename__ = 'subscription'

    user_id: Mapped[int] = mapped_column(Integer, nullable=False, primary_key=True)
    source: Mapped[str] = mapped_column(String(32), nullable=False, primary_key=True)
    tag: Mapped[str] = mapped_column(String(32), nullable=False, primary_key=True)

    __table_args__ = (
        UniqueConstraint('user_id', 'source', 'tag', name='user_source_tag'),
    )


# Декларативный класс для таблицы Content
class ContentBase(Base):
    __tablename__ = 'content'

    link: Mapped[str] = mapped_column(String, nullable=False, primary_key=True)
    title: Mapped[str] = mapped_column(String, nullable=False)
    source: Mapped[str] = mapped_column(String(16), nullable=False)
    tags: Mapped[list[str]] = mapped_column(MutableList.as_mutable(ARRAY(String)), nullable=False, default=lambda: [])
    date_time: Mapped[datetime] = mapped_column(DateTime, default=datetime.now)
    status: Mapped[bool] = mapped_column(Boolean, default=False)
    text: Mapped[Optional[str]] = mapped_column(Text, default=None)
    translation: Mapped[Optional[str]] = mapped_column(Text, default=None)
