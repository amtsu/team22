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
        """Проверка основного функционала класса"""
        test_object = EANabatovModule()
        test_object.prepare()
        test_object.step()
        assert test_object.is_done() is False
        test_object.step()
        assert test_object.is_done() is False
        test_object.step()
        assert test_object.is_done() is False
        test_object.step()
        assert test_object.is_done() is False
        test_object.step()
        assert test_object.is_done() is True

    def test_get_state(self, monkeypatch):
        """Тест проверки процедуры get_state()"""

        def monk_state(*args):
            return {"var A": "10.235667", "var B": "73"}

        monkeypatch.setattr(target=EANabatovModule, name="get_state", value=monk_state)

        test_object = EANabatovModule()
        test_object.prepare()
        test_object.step()
        assert test_object.get_state() == {"var A": "10.235667", "var B": "73"}

    def test_step_and_prepare(self):
        """Тест проверки процедуры step() и prepare()"""
        test_object = EANabatovModule()
        test_object.step()
        assert test_object.is_done() is True
        assert test_object.get_state() == {}

    def test_is_done(self):
        """Тест проверки процедуры step()"""
        test_object = EANabatovModule()
        test_object.prepare()
        test_counter: int = 0
        assert test_object.is_done() is False
        while test_counter <= 5:
            test_counter += 1
            test_object.step()
        assert test_object.is_done() is True
        assert test_object.get_state() != {}
