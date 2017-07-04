# -*- coding: utf-8 -*-

#Module: Crawl Spider
#Author: Swarupananda Bissoyi

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class myspiderPipeline(object):
	def __init__(self):
		self.ids_seen = set()
	def process_item(self, item, spider):
		titleStr = str(item['title'])
		if titleStr in self.ids_seen:
			raise DropItem("Duplicate item found: %s" % item)
		else:
			self.ids_seen.add(titleStr)
			return item
