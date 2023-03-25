from coffeeapp.models import City, CoffeeShop, Tag, Address, MetroStation
import json
import math


data = json.load(open('temporary_data_new.json', 'r'))
#uploaded_file = open('temporary_data_new.json', 'w')



# item.keys() все ключи

# создание нового json
'''
cnt = 0
for item in data:
    item['n'] = cnt
    item['city'] = 'Санкт-Петербург'
    item['street'] = item['adress'][:item['adress'].find(',')]
    item['building_number'] = item['adress'][item['adress'].find(',')+1:]
    item['longitude'] = item["location"][0]
    item['latitude'] = item["location"][1]
    if 'comment' not in item.keys():
        item['comment'] = ""
    t = item.pop('adress', None)
    t = item.pop('location', None)
    t = item.pop('togo', None)
    t = item.pop('discount', None)
    cnt += 1

#for k in data:
 #   print(k['description'])
json.dump(data, uploaded_file, ensure_ascii=False)
'''
'''
for item in data:
    print(item["location"][0], item["location"][1])
'''
'''
stations = json.load(open('stations.json', 'r'))
#заполнение таблицы Станции
for i in range(len(stations)):
    new = MetroStation.objects.create(\
        name = stations[i]['name'], \
        longitude= stations[i]['longitude'], \
        latitude = stations[i]['latitude'])

print(MetroStation.objects.all())
'''
'''
for item in MetroStation.objects.all():
    print(item.longitude, item.longitude*2)
'''
'''
#заполнение таблицы Город
new = City.objects.create(name="Санкт-Петербург")
new2 = City.objects.create(name="Москва")
print(City.objects.all())
'''
#проверка внешней связи
'''
print(MetroStation.objects.get(id=3).city.name)
'''
#добавление станций метро
'''
for item in data:
    i_long = item['longitude']
    i_lat = item["latitude"]
    min_distance = 100000
    for station in MetroStation.objects.all():
        st_long = station.longitude
        st_lat = station.latitude
        distance = math.sqrt(abs(i_lat-st_lat)+abs(i_long-st_long))
        if distance < min_distance:
            min_distance = distance
            res = station.id
    item['station'] = MetroStation.objects.get(id=res).name

json.dump(data, uploaded_file, ensure_ascii=False)
'''
'''
#заполняем Адрес и Кофейня
data = json.load(open('temporary_data_new.json', 'r'))
for item in data:
    new_addr = Address.objects.create(city=City.objects.get(name=item['city']), \
        street=item['street'], \
        building_number=item['building_number'], \
        longitude = item["longitude"], \
        latitude=item["latitude"], \
        metro_station = MetroStation.objects.get(name=item['station']), \
        description = item["comment"])

    new_coffeeShop = CoffeeShop.objects.create(name = item['name'], description=item['description'], \
        picture=item['image'], address=new_addr, link = item['instagram'])
'''
#удалить первую строку, она повторяется
#Address.objects.filter(id =1).delete()

#заполнение таблицы Тег и добавление тегов кофейням
'''
new_tag = Tag.objects.create(name='Новое')
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Слой'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='YNGЯНГ'))

new_tag = Tag.objects.create(name='Шведские булки')
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Характер кофе'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Парадная'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Слой'))


Tag.objects.get(id=2).delete()
Tag.objects.get(name='Шведские булки').coffeeshop_set.add(CoffeeShop.objects.get(name='Colors'))

new_tag = Tag.objects.create(name='Супер выпечка')
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Слой'))

new_tag = Tag.objects.create(name='Сытные завтраки')
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Смена'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='STIM'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Слой'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Nothing Fancy'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Пенка'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Aster'))

new_tag = Tag.objects.create(name='Декаф')
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Aster'))
#new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Mad Espresso Team'))

Tag.objects.get(name='Декаф').coffeeshop_set.add(CoffeeShop.objects.get(name='Больше кофе'))


new_tag = Tag.objects.create(name='Поработать')
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Характер кофе'))
#new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Фильтр'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Sibaristica'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Coffee3'))

new_tag = Tag.objects.create(name='Обжарщики')
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Sibaristica'))
#new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Mad Espresso Team'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Verle Garden'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Bolshecoffee roasters'))

new_tag = Tag.objects.create(name='Веган')
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Cookies'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Пенка'))

new_tag = Tag.objects.create(name='Светло')
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Cookies'))
#new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Civil'))
new_tag.coffeeshop_set.add(CoffeeShop.objects.get(name='Verle Garden'))
'''
#переместила комменты в таблицу Кофейня
'''
for addr in Address.objects.all():
    for place in addr.coffeeshop_set.all():
        place.comment = addr.description
        place.save()
'''