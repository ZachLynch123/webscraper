# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
	name = 'jobs'
	allowed_domains = ['www.upwork.com']
	start_urls = ['https://www.upwork.com/o/jobs/browse/?q=python/']

	def parse(self, response):

		title = response.xpath('//a[@class="job-title"]/text()').extract()
		print(title)
		
