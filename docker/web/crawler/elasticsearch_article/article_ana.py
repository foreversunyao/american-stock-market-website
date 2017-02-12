from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
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
	analyzer = SentimentIntensityAnalyzer()
	conn=MySQLdb.connect(host="stockserver",user='root',passwd='admin',db='db_stock',port=3306)
	cur=conn.cursor()
	init=0
	cur.execute('select id,search_key,link,title from tb_news_search')
	articlelist=cur.fetchall()
	for article in articlelist:
		print article[1]
		print article[0]
		idx= str(article[1]).lower()
		res= es.get(index=idx, doc_type='article', id=article[0])
		vs = analyzer.polarity_scores(res)
		vs_neg=vs['neg']
		print article[0]
		if vs_neg > 0.4 :
			 cur.execute("update tb_news_search set tag=2 where id=%s",(article[0],))
			 conn.commit()
		else:
			 cur.execute("update tb_news_search set tag=1 where id=%s",(article[0],))
			 conn.commit()
	cur.close()
	conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d:%s"%(e.args[0],e.args[1])
