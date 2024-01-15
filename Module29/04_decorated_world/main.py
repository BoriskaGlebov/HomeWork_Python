from typing import Callable
from functools import wraps


def decorator_with_args_for_any_decorator(decorator: Callable) -> Callable:
    """Декоратор для декоратора"""
    def wrap_decorator(*args, **kwargs):
        def wrapper_inner(func):
            return decorator(func, *args, **kwargs)

        return wrapper_inner

    return wrap_decorator


@decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs):
    """Декоратор функции"""
    @wraps(func)
    def wrap_func(*args1):
        print(f'Переданные арги и кварги в '
              f'декоратор: '
              f'{args} {kwargs}')
        return func(*args1, **kwargs)

    return wrap_func


@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


print('Задача 4. Весь мир — декоратор…')

decorated_function("Юзер", 101)
# @decorator_with_args_for_any_decorator
def decorated_decorator(func: Callable, *args, **kwargs): # отсюда уже сами!
    pass

@decorated_decorator(100, 'рублей', 200, 'друзей')
def decorated_function(text: str, num: int) -> None:
    print("Привет", text, num)


print('Задача 4. Весь мир — декоратор…')

decorated_function("Юзер", 101)
