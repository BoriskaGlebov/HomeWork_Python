def reg_analysis(us_f, good_f, bad_f):
    for i_line in us_f:
        i_list = i_line.rstrip().split()
        try:
            if field(i_list):
                if alfa(i_list) == symbol(i_list) == age(i_list):
                    good_f.write('{:<10}{:<25}{:<10}\n'.format(*i_list))
                elif not alfa(i_list):
                    raise NameError
                elif not symbol(i_list):
                    raise SyntaxError
                elif not age(i_list):
                    raise ValueError
            else:
                raise IndexError
        except IndexError:
            err_mess = 'НЕ присутствуют все три поля\n'
            bad_f.write('{:<35}|{:<}'.format(i_line.rstrip(), err_mess))
        except NameError:
            err_mess = 'Поле «Имя» содержит НЕ только буквы\n'
            bad_f.write('{:<35}|{:<}'.format(i_line.rstrip(), err_mess))
        except SyntaxError:
            err_mess = 'Поле «Имейл» НЕ содержит @ и . (точку)\n'
            bad_f.write('{:<35}|{:<}'.format(i_line.rstrip(), err_mess))
        except ValueError:
            err_mess = 'Поле «Возраст» НЕ является числом от 10 до 99\n'
            bad_f.write('{:<35}|{:<}'.format(i_line.rstrip(), err_mess))
    return


def field(an_list):
    if len(an_list) == 3:
        return True
    else:
        return False


def alfa(an_list):
    if an_list[0].isalpha():
        return True
    else:
        return False


def symbol(an_list):
    if '@' and '.' in an_list[1]:
        return True
    else:
        return False


def age(an_list):
    if an_list[2].isdigit() and (10 <= int(an_list[2]) <= 99):
        return True
    else:
        return False


print('Задача 03. Регистрация')

with (open('registrations.txt', 'r+', encoding='utf8') as registration_file,
      open('registrations_good.log', 'w+', encoding='utf8') as good_registration_file,
      open('registrations_bad.log', 'w+', encoding='utf8') as bad_registration_file):
    reg_analysis(registration_file, good_registration_file, bad_registration_file)
    good_registration_file.seek(0)
    bad_registration_file.seek(0)
    print('\nСодержимое файла registrations_bad.log:')
    print(bad_registration_file.read())
    print('\nСодержимое файла registrations_good.log:')
    print(good_registration_file.read())
