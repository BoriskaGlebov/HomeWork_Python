import functools, time
from typing import Callable, Any, Generator


def slow_down(funk: Callable) -> Callable:
    """"Декоратор функции. Замедляет распаковку функции"""""

    @functools.wraps(funk)
    def wrap_funk(num: int) -> Any:
        rez = funk(num)
        for el in rez:
            print(el)
            time.sleep(0.5)
        return rez

    return wrap_funk


@slow_down
def test(num: int) -> Generator:
    """Функция генератор
    :return Generator
    """
    sequence = (el + 2 for el in range(num))
    return sequence


print('Задача 2. Замедление кода')

d = test(5)

print(test.__name__)
print(test.__doc__)
