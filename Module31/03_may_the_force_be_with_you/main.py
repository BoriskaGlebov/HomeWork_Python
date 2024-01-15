import requests
import json
import time

print('Задача 3. May the force be with you')
# А есть способ быстрее? а то прям ответ долго выводится? или я что-то делаю не так?
# программа 18 секунд работает наверно это многовато
stat = time.time()
starship_request = requests.get('https://swapi.dev/api/starships/10/')
data = json.loads(starship_request.text)
new_data = dict()
new_data['name'] = data['name']
new_data["max_atmosphering_speed"] = data["max_atmosphering_speed"]
new_data["starship_class"] = data["starship_class"]
new_data["pilots"] = data["pilots"]
for num, pilot in enumerate(new_data["pilots"]):
    data_pilot = json.loads(requests.get(pilot).text)
    new_data["pilots"][num] = {}
    new_data["pilots"][num]["name"] = data_pilot["name"]
    new_data["pilots"][num]["height"] = data_pilot["height"]
    new_data["pilots"][num]["mass"] = data_pilot["mass"]
    new_data["pilots"][num]["planet"] = (
        json.loads(requests.get(data_pilot["homeworld"]).text))['name']
    new_data["pilots"][num]["homeworld"] = data_pilot["homeworld"]

with open('Millennium Falcon.json', 'w') as file:
    json.dump(data, file, indent=4)

with open('My_Millennium Falcon.json', 'w') as file:
    json.dump(new_data, file, indent=4)

print(f'Время ={time.time()-stat} ')
