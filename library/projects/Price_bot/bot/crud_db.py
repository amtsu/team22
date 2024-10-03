import sqlite3

DB_NAME = 'database.db'


def save_user_link(user_id, link):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS user_links (
            user_id TEXT,
            link TEXT
        )
    ''')
    cursor.execute('''
        INSERT INTO user_links (user_id, link)
        VALUES (?, ?)
    ''', (str(user_id), link))
    conn.commit()
    cursor.execute('''
        SELECT link FROM user_links
        WHERE user_id = ?
    ''', (str(user_id),))
    links = [row[0] for row in cursor.fetchall()]
    conn.close()
    return links


def get_user_links(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        SELECT link FROM user_links
        WHERE user_id = ?
    ''', (str(user_id),))
    links = [row[0] for row in cursor.fetchall()]
    conn.close()
    return links


def del_user_links(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    # Удаление всех ссылок для данного user_id
    cursor.execute('''
        DELETE FROM user_links
        WHERE user_id = ?
    ''', (str(user_id),))

    conn.commit()

    # Проверяем, удалены ли ссылки
    cursor.execute('''
        SELECT link FROM user_links
        WHERE user_id = ?
    ''', (str(user_id),))
    links = cursor.fetchall()

    conn.close()

    if not links:
        result = "Ссылки успешно удалены"
    else:
        result = "Что-то пошло не так"

    return result
