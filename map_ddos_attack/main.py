import sqlite3 as sql
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("map.html")

@app.route('/rest/getCountryStatistics')
def statistics():
    con = sql.connect("../db.sqlite")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select count(login), login from bad_users group by login order by count(login) DESC")

    rowsLogin = cur.fetchall()
    cur.close()

    cur = con.cursor()
    cur.execute("select count(country), country from bad_users group by country order by count(country) DESC")

    rowsCountry = cur.fetchall()
    cur.close()

    cur = con.cursor()
    cur.execute("select count(ip_addres), ip_addres from bad_users group by ip_addres order by count(ip_addres) DESC")

    rowsIp = cur.fetchall()
    cur.close()

    return render_template("table.html", rowsLogin = rowsLogin ,rowsCountry = rowsCountry, rowsIp = rowsIp)

if __name__ == "__main__":
    app.run()
