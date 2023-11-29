def file_changer(file_1, file_2):
    output_list = []
    count_players = 0
    for i_line in file_1:
        if i_line.rstrip().isdigit():
            score = int(i_line.rstrip())
        elif int(i_line.split()[2]) > score:
            output_list.append(i_line.split())
            count_players += 1
    output_list.sort(key=lambda x: -int(x[2]))
    file_2.write(str(count_players) + '\n')
    for i_num, i_elem in enumerate(output_list):
        file_2.write('{number}) {name_v}. {surname} {score}\n'.format(
            number=i_num + 1,
            name_v=i_elem[1][0],
            surname=i_elem[0],
            score=i_elem[2]
        ))
    file_1.close()
    file_2.close()


print('Задача 04. Турнир')

first_file = open('first_tour.txt', 'r', encoding='utf-8')
print('Содержимое файла first_tour.txt:')
print(first_file.read())

first_file.seek(0)
second_file = open('second_tour.txt', 'w', encoding='utf-8')
file_changer(first_file, second_file)

second_file = open('second_tour.txt', 'r', encoding='utf-8')
print('\nСодержимое файла second_tour.txt:')
print(second_file.read())
