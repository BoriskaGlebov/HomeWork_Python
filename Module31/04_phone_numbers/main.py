import re

print('Задача 4. Телефонные номера')
numerals = ['первый', 'второй', 'третий', 'четвертый', 'пятый']
user_nums = ['9999999999', '999999-999', '99999x9999']

for num, check_num in zip(numerals, user_nums):
    status = None
    if len(re.findall(r'^[8,9]\d{9}\b', check_num)):
        status = 'все в порядке'
    else:
        status = 'не подходит'

    print(f'{num} номер: {status}')
