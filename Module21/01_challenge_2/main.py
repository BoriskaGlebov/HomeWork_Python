def rec_my(number):
    if number == 1:
        return 1
    print(rec_my(number - 1))
    return number


# Фактически выводит цифры от 1 до n-1. Так нормально?
# Сделать что б все выводилось мне кажется слишком сложно

print('Задача 1. Challenge 2')

num = int(input('Введите num: '))
print(rec_my(num))
