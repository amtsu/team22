import sqlite3
from datetime import datetime

from config import DB_NAME

class TrialSportsDatabaseManager:
    def __init__(self, db_name=DB_NAME):
        self.db_name = db_name
        self.conn = sqlite3.connect(self.db_name)
        self.curs = self.conn.cursor()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.curs.close()
        self.conn.close()