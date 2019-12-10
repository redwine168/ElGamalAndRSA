
print("Welcome to the Fast Exponentiation Algorithm!")
x = input("Base: ")
e = input("Exponent: ")
M = input("Mod: ")

y = 1
while (e > 0):
    # if e is odd
    if (e%2 == 0):
        e = e / 2
        x = (x**2) % M
    # if e is even
    else:
        e -= 1
        y = (y*x) % M

    print(str(x) + "          " + str(e) + "          " + str(y))
        
