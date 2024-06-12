"""
Модуль тестирования класса StatusUpdate модуля status_update
"""
import pytest

from status_update import StatusUpdate

@pytest.mark.parametrize("set1,set2, expected", [
    ({'зеленый', 'желтый', 'оранжевый', 'красный', 'голубой'}, {'желтый', 'фиолетовый', 'синий', 'оранжевый', 'Мальвиновый'}, "Длины равны"),
    ({"красный", "оранжевый", "желтый", "зеленый", "голубой"}, {'желтый', 'оранжевый', 'фиолетовый', 'синий'}, "Длина set1 больше, чем длина set2"),
    ({}, {}, None),
    ({1}, {1, 2}, "Длина set1 меньше, чем длина set2"),
    ({12},{}, None),
    ({}, {0}, None),
    ({False}, {None}, "Длины равны"),
    ([], {2}, None)
])

def test_user_info():
    my_status = StatusUpdate("users/mvandreeva/study2024/exercise/hw15/visits_status.csv", "Andromary")
    assert my_status.user_info() == ''

def


