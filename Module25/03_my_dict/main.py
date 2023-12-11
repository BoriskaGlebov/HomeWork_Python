from random import randint


class MyDict(dict):
    def get(self, key, default=0):
        return super().get(key, default)


print('Задача 03. Свой словарь')

user = MyDict({i: [randint(1, 10) for el in range(5)] for i in range(10)})
print(user.get(1))
print(user.get(100))
