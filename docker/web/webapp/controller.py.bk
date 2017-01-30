#!/usr/bin/env python2.7
import MySQLdb
import json
import decimal
from flask import Flask,jsonify, request, render_template
from datetime import datetime,date
from flask_wtf import Form
from wtforms import StringField, SubmitField 
from wtforms.validators import Required

class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        elif isinstance(obj, date):
            return obj.strftime('%Y-%m-%d')
        elif isinstance(obj,decimal.Decimal):
	    return float(obj)
	else:
            return str(obj)
class StockSearch(Form):
    stockcode = StringField("stockcode",[Required()])
    submit = SubmitField("Submit")

class DB:
  conn = None
  def connect(self):
    self.conn = MySQLdb.connect(host="stockserver",user="root", passwd="admin",port=3306,db="db_stock", charset="utf8")
    self.conn.autocommit = True
  def query(self, sql):
    try:
      print sql
      self.conn.ping()
      cursor = self.conn.cursor()
      cursor.execute(sql)
    except (AttributeError, MySQLdb.OperationalError):
      self.connect()
      cursor = self.conn.cursor()
      cursor.execute(sql)
    return cursor

app = Flask(__name__)
app.config.from_object('config')
db =DB()
def countlogin():
    sql = ""
    if request.method == "POST":
        data = request.json
        try:
             sql="update tb_logincount set num=num+1;"
             ret = db.query(sql)
        except mysql.IntegrityError:
            pass
        return render_template("mon.html")
    else:
        return render_template("mon.html")

@app.route("/index", methods=["GET"])
def getstockcode():
    my_str="[";
    c=db.query("select distinct(stock_code) from tb_stockinfo_day ")
    data = c.fetchall()
    for row in data:
	my_str=my_str+"\"" + row[0] +"\","
    my_str=my_str+"\"\"]"
    return render_template("index.html",stockcodelistnew=my_str)

@app.route("/initdatatop",methods=['GET','POST'])
def gettop():
    c=db.query("select stock_code,close,truncate((close-open)*100/close,2)  from tb_stockinfo_day where stat_date=(select max(stat_date)-10 from tb_stockinfo_day) order by (close-open)/open desc limit 5")
    topdata=c.fetchall()
    return json.dumps(topdata,cls=ComplexEncoder)

@app.route("/initdatalow",methods=['GET','POST'])
def getdown():   
    c2=db.query("select stock_code,close,truncate((close-open)*100/close,2)  from tb_stockinfo_day where stat_date=(select max(stat_date)-10 from tb_stockinfo_day) order by (close-open)/open asc limit 5")
    lowdata=c2.fetchall()
    return json.dumps(lowdata,cls=ComplexEncoder)
@app.route("/initdataidx",methods=['GET','POST'])
def getidx():
    c3=db.query("select stock_code,open,high,close,volume from tb_stockinfo_day where stock_code in ('^DJI','^IXIC','^GSPC') and stat_date=(select max(stat_date)-1 from tb_stockinfo_day)")
    stockidx=c3.fetchall()
    return json.dumps(stockidx,cls=ComplexEncoder)



@app.route("/search",methods=['GET','POST'])
def stockController():
    form = StockSearch()
    code = request.form['stockcode']
    print code
    c=db.query("select UNIX_TIMESTAMP(stat_date)*1000,open,high,low,close,volume,stock_code from tb_stockinfo_day where stock_code='%s'" % code )
    ones = c.fetchall()
    return json.dumps(ones,cls=ComplexEncoder)

@app.route("/searcharticleup",methods=['GET','POST'])
def stockarticleupController():
    form = StockSearch()
    code = request.form['stockcode']
    c=db.query("select name from tb_americanstockcode where code='%s' and name is not null limit 1" % code )
    codename = c.fetchone()[0]
    c2=db.query("select link,title,tag from tb_news_search where search_key='%s' and tag =2 limit 5" % (codename))
    contents=c2.fetchall()
    return json.dumps(contents,cls=ComplexEncoder)

@app.route("/searcharticlefall",methods=['GET','POST'])
def stockarticlefallController():
    code = request.form['stockcode']
    c=db.query("select name from tb_americanstockcode where code='%s' and name is not null limit 1" % code )
    codename = c.fetchone()[0]
    c2=db.query("select link,title,tag from tb_news_search where search_key='%s' and tag=1 limit 5" % (codename))
    contents=c2.fetchall()
    return json.dumps(contents,cls=ComplexEncoder)

@app.route("/details",methods=['GET','POST'])
def stocklistController():
    c=db.query("select stat_date,stock_code,open,high,low,close,volume,adjclose,(close-open)/open from tb_stockinfo_day  where stat_date >current_date() -5 order by stat_date desc")
    ones = c.fetchall()
    return render_template("datatable.html",datalist=ones)

@app.route("/stats",methods=['GET','POST'])
def stockstatsdirect():
	return render_template("datastat.html")
@app.route("/statsajax",methods=['GET','POST'])
def stockstatsController():
    c=db.query("select stat_date,sum(a),sum(b),sum(c),sum(d),sum(e),sum(f) from (select stat_date,case when (close-open)/open >=0.5 then 1 else 0 end 'a',case  when (close-open)/open <0.5 and (close-open)/open>=0.1 then 1 else 0 end 'b',case  when (close-open)/open <0.1 and (close-open)/open>=0.0 then 1 else 0 end 'c',case  when (close-open)/open <0.0 and (close-open)/open>=(-0.1) then 1 else 0 end 'd',case  when (close-open)/open <(-0.1) and (close-open)/open>=(-0.5) then 1 else 0 end 'e',case  when (close-open)/open <(-0.5)  then 1 else 0 end 'f'  from tb_stockinfo_day)  as new_tb group by stat_date")
    ones = c.fetchall()
    return json.dumps(ones,cls=ComplexEncoder);


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8888, debug=True)
