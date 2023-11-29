print('Задача 01. Сумма чисел 2')

input_file = open('numbers.txt', 'r')
output_file = open('answer.txt', 'w')
sum = 0

print('Содержимое файла numbers.txt')
for i_line in input_file:
    if i_line.strip() != '':
        print(int(i_line.strip()))
        sum += int(i_line.strip())
output_file.write(str(sum))
# Зкрытие этих файлов
input_file.close()
output_file.close()
# Вывожу на экран, что записалось
output_file = open('answer.txt', 'r')
print('Содержимое файла answer.txt')
print(output_file.read())
output_file.close()



