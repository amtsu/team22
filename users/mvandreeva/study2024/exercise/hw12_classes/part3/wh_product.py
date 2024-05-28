class Product:
    """
    Класс продукт.
    Хранит наименование, категорию, цену продукта и методы для их вывода и изменения
    """
    def __init__(self, product, category, price):
        self.__product_data = {"Наименование": product, "Категория": category, "Цена": price}

    def get_product(self):
        return self.__product_data

    def get_price(self):
        return self.__product_data["Цена"]

    def get_category(self):
        return self.__product_data["Категория"]

    def get_name(self):
        return self.__product_data["Наименование"]

    def set_price(self, price):
        self.__product_data["Цена"] = price

    def set_name(self, name):
        self.__product_data["Наименование"] = name

    def set_category(self, category):
        self.__product_data["Категория"] = category
        
    
