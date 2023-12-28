import functools, datetime
from typing import Callable


def logging(funk: Callable) -> Callable:
    """
    Функция декоратор
    """

    def wrap_funk(*args):
        try:
            rez = funk(*args)
            print(f'Функция называется: {funk.__name__}')
            print(f'Документация к функции:\n{funk.__doc__}')
            print()
            return rez
        except TypeError as exc:
            with open('error.txt', 'a+', encoding='utf8') as error_file:
                today = datetime.datetime.now().strftime("%d/%m/%Y - %H:%M")
                error_file.write(f'{today} ERROR {type(exc)} в функции {funk.__name__}\n')
                print('ОШИБОЧКА типа данных!\n')

    return wrap_funk


@logging
def hi(name: str) -> None:
    """Функция приветствие"""
    print(f'Дарова {name}')


@logging
def age(num: int) -> None:
    """Функция выводит возраст"""
    print(f'Твой возраст {num + 1} лет')


@logging
def good_bye(name: str) -> str:
    """Функция прощается:return строка прощания
    """
    return f'Пока, до новых встреч {name}'


print('Задача 3. Логирование')

a = hi('Boris')
b = age('sad')
c = age(15)
print(good_bye('Tom'))
