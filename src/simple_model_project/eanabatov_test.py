""" Тесты для проверки класса EANabatovModule """
from eanabatov_module import EANabatovModule, create_instance, clear_txt


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
        with open("eanabatov_module.txt", "r") as test_file:
            test_data = [float(number.strip()) for number in test_file]
            test_data_with_line_number = [
                line_with_numbers for line_with_numbers in enumerate(test_data)
            ]
        assert test_step == test_data_with_line_number
        assert test_object.is_done() is True

    def test_clearing(self):
        """проверка функции очистки файла"""
        assert clear_txt() is None
