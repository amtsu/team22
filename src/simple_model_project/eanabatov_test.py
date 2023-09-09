""" Тесты для проверки класса EANabatovModule """
from eanabatov_module import EANabatovModule
from eanabatov_module import create_instance


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
        test_object.__prepare()
        test_object.step()
        assert test_object.__is_done() is False
        assert test_object.the_end() == 1
