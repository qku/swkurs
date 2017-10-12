f = open(input("file: "))
lines = f.readlines()
print(str(len(lines)) + " lines")

target = raw_input("word: ")

count = 0
for line in lines:
	line = line.split(" ")
	for word in line:
		if word == target:
			count += 1

print(str(count) + " instances found.")

for line in lines:
	line = line.upper()
#	print line
