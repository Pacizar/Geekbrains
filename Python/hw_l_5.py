"""
1. Создать программно файл в текстовом формате, записать в него построчно данные,
вводимые пользователем. Об окончании ввода данных свидетельствует пустая строка.
"""

new_file = open('test.txt', 'w')
line = input('Введите текст \n')  # Проблема_1: не смог разобраться, почему после \n не переносится на новую строку.
while line:
    new_file.writelines(line)
    line = input('Введите текст \n')  # Проблема_1
    if not line:
        break

new_file.close()
new_file = open('test.txt', 'r')
content = new_file.readlines()
print(content)
new_file.close()

"""
2. Создать текстовый файл (не программно), сохранить в нем несколько строк, 
выполнить подсчет количества строк, количества слов в каждой строке.
"""

new_file = open('test.txt', 'r')
content = new_file.read()
print(f'Содержимое файла: ', '\n')  # Проблема_1
new_file = open('test.txt', 'r')
content = new_file.readlines()
print(f'Количество строк в файле - {len(content)}')
new_file = open('test.txt', 'r')
content = new_file.readlines()
for i in range(len(content)):
    print(f'Количество символов {i + 1} - ой строки {len(content[i])}')
new_file = open('test.txt', 'r')
content = new_file.read()
content = content.split()
print(f'Общее количество слов - {len(content)}')
new_file.close()

"""
3. Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов. 
Определить, кто из сотрудников имеет оклад менее 20 тыс., вывести фамилии этих сотрудников. 
Выполнить подсчет средней величины дохода сотрудников.
"""

with open('sal.txt', 'r') as f:
    sal = []
    poor = []
    my_list = f.read().split('\n')
    for i in my_list:
        i = i.split()
        if int(i[1]) < 20000:
            poor.append(i[0])
        sal.append(i[1])
print(f'Оклад меньше 20.000 {poor}, средний оклад {sum(map(int, sal)) / len(sal)}')

"""
4. Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные. 
При этом английские числительные должны заменяться на русские. Новый блок строк должен 
записываться в новый текстовый файл.
"""

rus = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
new_file = []
with open('onetwothree.txt', 'r') as f:
    for i in f:
        i = i.split(" ", 1)
        new_file.append(rus[i[0]] + "  " + i[1])
    print(new_file)

with open('onetwothree_new.txt', 'w+') as f_2:
    f_2.writelines(new_file)

"""
5. Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами. 
Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
"""

def summary():
    try:
        with open('somemun.txt', 'w+') as f:
            line = input('Введите цифры через пробел \n')
            f.writelines(line)
            s_num = line.split()

            print(sum(map(int, s_num)))
    except IOError:
        print('Ошибка в файле')
    except ValueError:
        print('Неправильно набран номер. Ошибка ввода-вывода')
summary()

"""

6. Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет 
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество. 
Важно, чтобы для каждого предмета не обязательно были все типы занятий. 
Сформировать словарь, содержащий название предмета и общее количество занятий по нему. 
Вывести словарь на экран.
"""

import re
subj = {}
with open('dif_sub.txt', 'r') as f:
    for line in f.readlines():
        subj[re.findall(r'^\w+', line)[0]] = sum(map(int, re.findall(r'\d+', line)))
    print(f'Общее количество часов по предмету - \n {subj}')

"""
7. Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме: 
название, форма собственности, выручка, издержки.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль. 
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь 
со средней прибылью. Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Итоговый список сохранить в виде json-объекта в соответствующий файл.
"""


import json


def get_statistics():
    try:
        with open('for_tusk_7.txt', 'r+', encoding='utf-8') as f:
            statistics = []
            profit = {}
            average_profit = {}
            av = 0
            prof = 0
            i = 3
            for line in f:
                name, firm, earning, damage = line.split()
                total = int(earning) - int(damage)
                if total >= 0:
                    prof = prof + total
                else:
                    i -= 1
                profit[name] = total
            statistics.append(profit)
            if i != 0:
                (av) = prof / i
                average_profit['average_profit'] = round(av)
                statistics.append(average_profit)
            else:
                print('Все компании работают в убыток')
            print(statistics)
        with open('for_tusk_7.json', 'a+', encoding='utf-8') as json_file:
            json.dump(statistics, json_file)
    except FileNotFoundError:
        return 'Файл не найден.'


get_statistics()