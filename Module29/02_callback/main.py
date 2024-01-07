from typing import Any
from collections.abc import Callable
from functools import wraps

app = dict()


def callback(key: Any) -> Callable:
    """Функция обратного вызова"""

    def decorator(func: Callable) -> Callable:
        app[key] = func

        @wraps(func)
        def wrap_func(*args):
            rez = func()
            return func

        return wrap_func

    return decorator


@callback('//')
def example():
    """Функция пример"""
    print('Пример функции, которая возвращает ответ сервера')
    return 'OK'


print('Задача 2. Функция обратного вызова')
route = app.get('//')
if route:
    response = route()
    print('Ответ:', response)
else:
    print('Такого пути нет')
