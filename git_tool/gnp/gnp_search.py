#!/bin/bash
import gnp
import codecs
import json
import MySQLdb
import sys

if len(sys.argv) <> 2:
    print "Usage: " + sys.argv[0] + " CODE"
    sys.exit(-1)

stockcode = sys.argv[1]
print stockcode
result=gnp.get_google_news_query(stockcode)
j_output = json.dumps(result, indent=4, ensure_ascii=False )
data = json.loads(j_output)

try:
        conn=MySQLdb.connect(host='127.0.0.1',user='root',passwd='admin',db='db_stock',port=3307,charset='utf8')
        cur=conn.cursor()


	for element in data['stories']:
# 		print element['category']
#		print element['source']
#		print element['content_snippet']
#		print element['link']
#		print element['title']
		cur.execute("insert into tb_news_search(stat_date,search_key,category,source,content_snippet,link,title) values(current_date(),%s,%s,%s,%s,%s,%s)",(stockcode,element['category'],element['source'],element['content_snippet'],element['link'],element['title']))	
	cur.close()
        conn.commit()
        conn.close()	
except MySQLdb.Error,e:
        print "Mysql Error %d:%s"%(e.args[0],e.args[1])
