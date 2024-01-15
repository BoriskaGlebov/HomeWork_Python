import json


def compare_dict(dict1: dict, dict2: dict) -> dict:
    """Функция глубокого сравнения словарей"""
    dif_dict = dict()
    for key, value in dict1.items():
        if ((key in dict1.keys() and dict2.keys())
                and isinstance(value, dict)
                and dict1.get(key) != dict2.get(key)):
            result = compare_dict(dict1[key], dict2[key])
            dif_dict = result
        elif dict1.get(key) != dict2.get(key):
            dif_dict[key] = value
    return dif_dict


print('Задача 6. JSON comparison')
with (open('json_old.json', 'r', encoding='utf8') as file_old,
      open('json_new.json', 'r', encoding='utf8') as file_new,
      open('result.json', 'w', encoding='utf8') as file_result):
    data_old: dict = json.load(file_old)
    data_new: dict = json.load(file_new)
    result_dict = compare_dict(data_old, data_new)
    json.dump(result_dict, file_result, indent=4)
    print('Осуществлен поиск различий в двух словарях, '
          'результат записан в result.json')

with (open('result.json', 'r', encoding='utf8') as file,
      open('result2.json', 'w', encoding='utf8') as file2):
    data: dict = json.load(file)
    diff_list = ["services", "staff", "datetime"]
    result_dict = {el: data.get(el) for el in diff_list
                   if el in data.keys()}
    print(result_dict)
    json.dump(result_dict, file2, indent=4)
    print('Осуществлен поиск и сохранение результата '
          'в соответствии с заданным параметром в списке. '
          'Результат записан в файл result2.json')
