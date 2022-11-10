class Product:
    def __init__(self, url, critical_price, parser):
        self.__url = url
        self.__critical_price = critical_price
        self.__parser = parser

        self.__current_price = None
        self.update_price()

    def update_price(self):
        self.__current_price = self.__parser.get_price(self.__url)

    def get_price(self):
        return self.__current_price

    def get_critical_price(self):
        return self.__critical_price


# if __name__ == '__main__':
#     url = 'https://www.chitai-gorod.ru/catalog/book/2943798/'
#     critical_price = 500
#     parser = ChitaiGorodParser
#     product = Product(url, critical_price, parser)
#     print(product.get_price())
