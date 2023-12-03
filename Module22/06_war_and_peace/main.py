import zipfile

print('Задача 06. Война и мир')

alphabet = [chr(letter) for letter in range(ord('A'), ord('z') + 1) if chr(letter).isalpha()]

zip_archive = zipfile.ZipFile('voyna-i-mir.zip', 'r')
zip_archive.extractall()
zip_archive.close()

W_and_P_file = open('voyna-i-mir.txt', 'r', encoding='utf-8')
W_and_P_str = W_and_P_file.read()
analysis_dict = {letter: W_and_P_str.count(letter) for letter in alphabet if letter in W_and_P_str}
analysis_file = open('analysis.txt', 'w')
for k, v in sorted(analysis_dict.items(), key=lambda x: -x[1]):
    print(k, v)
    analysis_file.write(k + ' ' + str(v) + '\n')
