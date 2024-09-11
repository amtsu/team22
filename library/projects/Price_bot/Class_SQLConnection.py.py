import sqlite3
import datetime

class SQLConnection:
	def __init__(self, db_name='products.db'):
		self.db_name = db_name
		self.create_db()

	def create_db(self):
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()
		cursor.execute('''
            CREATE TABLE IF NOT EXISTS products (
                name TEXT NOT NULL,
                price REAL NOT NULL,
                date_added TEXT NOT NULL
            )
        ''')
		conn.commit()
		conn.close()

	def add_to_db(self, name: str, price: int):
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()
		self.create_db()
		date_added = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

		cursor.execute('''
            INSERT INTO products (name, price, date_added) VALUES (?, ?, ?)
        ''', (name, price, date_added))
		conn.commit()
		conn.close()

	def select_all_from_db(self, db_name='products.db'):
		conn = sqlite3.connect(self.db_name)
		cursor = conn.cursor()
		cursor.execute('''
            SELECT * FROM products 
        ''')

		result = cursor.fetchall()
		print(result) # для проверки
		conn.commit()
		conn.close()
		return result  # то, что будет дальше использоватьсяъ
