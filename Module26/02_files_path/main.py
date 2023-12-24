import os


def gen_files_path(name: str):
    path = os.path.abspath(os.path.sep)
    print(f'Поиск в содержимом корня {path}')
    for dirpath, dirnames, filenames in os.walk(path):
        if name in dirnames:
            new_path = os.path.abspath(os.path.join(dirpath, name))
            print(f'Поиск файлов в каталоге папки {new_path}')
            print()
            for path_name, dir_name, file_name in os.walk(new_path):
                for names in file_name:
                    yield os.path.abspath(os.path.join(path_name, names))


print('Задача 2. Пути файлов')
files_name = gen_files_path('Module26')
for el in files_name:
    print(el)
