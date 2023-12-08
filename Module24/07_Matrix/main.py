class Matrix:
    def __init__(self, row: int, col: int):
        self.row = row
        self.col = col
        self.data = [[' ' for col_el in range(self.col)] for row_el in range(self.row)]

    def __str__(self):
        for i_row in self.data:
            print('|  ', end=' ')
            for i_col in i_row:
                print(i_col, '\t', end='')
            print('| ')
        return ''

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.row == other.row and self.col == other.col:
                new_matrix = Matrix(self.row, self.col)
                new_matrix.data = [
                    [self.data[row_el][col_el] + other.data[row_el][col_el] for col_el in range(self.col)] for row_el
                    in range(self.row)]
                return new_matrix
            else:
                print('Сложение невозможно')

    def __sub__(self, other):
        if isinstance(other, Matrix):
            if self.row == other.row and self.col == other.col:
                new_matrix = Matrix(self.row, self.col)
                new_matrix.data = [
                    [self.data[row_el][col_el] - other.data[row_el][col_el] for col_el in range(self.col)] for row_el
                    in range(self.row)]
                return new_matrix
            else:
                print('Вычитание невозможно')

    def __mul__(self, other):
        if isinstance(other, Matrix):
            if self.col == other.row:
                new_matrix = Matrix(self.row, other.col)
                new_matrix.data = [[0 for col_el in range(other.col)] for row_el in range(self.row)]
                for row_el in range(self.row):
                    for col_el in range(other.col):
                        for i in range(len(self.data[0])):
                            new_matrix.data[row_el][col_el] += self.data[row_el][i] * other.data[i][col_el]
                return new_matrix
            else:
                print('Умножение невозможно')

    def transpose(self):
        new_matrix = Matrix(self.col, self.row)
        new_matrix.data = [[self.data[col_el][row_el] for col_el in range(self.row)] for row_el in range(self.col)]
        return new_matrix


print('Задача 07. Матрицы')

# Примеры работы с классом:

# Создание экземпляров класса Matrix
m1 = Matrix(2, 3)
m1.data = [[1, 2, 3], [4, 5, 6]]

m2 = Matrix(2, 3)
m2.data = [[7, 8, 9], [10, 11, 12]]

# Тестирование операций
print("Матрица 1:")
print(m1)

print("Матрица 2:")
print(m2)

print("Сложение матриц:")
print(m1 + m2)
#
print("Вычитание матриц:")
print(m1 - m2)
#
m3 = Matrix(3, 2)
m3.data = [[1, 2], [3, 4], [5, 6]]

print("Матрица 3:")
print(m3)
#
print("Умножение матриц:")
print(m1 * m3)
#
print("Транспонирование матрицы 1:")
print(m1.transpose())

