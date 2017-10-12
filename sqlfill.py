import sqlite3

conn = sqlite3.connect("stud.sqlite", isolation_level="DEFERRED")

curs = conn.cursor()

f = open("stud.dat")

for i in f:
	data = i.split()
	curs.execute('''INSERT INTO studenten VALUES (?,?,?,?,?)''', (None, data[0], data[1], data[2], data[3]))

conn.commit()
