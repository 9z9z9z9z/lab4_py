from Equipment import Equipment
from Food import Food

base = [Equipment("Skies", 300, "Sport_Equipment", 300, 20, 5),
        Equipment("Tanks", 3000, "War_Equipment", 30000, 2000, 500),
        Food("Chicken", 120, (5, 11, 2022), 10, 15, 10, 5)]

print((base[0] + base[2]).count(1000000, 1, 1))
print(base[0] + base[2])
print(base[0])
print(base[2])
