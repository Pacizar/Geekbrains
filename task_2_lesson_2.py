x_list = list(input("Введите числа: "))

for x in range(1, len(x_list), 2):
    x_list[x - 1], x_list[x] = x_list[x], x_list[x - 1]

print(x_list)
