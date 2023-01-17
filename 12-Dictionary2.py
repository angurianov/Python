enemy = {
    "loc_x": 50,
    "loc_y": 70,
    "color": "green",
    "health": 100,
    "name": "Enemy1",
    'awards': ['award1', 'award2'],
    'image': ['image1.jpg', 'image2.jpg', 'image3.jpg']
    }

all_enemies = []                # создать пустой массив и заполнить его объектами enemy 3 раза
#all_enemies.append(enemy)
#all_enemies.append(enemy)
#all_enemies.append(enemy)
#print(all_enemies)
print("-------------------------------------")

for x in range(0, 10):               # заполнить массив all_enemies 10 раз объектами enemy
    all_enemies.append(enemy.copy()) # создать 10 объектов enemy. Если не указать copy, то будет 10 объектов, но изменение одного изменит всех

print(all_enemies)
print("-------------------------------------")

for y in all_enemies:
    print(y)

all_enemies[5]['health'] = 30
for y in all_enemies:
    print(y)

print("--------------------------------------")

all_enemies[9]['name'] = "Big enemy"
all_enemies[8]['awards'] = ['award3']
for y in all_enemies:
    print(y)
