def rev_zen(inp_txt):
    outp_list = [i_line.rstrip('\n') for i_line in inp_txt]
    outp_list.reverse()
    inp_txt.close()
    return outp_list


print('Задача 02. Дзен Пайтона')

input_txt = open('zen.txt', 'r')
print('Исходный текст:\n')
print(input_txt.read())
input_txt.seek(0)
txt_list = rev_zen(input_txt)
print('\nОбратный текст:\n')
for i_elem in txt_list:
    print(i_elem)
