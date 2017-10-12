# faculty
def fak(n):
    product = 1
    for i in range(1, n+1):
        product *= i
    return product

number = input("number: ")
print fak(number)

#for i in range(1000):
#    print fak(i)
