from Class_SQLConnection import SQLConnection
from add_dict_to_db import SQLConnection

SQLTEST = SQLConnection()
#SQLTEST.add_to_db("banana", 150)
SQLTEST.select_all_from_db()
SQLTEST.add_dict_to_db({"milk": 100, "coffe": 150})
SQLTEST.select_all_from_db()

