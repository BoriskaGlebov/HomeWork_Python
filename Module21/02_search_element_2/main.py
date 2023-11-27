# deep = -1 для корректной работы вызова рекурсии без глубины
# rez='Такого нет!' для случая если глубин будет 0 то результат должен быть таким
def searcher(structure, key, deep=-1, rez='Такого нет!'):
    if deep != 0:
        deep -= 1
        if key in structure:
            rez = structure[key]
            return rez
        for sub_structure in structure.values():
            if isinstance(sub_structure, dict):
                rez = searcher(sub_structure, key,deep)
                if rez != 'Такого нет!':
                    break
        else:
            rez = 'Такого нет!'
    return rez


print('Задача 2. Поиск элемента 2')

site = {
    'html': {
        'head': {
            'title': 'Мой сайт'
        },
        'body': {
            'h2': 'Здесь будет мой заголовок',
            'div': 'Тут, наверное, какой-то блок',
            'p': 'А вот здесь новый абзац'
        }
    }
}

key_word = input('Введите искомый ключ: ')
choice = input('Хотите ввести максимальную глубину? Y/N: ').lower()
if choice == 'y':
    max_deep = int(input('Введите максимальную глубину: '))
    find = searcher(site, key_word, max_deep)
elif choice == 'n':
    find = searcher(site, key_word)
print(find)