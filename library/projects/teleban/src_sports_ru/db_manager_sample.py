import sqlite3
from config import DB_NAME


class DatabaseManager:
    def __init__(self, db_name):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.curs = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.curs.close()
        self.conn.close()

    def create_table(self):
        """Создает таблицу content_sports_ru с полями title, link, tags, datetime, text и status."""
        self.curs.execute("""CREATE TABLE IF NOT EXISTS content_sports_ru
        (title TEXT, link TEXT PRIMARY KEY, tags TEXT, datetime DATETIME, text TEXT, status INTEGER DEFAULT 0)""")
        self.conn.commit()

    def add_content(self, title, link, tags, datetime, text):
        """Добавляет новый контент в таблицу content_sports_ru."""
        self.curs.execute(
            "INSERT OR IGNORE INTO content_sports_ru (title, link, tags, datetime, text) VALUES (?, ?, ?, ?, ?)",
            (title, link, tags, datetime, text)
        )
        self.conn.commit()

    def remove_content(self, link):
        """Удаляет контент из таблицы content_sports_ru."""
        self.curs.execute("DELETE FROM content_sports_ru WHERE link = ?",
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
        return self.curs.fetchone()

    def get_new_content(self):
        """Возвращает все новые записи из таблицы content_sports_ru."""
        self.curs.execute("SELECT title, link, tags, datetime, text FROM content_sports_ru WHERE status = 0")
        return self.curs.fetchall()

    def close(self):
        """Закрывает соединение с базой данных."""
        self.curs.close()
        self.conn.close()


# создание базы данных
if __name__ == '__main__':
    with DatabaseManager('../' + DB_NAME) as db:
        db.create_table()
