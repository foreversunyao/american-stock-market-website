#!/bin/bash
for i in `cat stockcode.list`:
do
	wget -O $i.csv http://ichart.finance.yahoo.com/table.csv?s=$i&d=01&e=19&f=2015&g=d&a=01&b=19&c=2015&ignore=.csv
	sleep 0.1
done
#load data local infile '/home/stock/project/stock/stockcode_base/csv/2016.csv' INTO TABLE tb_stockinfo_day FIELDS TERMINATED BY ',' ENCLOSED BY '"' LINES TERMINATED BY '\n';
