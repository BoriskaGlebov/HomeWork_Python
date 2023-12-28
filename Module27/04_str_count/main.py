# Про атрибуты функции узнал впервые! Пока не очень понимаю зачем они!
# Есть вопросы!
# 1. Вот создал я атрибут функции и для доступа за пределами функции я получаю
# лишь когда  print(good_bye.ns), а
# не print(f.ns) почему так?
# 2. Почему в print(good_bye.ns) ns подчеркивается красным в Pycharm, но
# все равно код выполняется?
# 3. Декоратор создается один на все вызовы функции или для каждой
# функции создаемся свой экземпляр декоратора? Потому вызов разных функции с
# декоратором не происходило увеличение счетчика
#
#


from typing import Callable
import functools


def counter(funk: Callable) -> Callable:
    """Функция декоратор считает сколько раз ее вызывают"""

    def wrapped_funk(*args):
        wrapped_funk.count += 1
        rez = funk(*args)
        print(f'Вызвана функция декоратор {wrapped_funk.count} раз')
        return rez

    wrapped_funk.count = 0
    return wrapped_funk


@counter
def hi(name: str) -> None:
    """Функция выводит приветствие"""
    print(f'Привет, {name} - дружок пирожок')


@counter
def age(age: int) -> None:
    """Функция выводит возраст"""
    print(f'Возраст = {age}')


@counter
def good_bye(name: str) -> None:
    """Функция выводит прощание"""
    good_bye.ns = 12
    print(f'До свидание. Хорошего дня, {name}')


print('Задача 4. Счётчик')
ob = hi('Tom')
print(id(ob))
lob = hi('Tom')
print(id(lob))
mob = hi('Tom')
print(id(mob))

c = age(15)
print(id(c))
f = good_bye('Mike')
print(id(f))
print(good_bye.ns)
