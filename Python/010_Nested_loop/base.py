x = input("What symbol would you like to use?: ")
y = int(input("What width would you like your box to be?: "))
z = int(input("What height would you like your box to be?: "))
for i in range(0,z):
    print(" ")
    for j in range(0,y):
        print(" ", end = x)
    