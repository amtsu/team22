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
