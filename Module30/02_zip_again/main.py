from typing import List

print('Задача 2. И снова zip')
letters: List[str] = ['a', 'b', 'c', 'd', 'e']
numbers: List[int] = [1, 2, 3, 4, 5, 6, 7, 8]
rez = list(map(lambda a, b: (a, b), letters, numbers))
print(rez)
print(list(zip(letters, numbers)))