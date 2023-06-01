import sqlite3

connection = sqlite3.connect("Training_Workers.db")
cursor = connection.cursor()

cursor.execute("""
select name from sqlite_master where type = "table";
""")
print(cursor.fetchall())
connection.commit()
connection.close()