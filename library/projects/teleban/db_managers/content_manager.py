import sqlite3
from datetime import datetime

from config import DB_NAME


class ContentDatabaseManager:
    def __init__(self, table_name: str, db_name: str = DB_NAME):
        self.table_name = table_name
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.curs = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.curs.close()
        self.conn.close()

    def create_table(self):
        """Создает таблицу table_name с полями title, link, tags, datetime и status."""
        self.curs.execute(f'CREATE TABLE IF NOT EXISTS {self.table_name}'
                          f'(title TEXT, link TEXT PRIMARY KEY, tags TEXT,'
                          f'datetime DATETIME, status INTEGER DEFAULT 0)')
        self.conn.commit()

    def add_content(self, title, link, tags):
        """Добавляет новый контент в таблицу table_name."""
        current_time = datetime.now()
        self.curs.execute(f"INSERT OR IGNORE INTO {self.table_name}"
                          f"(title, link, tags, datetime) VALUES (?, ?, ?, ?)",
                          (title, link, tags, current_time))
        self.conn.commit()

    def remove_content(self, link):
        """Удаляет контент из таблицы table_name."""
        self.curs.execute(f"DELETE FROM {self.table_name} WHERE link = ?",
                          (link,))
        self.conn.commit()

    def update_status(self, link):
        """Меняет статус на 1 для записи link из таблицы content_sports_ru."""
        self.curs.execute("UPDATE content_sports_ru SET status = 1 WHERE link = ?",
                          (link,))
        self.conn.commit()

    def check_new_content(self):
        """Проверяет наличие новых записей в таблице content_sports_ru."""
        self.curs.execute("SELECT EXISTS (SELECT 1 FROM content_sports_ru WHERE status = 0)")
        return self.curs.fetchone()[0]

    def get_new_content(self):
        """Возвращает все новые записи из таблицы content_sports_ru."""
        self.curs.execute("SELECT title, link, tags FROM content_sports_ru WHERE status = 0")
        return self.curs.fetchall()

    def close(self):
        """Закрывает соединение с базой данных."""
        self.curs.close()
        self.conn.close()


if __name__ == '__main__':  # Запустить для создания таблиц в БД
    with ContentDatabaseManager('content_sports_ru', '../' + DB_NAME) as db:
        db.create_table()
    with ContentDatabaseManager('content_trial_sport_ru', '../' + DB_NAME) as db:
        db.create_table()
