instance = list()


# опять проблеммма с указанием типа возвращаемых данных
def singleton(cls):
    """Декоратор класса
    Позваляет создать только один объект класса"""

    def wrap_cls(*args, **kwargs):
        if len(instance) == 0:
            rez = cls()
            instance.append(rez)
            return rez
        else:
            return instance[0]

    return wrap_cls


@singleton
class Example:
    pass


print('Задача 5. Синглтон')

my_obj = Example()
my_another_obj = Example()

print(id(my_obj))
print(id(my_another_obj))

print(my_obj is my_another_obj)
