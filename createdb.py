import sqlite3 as lite
con = lite.connect('main.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS maintable")
    cur.execute("""CREATE TABLE maintable
                    (Id INT PRIMARY KEY,
                     Location INT,
		     Title TEXT)
               """)
