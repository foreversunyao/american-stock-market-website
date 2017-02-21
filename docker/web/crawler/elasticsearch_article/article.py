from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()
#!/usr/bin/env python2.7
import json
import MySQLdb
import sys
import time
import pycurl
import cStringIO
 

try:
	conn=MySQLdb.connect(host="stockserver",user='root',passwd='admin',db='db_stock',port=3306)
	cur=conn.cursor()
	init=0
	cur.execute('select id,search_key,link,title from tb_news_search')
	articlelist=cur.fetchall()
	for article in articlelist:
		print article[0]
		buf = cStringIO.StringIO()
		c=pycurl.Curl()
		c.setopt(c.URL,article[2])
		c.setopt(c.WRITEFUNCTION, buf.write)
		c.perform()
		idx= str(article[1]).lower()
		doc={'title':article[3],'text':str(buf.getvalue()).encode('utf-8').strip()}
		try:
			res = es.index(index=idx, doc_type='article', id=init, body=doc)
		except :
			continue
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d:%s"%(e.args[0],e.args[1])
