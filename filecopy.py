# copy a file

def copyfile(filename1, filename2):
	file1 = open(filename1)
	file2 = open(filename2, "w")
	lines1 = file1.readlines()
	
	for line in lines1:
		file2.write(line)
		
	file1.close()
	file2.close()

copyfile(input("source: "), input("target: "))
