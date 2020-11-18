import pymysql.cursors
from flask import Flask,jsonify

def get_data(type):
    cur.execute("""SELECT * FROM duyuru_db WHERE type = '%s'""" % (type))
    rows = cur.fetchall()
    return(rows)


con = pymysql.connect(host="localhost",user="root",passwd="ztR3hdTj5AEa9SE8",database="my_database",port=3306,charset='utf8',cursorclass=pymysql.cursors.DictCursor)
cur = con.cursor()

app= Flask(__name__)

@app.route('/bil_muh')
def bil_muh_page():
    return(jsonify(get_data("bil_muh")))

@app.route('/muh_fak')
def muh_fak_page():
    return(jsonify(get_data("muh_fak")))

@app.route('/obisis')
def obisis_page():
    return(jsonify(get_data("obisis")))

if __name__ == '__main__':
    app.run(host= '0.0.0.0')