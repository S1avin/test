from flask import Flask, render_template, request
import sqlite3 as sql
app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        try:
            Id = request.form['ID']
            Loc = request.form['LOC']
            Tit = request.form['TITL']
            t=[Id, Loc, Tit]

            with sql.connect("main.db") as con:
                cur = con.cursor()
            
                cur.execute("INSERT INTO maintable (Id,Location,Title) VALUES (?,?,?)",t)
            
                con.commit()

        except:
           con.rollback()
           msg = "error in insert operation"
      
        finally:
           return render_template("main.html")
           con.close()
    return render_template('main.html')


@app.route('/loc')
def loc():
   con = sql.connect("main.db")
   con.row_factory = sql.Row
   
   cur = con.cursor()
   cur.execute("select * from maintable")
   
   rows = cur.fetchall();
   return render_template("loc.html",rows = rows)

if __name__ == "__main__":
	app.run(debug = True, host='0.0.0.0', port=8080, passthrough_errors=True)
