import random
a = int(input("Введите сообщение(число):"))
b = int(random.randint(1, 200))
print("Коэф-т b:", b)
g = int(random.randint(1, 200))
print("Коэф-т g:",g)
p = int(random.randint(1, 200))
print("Коэф-т p:",p)
A = (g**a)%p
print("Коэф-т для общего ключа (А):",A)
B = (g**b)%p
print("Коэф-т для общего ключа (А):", B)
Ka = (B**a)%p
print("Ваш общий ключ:", Ka)
Kb = (A**b)%p
print("Общий ключ приятеля:",Kb)
print("Ka = Kb =",Kb)