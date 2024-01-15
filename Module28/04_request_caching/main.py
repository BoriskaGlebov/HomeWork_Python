from typing import Any


class LRUCache:
    """
    Класс LRU Cache (Least Recently Used Cache),
    который будет хранить ограниченное количество
    запросов и автоматически удалять самые старые
    при достижении лимита.
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._cache_dict = dict()
        self.use_counter = dict()

    @property
    def capacity(self) -> int:
        """Геттер максимального количества элементов Кэша"""
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        """Сеттер максимального количества элементов Кэша"""
        self._capacity = capacity

    @property
    def cache(self) -> str:
        """Геттер - этот метод должен возвращать самый старый элемент"""
        return (f'{list(self._cache_dict.keys())[0]} - '
                f'{self._cache_dict[list(self._cache_dict.keys())[0]]}')

    @cache.setter
    def cache(self, new_elem: tuple) -> None:
        """
        Сеттер этот метод должен добавлять новый элемент и
        удаляет наиболее старый элемент или менее используемый
        """
        if len(self._cache_dict.keys()) < self.capacity:
            self._cache_dict[new_elem[0]] = new_elem[1]
        elif len(self.use_counter.keys()) == 0:
            self._cache_dict.pop(list(self._cache_dict.keys())[0])
            self._cache_dict[new_elem[0]] = new_elem[1]
        else:
            max_used = max(self.use_counter.values())  # убрал сортировку на каждом цикле
            for k, v in self.use_counter.items():
                if v == max_used:
                    if list(self._cache_dict.keys())[0] == k:
                        if list(self._cache_dict.keys())[1] in self.use_counter.keys():
                            self.use_counter.pop(list(self._cache_dict.keys())[1])
                        self._cache_dict.pop(list(self._cache_dict.keys())[1])
                        self._cache_dict[new_elem[0]] = new_elem[1]
                        return
                    else:
                        if list(self._cache_dict.keys())[0] in self.use_counter.keys():
                            self.use_counter.pop(list(self._cache_dict.keys())[0])
                        self._cache_dict.pop(list(self._cache_dict.keys())[0])
                        self._cache_dict[new_elem[0]] = new_elem[1]
                        return

    def print_cache(self) -> None:
        """Выводит текущий кэш"""
        print(', '.join(f'{k}:{v}' for k, v in self._cache_dict.items()))

    def get(self, key) -> Any:
        """Получаем значение по ключу"""
        if key not in self.use_counter.keys():
            self.use_counter[key] = 1
            return self._cache_dict[key]
        else:
            self.use_counter[key] += 1
            return self._cache_dict[key]


print('Задача 4. Кэширование запросов')

# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

#
# # # # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3
# #
# # # Получаем значение по ключу
print(cache.get("key2"))  # value2
print(cache.get("key2"))
print(cache.get("key1"))

#
# #
# # # Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")


# #
# # # Выводим обновленный кэш
print(cache.cache)
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
from typing import Any


class LRUCache:
    """
    Класс LRU Cache (Least Recently Used Cache),
    который будет хранить ограниченное количество
    запросов и автоматически удалять самые старые
    при достижении лимита.
    """

    def __init__(self, capacity: int) -> None:
        self._capacity = capacity
        self._cache_dict = dict()
        self.use_counter = dict()

    @property
    def capacity(self) -> int:
        """Геттер максимального количества элементов Кэша"""
        return self._capacity

    @capacity.setter
    def capacity(self, capacity: int) -> None:
        """Сеттер максимального количества элементов Кэша"""
        self._capacity = capacity

    @property
    def cache(self) -> str:
        """Геттер - этот метод должен возвращать самый старый элемент"""
        return (f'{list(self._cache_dict.keys())[0]} - '
                f'{self._cache_dict[list(self._cache_dict.keys())[0]]}')

    @cache.setter
    def cache(self, new_elem: tuple) -> None:
        """
        Сеттер этот метод должен добавлять новый элемент и
        удаляет наиболее старый элемент или менее используемый
        """
        if len(self._cache_dict.keys()) < self.capacity:
            self._cache_dict[new_elem[0]] = new_elem[1]
        elif len(self.use_counter.keys()) == 0:
            self._cache_dict.pop(list(self._cache_dict.keys())[0])
            self._cache_dict[new_elem[0]] = new_elem[1]
        else:
            max_used = max(self.use_counter.values())  # убрал сортировку на каждом цикле
            for k, v in self.use_counter.items():
                if v == max_used:
                    if list(self._cache_dict.keys())[0] == k:
                        if list(self._cache_dict.keys())[1] in self.use_counter.keys():
                            self.use_counter.pop(list(self._cache_dict.keys())[1])
                        self._cache_dict.pop(list(self._cache_dict.keys())[1])
                        self._cache_dict[new_elem[0]] = new_elem[1]
                        break
                    else:
                        if list(self._cache_dict.keys())[0] in self.use_counter.keys():
                            self.use_counter.pop(list(self._cache_dict.keys())[0])
                        self._cache_dict.pop(list(self._cache_dict.keys())[0])
                        self._cache_dict[new_elem[0]] = new_elem[1]
                        break

    def print_cache(self) -> None:
        """Выводит текущий кэш"""
        print(', '.join(f'{k}:{v}' for k, v in self._cache_dict.items()))

    def get(self, key) -> Any:
        """Получаем значение по ключу"""
        if key not in self.use_counter.keys():
            self.use_counter[key] = 1
            return self._cache_dict[key]
        else:
            self.use_counter[key] += 1
            return self._cache_dict[key]


print('Задача 4. Кэширование запросов')

# Создаем экземпляр класса LRU Cache с capacity = 3
cache = LRUCache(3)

# Добавляем элементы в кэш
cache.cache = ("key1", "value1")
cache.cache = ("key2", "value2")
cache.cache = ("key3", "value3")

#
# # # # Выводим текущий кэш
cache.print_cache()  # key1 : value1, key2 : value2, key3 : value3
# #
# # # Получаем значение по ключу
print(cache.get("key2"))  # value2
print(cache.get("key2"))
print(cache.get("key1"))

#
# #
# # # Добавляем новый элемент, превышающий лимит capacity
cache.cache = ("key4", "value4")


# #
# # # Выводим обновленный кэш
print(cache.cache)
cache.print_cache()  # key2 : value2, key3 : value3, key4 : value4
