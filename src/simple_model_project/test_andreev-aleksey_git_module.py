import pytest


from andreev_aleksey_git_module import Сountdown, createinstance

# Тесты взял у Александра 

@pytest.fixture
def class_instance() -> Сountdown:
    return Сountdown()


def test_createinstance(class_instance: Сountdown):
    cls_instance = createinstance()
    assert type(cls_instance) == type(class_instance)


def test_name_method(class_instance: Сountdown):
    assert "Сountdown" == class_instance.name()


def test_prepare_method(class_instance: Сountdown):
    assert class_instance.prepare() is None
