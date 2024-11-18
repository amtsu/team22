import pytest

from sqlalchemy.exc import NoResultFound
from sqlalchemy.orm import sessionmaker

from data import SubscriptionBase, SubscriptionRepository, sync_engine


@pytest.fixture(scope="module")
def session():
    # Создаем движок и сессию для тестовой базы данных PostgreSQL
    engine = sync_engine
    SubscriptionBase.metadata.create_all(engine)
    test_session = sessionmaker(bind=engine)
    session = test_session()

    yield session
    session.rollback()
    # Очистка всех данных из таблиц после завершения всех тестов
    SubscriptionBase.metadata.drop_all(engine)
    session.close()
    engine.dispose()


def test_add_subscription(session):
    # Тест добавления подписки
    subscription = SubscriptionRepository.add_subscription(session, user_id=1, source="test_source", tag="test_tag")
    assert subscription.user_id == 1
    assert subscription.source == "test_source"
    assert subscription.tag == "test_tag"


def test_remove_subscription(session):
    # Тест удаления подписки
    SubscriptionRepository.add_subscription(session, user_id=2, source="test_source", tag="test_tag")
    result = SubscriptionRepository.remove_subscription(session, user_id=2, source="test_source", tag="test_tag")
    assert result is True
    with pytest.raises(NoResultFound):
        # Проверка, что подписка больше не существует
        SubscriptionRepository.remove_subscription(session, user_id=2, source="test_source", tag="test_tag")


def test_check_exist_subscription(session):
    # Тест проверки существования подписки
    SubscriptionRepository.add_subscription(session, user_id=3, source="test_source", tag="unique_tag")
    exists = SubscriptionRepository.check_exist_subscription(session, source="test_source", tag="unique_tag")
    assert exists is True
    # Проверка для несуществующей подписки
    not_exists = SubscriptionRepository.check_exist_subscription(session, source="test_source", tag="missing_tag")
    assert not_exists is False


def test_get_user_tags(session):
    # Тест получения тегов пользователя
    SubscriptionRepository.add_subscription(session, user_id=4, source="test_source", tag="tag1")
    SubscriptionRepository.add_subscription(session, user_id=4, source="test_source", tag="tag2")
    tags = SubscriptionRepository.get_user_tags(session, user_id=4, source="test_source")
    assert "tag1" in tags
    assert "tag2" in tags


def test_get_tag_users(session):
    # Тест получения пользователей по тегу
    SubscriptionRepository.add_subscription(session, user_id=5, source="test_source", tag="common_tag")
    SubscriptionRepository.add_subscription(session, user_id=6, source="test_source", tag="common_tag")
    users = SubscriptionRepository.get_tag_users(session, source="test_source", tag="common_tag")
    assert 5 in users
    assert 6 in users
    assert len(users) == 2
