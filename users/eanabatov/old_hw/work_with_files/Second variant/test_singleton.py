from main import SingletonPhonebook


def test_singleton():
    """THIS IS SINGLETOOOOOOOOOOOON !!!"""
    first_obj = SingletonPhonebook()
    second_obj = SingletonPhonebook()
    assert first_obj == second_obj


def test_global_instance_penetration():
    """
    Меняем переменную класса для проверки главного минуса singleton.
    Приватную переменную класса хоть и нельзя изменить извне объекта,
    но ее можно изменить в экземпляре объекта этого класса.
    """
    first = SingletonPhonebook()
    first.__instance = 123
    second = SingletonPhonebook()
    assert second.__instance == 123

