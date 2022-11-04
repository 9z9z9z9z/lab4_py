from Product import Product


class Equipment(Product):
    def __init__(self, name, price, type, weight, width=1, depth=1):
        super().__init__(name, price, weight, width, depth)
        self.__type = type

    @property
    def type(self): return self.__type

    @type.setter
    def type(self, value):
        self.__type = value

    def __str__(self):
        return "\n====================================\nName:\t" + self.name + "\nPrice:\t" + str(self.price) + "\nType:\t" + self.__type\
               + "\nDimensions:\t" + str(self.volume) + "\n====================================\n"
