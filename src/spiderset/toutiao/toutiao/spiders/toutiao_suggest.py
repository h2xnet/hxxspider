import scrapy


class ToutiaoSuggestSpider(scrapy.Spider):
    name = "toutiao_suggest"
    allowed_domains = ["www.toutiao.com"]
    start_urls = ["https://www.toutiao.com"]

    def parse(self, response):
        pass
