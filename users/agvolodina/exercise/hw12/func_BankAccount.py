#Создайте класс BankAccount, который представляет банковский счет. У него должны быть атрибуты для хранения номера счета, имени владельца и баланса. Добавьте методы для внесения и снятия денег со счета.

class BankAccount():
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    #метод для внесения денег на счет
    def add_money (self, money):
        return self.balance + money

    #метод для снятия денег со счета
    def del_money (self, money):
        return self.balance - money