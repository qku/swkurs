# test if prime
def isprime(number):
        for i in range(2, number):
                if not number%i:
                        return 0
        else:
                return 1


upper = input("number: ")
primecount = 0

# count number of primes below upper
for i in range(2, upper):
        primecount += isprime(i)

print primecount

# sieb des erasthones?
