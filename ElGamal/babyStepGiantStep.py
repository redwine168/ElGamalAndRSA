
import math

N = input("Please enter the order of the group.\n")
g = input("Please enter the generator of the group.\n")
gToX = input("Please enter the value of g^x (we will try to find x)\n")

m = (int)(math.ceil(math.sqrt(N)))


def fastExponentiate(base, exp, mod):
    y = 1
    while (exp > 0):
        # if e is odd
        if (exp%2 == 0):
            exp = exp / 2
            base = (base**2) % mod
        # if e is even
        else:
            exp -= 1
            y = (y*base) % mod
    return y







leftSide = [-1]*m
rightSide = [-1]*m

gToM = fastExponentiate(g, m, N)
gInverse = fastExponentiate(g, N-2, N)
gInverseToM = fastExponentiate(gInverse, m, N)

# First build out right side
for i in range(m):
    if (i == 0):
        rightSide[i] = 1
    else:
        rightSide[i] = (rightSide[i-1] * g) % N

# Then build out left side 
keepGoing = True
i = 0
i_val = -1
j_val = -1
while(keepGoing):
    if (i == 0):
        leftSide[i] = gToX
    else:
        leftSide[i] = (leftSide[i-1] * gInverseToM) % N

    # Check if this entry matches any from the right side
    for j in range(m):
        if (leftSide[i] == rightSide[j]):
            i_val = i
            j_val = j
            keepGoing = False
    i += 1

print("i = " + str(i_val))
print("j = " + str(j_val))
l = i_val*m + j_val
print("l = " + str(l))