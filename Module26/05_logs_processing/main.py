import os
import time


def error_log_generator(path):
    with (open(path, 'r', encoding='utf8') as input_file):
        for i_line in input_file:
            if i_line.startswith('ERROR'):
                yield i_line


def error_log_generator2(path):
    with (open(path, 'r', encoding='utf8') as input_file,
          open(output_file_path, 'w', encoding='utf8') as out_file):
        for i_line in input_file:
            if i_line.startswith('ERROR'):
                out_file.write(i_line)


# При помощи модуля os (и функции join) сформируйте пути до файлов work_logs.txt и output.txt в папке data
# (output.txt может не быть в папке data, но его нужно будет там создать, при помощи кода)
input_file_path = os.path.abspath(os.path.join('data', 'work_logs.txt'))
if os.path.isfile(input_file_path):
    print('Файл с логами существует')
else:
    print('Файла с логами нет!')
output_file_path = os.path.abspath('output.txt')
if os.path.isfile(output_file_path):
    print('Файл выходной уже создан!')
else:
    print('Надо будет создать выходной файл!')

# Документация по join https://docs-python.ru/standart-library/modul-os-path-python/funktsija-join-modulja-os-path/

# Не забудьте проверить наличие файлов перед тем как начать работу с ними
# https://docs-python.ru/standart-library/modul-os-path-python/funktsija-exists-modulja-os-path/
start1 = time.time()
with open(output_file_path, 'w') as output:
    for error_line in error_log_generator(input_file_path):
        output.write(error_line)
print("Файл успешно обработан.")
end1 = time.time()
rez1 = end1 - start1
print(rez1 * 10 ** 3, 'ms')

start2 = time.time()
d = error_log_generator2(input_file_path)
print("Файл успешно обработан.")
end2 = time.time()
rez2 = end2 - start2
print(rez2 * 10 ** 3, 'ms')
