# Кто самый умный супергерой?
# Есть API по информации о супергероях с информацией по всем супергероям.
# Нужно определить кто самый умный(intelligence) из трех супергероев-
# Hulk, Captain America, Thanos.


from pprint import pprint
import requests

# Адрес запроса зададим в переменной url
url = 'https://akabab.github.io/superhero-api/api/all.json'
# Произведём запрос , используя метод get .
# Результатом является объёкт Response , который мы запомним в переменную resp
resp = requests.get(url)
# В переменную heroes_json_data запишем json-файл с нашими данными
heroes_json_data = resp.json()

# Посмотрим на наш файл :
# pprint (heroes_json_data)

# Создаём словарь: { имёна троих супергероев : их интеллект }
heroes_dict={}
for data in heroes_json_data:
    if data['name'] == 'Hulk' or data['name'] == 'Captain America' or data['name'] == 'Thanos' :
        heroes_dict[data['name']]=data["powerstats"]["intelligence"]

#print(heroes_dict) # {'Captain America': 69, 'Hulk': 88, 'Thanos': 100}

# Cортировка словаря
heroes_dict_sort = sorted(heroes_dict.items(), key=lambda x: x[1], reverse=True)
#print(heroes_dict_sort) #  [('Thanos', 100), ('Hulk', 88), ('Captain America', 69)]

print(f'Из трёх обозначенных супергероев самый умный - {heroes_dict_sort[0][0]} c уровнем интеллекта - {heroes_dict_sort[0][1]},\n'
      f'За ним идет -{heroes_dict_sort[1][0]} c уровнем интеллекта - {heroes_dict_sort[1][1]},\n'
      f'И самый тупой - {heroes_dict_sort[2][0]} c уровнем интеллекта - {heroes_dict_sort[2][1]},\n'
      f'Что не удивительно - АМЕРИКАНЕЦ !')

# Из трёх обозначенных супергероев самый умный - Thanos c уровнем интеллекта - 100,
# За ним идет -Hulk c уровнем интеллекта - 88,
# И самый тупой - Captain America c уровнем интеллекта - 69,
# Что не удивительно - АМЕРИКАНЕЦ !