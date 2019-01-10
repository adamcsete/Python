def PrimeNumbers():
    counter = int(input("Number of the first prime numbers: "))
    ct = 0
    prime = 1
    while ct<counter:
        isprime = False
        num = 2
        while not isprime:
            prime += 1
            isok = True
            num = 2
            while isok:
                if prime % num == 0:
                    if prime == num:
                        print(prime, " ", end="")
                        isprime = True
                        isok = False
                    else:
                        isok = False
                else:
                    num += 1
        ct += 1


PrimeNumbers()
