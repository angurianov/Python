
cities = ['New York', 'Moscow', 'New Dehli', 'samara', 'Toronto']
print(cities)
print(len(cities))          #напечатать длину массива (сколько значений)

print(cities[0])            #вывести первое (нулевое) значение массива
print(cities[4])            #вывести последнее (4) значение массива
print(cities[-1])           #вывести последнее (4) значение массива
print(cities[-2].title())   #вывести предпоследнее (3) значение массива

cities[2] = 'Tula'          #заменить значение[2] в массиве на новое
print(cities[2])

cities.append('Kursk')      #добавить новое значение в массив (в конец массива)
cities.append('Yalta')
print(cities)

cities.insert(0, "Ulyanovsk") #добавить новое значение в массив (на позицию 0, в самое начало)
print(cities)

del cities[2]               #удалить значение из массива по номеру (номер 2, отсчёт с нуля)
print(cities)

cities.remove('Tula')       #удалить значение из массива по имени
print(cities)

deleted_city = cities.pop()                 #удалить значение из массива, по умолчанию последнее значение
print("Deleted city is: " + deleted_city)
print(cities)

deleted_city2 = cities.pop(2)               #удалить значение № 2
print("Deleted city2 is: " + deleted_city2)

cities.sort()               #сортировка значений массива по алфавиту
print(cities)

cities.sort(reverse=True)   #сортировка в обратном порядке
print(cities)

cities.reverse()            #обратный порядок
print(cities)
