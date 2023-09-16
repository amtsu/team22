from hw_exclusion import phone_book_func


def test_phone_book(monkeypatch):
    """Проверяется, что отдается правильный ответ, если имя найдено в
    телефонной книге."""
    monkeypatch.setattr("builtins.input", lambda _: "Ivan")
    result = phone_book_func()
    assert result == '1234'

def test_name_not_found_in_phone_book(monkeypatch):
    """Проверяется, что при запросе имени не из телефонной книги
    отображается сообщение 'Такого имени нет'."""
    monkeypatch.setattr("builtins.input", lambda _: "Platon")
    result = phone_book_func()
    assert result == "Такого имени нет"
