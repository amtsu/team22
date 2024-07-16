class BankAccount:
    """
    Класс, который представляет банковский счет. 
    Имеет атрибуты для хранения номера счета, имени владельца и баланса. 
    Имеет методы для внесения и снятия денег со счета.
    """
    def __init__(self, account_num, owner_name, balance = 0):
        self.__account = account_num
        self.__owner = owner_name
        self.__balance = balance

    def add_to_acc(self, input_amount):
        self.__balance += input_amount

    def sub_from_acc(self, out_amount):
        self.__balance -= out_amount

    def show_balance(self):
        return self.__balance