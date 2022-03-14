x_list = [9, 8, 7, 6, 5, 4, 3, 2, 1]
a = int(input("Введите число: "))
y = 0
for b in x_list:
    if a <= b:
        y += 1
    else:
        break
x_list.insert(y, a)
print(x_list)
