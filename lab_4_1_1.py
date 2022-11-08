from Equipment import Equipment
from Food import Food


base = [Equipment("Skies", 300, "Sport_Equipment", 300, 20, 5),
        Equipment("Tanks", 3000, "War_Equipment", 30000, 2000, 500),
        Food("Chicken", 120, (5, 11, 2022), 10, 15, 10, 5)]


print("\nCount of products in the box:")
print((base[1]).count(100000, 1, 1)) # Упаковка товаров в коробку

print(base[0])
print(base[2])
print(base[0] + base[2]) # "Сложение" товаров

print(base[0])
base[0].discount(25) # Изменение цены из-за скидки
print(base[0])
