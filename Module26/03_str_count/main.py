import os


def counter(folder):
    path = os.path.abspath(os.path.join('..', '..', folder))
    print(path)
    total_lines = 0
    for dirpath, dirname, filename in os.walk(path):
        for names in filename:
            if names.endswith('main.py'):
                temp_path = os.path.join(dirpath, names)
                with open(temp_path, 'r', encoding='utf8') as file_py:
                    line_counter = 0
                    for i_line in file_py:
                        if not i_line.isspace() and not i_line.startswith('#'):
                            line_counter += 1
                    print(f'В файле {os.path.join(dirpath, names)} =  '
                          f'{line_counter} строк')
                total_lines += line_counter
                yield f'В просмотренных файлах всего {total_lines} строк'


print('Задача 3. Количество строк')

folder_count = counter('Module26')
for elem in folder_count:
    print(elem)
