from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from data.config import settings

# Создаем синхронный и асинхронный движки
sync_engine = create_engine(
    url=settings.database_url_psycopg,
    echo=True,
)

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=True,
)

# Создаем фабрики сессий
session_factory = sessionmaker(bind=sync_engine)
async_session_factory = async_sessionmaker(bind=async_engine)
