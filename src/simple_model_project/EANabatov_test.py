""" Тесты для проверки класса EANabatovModule """
from EANabatov_module import EANabatovModule


class Test:
    def test_is_singleton(self):
        """
        Проверка на то, что паттерн синглтон действительно реализован правильно.
        Один объект для любого количества созданных объектов.
        """
        first_object = EANabatovModule()
        second_object = EANabatovModule()
        assert first_object == second_object

    def test_create_and_return_object_method(self):
        """Проверка корректной работы метода create_instance"""
        test_object = EANabatovModule()
        assert test_object.create_instance() == test_object
