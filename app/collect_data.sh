#!/usr/local/bin/python3.5
cd /home/usstock/git/stock-crawler/app
## scrapy data from yahoo
scrapy crawl stock -o output/stock.json -t json
## load data to influxdb
cd /home/usstock/app
python load_influxdb.py
