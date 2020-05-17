import sqlite3 as sql
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    lat = 56.7414181
    lon = 37.22414466976791
    if request.args.get('lat'):
        lat = float(request.args.get('lat'))
    if request.args.get('lon'):
        lon = float(request.args.get('lon'))

    con = sql.connect("../db.sqlite")
    con.row_factory = sql.Row

    cur = con.cursor()
    cur.execute("select count(ip_addres), lat, lon from bad_users group by ip_addres")

    coordinate = cur.fetchall()
    cur.close()
    length_list = len(coordinate)
    print(length_list)

    for i in range(length_list):
        print(coordinate[i][0])

    return render_template('map.html', lat = lat, lon = lon, coordinate = coordinate, length_list = length_list)

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
    cur.execute("select count(ip_address), ip_addres from bad_users group by ip_address order by count(ip_address) DESC")

    rowsIp = cur.fetchall()
    cur.close()

    return render_template("table.html", rowsLogin = rowsLogin ,rowsCountry = rowsCountry, rowsIp = rowsIp)

if __name__ == "__main__":
    app.run()
