# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'jobs'
    allowed_domains = ['https://lasvegas.craigslist.org/search/jjj?query=developer']
    start_urls = ['http://https://lasvegas.craigslist.org/search/jjj?query=developer/']

    def parse(self, response):
        pass
