from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from datetime import datetime
from elasticsearch import Elasticsearch
from elasticsearch import Elasticsearch,RequestsHttpConnection,serializer,compat,exceptions
class JSONSerializerPython2(serializer.JSONSerializer):
    """Override elasticsearch library serializer to ensure it encodes utf characters during json dump.
    See original at: https://github.com/elastic/elasticsearch-py/blob/master/elasticsearch/serializer.py#L42
    A description of how ensure_ascii encodes unicode characters to ensure they can be sent across the wire
    as ascii can be found here: https://docs.python.org/2/library/json.html#basic-usage
    """
    def dumps(self, data):
        # don't serialize strings
        if isinstance(data, compat.string_types):
            return data
        try:
            return json.dumps(data, default=self.default, ensure_ascii=True)
        except (ValueError, TypeError) as e:
            raise exceptions.SerializationError(data, e)

es = Elasticsearch(['stockserver'],serializer=JSONSerializerPython2())
#!/usr/bin/env python2.7
import json
import MySQLdb
import sys
import time
import pycurl
import cStringIO
 

try:
	analyzer = SentimentIntensityAnalyzer()
	conn=MySQLdb.connect(host='stockserver',user='root',passwd='admin',db='db_stock',port=3306,charset='utf8')
	cur=conn.cursor()
	init=0
	cur.execute('select id,search_key,link,title from tb_news_search')
	articlelist=cur.fetchall()
	for article in articlelist:
		try:
			print article[1]
			print article[0]
			idx= str(article[1]).lower()
			res= es.get(index=idx.replace(" ", ""), doc_type='article', id=int(str(article[0])))
			vs = analyzer.polarity_scores(str(res))
			vs_neg=vs['neg']
			print article[0]
			if vs_neg > 0.4 :
				 cur.execute("update tb_news_search set tag=2 where id=%s",(article[0],))
				 conn.commit()
			else:
				 cur.execute("update tb_news_search set tag=1 where id=%s",(article[0],))
				 conn.commit()
		except Exception as e:
			print e.args[0]
			print e.args[1]
	cur.close()
	conn.close()
except Exception as e:
	print e.args[0]
	print e.args[1]
