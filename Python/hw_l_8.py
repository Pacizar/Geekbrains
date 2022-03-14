# """
# 1. Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
# «день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число». Второй, с декоратором @staticmethod,
# должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.
# """
#
#
# class Date:
#     def __init__(self, day_month_year):
#         self.day_month_year = str(day_month_year)
#
#     @classmethod
#     def extract(cls, day_month_year):
#         date = []
#
#         for i in day_month_year.split():
#             if i != '-':
#                 date.append(i)
#
#         return int(date[0]), int(date[1]), int(date[2])
#
#     @staticmethod
#     def valid(day, month, year):
#
#         if 1 <= day <= 31:
#             if 1 <= month <= 12:
#                 if 2022 >= year >= 0:
#                     return f'All right'
#                 else:
#                     return f'Неправильный год'
#             else:
#                 return f'Неправильный месяц'
#         else:
#             return f'Неправильный день'
#
#     def __str__(self):
#         return f'Текущая дата {Date.extract(self.day_month_year)}'
#
#
# today = Date('03 - 11 - 2021')
# print(today)
# print(Date.valid(3, 11, 2025))
# print(today.valid(3, 15, 2021))
# print(Date.extract('45 - 11 - 2021'))
# print(today.extract('03 - 11 - 2021'))
# print(Date.valid(35, 11, 2021))
#
# """
# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию деления на нуль. Проверьте его работу
# на данных, вводимых пользователем. При вводе пользователем нуля в качестве делителя программа должна
# корректно обработать эту ситуацию и не завершиться с ошибкой.
# """
#
#
# class BOOM_DivisionByZero(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# try:
#     devidend = int(input('Введите число, которое необходимо разделить: '))
#     division = int(input('Введите число, НА которое собираетесь разделить: '))
#     if not division:
#         raise BOOM_DivisionByZero('BOOM! на ноль делить нельзя!')
#     print(f'Результат {devidend / division}')
#
# except ValueError:
#     print('вы ввели не числа')
# except BOOM_DivisionByZero as error:
#     print(error)
#
# """
# 3. Создайте собственный класс-исключение, который должен проверять содержимое списка на наличие только
# чисел. Проверить работу исключения на реальном примере. Необходимо запрашивать у пользователя данные и
# заполнять список. Класс-исключение должен контролировать типы данных элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются бесконечно, пока пользователь сам не
# остановит работу скрипта, введя, например, команду “stop”. При этом скрипт завершается, сформированный
# список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить только числа и строки.
# При вводе пользователем очередного элемента необходимо реализовать проверку типа элемента и вносить
# его в список, только если введено число. Класс-исключение должен не позволить пользователю ввести текст
# (не число) и отобразить соответствующее сообщение. При этом работа скрипта не должна завершаться.
# """
#
#
# class NotANumberException(Exception):
#     def __init__(self, txt):
#         self.txt = txt
#
#
# result_list = []
# while True:
#     value = input('Введите число для добавления в список или stop для выхода: ')
#
#     if value == 'stop':
#         print(f'Список на момент выхода{result_list}')
#         break
#
#     try:
#         if not value.isnumeric():
#             raise NotANumberException('Вы точно ввели число?!')
#         result_list.append(int(value))
#     except NotANumberException as error:
#         print('Вы ввели не число')

"""
4. Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс 
«Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники 
(принтер, сканер, ксерокс). В базовом классе определить параметры, общие для приведенных типов. 
В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

5. Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и
передачу в определенное подразделение компании. Для хранения данных о наименовании и количестве единиц
оргтехники, а также других данных, можно использовать любую подходящую структуру, например словарь.

6. Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.
Подсказка: постарайтесь по возможности реализовать в проекте «Склад оргтехники» максимум возможностей,
изученных на уроках по ООП.
"""


class Warehouse:

    def __init__(self, name, price, quantity, article, *args):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.article = article
        self.storage = []
        self.unit_dict = {'Модель': self.name, 'Цена': self.price, 'Количество': self.quantity, 'Артикул': self.article}

    def __str__(self):
        return f'{self.name}, цена {self.price} руб., количество {self.quantity} шт.'

    def add_dict(self):
        try:
            unit_n = input(f'Введите название: ')
            unit_p = int(input(f'Введите цену за ед.: '))
            unit_q = int(input(f'Введите количество: '))
            unit_a = int(input(f'Введите артикул: '))
            uni_input = {'Модель': unit_n, 'Цена': unit_p, 'Количество': unit_q, 'Артикул': unit_a}
            self.storage.append(uni_input)
            print(f'\n {self.storage}')
        except:
            return f'Что-то пошло не так'
        a = input('Для выхода - Q, продолжение - Enter')
        if a == 'Q' or a == 'q':
            print('Наш склад -\n', "\n ".join(map(str, self.storage)))
            return f'Отлично поработали!'
        else:
            return Warehouse.add_dict(self)


class Printer(Warehouse):
    pass


class Scanner(Warehouse):
    pass


class Copier(Warehouse):
    pass


unit1 = Printer('Sharp', 14000, 19, 100345)
unit2 = Scanner('Samsung', 4000, 8, 105437)
unit3 = Copier('HP', 17000, 7, 123248)
print(unit1)
print(unit2.add_dict())

"""
7. Реализовать проект «Операции с комплексными числами». Создайте класс «Комплексное число», 
реализуйте перегрузку методов сложения и умножения комплексных чисел. Проверьте работу проекта, 
создав экземпляры класса (комплексные числа) и выполнив сложение и умножение созданных экземпляров. 
Проверьте корректность полученного результата.
"""


class ComplexNumber:
    def __init__(self, a, b, *args):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        print(f'Сумма z1 и z2 равна')
        return f'z = {self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        print(f'Произведение z1 и z2 равно')
        return f'z = {self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'z = {self.a} + {self.b} * i'


z_1 = ComplexNumber(1, -3)
z_2 = ComplexNumber(3, 4)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
