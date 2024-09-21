from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Создаем базовый класс для моделей
Base = declarative_base()


# Определяем модель для таблицы user_links
class UserLink(Base):
    __tablename__ = 'user_links'

    id = Column(Integer, primary_key=True, autoincrement=True)  # Уникальный идентификатор
    user_id = Column(String, nullable=False)  # ID пользователя
    link = Column(String, nullable=False)  # Ссылка


# Создаем движок для подключения к БД
engine = create_engine('sqlite:///database.db')

# Создаем все таблицы, если их нет
Base.metadata.create_all(engine)

# Создаем сессию для взаимодействия с БД
Session = sessionmaker(bind=engine)
session = Session()


def save_user_link(user_id, link):
    # Проверяем, есть ли такая ссылка у пользователя
    existing_link = session.query(UserLink).filter_by(user_id=str(user_id), link=link).first()

    if not existing_link:
        # Если такой записи нет, создаем новую
        new_link = UserLink(user_id=str(user_id), link=link)
        session.add(new_link)
        session.commit()

    # Возвращаем все ссылки пользователя
    user_links = session.query(UserLink).filter_by(user_id=str(user_id)).all()
    return [ul.link for ul in user_links]


def get_user_links(user_id):
    # Запрашиваем все ссылки пользователя по user_id
    user_links = session.query(UserLink).filter_by(user_id=str(user_id)).all()

    # Возвращаем только ссылки
    return [ul.link for ul in user_links]


def del_user_links(user_id):
    # Удаляем все записи, соответствующие user_id
    session.query(UserLink).filter_by(user_id=str(user_id)).delete()
    session.commit()

    # Проверяем, остались ли записи для данного пользователя
    remaining_links = session.query(UserLink).filter_by(user_id=str(user_id)).all()

    if not remaining_links:
        result = "Ссылки успешно удалены"
    else:
        result = "Что-то пошло не так"

    return result
