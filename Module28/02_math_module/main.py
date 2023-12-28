import math


class MyMath:
    """
    Класс собственных математических функций\n
    - вычисление длины окружности,\n
    - вычисление площади окружности,\n
    - вычисление объёма куба,\n
    - вычисление площади поверхности сферы.
    """

    @classmethod
    def circle_len(cls, radius: float) -> float:
        """
        Функция возвращает длину окружности
            :return длина окружности
        """

        rez = 2 * math.pi * radius
        return rez

    @classmethod
    def circle_square(cls, radius: float) -> float:
        """
        Функция возвращает площадь окружности
            :return площадь окружности
        """
        rez = math.pi * radius ** 2
        return rez

    @classmethod
    def cube_volume(cls, side: float) -> float:
        """
        Функция вычисляет объем куба
            :return объем куба
        """
        rez = side * 3
        return rez

    @classmethod
    def sphere_square(cls, radius: float) -> float:
        """
        Функция вычисляет площадь поверхности шара
            :return площадь поверхности шара"""
        rez = 4 * math.pi * radius * 2
        return rez


print('Задача 2. Математический модуль')
res_1 = MyMath.circle_len(5)
res_2 = MyMath.circle_square(6)
print(res_1)
print(res_2)
