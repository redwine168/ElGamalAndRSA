
import random
import math

print("Welcome to the Blum Blum Shub random number generator!")
numBits = input("How many bits in the random number?\n")
numDigits = 10

est = (int)(math.floor(math.sqrt(10**(numDigits-1))))
bound = 10**(int)(math.floor(numDigits/3))

foundGoodPrime = False
while (foundGoodPrime == False):
    # CHOOSE GOOD p
    p = random.randint(est-bound,est+bound)
    goodP = False
    while (goodP == False):

        while ((p%4) != 3):
            p = random.randint(est-bound,est+bound)

        nMinusOne = p-1
        r = 0
        while (nMinusOne % 2 == 0):
            r += 1
            nMinusOne = nMinusOne / 2
        nMinusOne = p-1
        m = nMinusOne/(2**r)

        bases = [2, 3]
        numWitnesses = 0

        for b in bases:
            keepGoing = True
            bToM = b**m
            x = (bToM)%p
            if (x == 1):
                numWitnesses += 1
                keepGoing = False

            k = 0
            while (keepGoing):
                x = bToM**(2**k)
                if (x == -1):
                    numWitnesses += 1
                    keepGoing = False
                k += 1
                if (k == r):
                    keepGoing = False

        if (numWitnesses == len(bases)):
            goodP = True
        else:
            p = random.randint(est-bound,est+bound)


    # CHOOSE GOOD q
    q = random.randint(est-bound,est+bound)
    goodQ = False
    while (goodQ == False):

        while ((q%4) != 3):
            q = random.randint(est-bound,est+bound)

        nMinusOne = q-1
        r = 0
        while (nMinusOne % 2 == 0):
            r += 1
            nMinusOne = nMinusOne / 2
        nMinusOne = q-1
        m = nMinusOne/(2**r)

        bases = [2, 3]
        numWitnesses = 0

        for b in bases:
            keepGoing = True
            bToM = b**m
            x = (bToM)%q
            if (x == 1):
                numWitnesses += 1
                keepGoing = False

            k = 0
            while (keepGoing):
                x = bToM**(2**k)
                if (x == -1):
                    numWitnesses += 1
                    keepGoing = False
                k += 1
                if (k == r):
                    keepGoing = False

        if (numWitnesses == len(bases)):
            goodQ = True
        else:
            q = random.randint(est-bound,est+bound)

    n = p*q



    def gcd(a, b):
        while b != 0:
            a, b = b, a % b
        return a

    # FIND GOOD SEED s
    s = random.randint(2, n-1)
    while (gcd(s,n) != 1):
        s = random.randint(2, n-1)

    i = 0
    bits = []
    for i in range(0, numBits):
        if (i != 0):
            s = (s**2)%n
        bits.append(s%2)

    val = 0
    for i in range(0, numBits):
        if (bits[i] == 1):
            val += 2**((numBits-i)-1)
    if (val%2==0):
        val += 1


    nMinusOne = val-1
    r = 0
    while (nMinusOne % 2 == 0):
        r += 1
        nMinusOne = nMinusOne / 2
    nMinusOne = val-1
    m = nMinusOne/(2**r)

    bases = [2, 3]
    numWitnesses = 0

    for b in bases:
        keepGoing = True
        bToM = b**m
        x = (bToM)%val
        if (x == 1):
            numWitnesses += 1
            keepGoing = False

        k = 0
        while (keepGoing):
            x = bToM**(2**k)
            if (x == -1):
                numWitnesses += 1
                keepGoing = False
            k += 1
            if (k == r):
                keepGoing = False

    if (numWitnesses == len(bases)):
        foundGoodPrime = True
        print(str(val) + " is prime!")

        # FIND SAFE PRIME FOR GENERATOR  
        N = val
        foundSafeGenerator = False
        while (foundSafeGenerator == False):
            g = random.randint(2, N-1)
            if (g % 2 == 0):
                g += 1
            nMinusOne = g-1
            r = 0
            while (nMinusOne % 2 == 0):
                r += 1
                nMinusOne = nMinusOne / 2
            nMinusOne = g-1
            m = nMinusOne/(2**r)

            bases = [2, 3]
            numWitnesses = 0

            for b in bases:
                keepGoing = True
                bToM = b**m
                x = (bToM)%g
                if (x == 1):
                    numWitnesses += 1
                    keepGoing = False

                k = 0
                while (keepGoing):
                    x = bToM**(2**k)
                    if (x == -1):
                        numWitnesses += 1
                        keepGoing = False
                    k += 1
                    if (k == r):
                        keepGoing = False

            # IF THIS TRY AT g IS PRIME, SEE IF SOPHIE GERMAIN IS PRIME
            if (numWitnesses == len(bases)):
                sophieGermain = (g-1)/2
                nMinusOne = sophieGermain-1
                r = 0
                while (nMinusOne % 2 == 0):
                    r += 1
                    nMinusOne = nMinusOne / 2
                nMinusOne = sophieGermain-1
                m = nMinusOne/(2**r)

                bases = [2, 3]
                numWitnesses = 0

                for b in bases:
                    keepGoing = True
                    bToM = b**m
                    x = (bToM)%sophieGermain
                    if (x == 1):
                        numWitnesses += 1
                        keepGoing = False

                    k = 0
                    while (keepGoing):
                        x = bToM**(2**k)
                        if (x == -1):
                            numWitnesses += 1
                            keepGoing = False
                        k += 1
                        if (k == r):
                            keepGoing = False

                if (numWitnesses == len(bases)):
                    print("Here's a safe g: " + str(g))
                    foundSafeGenerator = True

                    foundQ = False
                    toTry = 2
                    while (foundQ == False):
                        e = toTry
                        x = g
                        M = N
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

                        if (y == 1):
                            foundQ = True
                            print("Multiplicative order q = " + str(toTry))
                        else:
                            toTry += 1
        




            


    
