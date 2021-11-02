"""
1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
который должен принимать данные (список списков) для формирования матрицы.
Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
Примеры матриц вы найдете в методичке.
Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса Matrix
(двух матриц). Результатом сложения должна быть новая матрица.
Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки первой матрицы
складываем с первым элементом первой строки второй матрицы и т.д.
"""


class Matrix:

    def __init__(self, list_1, list_2):
        self.list_1 = list_1
        self.list_2 = list_2

    def __add__(self):
        matrix = [
            [0, 0, 0],
            [0, 0, 0],
            [0, 0, 0],
        ]

        for i in range(len(self.list_1)):
            for k in range(len(self.list_2)):
                matrix[i][k] = self.list_1[i][k] + self.list_2[i][k]

        return str('\n'.join(['\t'.join([str(k) for k in i]) for i in matrix]))

    def __str__(self, matrix=None):
        return str('\n'.join(['\t'.join([str(k) for k in i]) for i in matrix]))


test_matrix = Matrix([
    [2, 3, 5],
    [2, 5, 2],
    [6, 1, 1],
], [
    [5, 7, 8],
    [2, 3, 9],
    [1, 1, 1],
]
)

print(test_matrix.__add__())

"""
2. Реализовать проект расчета суммарного расхода ткани на производство одежды. Основная сущность (класс) 
этого проекта — одежда, которая может иметь определенное название. К типам одежды в этом проекте 
относятся пальто и костюм. У этих типов одежды существуют параметры: размер (для пальто) и рост 
(для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать формулы: для пальто (V/6.5 + 0.5), 
для костюма (2 * H + 0.3). Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани. Проверить на практике полученные на этом уроке знания: 
реализовать абстрактные классы для основных классов проекта, проверить на практике работу декоратора @property.
"""


class Textile:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_coat_square(self):
        return self.width / 6.5 + 0.5

    def get_jacket_square(self):
        return self.height * 2 + 0.3

    @property
    def get_full_square(self):
        return str(f'Общая площадь ткани \n'
                   f' {(self.get_coat_square()) + (self.get_jacket_square())}')


class Coat(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_c = round(self.get_coat_square())

    def __str__(self):
        return f'Площадь, требуемая для пальто {self.square_c}'


class Jacket(Textile):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.square_j = round(self.get_jacket_square())

    def __str__(self):
        return f'Площадь, требуемая на костюм {self.square_j}'


coat = Coat(5, 9)
jacket = Jacket(2, 3)
print(coat)
print(jacket)
print(coat.get_full_square)
print(jacket.get_full_square)
print(jacket.get_coat_square())
print(jacket.get_jacket_square())

"""
3. Реализовать программу работы с органическими клетками. Необходимо создать класс Клетка. 
В его конструкторе инициализировать параметр, соответствующий количеству клеток (целое число). 
В классе должны быть реализованы методы перегрузки арифметических операторов: сложение (__add__()), 
вычитание (__sub__()), умножение (__mul__()), деление (__truediv__()).Данные методы должны 
применяться только к клеткам и выполнять увеличение, уменьшение, умножение и обычное 
(не целочисленное) деление клеток, соответственно. В методе деления должно осуществляться 
округление значения до целого числа.
"""


class Cell:
    def __init__(self, quantity):
        self.quantity = int(quantity)

    def __str__(self):
        return f'Результат операции {self.quantity * "*"}'

    def __add__(self, other):
        return Cell(self.quantity + other.quantity)

    def __sub__(self, other):
        return self.quantity - other.quantity if (self.quantity - other.quantity) > 0 else print(
            'Результат отрицательный')

    def __mul__(self, other):
        return Cell(int(self.quantity * other.quantity))

    def __truediv__(self, other):
        return Cell(round(self.quantity // other.quantity))

    def make_order(self, cells_in_row):
        row = ''
        for i in range(int(self.quantity / cells_in_row)):
            row += f'{"*" * cells_in_row} \\n'
        row += f'{"*" * (self.quantity % cells_in_row)}'
        return row


cells1 = Cell(12)
cells2 = Cell(3)
print(cells1)
print(cells1 + cells2)
print(cells2 - cells1)
print(cells2.make_order(12))
print(cells1.make_order(3))
print(cells1 / cells2)
