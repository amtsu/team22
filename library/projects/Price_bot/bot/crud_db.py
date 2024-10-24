import sqlite3
import os

# DB_NAME = "database.db"

DB_FOLDER = "database"
DB_NAME = os.path.join(DB_FOLDER, "database.db")
os.makedirs(DB_FOLDER, exist_ok=True)


def save_user_link(user_id, link):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS user_links (
            user_id TEXT,
            link TEXT,
            last_min_price REAL,
            UNIQUE(user_id, link)
        )
    """
    )
    try:
        cursor.execute(
            """
            INSERT INTO user_links (user_id, link)
            VALUES (?, ?)
        """,
            (str(user_id), link),
        )
        conn.commit()
    except sqlite3.IntegrityError as e:
        print(f"Ошибка: {e}")
        return "Такая ссылка уже есть"
    conn.close()
    return f"Ссылка сохранена: {link}"


def get_user_links(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT link FROM user_links
        WHERE user_id = ?
    """,
        (str(user_id),),
    )
    links = [row[0] for row in cursor.fetchall()]
    conn.close()
    return links


def get_last_min_price(user_id, link):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT last_min_price FROM user_links
        WHERE user_id = ? AND link = ?
    """,
        (str(user_id), link),
    )

    result = cursor.fetchone()
    conn.close()

    return result[0] if result else None


def save_or_update_last_min_price(user_id, link, last_min_price):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Обновление или вставка цены
    cursor.execute(
        """
        INSERT INTO user_links (user_id, link, last_min_price)
        VALUES (?, ?, ?)
        ON CONFLICT(user_id, link) DO UPDATE 
        SET last_min_price = excluded.last_min_price
    """,
        (str(user_id), link, last_min_price),
    )

    conn.commit()
    conn.close()


def del_user_links(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Удаление всех ссылок для данного user_id
    cursor.execute(
        """
        DELETE FROM user_links
        WHERE user_id = ?
    """,
        (str(user_id),),
    )

    conn.commit()

    # Проверяем, удалены ли ссылки
    cursor.execute(
        """
        SELECT link FROM user_links
        WHERE user_id = ?
    """,
        (str(user_id),),
    )
    links = cursor.fetchall()

    conn.close()

    if not links:
        result = "Ссылки успешно удалены"
    else:
        result = "Что-то пошло не так"

    return result


# заготовка для добавления новых колонок в бд
def add_new_column():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Добавляем новое поле last_min_price
    cursor.execute(
        """
        ALTER TABLE user_links
        ADD COLUMN last_min_price REAL
    """
    )

    conn.commit()
    conn.close()
