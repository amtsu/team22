class ShoppingCart:
    def __init__(self, basket = {}):
        self.basket = basket
        
    def add_basket(self, name, prices):
        self.basket[name] = prices
        return self.basket
    def del_basket(self, key):
        for key in self.basket:
            self.basket.pop(key)
            return self.basket
    def basket(self):
        return self.basket
    def prises_basket(self):
        sum_prises = []
        for k in self.basket.values():  
            sum_prises.append(k)
        return sum(sum_prises) 