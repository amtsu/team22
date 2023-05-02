"""
основной файл работы с базой данных бухгалтерии (accounts department)
"""
from stuff import SqlRequester


# ==============================================================================
def initialize_requests():
    """
    метод в котором я буду создавать список словариков с запросами
    """
    indexer = (str(i) for i in range(1, 100))
    interface_contents = []
    item = {
        "key": next(indexer),
        "name": "Вывести названия товаров в которые содержат слова молоко и стоимостью больше 50 рублей",
        "sql": """
            SELECT title
            FROM products_history
            WHERE (
		            title LIKE "Молоко %"
		            OR title LIKE "% молоко"
		            OR title LIKE "% молоко %"
		            OR title LIKE "% молоко,%"
		    )
	        AND price_sale > 50
        """,
    }
    interface_contents.append(item)
    # ==вставлять запросы сюда=====================================================
    item = {
        "key": next(indexer),
        "name": "Посчитать общее количество товарных позиций",
        "sql": """
            SELECT count(title)
            FROM products_history
            """,
    }
    interface_contents.append(item)
    # ================================================================================
    item = {
        "key": next(indexer),
        "name": "Посчитать количество товаров когда товаром является молоко размером 1 литр",
        "sql": """
            SELECT count(title)
            FROM products_history
            WHERE (
                    title LIKE "Молоко %"
                    OR title LIKE "% молоко"
                    OR title LIKE "% молоко %"
                    OR title LIKE "% молоко,%"
                    )
                AND title LIKE "%1 л%"
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Посчитать среднюю стоимость литрового пакет молока",
        "sql": """
            SELECT avg(price_sale)
            FROM products_history
            WHERE (
                    title LIKE "Молоко %"
                    OR title LIKE "% молоко"
                    OR title LIKE "% молоко %"
                    OR title LIKE "% молоко,%"
                    )
                AND title LIKE "%1 л%"

                """,
    }
    interface_contents.append(item)
    # ============================================================================
    # ============================================================================
    interface_contents.append({"key": "0", "name": "Закончить работу", "sql": None})
    return interface_contents


def user_interface(interface_contents):
    """
    пользовательский крутой консольный интерфейс к базе.
    пока будет как одна функция, может быть имеет смысл его разбить
    """
    auchan_sql_requester = SqlRequester("db_mini.sqlite3")
    is_working = True
    while is_working:
        print("=" * 30)
        for task in interface_contents:
            print(f"{task['key']}:{task['name']}")
        user_responce = input("Введите номер запроса:")
        user_responce = user_responce.strip()
        for task in interface_contents:
            if task["key"] == user_responce:
                if task["sql"] is None:
                    is_working = False
                else:
                    result = auchan_sql_requester.execute(task["sql"])
                    print("\n".join(map(str, result)))

    auchan_sql_requester.close()


# ==============================================================================
def main():
    """
    главная функция модуля
    """
    user_interface(initialize_requests())


# ==============================================================================
if __name__ == "__main__":
    main()
