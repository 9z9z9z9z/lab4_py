from Product import Product

class Equipment(Product):
    def __init__(self, name, price, type, weight, width=1, depth=1):
        Product.__init__(self, name, price, weight, width, depth)
        self.__type = type

    @type.setter
    def type(self, value):
        self.__type = value
