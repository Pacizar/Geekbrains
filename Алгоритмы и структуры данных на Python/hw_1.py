# # 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

# numb = int(input("Введите трехзначное число: "))

# a = numb // 100
# b = numb // 10 % 10
# c = numb % 10

# print("Сумма цифр числа равна: ", (a + b + c))
# print("Произведение цифр числа равна: ", (a * b * c))

# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

# a = 5
# print("%d = %s" % (a, bin(a)))
# b = 6
# print("%d = %s" % (b, bin(b)))

# print("%d & %d = %d (%s)" % (a, b, a & b, bin(a & b)))
# print("%d | %d = %d (%s)" % (a, b, a | b, bin(a | b)))
# print("%d ^ %d = %d (%s)" % (a, b, a ^ b, bin(a ^ b)))
# print("%d << 2 = %d (%s)" % (a, a << 2, bin(a << 2)))
# print("%d >> 2 = %d (%s)" % (a, a >> 2, bin(a >> 2)))

# Задание слизал из инета, абсолютно не понял задачи, возможно по причине того,
# что питон начинал изучать пол года назад и не практиковал его.

# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y=kx+b, проходящей через эти точки.

# print("Координаты точки A(x1;y1):")
# x1 = float(input("\tx1 = "))
# y1 = float(input("\ty1 = "))

# print("Координаты точки B(x2;y2):")
# x2 = float(input("\tx2 = "))
# y2 = float(input("\ty2 = "))

# print("Уравнение прямой, проходящей через эти точки:")
# k = (y1 - y2) / (x1 - x2)
# b = y2 - k * x2
# print(" y = %.2f*x + %.2f" % (k, b))

# 4. Написать программу, которая генерирует в указанных пользователем границах:

# случайное целое число;
# случайное вещественное число;
# случайный символ.

# Для каждого из трех случаев пользователь задает свои границы диапазона.
# Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
# Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

# from random import random

# m1 = int(input("Введите целое число 'от': "))
# m2 = int(input("Введите целое число 'до': "))
# n = int(random() * (m2 - m1 + 1)) + m1
# print(n)

# m1 = float(input("Введите вещественное число 'от': "))
# m2 = float(input("Введите вещественное число 'до': "))
# n = random() * (m2 - m1) + m1
# print(round(n, 3))

# m1 = ord(input("Введите символ 'от': "))
# m2 = ord(input("Введите символ 'до': "))
# n = int(random() * (m2 - m1 + 1)) + m1
# print(chr(n))

# 5. Пользователь вводит две буквы. Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

# a = ord(input('1-я буква: '))
# b = ord(input('2-я буква: '))
# a = a - ord('a') + 1
# b = b - ord('a') + 1
# print('Позиции: %d и %d' % (a, b))
# print('Между буквами символов:', abs(a - b) - 1)

# n = int(input('Номер буквы в алфавите: '))
# n = ord('a') + n - 1
# print('Это буква', chr(n))

# 6. Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

# n = int(input('Номер буквы в алфавите: '))
# n = ord('a') + n - 1
# print('Это буква', chr(n))

# 7. По длинам трех отрезков, введенных пользователем, определить возможность существования треугольника,
# составленного из этих отрезков. Если такой треугольник существует, то определить,
# является ли он разносторонним, равнобедренным или равносторонним.

# a = int(input("a = "))
# b = int(input("b = "))
# c = int(input("c = "))

# if a + b <= c or a + c <= b or b + c <= a:
#     print("Треугольник не существует")
# elif a != b and a != c and b != c:
#     print("Разносторонний")
# elif a == b == c:
#     print("Равносторонний")
# else:
#     print("Равнобедренный")

# 8. Определить, является ли год, который ввел пользователем, високосным или невисокосным.

# y = int(input())
# if y % 4 != 0 or (y % 100 == 0 and y % 400 != 0):
#     print("Обычный")
# else:
#     print("Високосный")

# 9. Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

# print('Введите три числа: ')
# a = int(input())
# b = int(input())
# c = int(input())

# if b < a < c or c < a < b:
#     print('Среднее:', a)
# elif a < b < c or c < b < a:
#     print('Среднее:', b)
# else:
#     print('Среднее:', c)
