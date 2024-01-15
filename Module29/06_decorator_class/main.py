from typing import Callable
from functools import update_wrapper
from time import time


class LoggerDecorator:
    """Класс-декоратор"""

    def __init__(self, func: Callable) -> None:
        update_wrapper(self, func)
        self.func = func

    def __call__(self, *args, **kwargs):
        print(f'Вызов функции {self.func.__name__}')
        print(f'Аргументы: {args} {kwargs}')
        start = time()
        rez_func = self.func(*args, **kwargs)
        print(rez_func)
        end = time()
        rez_time = end - start
        print(f'Время выполнения {rez_time} секунд')
        return rez_func


@LoggerDecorator
def complex_algorithm(arg1, arg2):
    # Здесь выполняется сложный алгоритм
    result = 0
    for i in range(arg1):
        for j in range(arg2):
            with open('test.txt', 'w', encoding='utf8') as file:
                file.write(str(i + j))
                result += i + j
    return result


# Пример вызова функции с применением декоратора
result = complex_algorithm(10, 50)
