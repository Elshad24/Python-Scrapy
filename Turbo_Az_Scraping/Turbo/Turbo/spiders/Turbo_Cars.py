import scrapy


class TurboCarsSpider(scrapy.Spider):
    name = 'Turbo_Cars'
    allowed_domains = ['turbo.az']
    start_urls = ['http://turbo.az/']

    def parse(self, response):
        pass
