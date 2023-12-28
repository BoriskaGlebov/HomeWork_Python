from typing import Callable
import time
from functools import wraps


# Почему для атрибудтов функции не выпадают автозаполнение PyCharm


def caching(funk: Callable) -> Callable:
    """Функция декоратор кэширует данные рекурсивной функции"""

    @wraps(funk)
    def wrapped_funk(*args):
        if args not in wrapped_funk.self_dict:
            rez = funk(*args)
            wrapped_funk.self_dict[args] = rez
            return rez
        else:
            return wrapped_funk.self_dict[args]

    wrapped_funk.self_dict = dict()

    return wrapped_funk


@caching
def fibonacci(number: int) -> int:
    """Функция рассчитывающая сумму членов последовательности Фибоначчи"""
    if number <= 1:
        return number
    return fibonacci(number - 1) + fibonacci(number - 2)


start = time.time()
# Вычисление числа Фибоначчи с использованием кеширования
print(fibonacci(10))  # Результат будет кеширован
end = time.time()
print(end - start)
# Повторное вычисление числа Фибоначчи с теми же аргументами
print(fibonacci(10))  # Результат будет взят из кеша

# Вычисление числа Фибоначчи с другим аргументом
print(fibonacci(5))  # Результат будет вычислен и закеширован
