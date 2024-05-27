from wh_product import Product

class Warehouse:
    """
    Класс склад.
    Хранит продукты и их количества
    """
    def __init__(self):
        self.__product_list = []

    def income(self, product, category, price, num):
        """
        Метод добавления остатков
        """
        prod = Product(product, category, price)
        income_prod = prod.get_product()
        income_prod["Количество"] = num
        self.__product_list.append(income_prod)

    def outcome(self, product, num):
        """
        Метод списания остатков
        """
        for item in self.__product_list:
            if product in item.values() and num <= item["Количество"]:
                item["Количество"] -= num
                outcome_product = Product(item["Наименование"], item["Категория"], item["Цена"])
                return outcome_product.get_product() #возвращаем прдукт (словарь данных о продукте)... хотя, наверно, можно возвращать весь объект...
            elif product in item.values() and item["Количество"] > 0:
                print("Недостаточное количество")
            else:
                print("Товара нет вналичии")

    def remains(self):
        """
        Метод учета остатокво на складе
        """
        return self.__product_list

