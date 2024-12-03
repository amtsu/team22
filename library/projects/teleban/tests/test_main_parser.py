import pytest

from data import ContentBase
from main_parser import SOURCE_LIST


@pytest.mark.parametrize(
    "parser_class",
    SOURCE_LIST,
)
def test_parser_get_new_content(parser_class):
    parser = parser_class()
    content = parser.get_new_content()

    # Проверяем, что результат - это список
    assert isinstance(content, list), f"Метод get_new_content() в {parser_class.__name__} должен возвращать список!"

    # Проверяем, что элементы списка - экземпляры ContentBase
    assert all(
        isinstance(item, ContentBase) for item in content
    ), f"Метод get_new_content() в {parser_class.__name__} возвращает элементы, которые не являются экземплярами ContentBase!"

    # Проверяем, что количество элементов не меньше 5
    assert len(content) >= 5, f"Парсер {parser_class.__name__} работает некорректно! Найдено объектов: {len(content)}"
