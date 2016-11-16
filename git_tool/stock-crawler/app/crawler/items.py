# coding: utf-8
from scrapy.item import Item, Field

class StockItem(Item):
	fields = Field()
	measurement = Field()
	time = Field()
	tags = Field()

