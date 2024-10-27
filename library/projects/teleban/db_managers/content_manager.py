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

    def create_table(self) -> None:
        """Создает таблицу с полями title, link, source, tags, datetime и status."""
        self.curs.execute(f"""
            CREATE TABLE IF NOT EXISTS {self.table_name} (
                title TEXT,
                link TEXT PRIMARY KEY,
                source TEXT,
                tags TEXT,
                datetime DATETIME,
                status INTEGER DEFAULT 0
            )
        """)
        self.conn.commit()

    def add_content(self, title: str, link: str, source: str, tags: str) -> None:
        """Добавляет новый контент в таблицу с полем source."""
        current_time = datetime.now()
        self.curs.execute(f"""
            INSERT OR IGNORE INTO {self.table_name} (title, link, source, tags, datetime) 
            VALUES (?, ?, ?, ?, ?)
        """, (title, link, source, tags, current_time))
        self.conn.commit()

    def remove_content(self, link: str) -> None:
        """Удаляет контент по ссылке."""
        self.curs.execute(f"DELETE FROM {self.table_name} WHERE link = ?", (link,))
        self.conn.commit()

    def update_status(self, link: str) -> None:
        """Обновляет статус записи по ссылке."""
        self.curs.execute(f"UPDATE {self.table_name} SET status = 1 WHERE link = ?", (link,))
        self.conn.commit()

    def check_new_content(self) -> bool:
        """Проверяет наличие новых записей."""
        self.curs.execute(f"SELECT EXISTS (SELECT 1 FROM {self.table_name} WHERE status = 0)")
        return bool(self.curs.fetchone()[0])

    def get_new_content(self) -> list[tuple[str, str, str, str]]:
        """Возвращает все новые записи."""
        self.curs.execute(f"SELECT title, link, source, tags FROM {self.table_name} WHERE status = 0")
        return self.curs.fetchall()

    def close(self):
        """Закрывает соединение с базой данных. Не использовать без необходимости!"""
        self.curs.close()
        self.conn.close()


TABLE_NAMES = [
    'content_sports_ru',
    'content_trial_sport_ru',
]

if __name__ == '__main__':
    # Создание таблиц в БД
    for table in TABLE_NAMES:
        with ContentDatabaseManager(table, '../' + DB_NAME) as db:
            db.create_table()
