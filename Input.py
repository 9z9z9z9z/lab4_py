from Product import Product
from Equipment import Equipment
from Food import Food


def input_int() -> int:
    while True:
        try:
            return int(input("Input integer number:\t"))
        except TypeError:
            print("Incorrect input")
        except ValueError:
            print("Incorrect input")


def input_float() -> float:
    while True:
        try:
            return float(input("Input fractional number:\t"))
        except TypeError:
            print("Incorrect input")
        except ValueError:
            print("Incorrect input")

