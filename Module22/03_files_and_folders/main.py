import os


def counter(path, count_dir=0, count_file=0, size=0):
    for i_elem in os.listdir(path):
        if os.path.isdir(os.path.join(path, i_elem)):
            count_dir, count_file, size = counter(os.path.join(path, i_elem), count_dir, count_file, size)
            count_dir += 1
        elif os.path.isfile(os.path.join(path, i_elem)):
            count_file += 1
            size = os.path.getsize(os.path.join(path, i_elem)) / 1024
    return count_dir, count_file, size


print('Задача 03. Файлы и папки')

path_folder = os.path.abspath(os.path.join('..', '..', 'Module21'))
rez = counter(path_folder)
print(path_folder)
print('Размер каталога (в Кб):', rez[2])
print('Количество подкаталогов:', rez[0])
print('Количество файлов:', rez[1])
