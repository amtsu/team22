""" Тесты для проверки класса EANabatovModule """
from eanabatov_module import EANabatovModule, create_instance


class Test:
    """тесты для проверки eanabatov_module"""

    def test_is_singleton(self):
        """
        Проверка на то, что паттерн синглтон действительно реализован правильно.
        Один объект для любого количества созданных объектов.
        """
        first_object = EANabatovModule()
        second_object = EANabatovModule()
        assert first_object == second_object

    def test_object(self):
        """Проверка корректной работы метода create_instance"""
        assert isinstance(create_instance(), EANabatovModule)

    def test_name(self):
        """Проверка работы метода name"""
        assert create_instance().name() == "EANabatovModule"

    def test_main_work(self):
        """проверка основного функционала класса"""
        test_object = EANabatovModule()
        test_object.prepare()
        test_step = test_object.step()
        assert isinstance(test_step[0], float)
        assert isinstance(test_step[1], int)
        assert test_object.is_done() is True
