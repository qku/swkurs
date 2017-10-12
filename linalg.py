# scalar product
def scalarp(a, b):
    product = 0
    for i in range(len(a)):
        product += (a[i] * b[i])
    return product

# vector product
def vectorp(a,b):
    product = [(a[1]*b[2]) - (a[2]*b[1]), (a[2]*b[0]) - (a[0]*b[2]), (a[0]*b[1]) - (a[1]*b[0])]
    return product

u, v = [ 0.3, 1.8, -2.2 ], [ -2.5, 3.8, 0.4]
print scalarp(u, v)
print vectorp(u, v)
