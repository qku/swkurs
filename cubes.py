# squares and cubes
lower = 1
upper = 150

sumi = 0
sums = 0
sumc = 0

for i in range(lower, upper):
	square = i**2
	cube = i**3
	sumi += i
	sums += square
	sumc += cube
	print i, square, cube, sums, sumc, sumi**2
