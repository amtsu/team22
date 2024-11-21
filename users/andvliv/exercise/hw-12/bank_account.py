#Создайте класс BankAccount, который представляет банковский счет. У него должны быть атрибуты для хранения номера счета, имени владельца и баланса. Добавьте методы для внесения и снятия денег со счета.

class BankAccount:
    def __init__(self, account_num, name, balance):
        self.account_num = account_num
        self.name = name
        self.balance = balance

    def deposit_money(self, x):
        return self.balance + x

    def withdrawal_money(self, x):
        if self.balance >= x:
            return self.balance - x
        if self.balance < x:
            return "Not enough money"