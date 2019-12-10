
N = input("Please enter N: \n")

def g(x, N):
    return (((x**2)+1)%N)

def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a


# intialize variables 
x = 2
y = 2
d = 1

# loop until d is not equal to 1
while (d == 1):
    x = g(x, N)
    y = g(g(y, N), N)
    d = gcd(abs(x-y), N)

if (d == N):
    print("Failure :(")
else:
    print("Success!")
    other = N/d
    print("p = " + str(d))
    print("q = " + str(other))

