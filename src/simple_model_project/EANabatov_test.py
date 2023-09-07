""" Тесты для проверки класса EANabatovModule """
from EANabatov_module import EANabatovModule
from EANabatov_module import create_instance


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
        assert create_instance() == test_object

    def test_name(self):
        assert create_instance().name() == "EANabatovModule"

    def test_main_work(self):
        test_object = EANabatovModule()
        test_object.prepare()
        test_object.step()
        assert test_object.is_done() == False

    def test_second_work(self):
        test_object = EANabatovModule()
        test_object.prepare()
        test_object.step()
        assert test_object.the_end() == 1
