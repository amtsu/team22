from fastapi import FastAPI, HTTPException
from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session
from pydantic import BaseModel

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
Base.metadata.create_all(engine)

# Создаем сессию для взаимодействия с БД
SessionLocal = sessionmaker(bind=engine)

# Создаем FastAPI приложение
app = FastAPI()


# Модель Pydantic для входящих данных
class UserLinkCreate(BaseModel):
    user_id: str
    link: str


# Загрузка и сохранение пользовательских ссылок
@app.post("/links/", response_model=list[str])
def save_user_link(user_link: UserLinkCreate):
    with SessionLocal() as session:
        # Проверяем, есть ли такая ссылка у пользователя
        existing_link = session.query(UserLink).filter_by(user_id=user_link.user_id, link=user_link.link).first()

        if not existing_link:
            # Если такой записи нет, создаем новую
            new_link = UserLink(user_id=user_link.user_id, link=user_link.link)
            session.add(new_link)
            session.commit()

        # Возвращаем все ссылки пользователя
        user_links = session.query(UserLink).filter_by(user_id=user_link.user_id).all()
        return [ul.link for ul in user_links]


# Получение всех ссылок пользователя
@app.get("/links/{user_id}", response_model=list[str])
def get_user_links(user_id: str):
    with SessionLocal() as session:
        # Запрашиваем все ссылки пользователя по user_id
        user_links = session.query(UserLink).filter_by(user_id=user_id).all()
        return [ul.link for ul in user_links]


# Удаление всех ссылок пользователя
@app.delete("/links/{user_id}", response_model=str)
def del_user_links(user_id: str):
    with SessionLocal() as session:
        # Удаляем все записи, соответствующие user_id
        session.query(UserLink).filter_by(user_id=user_id).delete()
        session.commit()

        # Проверяем, остались ли записи для данного пользователя
        remaining_links = session.query(UserLink).filter_by(user_id=user_id).all()

        if not remaining_links:
            return "Ссылки успешно удалены"
        else:
            raise HTTPException(status_code=500, detail="Что-то пошло не так")
