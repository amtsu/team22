from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import sessionmaker

from config import settings

# Создаем синхронный и асинхронный движки
sync_engine = create_engine(
    url=settings.database_url_psycopg,
    echo=False,
)

async_engine = create_async_engine(
    url=settings.database_url_asyncpg,
    echo=False,
)

# Создаем фабрики сессий
session_factory = sessionmaker(bind=sync_engine)
async_session_factory = async_sessionmaker(bind=async_engine)
