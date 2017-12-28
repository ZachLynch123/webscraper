# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class JobsSpider(scrapy.Spider):
	name = 'jobs'
	allowed_domains = ['https://lasvegas.craigslist.org/search/sof']
	start_urls = ['http://https://lasvegas.craigslist.org/search/sof/']

	def parse(self, response):
		# started xpath with `//` meaning it starts from <html> until <p> whose class name is 'result-info'
		jobs = response.xpath('//p[@class="result-info"]')
		for job in jobs: 
			# note the lack of response.xpath in the for loop
			# instead use the wrapper selecter that is referred to in the 'jobs' vaiable
			# or title = job.xpath('a/text()').extract_first()
			title = job.xpath('.//a/text()').extract_first()

			# extracting job addresses and urls
			# the empty quotes in extract_first("") set a default empty string so that the string slicing doesn't throw an error
			# when trying to slice `None` which isn't a string
			address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
			# only returns the last half of the url. like ".../sdf/23/q?="
			relative_url = job.xpath('a/@href').extract_first()
			# joins the initial web address with the relative url to make somethingk like "https://www.google.com/something/something"
			absolute_url = response.urljoin(relative_url)
			# yield as dictionary
			yield{'URL': absolute_url, 'Title': title, 'Address':address}

		relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
		absolute_next_url = response.urljoin(relative_next_url)

		yield Request(absolute_next_url,callback=self.parse)

