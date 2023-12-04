import datetime

print('Задача 04. Чат')

with open('chat.txt', 'a+', encoding='utf8') as chat:
    while True:
        user = input('Введите имя пользователя: ')
        last_user = user
        print(f'Что вы хотите сделать, {user}?\n'
              '1.Посмотреть текущий текст чата.\n'
              '2.Отправить сообщение (затем вводит сообщение).', end=' ')
        try:
            choice = int(input())
            if choice == 1:
                chat.seek(0)
                for i_line in chat:
                    if not i_line.isspace():
                        i_line_list = i_line.split('*')
                        # что б сообщения текущего пользователя были выравненны вправо, а остальные сообщения влево
                        if i_line_list[0].strip() == user:
                            print('_' * 80 + '|')
                            print('{:>80}|'.format(' '.join([i_line_list[0], i_line_list[1]])))
                            for i in range(0, len(i_line_list[2].split()) + 1, 10):
                                print('{:>80}|'.format(' '.join(i_line_list[2].split()[i:i + 10])))
                            print('_' * 80 + '|')
                        else:
                            print('_' * 80 + '|')
                            print('{:<80}|'.format(' '.join([i_line_list[0], i_line_list[1]])))
                            for i in range(0, len(i_line_list[2].split()) + 1, 10):
                                print('{:<80}|'.format(' '.join(i_line_list[2].split()[i:i + 10])))
                            print('_' * 80 + '|')
            elif choice == 2:
                chat.seek(2)
                time = datetime.datetime.now().strftime('%H:%M:%S')
                print(type(time))
                user_text = input('Введите сообщение на отправку: ')
                chat.write('{:<.10}*{:<}*{:<}\n'.format(user, time, user_text, ))
                chat.flush()
        except ValueError:
            print('Ты ввел строку , а не число. Исправься!')
