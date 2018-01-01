# -*- coding: utf-8 -*-
import scrapy
from scrapy import Request


class JobsSpider(scrapy.Spider):
	name = 'jobs'
	allowed_domains = ['craigslist.org']
	# change starting url to whatever city is nearest for you for craigslist
	start_urls = ['https://lasvegas.craigslist.org/search/sof/']

	def parse(self, response):
		# started xpath with `//` meaning it starts from <html> until <p> whose class name is 'result-info'
		jobs = response.xpath('//p[@class="result-info"]')
		for job in jobs: 
			# note the lack of response.xpath in the for loop
			# instead use the wrapper selecter that is referred to in the 'jobs' vaiable
			# the empty quotes in extract_first("") set a default empty string so that the string slicing doesn't throw an error
			# when trying to slice `None` which isn't a string
			title = job.xpath('.//a/text()').extract_first()

			# extracting job addresses and urls
			address = job.xpath('span[@class="result-meta"]/span[@class="result-hood"]/text()').extract_first("")[2:-1]
			relative_url = job.xpath('a/@href').extract_first()
			absolute_url = response.urljoin(relative_url)

			# setting meta as a dictionary for the parse_page funtion to call it using the get() method
			yield Request(absolute_url,callback=self.parse_page, meta={'URL': absolute_url, 'Title': title, 'Address':address})

		# Uses the 'next' button to scrape on other pages, not just the front page
		relative_next_url = response.xpath('//a[@class="button next"]/@href').extract_first()
		absolute_next_url = response.urljoin(relative_next_url)

		yield Request(absolute_next_url, callback=self.parse)


	def parse_page(self, response): 

		# using the get() method to gather all values for the dictionary keys and assign them new variable names
		# gather compensation and employment type from their respective spans in the attrgroup class of the <p> tag
		url = response.meta.get('URL')
		title = response.meta.get('Title')
		address = response.meta.get('Address')

		compensation = response.xpath('//p[@class="attrgroup"]/span[1]/b/text()').extract_first()
		employment_type = response.xpath('//p[@class="attrgroup"]/span[2]/b/text()').extract_first()

		yield{'URL': url, 'Title': title, 'Address':address, 'Compensation': compensation, 'Employment_type': employment_type}

		# save in .json, .csv, or .xml format using the following command in the terminal or cmd
		# $scrapy crawl jobs -o [filename].[extension]










