import sqlite3

DB_NAME = 'database.db'


# Определение класса Reqv
class Reqv:
    def __init__(self, reqv_id, user_id, link):
        self.id = reqv_id
        self.user_id = user_id
        self.link = link

    def __repr__(self):
        return f'Reqv(id={self.id}, user_id={self.user_id}, link={self.link})'


# Создание таблицы для хранения объектов Reqv
def create_table():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS reqv (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id TEXT NOT NULL,
            link TEXT NOT NULL
        )
    ''')
    conn.commit()
    conn.close()


# Функция для сохранения объекта Reqv в базу данных
def save_user_link(user_id, link):
    reqv = Reqv(reqv_id=None, user_id=user_id, link=link)
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO reqv (user_id, link)
        VALUES (?, ?)
    ''', (reqv.user_id, reqv.link))

    conn.commit()
    conn.close()


# Функция для получения всех объектов Reqv по user_id
def get_user_links(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('''
        SELECT id, user_id, link FROM reqv WHERE user_id = ?
    ''', (str(user_id),))

    reqvs = [row[2] for row in cursor.fetchall()]

    conn.close()

    return reqvs


# Функция для удаления всех объектов Reqv по user_id
def del_user_links(user_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute('DELETE FROM reqv WHERE user_id = ?', (str(user_id),))

    conn.commit()
    conn.close()

    return f'Все записи для user_id {user_id} удалены'


if __name__ == '__main__':
    create_table()