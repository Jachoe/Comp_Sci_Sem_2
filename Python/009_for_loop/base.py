a = int(input("Plesase enter line length?"))
b = input("Do you want your line to be horizontal or vertical?")

for l in range(0, a):
    if "vertical" == b:
        print(a)
    elif "horizontal" == b:
        print(a, end=" ")
