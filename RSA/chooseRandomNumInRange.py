
import random
from fractions import gcd

N = input("Please enter N.\n")
phiN = input("Please enter phi(N).\n")




num = random.randint(1, phiN)
goodNum = False
while (goodNum == False):
    if (gcd(num, N) == 1):
        if (gcd(num, phiN) == 1):
            goodNum = True
        else:
            num = random.randint(1, phiN)
    else:
        num = random.randint(1, phiN)


print(num)