print('Задача 05. Частотный анализ')
user_text = open('text.txt', 'r')
print(user_text.read())
user_text.seek(0)

user_string = user_text.read().lower()
alphabet = [chr(el) for el in range(ord('a'), ord('z'))]
# Сразу убираю для подсчета пробелы и точку
len_string = len(user_string.rstrip('.').replace(' ', ''))
user_str_set = set(user_string)
user_dict = {letter: round(user_string.count(letter) / len_string, 3) for letter in user_str_set if letter in alphabet}
user_text_2 = open('analysis.txt', 'w')

print('Содержимое файла analysis.txt:')
for el in sorted(user_dict.items(), key=lambda x: (-x[1], x[0])):
    outp_str = el[0] + '  ' + str(el[1]) + '\n'
    user_text_2.write(outp_str)
user_text_2.close()

user_text_2 = open('analysis.txt', 'r')
print(user_text_2.read())
