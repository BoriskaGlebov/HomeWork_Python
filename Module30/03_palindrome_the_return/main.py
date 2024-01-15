from collections import Counter


def can_be_poly(text: str) -> bool:
    """Функция проверяет можно ли получить палиндром из текста"""
    rez = len(list(filter(lambda el: el % 2 != 0, Counter(text).values()))) < 2
    return rez


print('Задача 3. Палиндром: возвращение')

print(can_be_poly('abcba'))
print(can_be_poly('abbbc'))
