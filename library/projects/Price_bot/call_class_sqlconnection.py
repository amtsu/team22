from Class_SQLConnection import SQLConnection

SQLTEST = SQLConnection()
SQLTEST.add_to_db("banana", 150)
SQLTEST.select_all_from_db()