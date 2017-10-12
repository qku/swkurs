# testing pickle

import cPickle

class Student:
	def __init__(self, data):
		self.firstname = data[0]
		self.name = data[1]
		self.mnumber = data[2]
		self.mark = data[3]

f = open("stud.dat")
students = []

for line in f:
	students.append(Student(line.split(" ")))
	
f.close()

print(students[3].firstname)

out = open("stud.pickle", "wb")
cPickle.dump(students, out)
out.close()

inp = open("stud.pickle", "rb")
studentsIn = cPickle.load(inp)
inp.close()

print(studentsIn[3].firstname)
