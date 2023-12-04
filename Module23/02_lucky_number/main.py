import random

print('Задача 02. Счастливое число')
sum_num = 0
with (open('out_file.txt', 'w+') as out_file):
    try:
        while sum_num <= 777:
            usr_number = int(input('Введите число:'))
            if 13 == random.randint(1, 13):
                raise ValueError
            out_file.write(str(usr_number) + '\n')
            sum_num += usr_number
    except ValueError:
        print('-' * 80)
        print('| {:^76} |'.format('Вас постигла неудача!'))
        print('-' * 80)
    else:
        print('Вы успешно выполнили условие для выхода из порочного цикла!')
    out_file.seek(0)
    print('\nСодержимое файла out_file.txt:')
    print(out_file.read())
