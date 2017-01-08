#!/usr/bin/env python2.7
import ystockquote
import json
import MySQLdb
import sys
import time

if len(sys.argv) <> 3:
    print "Usage: " + sys.argv[0] + " 20160101 20160102"
    sys.exit(-1)

s_date = sys.argv[1]
e_date = sys.argv[2]

try:
	conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='admin',db='db_stock',port=3307)
	cur=conn.cursor()
	#sql= "delete from tb_stockinfo_day where stat_date>='s%' and end_date<'s%'" % (s_date,e_date)
	cur.execute('delete from tb_stockinfo_day where stat_date>="%s" and stat_date<"%s"' % (s_date,e_date))
	cur.execute("commit")
	init=0
	cur.execute('select code from tb_americanstockcode')
	#cur.execute('select code from tb_stockinfo_day')
	codelist=cur.fetchall()
	for code in codelist:
#		print code[0]
		pre_data2 = ystockquote.get_historical_prices(code[0],s_date,e_date)
		print pre_data2
		if  pre_data2[0][0].find('doctype') >= 0:
			continue
		processed_data2 = json.dumps(pre_data2,sort_keys=False,indent=4)
#		print processed_data2
                for data in pre_data2:
			if data[0].find('Date') >= 0:
				continue
			sql_ex="insert into db_stock.tb_stockinfo_day(stat_date,stock_code,open,high,low,close,volume,adjclose) values('"+data[0]+"','"+code[0]+"',"+data[1]+","+data[2]+","+data[3]+","+data[4]+","+data[5]+","+data[6]+")"	 
	                print sql_ex
			cur.execute(sql_ex)
		cur.execute("commit")
	cur.close()
	conn.commit()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d:%s"%(e.args[0],e.args[1])

#pre_data = ystockquote.get_all('GOOG')
#processed_data = json.dumps(pre_data,sort_keys=False,indent=4)
#print processed_data

#pre_data2 = ystockquote.get_historical_prices('GOOG','20160609','20160610')
#processed_data2 = json.dumps(pre_data2,sort_keys=False,indent=4)
#print processed_data2
