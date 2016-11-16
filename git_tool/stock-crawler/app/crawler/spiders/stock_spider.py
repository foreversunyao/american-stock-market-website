# coding: utf-8
from scrapy.spider import BaseSpider
#from scrapy.xpathor import HtmlXPathSelector
from scrapy.selector import Selector
from crawler.items import StockItem
from datetime import datetime, date, time
import json
class StockSpider(BaseSpider):
	name = 'stock'
	allowed_domains = ['br.financas.yahoo.com']
	start_urls=[]
	open('/home/usstock/git/stock-crawler/app/output/stock.json', 'w').close()
	with open('/home/usstock/git/stock-crawler/app/crawler/spiders/stock_scrawl.list','r') as f:
		start_urls=f.read().splitlines()
		print(start_urls)
	def parse(self, response):
		self.log('URL: %s' % response.url)

		hxs = Selector(response)
		item = StockItem()
		title = hxs.xpath('//*[@id="yfi_rt_quote_summary"]/div[1]/div/h2/text()').extract()
		price = hxs.xpath('//*[@id="yfi_rt_quote_summary"]/div[2]/div/span[1]/span/text()').extract()
		before_closed = hxs.xpath('//*[@id="yfi_rt_quote_summary"]/div[2]/div/span[1]/span/text()').extract()
		open_amount = hxs.xpath('//*[@id="yfi_rt_quote_summary"]/div[2]/div/span[1]/span/text()').extract()
		item['time'] = datetime.utcnow()
		price = ''.join(price).replace(',','.')
		title=''.join(title)
		item['measurement']="stockrealtime"
		item['tags']= {"name": title,"code": title }
		item['fields']= {"Volume": before_closed,"changepercent": before_closed,"High": before_closed,"Open": open_amount,"Prev Close": before_closed,"Low": before_closed,"Turnoverratio": before_closed,"value" : price }
		return item
