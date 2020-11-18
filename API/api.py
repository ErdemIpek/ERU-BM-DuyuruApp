import pymysql.cursors
from flask import Flask,jsonify

def get_data(type):
    cur.execute("""SELECT * FROM duyuru_db WHERE type = '%s'""" % (type))
    rows = cur.fetchall()
    return(rows)


con = pymysql.connect(host="localhost",charset='utf8',cursorclass=pymysql.cursors.DictCursor)
cur = con.cursor()

app= Flask(__name__)
# Created three routes for the data fetched from three seperate websites.
@app.route('/bm_page')
def bil_muh_page():
    return(jsonify(get_data("bm_page")))

@app.route('/gm_page')
def muh_fak_page():
    return(jsonify(get_data("gm_page")))

@app.route('/obisis_page')
def obisis_page():
    return(jsonify(get_data("obisis_page")))

#Flask will run on localhost.
if __name__ == '__main__':
    app.run(host= '0.0.0.0')
