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
            SET title = "Винишко"
            WHERE title LIKE 'Вино%' 
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Посчитать сумму стоимости товаров с id от 2877 до 2922",
        "sql": """
            SELECT sum(price_sale)
            FROM products_history ph
            WHERE id >= 2876
                AND id <= 2922
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Добавить столбец \"Количество товаров в магазине\"",
        "sql": """
            ALTER TABLE products_history ADD goods_quantity INTEGER NOT NULL DEFAULT 0
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    # лол, это не работает
    # item = {
    #     "key": next(indexer),
    #     "name": "Удалить столбец \"Количество товаров в магазине\"",
    #     "sql": """
    #         ALTER TABLE products_history DROP COLUMN goods_quantity
    #             """,
    # }
    # interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Посчитать количество товаров в названиях которых есть \"Лыжный комплект\" и \"Игрушка для собак\".",
        "sql": """
            SELECT count(1)
            FROM products_history ph
            WHERE title LIKE "Лыжный комплект%"
                OR title LIKE "Игрушка для собак%";
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести среднюю стоимость товаров типа виски",
        "sql": """
            SELECT DISTINCT title
                ,price_sale
            FROM products_history ph
            WHERE title LIKE "Виски%"
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
            SELECT DISTINCT title, price_sale FROM products_history ph 
            ORDER BY price_sale DESC
            LIMIT 200
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести 5 самых дорогих и самых дешевых товара",
        "sql": """
            SELECT DISTINCT title
                ,price_sale
            FROM products_history
            WHERE id IN (
                    SELECT id
                    FROM products_history ph
                    GROUP BY ph.title
                    ORDER BY max(ph.price_sale) DESC limit 5
                    )
                OR id IN (
                    SELECT id
                    FROM products_history ph
                    GROUP BY ph.title
                    ORDER BY min(ph.price_sale) ASC limit 5
                    )
            ORDER BY price_sale ASC
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Дать псевдоним столбцу 'price_sale' и вывести цену 2 товаров из таблицы",
        "sql": """
            SELECT price_sale AS price
                ,title
            FROM products_history ph LIMIT 2
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести 5 названий шоколадок с ценой до 120 рублей",
        "sql": """
            SELECT title
            FROM products_history ph
            WHERE title LIKE "Шоколад %"
                AND price_sale < 120
            LIMIT 5
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести максимальную стоимость шоколадки",
        "sql": """
            SELECT max(price_sale)
            FROM products_history ph
            WHERE title LIKE "Шоколад %"
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести 3 названия шоколадок и цен на них, отфильтрованных по убыванию по цене",
        "sql": """
            SELECT DISTINCT title
                ,price_sale
            FROM products_history ph
            WHERE title LIKE "Шоколад %"
            ORDER BY price_sale DESC LIMIT 3
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести названия шоколадок, у которых повторяющиеся цены - 5 шт",
        "sql": """
            SELECT title
                ,price_sale
                ,COUNT(price_sale) AS repeats
            FROM products_history ph
            WHERE title LIKE "Шоколад %"
            GROUP BY price_sale
            HAVING repeats > 1 LIMIT 5
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести не более 50 записей для товаров, цена которых не больше чем цена товара, пятого по дешевизне",
        "sql": """
            SELECT *
            FROM products_history ph
            WHERE price_sale IN (
                    SELECT DISTINCT price_sale
                    FROM products_history
                    ORDER BY price_sale ASC limit 5
                    )
            ORDER BY price_sale limit 50
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести название и среднюю цену всех товаров, у которых со временем цена менялась",
        "sql": """
            SELECT ph.title
                ,avg(ph.price_sale)
            FROM products_history ph
            GROUP BY title
            HAVING MIN(price_sale) < MAX(price_sale);
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести среднюю цену соленых огурцов за 6 декабря",
        "sql": """
            SELECT avg(price_sale)
            FROM products_history ph
            WHERE (
                    title LIKE "Огур%"
                    OR title LIKE "% огур%"
                    )
                AND (
                    title LIKE "%соленые%"
                    OR title LIKE "Соленые%"
                    )
                AND datetime_create > ('2022-12-06')
                AND datetime_create < ('2022-12-07')
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести название и среднюю цену всех товаров, у которых со временем цена изменилась",
        "sql": """
            WITH price_checker
            AS (
                SELECT title
                    ,FIRST_VALUE(price_sale) OVER (
                        PARTITION BY title ORDER BY datetime_create ASC
                        ) AS first_price
                    ,FIRST_VALUE(price_sale) OVER (
                        PARTITION BY title ORDER BY datetime_create DESC
                        ) AS last_price
                FROM products_history
                )
            SELECT pc.title
                ,first_price
                ,last_price
                ,avg(ph.price_sale)
            FROM price_checker pc
            JOIN products_history ph ON pc.title = ph.title
            GROUP BY ph.title
            HAVING first_price <> last_price
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Заменить во всей таблице в названии товара слово \"вино\" на \"винишко\" (а \"Вино\" на \"Винишко\", чтобы красиво было)",
        "sql": """
            UPDATE products_history
            SET title = replace(title, 'ино', 'инишко')
            WHERE title LIKE 'Вино%'
                OR title LIKE '%вино %'
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Найти сколько раз встречается в таблице записи с одинаковым названием и ценой",
        "sql": """
            SELECT COUNT(1) AS "number of entries"
                ,title
                ,price_sale
            FROM products_history
            GROUP BY title
                ,price_sale
            ORDER BY title
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Найти максимальную и минимальную дату появления товара в таблице",
        "sql": """
            SELECT min(datetime_create) AS MinDate
                ,max(datetime_create) AS MaxDate
                ,title
                ,count(1) AS Entities
            FROM products_history ph
            GROUP BY title
            ORDER BY MinDate LIMIT 50
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": """Найти количество товаров и их среднюю стоимость (округленную до двух знаков после запятой)
    появившихся в таблице в перод с 13 часов 7-го декабря 2022, до 10 декабря 2022 (не включая его)""",
        "sql": """
            SELECT count(1) AS Entities
                ,ROUND(AVG(price_sale), 2) AS Average_price
            FROM products_history
            WHERE datetime_create >= '2022-12-07 13:00:00.00'
                AND datetime_create < '2022-12-10'
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
            SELECT COUNT(1) AS Entities
                ,CASE 
                    WHEN LENGTH(title) < 10
                        THEN 'мало букв'
                    WHEN LENGTH(title) > 20
                        THEN 'много букв'
                    ELSE 'Норм'
                    END AS Name
            FROM products_history ph
            GROUP BY Name
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "В sql решить пример (100+99)/2 + (95-5)/3. ...",
        "sql": """
                SELECT (100+99)/2. + (95-5)/3. AS result
                """,
    }
    interface_contents.append(item)
    # ============================================================================
    item = {
        "key": next(indexer),
        "name": "Вывести информацию о структуре таблицы products_history",
        "sql": """
                    PRAGMA table_info(products_history)
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
