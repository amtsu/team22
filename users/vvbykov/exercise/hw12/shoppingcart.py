
class ShoppingItem:
    _cnt = 0

    def __new__(cls, *args, **kwargs):
        cls._cnt += 1
        return super().__new__(cls)
        
    def __init__(self, art: str, title: str, qnty: int, price: float):
        self._art = art
        self._title = title
        self._qnty = qnty
        self._price = price
        self._id = self._cnt

    def __str__(self):
        return f"{self.art}\t{self.title}\t{self.qnty}\t{self.price}\t{self.cost}"
        
    @property 
    def id(self):
        return self._id

    @property 
    def art(self):
        return self._art
    
    @property
    def title(self):
        return self._title

    @property
    def qnty(self):
        return self._qnty

    @property
    def price(self):
        return self._price
    
    @property 
    def cost(self):
        return round(self._qnty * self._price, 2)
        

class ShoppingCart:

    def __init__(self):
        self._cart = []

    def __len__(self):
        return len(self._cart)

    @property
    def items(self):
        return self._cart
    
    
    @property
    def total(self):
        total = 0            
        for item in self._cart:
            total += item.cost
        return round(total, 2)
        
    
    def cart_print(self):
        if len(self._cart) > 0:
            print("Art.\tItem\tQnty\tPrice\tCost")
            print("="*60)
            for item in self._cart:
                print(item)
            print("")
            print(f"Total {self.total}")
        else:
            print(f"The cart is empty")

    def cart_add(self, item):
        self._cart.append(item)
        return len(self._cart)

    def cart_remove(self, id: int):
        if len(self._cart) > 0:
            for item in self._cart:
                if item.id == id:
                    self._cart.remove(item)
        return len(self._cart) 
                            
