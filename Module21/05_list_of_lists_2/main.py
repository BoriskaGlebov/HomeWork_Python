def rectifier(n_list):
    new_list = []
    for el in n_list:
        if isinstance(el, int):
            new_list.append(el)
        else:
            new_list += rectifier(el)
    return new_list


print('Задача 5. Список списков 2')

nice_list = [1, 2, [3, 4], [[5, 6, 7], [8, 9, 10]],
             [[11, 12, 13], [14, 15], [16, 17, 18]]]
print(nice_list)
print(rectifier(nice_list))