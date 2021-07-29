n = int(input("Введите целое положительное число: "))
max_n = n % 10
n = n // 10
while n > 0:
    if n % 10 > max_n:
        max_n = n % 10
    n = n // 10
print(max_n)
