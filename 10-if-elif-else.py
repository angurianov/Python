
x = 25
if x == 25:
    print("Right")
else:
    print("Wrong")

age = 33
if age <=4:
    print("Baby")
elif age > 4 and age < 12:
    print("Kid")
elif age >=12 and age < 18:
    print("Teenager")
else:
    print("Old")



all_cars = ['chrusler',  'dacia' ,'bmw', 'Kia' , 'vw' ,'seat', 'skoda' , 'lada', ' audi ' , 'ford' , ' Chevrolet' ]
german_cars = ['bmw', 'vw' , 'audi']

if 'lada' in all_cars:              # используем значение 'lada' из массива all_cars
    print("LADA in the list")
else:
    print("LADA not in the list")

for x in all_cars:                  # цикл, где x поочередно принимает все значения из массива all_cars
    if x in german_cars:            # условие внутри цикла, если x принимает одно из значений из массива german_cars
        print(x + " is German car")
    else:
        print(x + " is not German car")
