
#name = input("Enter your name: ")
#print("Your name is: " + name)

#----------------------------------------------------------------

#num1 = input("Enter X: ")
#num2 = input("Enter Y: ")

#sum = int(num1) + int(num2)        # вместо сложения будет указана последовательность введенных num1num2
#print(sum)

#----------------------------------------------------------------

#message = ""
#while True:
#    message = input("Enter password: ")
#    if message == 'secret':
#        print("Password correct. Welcome")
#        break
#    print(message + "Password not correct")

#----------------------------------------------------------------

list = []
msg = ""

while msg != 'stop':
    msg = input("Enter new item. Stop to finish: ")
    list.append(msg)

print(list)