import copy


# Функция просто раскрывает словарь и печатает его
def output_dict(data, count=1):
    if isinstance(data, dict):
        count += 1
        comma = len(data)
        for key, value in data.items():
            comma -= 1
            if count == 2:  # для названия словаря
                print('site = {')
            if isinstance(value, dict):
                print('\t' * count, key, ': {')
                output_dict(value, count)
                if comma > 0:
                    print('\t' * (count + 1), '},')
                else:
                    print('\t' * (count + 1), '}')
            else:
                if comma > 0:
                    print('\t' * count, key, ':', value + ',')
                else:
                    print('\t' * count, key, ':', value)
            if count == 2:  # закрытие всего словаря
                print('\t\t}')
    else:
        print('Ошибка, функция для словарей!')


# Сложная функция по поиску и замене элементов в словаре
# За счет *old_w может менять неограниченное количество элементов в словаре,
# Их можно вводить либо у пользователя спрашивать либо, при вызове ручками записать, как у меня сейчас
def finder(data, new_w, *old_w):
    for old_w in old_w:
        if isinstance(data, dict):
            if old_w in data.keys(): #Здесь реализовал замену ключа в структре сайта, ну вдруг надо будет поменять
                data[new_w] = data.pop(old_w)
                return 1
            for sub_data_keys, sub_data_values in data.items():
                rez = finder(sub_data_values, new_w, old_w)
                if rez == 1:
                    break
                elif isinstance(rez, str):
                    data[sub_data_keys] = rez
                    return 0
        elif isinstance(data, str):
            if old_w in data:
                data = data.replace(old_w, new_w)
                return data
            return 0
    return None


print('Задача 3. Глубокое копирование')

site = {
    'html': {
        'head': {
            'title': 'Куплю/продам телефон недорого'
        },
        'body': {
            'h2': 'У нас самая низкая цена на iPhone',
            'div': 'Купить',
            'p': 'Продать'
        }
    }
}

num = int(input('Сколько сайтов: '))
# Хранит фирму телефона и значение сайта
site_dict = {}
for _ in range(num):
    site_n = copy.deepcopy(site)
    firm = input('Введите название продукта для нового сайта: ')
    finder(site_n, firm, 'iPhone', 'телефон')
    site_dict[firm] = site_n
    for i_name, i_site in site_dict.items():
        print('Сайт для {}:'.format(i_name))
        output_dict(i_site)
