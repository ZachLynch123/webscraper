# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['https://lasvegas.craigslist.org/search/sof']
    start_urls = ['http://https://lasvegas.craigslist.org/search/sof/']

    def parse(self, response):
        jobs = response.xpath('//p[@class="result-info"]')
        for job in jobs: 
        	# note that I didn't use the response.xpath in the for loop
        	# instead I used the wrapper selecter that is referred to in the 'jobs' vaiable
        	title = job.xpath('.//a/text()').extract_first()

        	yield{'Title': title}
