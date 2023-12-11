import math


class Shape:

    def area(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2


class Rectangle(Shape):
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def area(self):
        return self.a * self.b


class Triangle(Shape):
    def __init__(self, a, h):
        self.a = a
        self.h = h

    def area(self):
        return self.a * self.h / 2


print('Задача 06. Абстрактный класс')
# Примеры работы с классом:
# Создание экземпляров классов
circle = Circle(5)
rectangle = Rectangle(4, 6)
triangle = Triangle(3, 8)

# Вычисление площади фигур
circle_area = circle.area()
rectangle_area = rectangle.area()
triangle_area = triangle.area()

# Вывод результатов
print("Площадь круга:", circle_area)

print("Площадь прямоугольника:", rectangle_area)

print("Площадь треугольника:", triangle_area)

print(f"foo{circle_area}")
