def quick_sort(us_list):
    us_list = sep(us_list)
    sort_list = []
    for el in us_list:
        if len(el) >= 2:
            if el[0] != el[1]:
                el = quick_sort(el)
        sort_list += el
    return sort_list


def sep(n_list):
    rez_less = []
    rez_equally = []
    rez_more = []
    for el in n_list:
        if el < n_list[-1]:
            rez_less.append(el)
        elif el == n_list[-1]:
            rez_equally.append(el)
        else:
            rez_more.append(el)
    return rez_less, rez_equally, rez_more


print('Задача 6. Быстрая сортировка')

num_list = [5, 8, 9, 4, 6, 7, 9, 5, 1, 3, 5, 7, 8, 9, 1, 6, 5, 4, 7, 4, 2, 9, 1, 8]
print(num_list)
rez = quick_sort(num_list)
print(rez)
