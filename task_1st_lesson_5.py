x = int(input("Введите выручку: "))
y = int(input("Введите расходы: "))

if x > y:
    z = x - y
    print("Вы в плюсе на", z)
    p = int(input("Введите колличество сотрудников: "))
    zp = (z / p)
    print("Прибыль на одного сотрудника состовляет ", f"{zp:.2f}")
else:
    z = x - y
    print("Вы в минусе на: ", z)
    p = int(input("Введите колличество сотрудников: "))
    zp = (z / p)
    print("Убыток на одного сотрудника состовляет ", f"{zp:.2f}")
