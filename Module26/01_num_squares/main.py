# класс-итератор
class Generator:
    def __init__(self, num=10):
        self.limit = num
        self.next_num = -1

    def __iter__(self):
        self.next_num = -1
        return self

    def __next__(self):
        if self.next_num != self.limit:
            self.next_num += 1
            return self.next_num ** 2
        else:
            raise StopIteration


# функция-генератор
def generator(num=10):
    for i in range(num + 1):
        yield i ** 2
        i += 1


print('Задача 1. Квадраты чисел')
# num = int(input('Введите число? '))
num = 10

gen_1 = Generator()
for el in gen_1:
    print(el, end=' ')
print(type(gen_1))

gen_2 = generator()
for el in gen_2:
    print(el, end=' ')
print(type(gen_2))
# генераторное выражение
gen_3 = (i ** 2 for i in range(0, num + 1))
for el in gen_3:
    print(el, end=' ')
print(type(gen_2))
