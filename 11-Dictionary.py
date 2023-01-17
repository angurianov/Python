#   (-----Item-----)
#   (key)    (value)    # внутри словаря параметры называются Item, названия параметров Key, их значения value
enemy = {               # создание словаря (объекта), и задание его параметров
    "loc_x": 50,
    "loc_y": 70,
    "color": "green",
    "health": 100,
    "name": "Enemy1"
}

print(enemy)

print("Location X = " + str(enemy['loc_x']))
print("Location Y = " + str(enemy['loc_y']))
print("Name is " + enemy['name'])               # вывод value одного из параметров(key) словаря enemy

enemy['rank'] = 'captain'           # добавить новый item (rank) для словаря enemy и присвоить ему значение (captain)
print(enemy['rank'])

del enemy['rank']                   # удалить item

enemy['loc_x'] = enemy['loc_x'] + 40    # изменить значение item (loc_x) на +40
enemy['health'] = enemy['health'] - 30  # изменить значение item (health) на -30
if enemy['health'] < 80:
    enemy['color'] = 'yellow'

print(enemy)

print(enemy.keys())         # показать только все keys
print(enemy.values())       # показать только все values
