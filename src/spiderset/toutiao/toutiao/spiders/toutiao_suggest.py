import scrapy
from toutiao.items import ToutiaoItem

import sys
sys.path.append('..')
from toutiao.common import item_toutiao_suggest_response_text_key

#
# Desc: 头条推荐爬虫
# Auth: zfs
# Date: 2023-12-15
#
class ToutiaoSuggestSpider(scrapy.Spider):
    name = "toutiao_suggest"
    allowed_domains = ["www.toutiao.com"]
    start_urls = ["https://www.toutiao.com/ch/news_hot/"]

    def parse(self, response):
        #pass
        item = ToutiaoItem()

        item[item_toutiao_suggest_response_text_key] = response.text

        for news in response.css('.title-box'):
            title = news.css('.title::text').extract_first()
            url = news.css('.link::attr(href)').extract_first()

            print('item title:' + title + ", url:" + url)

        # 提交item到管道文件
        yield item
