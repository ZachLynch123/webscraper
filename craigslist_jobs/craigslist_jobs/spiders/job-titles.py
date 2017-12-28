# -*- coding: utf-8 -*-
import scrapy


class JobsSpider(scrapy.Spider):
    name = 'job-titles'
    allowed_domains = ['craigslist.org']
    start_urls = ['https://lasvegas.craigslist.org/search/sof']

    def parse(self, response):
    	# xpath is how the script will extract portions of text with a set of rules to follow
    	# for instance in the next line
    	# `//` means instead of starting from the <html> tag, just start from the tag that is specified after it
    	# in this intance, /a would mean <a> tag
    	# the `[@class="result-title hdrlink"]` means that the <a> tag must have the class name of title
    	# text() refers to the text of the <a> tag 
    	# extact() extracts every instance on the web page that follows these xpath rules
    	# if extract_first() is used instead of extract(), then only the first instance that follows the xpath will be extracted
    	titles = response.xpath('//a[@class="result-title hdrlnk"]/text()').extract()
    	for title in titles: 
    		yield {'Title': title}

