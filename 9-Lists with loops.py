cars = ['bmw', 'vw', 'fiat', 'skoda', 'lada']

for x in cars:              # с помощью цикла подставить все значения из массива
    print(x.upper())        # и вывести их

for x in range(1,6):
    print(x)

number_list = list(range(0,10))     # создать массив с цифрами от 0 до 9
print(number_list)

for x in number_list:
    x = x * 2
    print(x)

number_list.sort(reverse=True)
print(number_list)

print(max(number_list))         # вывести максимальное значение из всех значений массива
print(min(number_list))         # минимальное значение
print("Summa = " + str(sum(number_list)))   # сумма значений массива

mycars = cars[1:3]          # создать массив mycars и дать ему значения из массива cars, начиная со значения 1
print(mycars)               # и количество используемых значений = 2 (3-1)

mycars2 = cars[:4]          # новый массив со значениями cars с 0 до 3 (4-3)
print(mycars2)

mycars3 = cars[-2:]         # новый массив со значениями с конца и до второго справа значения
print(mycars3)

mycars4 = cars[:]           # новый массив, который в этой строке возьмет значения из cars
                            # если в дальнейшем изменить значения cars, то значения mycars4 не поменяются
