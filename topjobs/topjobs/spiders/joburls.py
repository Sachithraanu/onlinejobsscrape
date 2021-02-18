import scrapy
from ..items import TopjobsItem


class joburlsSpider(scrapy.Spider):
		name = 'jobs'

		start_urls = [
			'https://topjobs.lk/applicant/vacancybyfunctionalarea.jsp?jst=OPEN',
		]

		def parse(self, response):

			items = TopjobsItem()

			# company = response.css('h1').extract()
			# yield {'companyname' : company}
			# title = response.xpath('//*[@id="table"]/tr')

			for job in response.xpath('//*[@id="table"]/tr'):
				company = job.xpath("//h1/text()").extract()
				position = job.xpath('.//h2//text()').extract()
				link = job.xpath('.//h2/a/@href').extract()
				openingdate = job.xpath('.//td[5]//text()').extract()
				closingdate = job.xpath('.//td[7]//text()').extract()

				items['company'] = company
				items['position'] = position
				items['link'] = link
				items['openingdate'] = openingdate
				items['closingdate'] = closingdate


				yield items
