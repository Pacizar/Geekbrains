x = input("Введите слово: ").split()

for a, b in enumerate(x, 1):
    print(a, b) if len(b) <= 10 else print(a, b[:10])
