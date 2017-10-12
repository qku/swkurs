# read file
f = open("numbers.dat")
yournumbers = []

for i in f:
	yournumbers.append(float(i))

f.close()

yournumbers.sort()

print "smallest: ", yournumbers[0] # smallest number
print "largest:", yournumbers[-1] # largest number

def closest(number, numbers):
	for i in range(len(numbers)):
		if numbers[i] > number:
			if abs(numbers[i] - number) > abs(numbers[i-1] - number):
				return numbers[i-1]
			else:
				return numbers[i]
				
yournumber = input("number: ")
print closest(yournumber, yournumbers)

yournumbers.reverse()
print yournumbers
