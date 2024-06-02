import itertools

class BankAccount:

    def __init__(self, id: int, first_name: str, last_name: str):
        self._first_name = first_name
        self._last_name = last_name
        self._balance = 0
        self._id = id

    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"

    @property
    def id(self):
        return self._id
        
    @property
    def balance(self):
        return self._balance

    def deposit(self, value):
        self._balance += value
        return self._balance

    def withdraw(self, value):
        self._balance -= value
        return self._balance

    
        
        

