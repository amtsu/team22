import sqlite3
from config_old import DB_NAME


class SubscriptionDatabaseManager:
    def __init__(self, db_name: str = DB_NAME):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.curs = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.curs.close()
        self.conn.close()

    def create_table(self):
        """Создает таблицу subscriptions с полями user_id, source и tag."""
        self.curs.execute("CREATE TABLE IF NOT EXISTS subscriptions (user_id INTEGER, source TEXT, tag TEXT)")
        self.conn.commit()

    def add_subscription(self, user_id, source, tag):
        """Добавляет подписку пользователя в таблицу subscriptions."""
        self.curs.execute("INSERT INTO subscriptions VALUES (?, ?, ?)",
                          (user_id, source, tag))
        self.conn.commit()

    def remove_subscription(self, user_id, source, tag):
        """Удаляет подписку пользователя из таблицы subscriptions."""
        self.curs.execute("DELETE FROM subscriptions WHERE user_id = ? AND source = ? AND tag = ?",
                          (user_id, source, tag))
        self.conn.commit()

    def check_exist_subscription(self, source, tag):
        """Проверяет наличие подписок на tag в таблице subscriptions."""
        self.curs.execute("SELECT EXISTS (SELECT 1 FROM subscriptions WHERE source = ? AND tag = ?)",
                          (source, tag))
        return self.curs.fetchone()[0]

    def get_user_tags(self, user_id, source) -> list[str]:
        """Возвращает все теги пользователя из таблицы subscriptions."""
        self.curs.execute("SELECT tag FROM subscriptions WHERE user_id = ? AND source = ?",
                          (user_id, source))
        return [item[0] for item in self.curs.fetchall()]

    def get_tag_users(self, source, tag):
        """Возвращает всех пользователей тега из таблицы subscriptions."""
        self.curs.execute("SELECT user_id FROM subscriptions WHERE source = ? AND tag = ?",
                          (source, tag,))
        return [item[0] for item in self.curs.fetchall()]

    def close(self):
        """Закрывает соединение с базой данных."""
        self.curs.close()
        self.conn.close()


# создание базы данных
if __name__ == '__main__':
    with SubscriptionDatabaseManager('../' + DB_NAME) as db:
        db.create_table()