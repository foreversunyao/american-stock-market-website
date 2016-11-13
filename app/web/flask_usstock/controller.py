import MySQLdb as mysql
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
            #return json.JSONEncoder.default(self, obj)
            return str(obj)
class StockSearch(Form):
    stockcode = StringField("stockcode",[Required()])
    submit = SubmitField("Submit")



app = Flask(__name__)
app.config.from_object('config')
db = mysql.connect(host="127.0.0.1",user="root", passwd="root_pwd",port=3307,db="db_stock", charset="utf8")
db.autocommit(True)
c = db.cursor()
def countlogin():
    sql = ""
    if request.method == "POST":
        data = request.json
        try:
             sql="update tb_logincount set num=num+1;"
             ret = c.execute(sql)
        except mysql.IntegrityError:
            pass
        return render_template("mon.html")
    else:
        return render_template("mon.html")

@app.route("/index", methods=["GET"])
def getstockcode():
    my_str="[";
    c.execute("select distinct(stock_code) from tb_stockinfo_day ")
    data = c.fetchall()
    for row in data:
	my_str=my_str+"\"" + row[0] +"\","
    my_str=my_str+"\"\"]"
    print my_str
    #return render_template("index.html",stockcodelist=json.dumps(stockcodelist,cls=ComplexEncoder))
    return render_template("index.html",stockcodelistnew=my_str)

@app.route("/search",methods=['GET','POST'])
def stockController():
    form = StockSearch()
    code = request.form['stockcode']
    print code
   
    c.execute("select UNIX_TIMESTAMP(stat_date)*1000,open,high,low,close,volume,stock_code from tb_stockinfo_day where stock_code=%s",[code])
    ones = c.fetchall()
    
    return json.dumps(ones,cls=ComplexEncoder);

    #return "%s(%s);" % (request.args.get('callback'), json.dumps(ones,cls=ComplexEncoder))
    #return render_template("index.html",data=json.dumps(ones,cls=ComplexEncoder))
    #return "%s(%s);" % (request.args.get('callback'), json.dumps(ones,cls=ComplexEncoder))


@app.route("/details",methods=['GET','POST'])
def stocklistController():
    c.execute("select stat_date,stock_code,open,high,low,close,volume,adjclose,(close-open)/open from tb_stockinfo_day  order by stat_date desc")
    ones = c.fetchall()
    #return json.dumps(ones,cls=ComplexEncoder);
    #return "%s(%s);" % (request.args.get('callback'), json.dumps(ones,cls=ComplexEncoder))
    return render_template("datatable.html",datalist=ones)
@app.route("/stats",methods=['GET','POST'])
def stockstatsdirect():
	return render_template("datastat.html")
@app.route("/statsajax",methods=['GET','POST'])
def stockstatsController():
    #c.execute("select stat_date,cnt,per from (select stat_date,count(1) as cnt,'50%+' as per from  tb_stockinfo_day  where (close-open)/open >=0.5 group by stat_date union all select stat_date,count(1) as cnt,'10%~50%' as per from tb_stockinfo_day  where (close-open)/open <0.5 and (close-open)/open>=0.1 group by stat_date union all select stat_date,count(1) as cnt,'0%~10%' as per from tb_stockinfo_day  where (close-open)/open <0.1 and (close-open)/open>=0.0 group by stat_date union all select stat_date,count(1) as cnt,'-10%~0%' as per from tb_stockinfo_day  where (close-open)/open <0.0 and (close-open)/open>=(-0.1) group by stat_date union all select stat_date,count(1) as cnt,'-50%~-10%' as per from tb_stockinfo_day  where (close-open)/open <(-0.1) and (close-open)/open>=(-0.5) group by stat_date union all select stat_date,count(1) as cnt,'-50%' as per from tb_stockinfo_day  where (close-open)/open <(-0.5)  group by stat_date) as newt order by stat_date asc,per asc")
    c.execute("select stat_date,sum(a),sum(b),sum(c),sum(d),sum(e),sum(f) from (select stat_date,case when (close-open)/open >=0.5 then 1 else 0 end 'a',case  when (close-open)/open <0.5 and (close-open)/open>=0.1 then 1 else 0 end 'b',case  when (close-open)/open <0.1 and (close-open)/open>=0.0 then 1 else 0 end 'c',case  when (close-open)/open <0.0 and (close-open)/open>=(-0.1) then 1 else 0 end 'd',case  when (close-open)/open <(-0.1) and (close-open)/open>=(-0.5) then 1 else 0 end 'e',case  when (close-open)/open <(-0.5)  then 1 else 0 end 'f'  from tb_stockinfo_day)  as new_tb group by stat_date")
    ones = c.fetchall()
    return json.dumps(ones,cls=ComplexEncoder);
    #return "%s(%s);" % (request.args.get('callback'), json.dumps(ones,cls=ComplexEncoder))
    #return render_template("datastat.html",datalist=ones)


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8888, debug=True)
