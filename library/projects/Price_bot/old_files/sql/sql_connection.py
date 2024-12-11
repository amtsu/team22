import sqlite3
import datetime

from team22.library.projects.Price_bot.start_manager.singleton import singleton


@singleton
class SQLConnection:
    def __init__(self, db_name="../sql/products.db"):
        self.db_name = db_name
        self.create_db()

    def create_db(self):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                price REAL NOT NULL,
                date_added TEXT NOT NULL
            )
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS products_admarginem (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                link TEXT NOT NULL,
                price REAL NOT NULL,
                date_added TEXT NOT NULL
            )
        """
        )
        cursor.execute(
            """
            CREATE TABLE IF NOT EXISTS users_admarginem (
                user_id INTEGER NOT NULL,
                product_link TEXT NOT NULL,
                date_added TEXT NOT NULL
            )
        """
        )
        conn.commit()
        conn.close()

    def add_to_db(self, data_to_save: dict | int, user_link=None, user_id=None):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        self.create_db()
        date_added = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        if isinstance(data_to_save, dict):
            for key, value in data_to_save.items():
                cursor.execute(
                    """
                INSERT INTO products (name, price, date_added) VALUES (?, ?, ?)
                """,
                    (key, value, date_added),
                )
        else:
            cursor.execute(
                """
            INSERT INTO users_admarginem (user_id, product_link, date_added) VALUES (?, ?, ?)
            """,
                (user_id, user_link, date_added),
            )
            cursor.execute(
                """
            INSERT INTO products_admarginem (link, price, date_added) VALUES (?, ?, ?)
            """,
                (user_link, data_to_save, date_added),
            )
        print("Данные сохранены в БД")
        conn.commit()
        conn.close()

    def get_all_from_admarginem(self, db_name="products.db"):
        conn = sqlite3.connect(self.db_name)
        cursor = conn.cursor()
        cursor.execute(
            """
            SELECT product.id, user.user_id, user.product_link, user.date_added, product.price
            FROM users_admarginem AS user
            JOIN products_admarginem AS product
            ON user.product_link = product.link
        """
        )
        result = cursor.fetchall()
        print(result)  # для проверки
        conn.commit()
        conn.close()
        return result  # то, что будет дальше использоватьсяъ
