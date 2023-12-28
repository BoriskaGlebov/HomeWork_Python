from collections.abc import Callable
from functools import wraps


def check_permission(user: str) -> Callable:
    """
    Декоратор с аргументом
    Проверяет, есть ли у
    пользователя доступ к
    вызываемой функции, и если
    нет, то выдаёт исключение
    PermissionError
    """

    # Правильно я называю эту функцию декоратором с аргументом?

    def decorator(func: Callable) -> Callable:
        """Функция декоратор проверят право доступа"""
        @wraps(func)
        def wrap_func(*args) -> Callable:
            try:
                if user in user_permissions:
                    rez = func()
                    return rez
                raise PermissionError
            except PermissionError as exc:
                print(f'{type(exc).__name__}: '
                      f'У пользователя '
                      f'недостаточно прав, '
                      f'чтобы выполнить '
                      f'функцию {func.__name__}')

        return wrap_func

    return decorator
    pass


user_permissions = ['admin']


@check_permission('admin')
def delete_site():
    """Функция удаления сайта"""
    print('Удаляем сайт')


@check_permission('user_1')
def add_comment():
    """Функция добавление комментария на сайт"""
    print('Добавляем комментарий')


print('Задача 1. Права доступа')

delete_site()
add_comment()
