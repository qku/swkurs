import sqlite3

conn = sqlite3.connect("stud.sqlite", isolation_level="DEFERRED")

curs = conn.cursor()

curs.execute('''SELECT * FROM studenten ORDER BY id''')

result=curs.fetchone()
while result is not None:
    print result
    result = curs.fetchone()

conn.close()
