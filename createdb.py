import sqlite3 as lite
con = lite.connect('loc.db')
with con:
    cur = con.cursor()
    cur.execute("DROP TABLE IF EXISTS Location")
    cur.execute("""CREATE TABLE Loction
                    (Id INT PRIMARY KEY,
                     Location INT)
               """)
