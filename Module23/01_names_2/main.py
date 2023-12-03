import os, time

print('Задача 01. Имена 2')
user_name = ['Василий', 'Николай', 'Надежда', 'Никита', 'Ян', 'Ольга', 'Евгения', 'Кристина']
with open('people.txt', 'w', encoding='utf8') as people_file:
    for elem in user_name:
        people_file.write(elem + '\n')

count = 0
count_str = 0
tot_len = 0

with (open('people.txt', 'r', encoding='utf8') as people_file,
      open('error.log', 'a', encoding='utf8') as log_file):
    for i_line in people_file:
        count_str += 1  # в текстовом документе Ян будет именно на 5 строке, а не 4-ой если считать с нуля
        try:
            if len(i_line.rstrip('\n')) < 3:
                raise ValueError
        except ValueError:
            print('-' * 50)
            err_str = f'Ошибка: менее трёх символов в строке {count_str}.'
            print(err_str)
            print('-' * 50)
            log_file.write(time.ctime(time.time()) + ' ' + err_str + '\n')
        count += 1
        tot_len += len(i_line.rstrip('\n'))
print('Ответы')
print('Общее количество символов: ', tot_len)
