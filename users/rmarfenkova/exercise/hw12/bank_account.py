class BankAccount:
    """
    Создайте класс BankAccount, который представляет банковский счет.
    У него должны быть атрибуты для хранения номера счета, имени владельца и баланса.
    Добавьте методы для внесения и снятия денег со счета.
    """
    def __init__(self, account_number, owner_name, balance=0):
        self._account_number = account_number
        self._owner_name = owner_name
        self._balance = balance

    @property
    def account_number(self):
        return self._account_number

    @account_number.setter
    def account_number(self, value):
        if isinstance(value, int) and value > 0:
            self._account_number = value
        else:
            raise ValueError("Номер счета должен быть положительным целым числом")

    @property
    def owner_name(self):
        return self._owner_name

    @owner_name.setter
    def owner_name(self, value):
        if isinstance(value, str):
            self._owner_name = value
        else:
            raise ValueError("Имя владельца должно быть строкой")

    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, value):
        if isinstance(value, int) and value >= 0:
            self._balance = value
        else:
            raise ValueError("Баланс должен быть положительным целым числом или нулем")

    def deposit(self, amount: int):
        self.balance += amount
        return f"Вы пополнили счет на {amount}. Текущий баланс: {self.balance}"
        
    def withdraw(self, amount: int):
        if amount <= self.balance:
            self.balance -= amount
            return f"Вы сняли со счета {amount}. Текущий баланс: {self.balance}"
        else:
            return "Недостаточно средств на счете"

            


            
            
        