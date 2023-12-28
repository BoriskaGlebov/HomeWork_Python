from typing import Callable

print('Задача 1. Как дела?')


def how_are_you(funk: Callable) -> Callable:
    """ Функция декоратор """
    # Необходимости в функции functools.wraps нет
    # Так как я исходную функцию не меняю совсем то и документация не меняется
    input('как дела?')
    print('А у меня не очень! Ладно, держи свою функцию.')
    return funk


@how_are_you
def test():
    """Функция просто выводит строчку """
    print('<Тут что-то происходит...>')


d = test()
print('Название функции:', test.__name__)
print('Документация к функции:', test.__doc__)
