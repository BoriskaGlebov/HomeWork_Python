def sum_my(*num):
    sum = 0
    for el in num:
        if isinstance(el, int):
            sum += el
        else:
            for sub_el in el:
                sum += sum_my(sub_el)
    return sum


print('Задача 4. Продвинутая функция sum')

print('Ответ в консоли:', sum_my([[1, 2, [3]], [1], 3]))
# Ответ в консоли: 10

print('Ответ в консоли:', sum_my(1, 2, 3, 4, 5))
# Ответ в консоли: 15
