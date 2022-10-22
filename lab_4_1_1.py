from _distutils_hack import override


class Product:
    def __init__(self, name, price, weight, width = 1, depth = 1):
        self.__name = name
        self.__price = price
        self.__volume = (weight * width * depth)

    def discount(self, percent):
        ans = round((self.price * (100 - percent) / 100), 2)
        if ans == 0:
            return 0.01
        else:
            return ans

    def count(self, weight, width, depth): return self.volume // (weight * width * depth)

    @property
    def price(self): return self.__price

    @property
    def volume(self): return self.__volume

    @price.setter
    def price(self, price): self.__price = price

    @volume.setter
    def volume(self, volume): self.__volume = volume

    def __add__(self, other): return Product(self.__name + "\n" + other.__name, self.__price + other.__price, self.__volume + other.__volume)

    def __str__(self):
        return "Name: \t" + self.__name + "\nPrice:\t" + str(self.__price) + "\nVolume:\t" + str(self.__volume)


product1 = Product("Mef", 100, 200, 1, 1)
product2 = Product("Gay", 200, 100, 1, 1)
print(product1, "\n\n")
print(product1 + product2)
