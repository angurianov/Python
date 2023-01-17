def privetstvie(name):
    """Print privetstvie"""
    print("Congratulations " + name)
    print("Hello " + name)

def summa(x, y):
    return x+y

def factorial(x):
    """Calculation of factorial"""
    otvet = 1
    for i in range(1, x+1):
        otvet = otvet * i
    return otvet

#-----------------------

print("-----------------------")
privetstvie("Artem")
privetstvie("Vasya")

x = summa(5, 10)
print(x)

#-----------------------
print("-----------------------")

for i in range(1, 10):
    print(str(i) + "!\t = " + str(factorial(i)))