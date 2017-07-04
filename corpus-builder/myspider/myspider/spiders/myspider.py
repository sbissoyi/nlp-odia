#Module: Crawl Spider
#Author: Swarupananda Bissoyi

import scrapy

from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors.lxmlhtml import LxmlLinkExtractor
from scrapy.linkextractors import LinkExtractor
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from scrapy.http.request import Request

class mySpider(CrawlSpider):
	name = 'mySpider'
	start_urls = ['https://kanaknews.com']
	allowed_domains = ['kanaknews.com']

	rules = (Rule(
    	LinkExtractor(
        allow_domains = ('kanaknews.com'),
        attrs = ('href'),
        tags = ('a'),
        deny = (),
        deny_extensions = (),
        unique = True,
    ),
    callback = 'parse', follow = True),)

	def parse(self, response):
		extractor = LinkExtractor(allow_domains='kanaknews.com')
		links = extractor.extract_links(response)
		for link in links:
			yield Request(link.url, self.parse)
		for title in response.xpath("//div[@class='post-content']"):
			yield {'title': title.xpath("//div[@class='post-content']/p/text()").extract()}
			