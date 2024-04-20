class BankAccount:
    """
    Создайте класс BankAccount, который представляет банковский счет. У него должны быть атрибуты для хранения номера счета, имени владельца и баланса. Добавьте методы для внесения и снятия денег со счета.
    """
    def __init__(self, deposit_number, holder_name, balance):
        self.deposit_number = deposit_number
        self.holder_name = holder_name
        self.balance = balance

    
        
    
    def moneyAdd(self, value):
        self.balance += value
        return self.balance

    def moneyDeduct(self, value):
        self.balance -= value
        return self.balance

