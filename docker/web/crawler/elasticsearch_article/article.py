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
		print idx
		print article[0]
		#print str(buf.getvalue())
		#doc={'title':article[3],'text':str(buf.getvalue()).encode('utf-8').strip()}
		doc={'title':article[3],'text':buf.getvalue().decode('utf-8')}
		#try:
		res = es.index(index=idx.replace(" ", ""), doc_type='article', id=article[0], body=doc)
		#except :
			#continue
	cur.close()
	conn.close()
except Exception as e:
	print e.args[0]
	print e.args[1]
