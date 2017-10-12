# fibonacci numbers

iterations = 200

f0 = 0
f1 = 1
fib = [f0, f1]

#print f0
#print f1

for i in range(iterations):
	f2 = f0 + f1
	print (f2*f0 - f1**2)
	#print f2
	fib.append(f2)
	f0 = f1
	f1 = f2

#print fib
