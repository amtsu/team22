"""
основной файл работы с базой данных
"""
from stuff import SqlRequester
from requests import initialize_requests

def user_interface(interface_contents):
    """
    пользовательский крутой консольный интерфейс к базе.
    пока будет как одна функция, может быть имеет смысл его разбить
    """
    auchan_sql_requester = SqlRequester("db_mini.sqlite3")
    is_working = True
    while is_working:
        print("=" * 30)
        for task in interface_contents:
            print(f"{task['key']}:{task['name']}")
        user_responce = input("Введите номер запроса:")
        user_responce = user_responce.strip()
        for task in interface_contents:
            if task["key"] == user_responce:
                if task["sql"] is None:
                    is_working = False
                else:
                    result = auchan_sql_requester.execute(task["sql"])
                    print("\n".join(map(str, result)))
                    dummy_responce = input("Нажмите Enter чтобы продолжить...")

    auchan_sql_requester.close()


# ==============================================================================
def main():
    """
    главная функция модуля
    """
    user_interface(initialize_requests())


# ==============================================================================
if __name__ == "__main__":
    main()
