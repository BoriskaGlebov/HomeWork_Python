from collections.abc import Callable
from datetime import datetime
from time import time
from functools import wraps
import locale

locale.setlocale(locale.LC_ALL, 'ru_RU')


# Блин тут какой-то ужас!
# У меня есть декоратор таймер


def log_methods(format_data: str):
    new_format = ''.join('%' + el if el.isalpha() else el for el in format_data)

    def format_for_timer(cls, func: Callable) -> Callable:
        @wraps(func)
        def wrap_func(*args, **kwargs):
            start = time()
            print(
                f'-Запускается {cls.__name__}.{func.__name__}. '
                f'Дата и время запуска: {datetime.now().strftime(new_format)}')
            rez = func(*args)
            rez_time = round((time() - start), 3)
            print(f'-Завершение {cls.__name__}.{func.__name__}, '
                  f'время работы = {rez_time} s')
            return rez

        return wrap_func

    def decorated_cls(cls):
        for i_methods in dir(cls):
            if i_methods.startswith('__') is False:
                cur_method = getattr(cls, i_methods)
                decorated_method = format_for_timer(cls, cur_method)
                setattr(cls, i_methods, decorated_method)
        return cls

    return decorated_cls


@log_methods("b d Y - H:M:S")
class A:
    def test_sum_1(self) -> int:
        print('Тут метод test sum 1')
        number = 100
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


@log_methods("b d Y - H:M:S")
class B(A):

    def test_sum_1(self):
        super().test_sum_1()
        print("Тут метод test sum 1 у наследника")

    def test_sum_2(self):
        print("test sum 2")
        number = 200
        result = 0
        for _ in range(number + 1):
            result += sum([i_num ** 2 for i_num in range(10000)])

        return result


print('Задача 3. Логирование в формате')

my_obj = B()
my_obj.test_sum_1()
my_obj.test_sum_2()
