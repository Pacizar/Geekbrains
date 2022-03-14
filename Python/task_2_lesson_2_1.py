r_list = []
q = None
for q in r_list:
    q = input("Желаете добавить значение в лист?: Y/N ")
    if q == "Y" or "y":
        x = input("Введите значение для списка: ")
        r_list.append(x)
        print(r_list)
    elif q == "N" or "n":
        print(r_list)
        break
    else:
        print(input("Введите символ 'Y' если Да и 'N' если Нет: "))
