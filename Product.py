class Product:
    def __init__(self, name, price, weight, width=1, depth=1):
        self.__name = name
        self.__price = price
        self.__weight = weight
        self.__width = width
        self.__depth = depth
        self.__volume = self.__depth * self.__weight * self.__width

    def discount(self, percent) -> float:
        ans = round((self.price * (100 - percent) / 100), 2)
        if ans == 0:
            return 0.01
        else:
            return ans

    def count(self, weight, width=1, depth=1) -> int:
        limit = max(width, weight, depth)
        if self.__width > limit or self.__weight > limit or self.__depth > limit:
            return 0
        else:
            return (weight * width * depth) // self.volume

    @property
    def price(self): return self.__price

    @property
    def volume(self): return self.__volume

    @property
    def name(self): return self.__name

    @name.setter
    def name(self, name): self.__name = name

    @price.setter
    def price(self, price): self.__price = price

    @volume.setter
    def volume(self, volume): self.__volume = volume

    def __add__(self, other): return Product(self.__name + "\n\t\t" + other.__name, self.__price + other.__price, self.__volume + other.__volume)

    def __str__(self):
        return "Name:\t" + self.__name + "\nPrice:\t" + str(self.__price) + "\nVolume:\t" + str(self.__volume)