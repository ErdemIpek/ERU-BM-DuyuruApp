from bs4 import BeautifulSoup
import urllib
from urllib.request import urlopen
import pymysql
import time
import pymysql.cursors
from flask import Flask,jsonify

start_time = time.time()

#This function is for correcting the fetched texts.
def strip_func(list):
    list = [s.strip('\r\n        ') for s in list]
    list = [w.replace('\r', ' ') for w in list]
    list = [w.replace('\n', ' ') for w in list]
    list_copy = ''.join(list)
    if list_copy == '':
        list = ["İçeriği görüntülemek için tıklayınız."]
    return(list)
#Database connection
connection = pymysql.connect(host="localhost",user="root",passwd="ztR3hdTj5AEa9SE8",database="my_database",port=3306)
cursor = connection.cursor()

#Table truncating
cursor.execute("TRUNCATE TABLE duyuru_db")

def bm_fetchData():
    url = "https://bm.erciyes.edu.tr/?Duyurular"
    sayfa = urllib.request.urlopen(url)
    soup = BeautifulSoup(sayfa, "html.parser")
    main = soup.find('body')
    head=main.findAll('h5',attrs={"class":"entry-title text-white text-uppercase m-0 mt-5"})
    sub_date = main.findAll("li",attrs={"class":"font-12 text-white font-weight-600","style":"min-width:60px"})
    header_list = []
    date_list=[]
    for i in range(20):
        header_list.append(head[i].text)
        date_list.append(sub_date[i].text)

    ##Finding page  id
    sayfa_id1 = urllib.request.urlopen(url)
    soup_id1 = BeautifulSoup(sayfa_id1, "lxml")
    ana_id1 = soup_id1.find('div',attrs={"class":"col-md-12","style":"z-index:99"})
    alt_id1=ana_id1.findAll("a")
    list_id1 = []
    for meta in alt_id1:
        list_id1.append(meta.get('href'))
        res = []
    for ix in list_id1:
        if ix not in res:
            res.append(ix)

    res = res[1:]

    for var1 in range (20):
        url_bil_det = "https://bm.erciyes.edu.tr/"+res[var1]
        sayfa_bil_det = urllib.request.urlopen(url_bil_det)
        soup_bil_det = BeautifulSoup(sayfa_bil_det, "lxml")
        ana_bil_det = soup_bil_det.find('div',attrs={"class":"mt-10"})
        alt_bil_det = ana_bil_det.findAll('p')
        list_bil_det=[]
        for x in range(len(alt_bil_det)):
            title = alt_bil_det[x].text
            list_bil_det.append(title)

        list_bil_det=strip_func(list_bil_det)
        string = " "
        string=string.join(list_bil_det)
        cursor.execute("INSERT IGNORE INTO duyuru_db (type,head,details,url,date) VALUES(%s,%s,%s,%s,%s)", ("bil_muh",header_list[var1],string,url_bil_det,date_list[var1]))

def muh_fetchData():
    url_muh = "https://mf.erciyes.edu.tr/?Duyurular"
    sayfa_muh = urllib.request.urlopen(url_muh)
    soup_muh = BeautifulSoup(sayfa_muh, "html.parser")
    ana_muh = soup_muh.find('div',attrs={"class":"tab-pane fade in active","id":"Guncel_Duyurular"})
    alt_muh=ana_muh.findAll('h5',attrs={"class":"entry-title text-white text-uppercase m-0 mt-5"})
    alt_muh_tarih=ana_muh.findAll('li',attrs={"class":"font-12 text-white font-weight-600","style":"min-width:60px;"})
    list_muh = []
    list_tarih_muh =[]

    for j in range (20):
        list_muh.append(alt_muh[j].text)
        list_tarih_muh.append(alt_muh_tarih[j].text)
    ##
    ######Finding duyuru id
    sayfa_id2 = urllib.request.urlopen(url_muh)
    soup_id2 = BeautifulSoup(sayfa_id2, "lxml")
    ana_id2 = soup_id2.find('div',attrs={"class":"col-md-12","style":"z-index:99;"})
    alt_id2=ana_id2.findAll("a")
    list_id2 = []
    for i in alt_id2:
        list_id2.append(i.get('href'))
    res2 = []
    for ix in list_id2:
        if ix not in res2:
            res2.append(ix)

    res2 = res2[1:]
    ##

    for var2 in range (20):
        url_muh_det = "https://mf.erciyes.edu.tr/"+res2[var2]
        sayfa_muh_det = urllib.request.urlopen(url_muh_det)
        soup_muh_det = BeautifulSoup(sayfa_muh_det, "html.parser")
        ana_muh_det= soup_muh_det.find('div',attrs={"class":"mt-10"})
        alt_muh_det = ana_muh_det.findAll('p')
        list_muh_det=[]
        for x in range(len(alt_muh_det)):
            list_muh_det.append(alt_muh_det[x].text)

        if "Dosyayı indirmek için tıklayınız Click for download!" in list_muh_det:
            list_muh_det=[]
            list_muh_det.append("İndirilebilir içerik mevcut. İndirmek için tıklayınız.")
        list_muh_det=strip_func(list_muh_det)
        string2 = " "
        string2=string2.join(list_muh_det)

        cursor.execute("INSERT IGNORE INTO duyuru_db (type,head,details,url,date) VALUES(%s,%s,%s,%s,%s)", ("muh_fak",list_muh[var2],string2,url_muh_det,list_tarih_muh[var2]))

######

def obisis_fetchData():
    url_a = "https://obisis.erciyes.edu.tr/"
    sayfa_a = urllib.request.urlopen(url_a)
    soup_a = BeautifulSoup(sayfa_a, "lxml")# html.parser only finds one text between tags for this spesific page both "lxml" and "html5lib" parsers could be used. Warning "html5lib" parser does not support Turkish characters.

    ana_a = soup_a.find("table",attrs={"id":"ctl03_dlDuyuru"})
    alt_a=ana_a.findAll("span",attrs={"class": "NormalBlue"})
    list_a = []
    list_a = [s.strip('\r\n        ') for s in list_a]
    for x in range(20):
        title_a = alt_a[x].text
        list_a.append(title_a)


    sayfa_a1 = urllib.request.urlopen(url_a)
    soup_a1 = BeautifulSoup(sayfa_a1, "lxml")# html.parser only finds one text between tags for this spesific page both "lxml" and "html5lib" parsers could be used. Warning "html5lib" parser does not support Turkish characters.

    ana_a1 = soup_a1.find('table', attrs={"id":"ctl03_dlDuyuru"})
    alt_a1=ana_a1.findAll('td', attrs={"id":"HtmlIcerik","class":"Normal"})
    list_a1 = []
    for x in range(20):
        list_a1.append(alt_a1[x].text)
    list_a1 = strip_func(list_a1)

    list_a = strip_func(list_a)

    for i in range (len(list_a1)):
       cursor.execute("INSERT IGNORE INTO duyuru_db (type,head,details) VALUES(%s,%s,%s)", ("obisis",list_a[i],list_a1[i]))

bm_fetchData()
muh_fetchData()
obisis_fetchData()
connection.commit()
connection.close()


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
