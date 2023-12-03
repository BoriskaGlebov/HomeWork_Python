import math


def get_sage_sqrt(num):
    try:
        rez = math.sqrt(num)
        return rez
    except (ValueError, TypeError):
        # print('Поступило отрицательное число! Ошибка')
        return 'Ошибка!'


# Здесь создайте функцию get_sage_sqrt


# Тестовые случаи
numbers = [16, 25, -9, 0, 4.5, "abc"]
for number in numbers:
    result = get_sage_sqrt(number)
    print(f"Квадратный корень numbers {number}: {result}")
