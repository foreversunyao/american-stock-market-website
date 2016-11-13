#!/bin/python
import json
from influxdb import InfluxDBClient
data_json=[]
with open('/home/usstock/git/stock-crawler/app/output/stock.json') as data_file:
	data=json.load(data_file)

#for line in open('/home/usstock/git/stock-crawler/app/output/stock.json','r'):
#	data_json.append(json.loads(line))


client = InfluxDBClient('localhost', 8086, 'root', 'root', 'stock_frequent_data')
client.write_points(data)
client.request('',method='GET',)
#result = client.query('select * from stockrealtime')
#print("Result: {0}".format(result))
