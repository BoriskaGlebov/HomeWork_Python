import re
import requests

#я здесь могу искать только по окончанию фразы,
# ведь начало может быть разной длинны
#[\w .:] на сколько это корректно? или надо
# было как-то [\w\s\W] но тогда нужный результат не получается
print('Задача 5. Web scraping')

# В данном случае запрос request.get заменен на загрузку сайта из файла html
with open('examples.html', 'r') as f:
    text = f.read()
# По итогу вы так же получаете код сайта в виде одной строки
# print(text)
print(re.findall(r'[\w .:]+(?=</h3>)', text))
us_request = requests.get('https://www.columbia.edu/~fdc/sample.html')
# print(us_request.text)
print(re.findall(r'[\w .:]+(?=</h3>)', us_request.text))
us_request2 = requests.get('https://htmlacademy.ru/blog/html-tags/h3')
# print(us_request2.text)
print(re.findall(r'[\w .:]+(?=</h3>)', us_request2.text))


