from shoppingcart import * 

class Product:
        
    def __init__(self, art: str, title: str, qnty: int):
        self._art = art
        self._title = title
        self._qnty = qnty

    def __str__(self):
        return f"{self.art}\t{self.title}\t{self.qnty}"
  

    @property 
    def art(self):
        return self._art
    
    @property
    def title(self):
        return self._title

    @property
    def qnty(self):
        return self._qnty

    @qnty.setter
    def qnty(self, value):
        self._qnty = value


class Warehouse:

    def __init__(self):
        self._items = []

    def __len__(self):
        return len(self._items)

    def __str__(self):
        if len(self._items) > 0:
            report = f"Remaining stocks\n"
            report += f"Art. \t Title \t Qnty \n"
            report += f"="*40 + f"\n"
            for item in self._items:
                report += str(item) + f"\n"
        else:
            report = "Stok is empty"
            
        return report


    @property
    def items(slef):
        return self._items

    def recive(self, item: Product) -> int:
        self._items.append(item)
        return len(self._items)

    def writeoff(self, art: int, qnty: int) -> bool:
        for item in self._items:
            if item.art == art:
                if item.qnty >= qnty:
                    item.qnty -= qnty
                    return True
                else:
                    raise ValeError("Not enough quantity")
        return False


class Order:

    def __init__(self, cart: ShoppingCart):
        self._cart = cart
        self._state = "created"

    @property 
    def items(self):
        return self._cart.items

    @property 
    def state(self):
        return self._state
    
    @property
    def total(self):
        return self._cart.total

    def change_state_to_paid(self):
        self._state = "paid"

    def change_state_to_ready(self):
        self._state = "ready"

    def change_state_to_compleated(self):
        self._state = "compleated"


        

    
    



