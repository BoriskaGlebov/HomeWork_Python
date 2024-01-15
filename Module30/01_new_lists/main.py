from typing import List
from functools import reduce


def multiplication(a: int, b: int) -> int:
    """Произведение двух чисел"""
    result = a * b
    return result


print('Задача 1. Новые списки')

floats: List[float] = [12.3554, 4.02, 5.777, 2.12, 3.13, 4.44, 11.0001]
names: List[str] = ["Vanes", "Alen", "Jana", "William", "Richards", "Joy"]
numbers: List[int] = [22, 33, 10, 6894, 11, 2, 1]

rez1 = list(map(lambda el: round(el ** 3, 3), floats))
print(rez1)
rez2 = list(filter(lambda el: len(el) >= 5, names))
print(rez2)
rez3 = reduce(lambda a, b: a * b, numbers)
rez4 = reduce(multiplication,numbers)
print(rez3)
print(rez4)
