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
    item = {
        "key": next(indexer),
        "name": "В одном запросе вывести среднюю стоимость для пакетов молока 1 литр 950 и 900 миллилитров",
        "sql": """
            SELECT CASE 
                    WHEN title LIKE "%900%"
                        THEN "900"
                    WHEN title LIKE "%950%"
                        THEN "950"
                    WHEN title LIKE "%1 л%"
                        THEN "1000"
                    END AS litter
                ,avg(price_sale)
            FROM products_history
            WHERE (
                    title LIKE "Молоко %"
                    OR title LIKE "% молоко"
                    OR title LIKE "% молоко %"
                    OR title LIKE "% молоко,%"
                    )
                AND (
                    title LIKE "%1 л%"
                    OR title LIKE "%950%"
                    OR title LIKE "%900%"
                    )
            GROUP BY litter

                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Выбрать 50 товаров, цена которых больше 50'000 и отсортировать по убыванию по цене",
        "sql": """
                SELECT title
                    ,price_sale
                FROM products_history
                WHERE price_sale > 50000
                ORDER BY price_sale DESC LIMIT 50
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Изменить все названия в которых есть слово \"Вино\" в столбце \"title\" на \"Винишко\"",
        "sql": """
                UPDATE products_history
                SET title = replace(title, 'Вино', 'Винишко')
                WHERE title LIKE 'Вино%'

                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Посчитать сумму стоимости товаров с id от 2877 до 2922",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Добавить столбец \"Количество товаров в магазине\"",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Посчитать количество товаров в названиях которых есть \"Лыжный комплект\" и \"Игрушка для собак\".",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести среднюю стоимость товаров типа виски",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести товары совпадающие по типу",
        "sql": """
                SELECT "Сложнаа"
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести товары весом меньше 50г",
        "sql": """
                SELECT "Сложнаа"
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Упорядочить товары по цене",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести 5 самых дорогих и самых дешевых товара",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Дать псевдоним столбцу 'price_sale' и вывести цену 2 товаров из таблицы",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести 5 названий шоколадок с ценой до 120 рублей",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести максимальную стоимость шоколадки",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести 3 названия шоколадок и цен на них, отфильтрованных по убыванию по цене",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести названия шоколадок, у которых повторяющиеся цены - 5 шт",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести не более 50 записей для товаров, цена которых не больше чем цена товара, пятого по дешевизне",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести название и среднюю цену всех товаров, у которых со временем цена менялась",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести среднюю цену соленых огурцов за 6 декабря",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести название и среднюю цену всех товаров, у которых со временем цена изменилась",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Заменить во всей таблице в названии товара слово \"вино\" на \"винишко\" (а \"Вино\" на \"Винишко\", чтобы красиво было)",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Найти сколько раз встречается в таблице записи с одинаковым названием и ценой",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Найти максимальную и минимальную дату появления товара в таблице",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": """Найти количество товаров и их среднюю стоимость (округленную до двух знаков после запятой)
    появившихся в таблице в перод с 13 часов 7-го декабря 2022, до 10 декабря 2022 (не включая его)""",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": """В одном запросе вывести количество строк с условием: 
    если длина title больше 20 символов вывести "много букв"; 
    если длина title больше 10 символов, но меньше 20, вывести "норм"; 
    в любом другом случае вывести "мало букв";""",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "В sql решить пример (100+99)/2 + (95-5)/3.",
        "sql": """
                SELECT 1
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    # item = {
    #     "key": next(indexer),
    #     "name": "dummy",
    #     "sql": """
    #             SELECT 1
    #             """,
    # }
    # interface_contents.append(item)
    # ============================================================================
    # ============================================================================
    interface_contents.append({"key": "0", "name": "Закончить работу", "sql": None})
    return interface_contents
